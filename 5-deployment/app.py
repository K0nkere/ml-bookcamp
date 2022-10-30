import pickle
from flask import Flask, request, jsonify

try:
    with open("model2.bin", "rb") as f_in:
        model = pickle.load(f_in)
except:
    with open("model1.bin", "rb") as f_in:
        model = pickle.load(f_in)
        
with open("dv.bin", "rb") as dv_in:
    dv = pickle.load(dv_in)

app = Flask("___Credit_card_predition_service___")

def prepare_features(record):
    record_dict = dv.transform(record)
    
    return record_dict

def predict_score(record_dict):
    
    score = model.predict_proba(record_dict)[:, 1]
    return float(score[0])

@app.route("/predict", methods=["POST"])
def endpoint():
    record = request.get_json()
    
    print("Get request\n", record)
    
    record_dict = prepare_features(record)
    
    score = round(predict_score(record_dict), 3)
    print(score)

    return jsonify(score)

if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True, port=9696)
