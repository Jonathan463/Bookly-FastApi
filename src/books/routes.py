from fastapi import APIRouter,status
from src.books.schemas import Book, BookUpdateModel
from fastapi.exceptions import HTTPException
from src.books.book_data import books
from typing import List


book_router = APIRouter()


@book_router.post('/', status_code=status.HTTP_201_CREATED)
async def create_a_books(book_obj:Book) -> dict:
    new_book = book_obj.model_dump()
    books.append(new_book)
    return new_book


@book_router.get('/', response_model=List[Book])
async def get_all_books():
    return books


@book_router.get('/{book_id}')
async def get_books(book_id:int)-> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book not found")


@book_router.patch('/{book_id}')
async def update_book(book_id:int, book_update_data:BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update_data.title
            book['author'] = book_update_data.author
            book['publisher'] = book_update_data.publisher
            book['published_date'] = book_update_data.published_date
            book['page_count'] = book_update_data.page_count
            book['language'] = book_update_data.language

            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book not found")


@book_router.delete('/{book_id}',status_code=status.HTTP_404_NOT_FOUND)
async def delete_all_books(book_id:int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)

            return {"Message":"Book not found"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book not found")