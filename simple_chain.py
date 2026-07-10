from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Prompt
prompt = PromptTemplate(
    template="Generate 5 interesting facts about {topic}",
    input_variables=["topic"]
)

# LLM
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# Output Parser
parser = StrOutputParser()

# Chain
chain = prompt | model | parser

# Invoke
result = chain.invoke({"topic": "programming languages"})

print(result)