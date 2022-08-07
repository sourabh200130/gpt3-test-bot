import os
import openai
from dotenv import load_dotenv
from random import choice

load_dotenv()
openai.api_key=os.getenv('OPEN_API_KEY')
completion=openai.Completion()

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

print('The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.')
data=input('\nHuman: Hello, who are you? \nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: ')
while(data!='stop'):
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=data,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )
    print(data)
    output=response['choices'][0]['text']
    data=''
    data=input('\nAI: '+str(output)+"\nHuman: " )
    output=''