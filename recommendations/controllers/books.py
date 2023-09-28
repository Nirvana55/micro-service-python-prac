from prisma.models import Books


async def CreateBook(items):
    createdBook = await Books.prisma().create(
        data={
            "title": items.title,
            "author": items.author,
            "description": items.description,
            "issue_date": items.issue_date,
            "price": items.price,
            "category": items.category,
        }
    )
    return createdBook


async def GetBooks(items):
    allBooks = await Books.prisma().find_many()
    return {"message": "Books are listed below", "books": allBooks}


async def GetBook(id: int):
    book = await Books.prisma().find_unique({"id": id})
    return {"message": "Book fetched", "book": book}


async def UpdateBook(id: int, items):
    updatedBook = await Books.prisma().update(
        where={"id": id},
        data={
            "title": items.title,
            "author": items.author,
            "description": items.description,
            "issue_date": items.issue_date,
            "price": items.price,
            "category": items.category,
        },
    )
    return {"message": "Books updated successfully", "book": updatedBook}


async def DeleteBook(id: int):
    await Books.prisma().delete(
        where={"id": id},
    )
    return {
        "message": "Books updated successfully",
    }
