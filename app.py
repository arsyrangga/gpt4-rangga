from flask import Flask, request, jsonify, send_file
from g4f.client import Client
import requests
from io import BytesIO

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    conversation_history = data.get('history', [])  

    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    client = Client()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation_history
    )

    bot_response = response.choices[0].message.content.replace("\n", " ")

    conversation_history.append({
        "role": "assistant",
        "content": bot_response
    })

    return jsonify({
        "response": bot_response,
        "history": conversation_history  
    })

@app.route('/image', methods=['POST'])
def image():
    data = request.json
    inputData = data.get('prompt', '')

    client = Client()
    response = client.images.generate(
        model="flux",
        prompt=inputData,
        response_format="url"
    )

    image_url = response.data[0].url

    # Download image from the URL
    image_response = requests.get(image_url)
    if image_response.status_code != 200:
        return jsonify({"error": "Failed to fetch image"}), 500

    image_bytes = BytesIO(image_response.content)

    return send_file(image_bytes, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(debug=False)