from flask import Flask, request, jsonify
from g4f.client import Client

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

if __name__ == '__main__':
    app.run(debug=False)