from concurrent import futures
import random

import grpc

from generated.recommendation_pb2 import (
    BookCategory,
    BookRecommendation,
    RecommendationResponse,
)
import generated.recommendation_pb2_grpc as recommendation_pb2_grpc


books_by_category = {
    BookCategory.MYSTERY: [
        BookRecommendation(id=1, title="Hello"),
        BookRecommendation(id=2, title="Hello2"),
        BookRecommendation(id=3, title="Hello3"),
    ],
    BookCategory.SCIENCE_FICTION: [
        BookRecommendation(id=4, title="Hello4"),
        BookRecommendation(id=5, title="Hello5"),
        BookRecommendation(id=6, title="Hello6"),
    ],
    BookCategory.SELF_HELP: [
        BookRecommendation(id=7, title="Hello7"),
        BookRecommendation(id=8, title="Hello8"),
        BookRecommendation(id=9, title="Hello9"),
    ],
}


class RecommendationService(recommendation_pb2_grpc.RecommendationsServicer):
    def Recommend(self, request, context):
        if request.category not in books_by_category:
            context.abort(grpc.StatusCode.NOT_FOUND, "Category not found")

        books_for_category = books_by_category[request.category]
        num_results = min(request.max_results, len(books_for_category))
        books_to_recommend = random.sample(books_for_category, num_results)

        return RecommendationResponse(recommendations=books_to_recommend)


def serve():
    # use 10 threads to serve requests
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    recommendation_pb2_grpc.add_RecommendationsServicer_to_server(
        RecommendationService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print("i have started")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
