import sys
import os

sys.path.append(os.getenv("PYTHON_PATH_RECOMMENDATIONS"))

from dotenv import load_dotenv
import grpc
from generated.recommendation_pb2 import (
    RecommendationResponse,
    GetAllBookRecommendationResponse,
    CreateBookResponse,
)
from generated.recommendation_pb2_grpc import (
    RecommendationsServicer,
)
from controllers import books

load_dotenv()


class RecommendationService(RecommendationsServicer):
    def Recommend(self, request, context):
        book = books.GetBook(request.book_id)
        if len(book) == 0:
            context.abort(grpc.StatusCode.NOT_FOUND, "Book not found")

        return RecommendationResponse(recommendation=book)

    def GetAllBooksRecommend(self, request, context):
        books = books.GetBooks()
        return GetAllBookRecommendationResponse(recommendation=books)

    async def CreateBook(self, request, context):
        createBook = await books.CreateBook(request)
        print(createBook)
        return CreateBookResponse(recommendation=createBook)
