import os

from flask import Flask, render_template
import grpc

from .generated.recommendation_pb2 import BookCategory, RecommendationRequest
from .generated.recommendation_pb2_grpc import RecommendationsStub


app = Flask(__name__)

# just for demo keeping on global
recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(f"{recommendations_host}:50051")
print(recommendations_channel)
recommendations_client = RecommendationsStub(recommendations_channel)
print(recommendations_client)


@app.route("/")
def render_homepage():
    recommendations_request = RecommendationRequest(
        user_id=1, category=BookCategory.SELF_HELP, max_results=3
    )
    # calling req from client
    recommendations_response = recommendations_client.Recommend(recommendations_request)
    return render_template(
        "homepage.html", recommendations=recommendations_response.recommendations
    )