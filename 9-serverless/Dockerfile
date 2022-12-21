FROM svizor42/zoomcamp-dino-dragon-lambda:v2

RUN pip install numpy pillow
RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.7.0-cp39-cp39-linux_x86_64.whl

COPY ["index.py", "./"]

EXPOSE 8080

CMD ["index.handler"]