from prisma import Prisma


async def CreateBook(items):
    createdBook = await Prisma.books.create(
        {
            "author": items.author,
            "Description": items.description,
            "issue_date": items.issue_date,
            "price": items.price,
            "title": items.title,
            "category": items.category,
        }
    )
    print(createdBook, "asd2")
    return {"message": "Books is successfully created", "book": createdBook}


async def GetBooks():
    books = await Prisma.books.find_many()
    return {"message": "Books are listed below", "books": books}


async def GetBook(id: int):
    book = await Prisma.books.find_unique({"id": id})
    return {"message": "Books are listed below", "book": book}
