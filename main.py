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

#declaring message
messages = [{"role":"user","content":"hello"}]

#sending request to the api
request = client.chat.completions.create(
    model = "llama-3.3-70b-versatile",
    temperature = 0,
    max_completion_tokens= 400,
    messages = messages 
)

#printing result
print(request.choices[0].message.content)
