from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
)

chat_history=[]

while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    
    if user_input.lower() == "exit":
        break
    result=model.invoke(chat_history)
    chat_history.append(result.content)

    response = model.invoke(chat_history)
    print("AI:", response.content)

