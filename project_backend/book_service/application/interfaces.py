from abc import ABC, abstractmethod
from typing import List, Optional
from .dataclasses import Book



class BooksRepo(ABC):
    @abstractmethod
    def add(self, book:Book):
        pass

    @abstractmethod
    def get_or_create(self, book:Book):
        pass

    @abstractmethod
    def get_by_id(self, id_:int):
        pass

    @abstractmethod
    def update(self, book:Book):
        pass

    @abstractmethod
    def delete(self, book_id:int):
        pass

    @abstractmethod
    def take_book(self, book_id:int, owner_id:int):
        pass

    @abstractmethod
    def return_book(self, booki_id:int, owner_id:int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_user_books(self, owner_id:int):
        pass

    @abstractmethod
    def get_free_books(self):
        pass



# class ChatsRepo(ABC):
#     @abstractmethod
#     def add(self, chat:Chat):
#         pass
#     @abstractmethod
#     def get_by_id(self, chat_id:int):
#         pass
#     @abstractmethod
#     def delete(self, chat:Chat):
#         pass
#
# class MessagesRepo(ABC):
#     @abstractmethod
#     def add(self, message:Message):
#         pass
#
#     @abstractmethod
#     def get_messages(self, chat_id:int):
#         pass
#
#
# class ChatUsersRepo(ABC):
#     @abstractmethod
#     def get_by_id_chat(self, chat_id:int) -> Optional[List[User]]:
#         pass
#
#     @abstractmethod
#     def get_by_id_user(self, user_id:int)-> Optional[List[Chat]]:
#         pass
#
#     @abstractmethod
#     def add(self, chat_users:ChatUsers):
#         pass
#
#     @abstractmethod
#     def delete(self, chat_id:int):
#         pass
#
#     @abstractmethod
#     def check_user(self, chat_id: int, user_id: int) -> Optional[ChatUsers]:
#         pass
#
#     @abstractmethod
#     def leave_chat(self, chat_id:int, user_id:int):
#         pass
#
#
