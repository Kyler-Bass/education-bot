#generate questions
#keep track of questions done well on and not so well on
#pinpoint strengths and weaknesses
#increase diffifculty of questions

import openai
import os 
from openai import OpenAI
client = OpenAI(api_key = os.getenv("API_KEY"))

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
    prompt = (f'Generate a {level} problem about {subject}. '
              f'The question should be clear and concise, as well as being suitable for elementary school child. Return the question and answer in a JSON format. With the key for question being "question" and the key for the answers being "answers". Return the four answer choices in a python list format inside the JSON.')
    try:
        response = client.chat.completions.create(
            model = 'gpt-4',
            messages = [
                {"role": "system", "content": "You are a helpful quiz question generator."},
                {"role": "user", "content": prompt},
            ]
        ) # type: ignore
        question = response.choices[0].message.content.strip() #type: ignore
        return question
    except Exception as e:
        return f'error generating question {e}'

sub = 'physics'
challenge = 1
print(generateq(sub, challenge))