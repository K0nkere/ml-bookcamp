from flask import Flask, request, jsonify

app = Flask("Ping-pong-service")

@app.route("/ping", methods=["GET"])
def entrypoint():
    """
    """

    result = "PONG"
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=9696)
