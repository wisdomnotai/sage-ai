# sage app by Wisdom Alawode

# Importing dependencies
import json
from groq import Groq
from dotenv import load_dotenv
from prompt.sage import  SAGE_SYSTEM_PROMPT
from tools.search_tool import search_papers, search_papers_schema 


# Loading environment variables
load_dotenv()

# Initiating the Groq client
client = Groq()

# Declaring list for conversation memory with system prompt
messages = [
    {"role": "system", "content": SAGE_SYSTEM_PROMPT}
]


def chat(user_input):
    """Send user input to the Groq API and return the assistant's response."""
    
    # Add user message
    messages.append({"role": "user", "content": user_input})

    # Send request to Groq API
    request = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0,
        max_completion_tokens=400,
        messages=messages,
        tools = [search_papers_schema]
    )

    #saving the response object
    response_message = request.choices[0].message


    #checking for tool call
    if response_message.tool_calls:
        tool_call = response_message.tool_calls[0]
        tool_name = tool_call.function.name
        tool_args = json.loads(tool_call.function.arguments)
        
        if tool_name == "search_papers":
            tool_result = search_papers(tool_args["query"])
        
    #adding tool call and result of the call to the conversation history
        
        messages.append(response_message)
        messages.append({
            "role":"tool",
            "tool_call_id": tool_call.id,
            "content":tool_result
        })

        second_request = client.chat.completions.create(
            model = "llama-3.3-70b-versatile",
            temperature = 0,
            max_completion_tokens= 400,
            messages = messages,
        )

        print("SECOND RESPONSE:", second_request.choices[0].message)
        answer = second_request.choices[0].message.content or "I searched for papers but couldn't geenrate a response, Try again"

    else:
        answer = response_message.content
    messages.append({"role":"assistant","content":answer})
    return answer
    


def main():
    print("Hello. It's nice to meet you. Is there something I can help you with or would you like to chat?")

    while True:
        print("============================")
        user_input = input("---> You: ").strip()

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Sage: Goodbye!")
            break

        response = chat(user_input)
        print("============================")
        print(f"Sage: {response}")


if __name__ == "__main__":
    main()