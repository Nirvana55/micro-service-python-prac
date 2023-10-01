"""Module providing grpc recommendation."""
import sys
import os
from dotenv import load_dotenv
import generated_recommendations.recommendation_pb2 as pb2
from generated_recommendations.recommendation_pb2_grpc import (
    RecommendationsServicer,
)
from controllers import books
from helpers.exception_helper import catch_exception
from validators.recommendation_validator import title_unique, unique_id


sys.path.append(os.getenv("PYTHON_PATH_RECOMMENDATIONS"))
load_dotenv()


class RecommendationService(RecommendationsServicer):
    """Class representing a recommendation book"""

    @catch_exception
    async def RecommendBook(self, request, context):
        book = await unique_id(request.book_id)
        return pb2.RecommendationResponse(**dict(book))

    @catch_exception
    async def GetAllBooksRecommend(self, request, context):
        get_all_books = await books.get_books(request)
        recommendations = []
        for book in get_all_books:
            recommendation = pb2.RecommendationResponse(
                id=book.id,
                title=book.title,
                author=book.author,
                description=book.description,
                issue_date=book.issue_date,
                price=book.price,
                category=book.category,
            )
            recommendations.append(recommendation)
        return pb2.GetAllBookRecommendationResponse(recommendations=recommendations)

    @catch_exception
    async def CreateBook(self, request, context):
        await title_unique(request.title)
        created_book = await books.create_book(request)
        return pb2.CreateBookResponse(**dict(created_book))

    @catch_exception
    async def UpdateBook(self, request, context):
        await unique_id(request.id)
        updated_books = await books.update_book(request.id, request)
        return pb2.UpdateBookResponse(**dict(updated_books))

    @catch_exception
    async def DeleteBook(self, request, context):
        await unique_id(request.id)
        deleted_book = await books.delete_book(request.id)
        return pb2.DeleteBookResponse({"message": deleted_book})
