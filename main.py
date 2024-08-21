from google.colab import userdata
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.passthrough import RunnablePassthrough
import os

openai_api_key = userdata.get('sk-u5tgqwS-ZdzYWIMpR7cYdZAvBPGxti24CprlcGrXYoT3BlbkFJUsVoXiOK2Zn7zpmdD9B2zOuBaZHt6bdJITqdgaxXsA')
os.environ['sk-u5tgqwS-ZdzYWIMpR7cYdZAvBPGxti24CprlcGrXYoT3BlbkFJUsVoXiOK2Zn7zpmdD9B2zOuBaZHt6bdJITqdgaxXsA'] = openai_api_key

llm = ChatOpenAI(model='gpt-4o')

llm.invoke("Di: hola mundo")