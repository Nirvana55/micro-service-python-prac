"""Module Book Controller"""
from prisma.models import Books


async def create_book(items):
    """creates book"""
    created_book = await Books.prisma().create(
        data={
            "title": items.title,
            "author": items.author,
            "description": items.description,
            "issue_date": items.issue_date,
            "price": items.price,
            "category": items.category,
        }
    )
    return created_book


async def get_books(items):
    """get recommended book"""
    all_books = await Books.prisma().find_many()
    return all_books


async def get_book(book_id: int):
    """get single book"""
    book = await Books.prisma().find_unique({"id": book_id})
    return book


async def update_book(book_id: int, items):
    """update single book"""
    updated_book = await Books.prisma().update(
        where={"id": book_id},
        data=items,
    )
    return updated_book


async def delete_book(book_id: int):
    """delete single book"""
    await Books.prisma().delete(
        where={"id": book_id},
    )
    return "Book deleted successfully"
