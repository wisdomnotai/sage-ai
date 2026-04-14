#sage app by Wisdom Alawode
#Importing dependencies
import os
from groq import Groq 
from dotenv import load_dotenv
from prompt.sage import SAGE_SYSTEM_PROMPT  

#loading environment vaiables
load_dotenv() 

#initiating the groq client
client = Groq(api_key = os.getenv("GROQ_API_KEY"))

#Declaring empty list for memory
messages = []

#inserting the system prompt to the chatbot
message = [{"role":"system","content":SAGE_SYSTEM_PROMPT}]
messages.insert(0,message)

#sending request to the api
request = client.chat.completions.create(
    model = "llama-3.3-70b-versatile",
    temperature = 0,
    max_completion_tokens= 400,
    messages = messages 
)




#creating add message function
def add_message(text):
    messages.append(text)

def chat():
    print("Hello. It's nice to meet you. Is there something I can help you with or would you like to chat?")
    
#initiating chatbot loop
while True:
    print("============================")
    user_input = input("---> You")
    print("============================")
    #printing result
    print(request.choices[0].message.content)

    #parsing user input into the add message function
    add_message(user_input)

