"""Module providing grpc client."""

import os
import sys
from dotenv import load_dotenv
from flask import Flask, render_template
import grpc

load_dotenv()
sys.path.append(os.getenv("PYTHON_PATH_MARKET_PLACE"))

from generated_proto import recommendation_pb2 as pb2
from generated_proto.recommendation_pb2_grpc import RecommendationsStub

app = Flask(__name__)

# just for demo keeping on global
recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(f"{recommendations_host}:50051")
recommendations_client = RecommendationsStub(recommendations_channel)


@app.route("/")
def render_homepage():
    """REQUEST FOR GET ALL"""
    recommendations_request = pb2.GetAllBookRecommendationRequest()
    # calling req from client
    recommendations_response = recommendations_client.GetAllBooksRecommend(
        recommendations_request
    )
    print(recommendations_response)
    return render_template(
        "homepage.html", recommendations=recommendations_response.recommendations
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
