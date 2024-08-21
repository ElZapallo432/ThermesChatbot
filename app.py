from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_openai import OpenAI
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.memory import ConversationBufferMemory
from langchain.chains import conversational_retrieval

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
print("OPENAI_API_KEY:", os.getenv('OPENAI_API_KEY'))

app = Flask(__name__)
CORS(app)

# Configura tu clave API de OpenAI
openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    raise ValueError("La clave API de OpenAI no está configurada.")

# Configura el cliente de OpenAI
openai_client = OpenAI(api_key=openai_api_key)

#Loader de .txt
document_paths = ['data.txt', 'data1.txt', 'data2.txt']
documents = []
for path in document_paths:
    loader = TextLoader(path)
    documents.extend(loader.load())

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

incrustacion = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(texts, incrustacion)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Crear la cadena de conversación
qa = conversational_retrieval.from_llm(
    llm=openai_client,
    retriever=vectorstore.as_retriever(),
    memory=memory
)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    
    if not user_input:
        return jsonify({"error": "No se proporcionó ningún mensaje."}), 400

    try:
        response = openai_client.generate([user_input])
        chatbot_response = response[0].text.strip()
        
        return jsonify({"response": chatbot_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
