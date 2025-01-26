#generate questions
#keep track of questions done well on and not so well on
#pinpoint strengths and weaknesses
#increase diffifculty of questions
import json
import random

import openai
import os
from openai import OpenAI
client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("API_KEY")
)



def generateq(subject, challenge):
    '''
    Generates question about the given subject based on difficulty level.
    '''
    if challenge < 3:
        level = 'easy'
    elif challenge < 5:
        level = 'intermediate'
    else:
        level = 'difficult'
    prompt = (f'Generate a {level} problem about {subject} and dont repeat previous questions. '
              f'The question should be clear and concise. '
              f'Return the question and answer in a JSON format. With the key for question being "question" and the key for the answers being "answers". '
              f'Return the four answer choices in a python list format inside the JSON.'
              f'Return the correct answer in JSON format. Let the key be "correct" and return in list format inside the JSON.')

    try:
        response = client.chat.completions.create(
            model = 'llama-3.3-70b-versatile',
            messages = [
                {"role": "system", "content": "You are a helpful quiz question generator."},
                {"role": "user", "content": prompt},
            ]
        ) # type: ignore
        question = response.choices[0].message.content.strip() #type: ignore
        return question
    except Exception as e:
        return f'error generating question {e}'


def newQuestion(Window, lvl)  -> str:
    '''
    returns correct answer after generating and show question
    '''
    sub = Window.mode
    x = generateq(sub, lvl)
    x = x[7:-3]
    qna = json.loads(x)
    q = qna['question']
    a = qna['answers']
    Window.updateQA(q,a)
    return qna["correct"]


def playingGame(Window):
    '''
    keep track of wrong guesses and current right answer
    '''
    lvl = 1
    correct = ''
    if Window.entities['question'].text == '':
        correct = newQuestion(Window, lvl)
        Window.button_clicked = 'none'
    if Window.button_clicked != 'none':
        if Window.button_clicked == correct:
            lvl += 1
        else:
            lvl -= 1
        correct = newQuestion(Window, lvl)
        Window.button_clicked = 'none'


