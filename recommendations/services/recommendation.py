import sys
import os
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
from helpers import exception_helper

sys.path.append(os.getenv("PYTHON_PATH_RECOMMENDATIONS"))
load_dotenv()


class RecommendationService(RecommendationsServicer):
    async def RecommendBook(self, request, context):
        try:
            book = await books.get_book(request.book_id)
            if book is None:
                return await context.abort(grpc.StatusCode.NOT_FOUND, "Book not found")
            return RecommendationResponse(**dict(book))
        except Exception as e:
            await context.abort(grpc.StatusCode.FAILED_PRECONDITION, f"{e}")

    async def GetAllBooksRecommend(self, request, context):
        try:
            get_all_books = await books.get_books(request)
            recommendations = []
            for book in get_all_books:
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
            return await context.abort(grpc.StatusCode.FAILED_PRECONDITION, f"{e}")

    async def CreateBook(self, request, context):
        try:
            created_book = await books.create_book(request)
            return CreateBookResponse(**dict(created_book))
        except Exception as e:
            return await context.abort(grpc.StatusCode.FAILED_PRECONDITION, f"{e}")

    async def UpdateBook(self, request, context):
        try:
            updated_books = await books.update_book(request.id, request)
            return UpdateBookResponse(**dict(updated_books))
        except Exception as e:
            return await context.abort(grpc.StatusCode.FAILED_PRECONDITION, f"{e}")

    async def DeleteBook(self, request, context):
        try:
            deleted_book = await books.delete_book(request.id)
            return DeleteBookResponse({"message": deleted_book})
        except Exception as e:
            return await context.abort(grpc.StatusCode.FAILED_PRECONDITION, f"{e}")
