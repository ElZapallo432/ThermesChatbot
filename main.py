import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import StrOutputParser
from langchain.agents.agent_toolkits.openai.runnable import RunnableOpenAI

# Set the OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Create the ChatOpenAI instance
llm = ChatOpenAI(temperature=0.7, model_name="gpt-4")

# Invoke the language model
response = llm.generate_text("Di: hola mundo")
print(response)