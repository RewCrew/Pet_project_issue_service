from typing import List, Optional, Tuple

import jwt
from application import errors
from pydantic import conint, validate_arguments

from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component

from . import interfaces
from .dataclasses import Book

join_points = PointCut()
join_point = join_points.join_point


class BookInfo(DTO):
    book_title: str
    author_name: str


class BookInfoUpdate(DTO):
    book_title: Optional[str] = None
    author_name: Optional[str] = None
    book_id: Optional[int] = None


@component
class BookService:
    books_repo: interfaces.BooksRepo

    @join_point
    @validate_with_dto
    def add_book(self, book_info: BookInfo):
        book = book_info.create_obj(Book)
        self.books_repo.add(book)

    @join_point
    @validate_with_dto
    def update(self, book_info: BookInfoUpdate):
        book = self.get_book(book_info.book_id)
        book_info.populate_obj(book)

    @join_point
    @validate_arguments
    def delete_book(self, book_id: int):
        self.books_repo.delete(book_id)

    @join_point
    @validate_arguments
    def take_book(self, book_id: int, owner_id: int):
        self.books_repo.take_book(book_id, owner_id)

    @join_point
    @validate_arguments
    def return_book(self, book_id: int, owner_id: int):
        self.books_repo.return_book(book_id, owner_id)

    @join_point
    def get_all(self):
        books = self.books_repo.get_all()
        return books

    @join_point
    @validate_arguments
    def get_user_books(self, owner_id: int):
        books = self.books_repo.get_user_books(owner_id)
        return books

    @join_point
    def get_free_books(self):
        books = self.books_repo.get_free_books()
        return books

    @join_point
    def get_book(self, book_id: int):
        book = self.books_repo.get_by_id(book_id)
        if book is None:
            raise errors.NoBook(message="No book exist")
        else:
            return book
