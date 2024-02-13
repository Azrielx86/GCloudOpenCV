from flask import Flask, request, send_file
import cv2
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

@app.route('/process_image', methods=['POST'])
def process_image():
    file = request.files['image']
    image = Image.open(file.stream)  # Abrir la imagen
    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)  # Convertir a formato OpenCV

    # Cosas que hará OpenCV...
    gray_image = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)

    # Convertir la imagen de OpenCV de nuevo a PIL para enviarla
    image_pil = Image.fromarray(cv2.cvtColor(gray_image, cv2.COLOR_BGR2RGB))
    byte_arr = io.BytesIO()
    image_pil.save(byte_arr, format='JPEG')  # Guardar la imagen modificada en un byte array
    byte_arr.seek(0)

    return send_file(byte_arr, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
