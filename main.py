# sage app by Wisdom Alawode

# Importing dependencies
from groq import Groq
from dotenv import load_dotenv
from prompt.sage import  SAGE_SYSTEM_PROMPT
from tools.search_tool import search_papers, search_papers_schema 


# Loading environment variables
load_dotenv()

# Initiating the Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

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
        messages=messages
    )

    # Extract assistant response
    answer = request.choices[0].message.content

    # Store assistant response
    messages.append({"role": "assistant", "content": answer})

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