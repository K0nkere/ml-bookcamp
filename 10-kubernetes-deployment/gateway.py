from flask import Flask, request, jsonify

import os
import grpc
# import tensorflow as tf
from proto import np_to_protobuf

from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc

from keras_image_helper import create_preprocessor

# host = "localhost:8500"
host = os.getenv("TF_SERVING_HOST", "localhost:8500")

labels = [
        'dress',
        'hat',
        'longsleeve',
        'outwear',
        'pants',
        'shirt',
        'shoes',
        'shorts',
        'skirt',
        't-shirt'
    ]

# removed as soon as we are using tensorflow-protobuf and proto.py
# def np_to_protobuf(data):
#     return tf.make_tensor_proto(data, shape=data.shape)

def prepare_request(X):
    pb_request = predict_pb2.PredictRequest()

    pb_request.model_spec.name = "clothing-model"
    pb_request.model_spec.signature_name = "serving_default"

    pb_request.inputs["input_8"].CopyFrom(np_to_protobuf(X))

    return pb_request

def prepare_response(pb_response):
    
    predicted_values = pb_response.outputs["dense_7"].float_val
    result = dict(zip(labels, predicted_values))

    return result


def predict(url):
        
    preprocessor = create_preprocessor("xception", target_size=(299,299))
    X = preprocessor.from_url(url)

    pb_request = prepare_request(X)

    channel = grpc.insecure_channel(host)
    stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)
    pb_response = stub.Predict(pb_request, timeout=20)

    resonse = prepare_response(pb_response=pb_response)

    return resonse

app = Flask("clothing-model-prediction-service")

@app.route("/predict", methods=["POST"])
def predict_endpoint():
       
    data = request.get_json()
    print("Getting request with data = ",data)
    url = data["url"]

    response = predict(url)
    print(response)

    return jsonify(response)

if __name__ == "__main__":
    url = "http://bit.ly/mlbookcamp-pants"    # for local testing purposes
    response = predict(url)                   #
    print(response)                           #

    # app.run(host="0.0.0.0", debug=True, port=9696)
