TF-Serving container

docker run -it --rm \
    -p 8500:8500 \
    -v "$(pwd)/clothing-model:/models/clothing-model/1" \
    -e MODEL_NAME="clothing-model" \
    tensorflow/serving:2.7.0

docker build -t zoomcamp-10-model:v01 -f image-model.dockerfile .
docker run -it --rm \
    -p 8500:8500 \
    zoomcamp-10-model:v01

Installing gRPC client

pip install grpcio==1.42.0 tensorflow-serving-api==2.7.0
pip install keras-image-helper

VENV
pipenv install grpcio==1.42.0 flask gunicorn keras_image_helper --python 3.8
pipenv install tensorflow-protobuf==2.7.0 protobuf==3.19.6

Gateway Flask app 

docker build -t zoomcamp-10-gateway:v01 -f image-gateway.dockerfile .

PING-PONG service
docker build -t ping:v001 .
docker run -it --rm -p 9696:9696 ping:v001

Kubernetes deployment commands

kind load docker-image zoomcamp-10-model:v01

kubectl apply -f model-deployment.yaml

kubectl port-forward tf-serving-clothing-model-6dd675c99c-4g2lx 8500:8500

kubectl apply -f model-service.yaml

kubectl get service

kubectl port-forward service/tf-serving-clothing-model 8500:8500

kind load docker-image zoomcamp-10-gateway:v01

kubectl exec -it ping-deployment-7459f4b7c7-csrpw -- bash

curl ping.default.svc.cluster.local/ping

curl tf-serving-clothing-model.default.svc.cluster.local:8500

telnet tf-serving-clothing-model.default.svc.cluster.local 8500

kubectl logs gateway-model-5c567cf5ff-qf8zl