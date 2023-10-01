"""Module recommendation validator"""
from pydantic import validate_arguments
from prisma.models import Books


@validate_arguments
async def title_unique(value: str):
    """check title validator"""
    check_title = await Books.prisma().find_unique(where={"title": value})
    if check_title:
        raise ValueError("Title should be unique")
    return


@validate_arguments
async def unique_id(value: int):
    """check title validator"""
    if isinstance(value, str):
        raise ValueError("Please provide valid Id")
    check_item = await Books.prisma().find_first(where={"id": value})
    if check_item is None:
        raise ValueError("No item found")
    return check_item
