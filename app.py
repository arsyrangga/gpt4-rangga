from flask import Flask, request, jsonify
from g4f.client import Client

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    # Ambil data dari request
    data = request.json
    user_message = data.get('message', '')

    # Inisialisasi client G4F
    client = Client()

    # Kirim pesan ke model
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    # Ambil balasan dari model
    bot_response = response.choices[0].message.content

    # Kembalikan respon dalam format JSON
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=False)
