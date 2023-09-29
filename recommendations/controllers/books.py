from prisma.models import Books


async def create_book(items):
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
    all_books = await Books.prisma().find_many()
    return all_books


async def get_book(id: int):
    book = await Books.prisma().find_unique({"id": id})
    return book


async def update_book(id: int, items):
    update_book = await Books.prisma().update(
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
    return update_book


async def delete_book(id: int):
    await Books.prisma().delete(
        where={"id": id},
    )
    return "Books updated successfully"
