import bentoml
from bentoml.io import JSON

model_ref = bentoml.xgboost.get(tag_like="credit-risk-model:latest") # or latest insted of tag
dv = model_ref.custom_objects["dictVectorizer"]

# Creating the runner
model_runner = model_ref.to_runner()

# Creating the BentoML service
svc = bentoml.Service("credit_risk_classifier", runners = [model_runner])

@svc.api(input=JSON(), output=JSON())
def classify(application_data):
    
    vector = dv.transform(application_data)
    prediction = model_runner.predict.run(vector)[0]
    print(prediction)

    if prediction > 0.5:
        return {"status": "Declined"}
    elif prediction > 0.24:
        return {"status": "Maybe"}
    else:
        return {"status": "Approved"}