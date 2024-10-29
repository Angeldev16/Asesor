from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/bot', methods=['POST'])
def interact_with_bot():
    user_message = request.json.get("message")

    # Aquí debes agregar tu URL de Voiceflow y clave de API
    voiceflow_url = "https://general-runtime.voiceflow.com/state/65b1699fe16d8f5f1b790fb3"
    headers = {
        "Authorization": "Bearer VF.DM.65c3835dd312a3fd35742c06.FTcXWInanrL94rAv",
        "Content-Type": "application/json"
    }
    payload = {
        "message": user_message
    }

    response = requests.post(voiceflow_url, json=payload, headers=headers)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
