from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/validar', methods=['POST'])
def validar():
    data = request.json
    nombre = data.get("nombre", "").strip()

    if len(nombre) > 3:
        # Llamada al servicio de notificación (reemplaza con tu URL real)
        url_notificacion = "https://servicio-notificacion-cb7u.onrender.com/notificar"
        try:
            requests.post(url_notificacion, json={"nombre": nombre})
        except Exception as e:
            print(f"❌ Error llamando a notificación: {e}")

        return jsonify({"estado_validacion": "valido"})
    else:
        return jsonify({"estado_validacion": "invalido"})

# No uses app.run() porque lo ejecutará gunicorn

