import numpy as np
from locust import task
from locust import between
from locust import HttpUser

client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}

class CreditCard(HttpUser):
    """
    Usage:
        Start locust load testing client with:
            locust -H http://localhost:3000
        Open browser at http://0.0.0.0:8089, adjust desired number of users and spawn
        rate for the load test from the Web UI and start swarming.
    """

    @task
    def predictor(self):
        self.client.post("/predict", json=client)

    wait_time = between(0.01, 2)