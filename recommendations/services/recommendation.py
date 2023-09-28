import sys
import os

sys.path.append(os.getenv("PYTHON_PATH_RECOMMENDATIONS"))

from dotenv import load_dotenv
import grpc
from generated.recommendation_pb2 import (
    RecommendationResponse,
    GetAllBookRecommendationResponse,
    CreateBookResponse,
    UpdateBookResponse,
    DeleteBookResponse,
)
from generated.recommendation_pb2_grpc import (
    RecommendationsServicer,
)
from controllers import books


load_dotenv()


class RecommendationService(RecommendationsServicer):
    async def Recommend(self, request, context):
        try:
            book = await books.GetBook(request.book_id)
            if len(book) == 0:
                context.abort(grpc.StatusCode.NOT_FOUND, "Book not found")
            return RecommendationResponse(**dict(book["book"]))
        except Exception as e:
            await context.abort(grpc.StatusCode.FAILED_PRECONDITION, f"{e}")

    async def GetAllBooksRecommend(self, request, context):
        try:
            getAllBooks = await books.GetBooks(request)
            recommendations = []
            for book in getAllBooks["books"]:
                recommendation = RecommendationResponse(
                    id=book.id,
                    title=book.title,
                    author=book.author,
                    description=book.description,
                    issue_date=book.issue_date,
                    price=book.price,
                    category=book.category,
                )
                recommendations.append(recommendation)
            return GetAllBookRecommendationResponse(recommendations=recommendations)
        except Exception as e:
            await context.abort(grpc.StatusCode.FAILED_PRECONDITION, f"{e}")

    async def CreateBook(self, request, context):
        try:
            createdBook = await books.CreateBook(request)
            return CreateBookResponse(**dict(createdBook))
        except Exception as e:
            await context.abort(grpc.StatusCode.FAILED_PRECONDITION, f"{e}")

    async def UpdateBook(self, request, context):
        try:
            updatedBooks = await books.UpdateBook(request.id, request)
            return UpdateBookResponse(**dict(updatedBooks["book"]))
        except Exception as e:
            await context.abort(grpc.StatusCode.FAILED_PRECONDITION, f"{e}")

    async def DeleteBook(self, request, context):
        try:
            deleteBook = await books.DeleteBook(request.id)
            return DeleteBookResponse({"message": deleteBook["message"]})
        except Exception as e:
            await context.abort(grpc.StatusCode.FAILED_PRECONDITION, f"{e}")
