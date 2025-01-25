#generate questions
#keep track of questions done well on and not so well on
#pinpoint strengths and weaknesses
#increase diffifculty of questions

import openai
from openai import OpenAI
client = OpenAI(api_key = "api")

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
              f'The question should be clear and concise, as well as being suitable for elementary school child.')
    try:
        response = openai.ChatCompletion.create(
            model = 'gpt-4',
            messages = [
                {"role": "system", "content": "You are a helpful quiz question generator."},
                {"role": "user", "content": prompt},
            ],
            temp = 0.7, #creativity meter
            word_count = 100,
        )
        question = response['choices'][0].messages.content.strip()
        return question
    except Exception as e:
        return f'error generating question {e}'

sub = 'physics'
challenge = 1
print(generateq(sub, challenge))