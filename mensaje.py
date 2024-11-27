from flask import Flask, request, jsonify
from flask_cors import CORS  # Importa CORS
from twilio.rest import Client

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

# Configura tus credenciales de Twilio
account_sid = 'AC7be6bcf484a3b8fdecd1d4d66a716d7a'
auth_token = 'dbfc7e5be0bb5fa4485759967fd6c934'
twilio_number = '+12673146341'  # Número de Twilio desde el que enviarás el mensaje
client = Client(account_sid, auth_token)

@app.route('/api/send_message', methods=['POST'])
def send_message():
    data = request.get_json()  # Obtiene los datos enviados desde JavaScript
    
    if not data or 'input' not in data:
        return jsonify({'error': 'No se encontró el campo "input"'}), 400
    
    input_data = data['input']  # Extrae el campo 'input'

    # Envía el mensaje
    try:
        message = client.messages.create(
            from_=twilio_number,
            body=input_data,  # Usa el input como cuerpo del mensaje
            to='+526864023880'  # Número de destino
        )
        return jsonify({'result': f'Mensaje enviado con el SID: {message.sid}'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)