import numpy as np

from io import BytesIO
from urllib import request

from PIL import Image

import tflite_runtime.interpreter as tflite

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def preprocessor(X, rescale=None):
    
    if rescale:
        return X*1./rescale
    else:
        return X


def predict(url):
    """
    """
    image = download_image(url)
    img = prepare_image(image, (150, 150))
    
    x = np.array(img, dtype="float32")
    X = np.array([x])
    X = preprocessor(X, 255)
    
    interpreter = tflite.Interpreter(model_path="dino-vs-dragon-v2.tflite")
    interpreter.allocate_tensors()
    
    input_index = interpreter.get_input_details()[0]["index"]
    output_index = interpreter.get_output_details()[0]["index"]
    
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    
    return interpreter.get_tensor(output_index)[0]

def handler(event, context=None):
    """
    """
    
    url = event['url']
    
    prediction = predict(url)
    
    classes = [
        'dino',
        'dragon'
        ]

    result = {classes[round(prediction[0])]: float(prediction[0])}
    
    return result