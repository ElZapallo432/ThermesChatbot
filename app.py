from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_openai import OpenAI
import os
from dotenv import load_dotenv

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
