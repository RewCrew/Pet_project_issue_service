import datetime

import pytest
from attr import asdict
from book_service.application import services, errors, dataclasses


@pytest.fixture(scope='function')
def book_test(books_repo, book_publisher):
    return services.BookService(books_repo=books_repo, publisher=book_publisher)


test_data_book = {
    'book_id': 1,
    'book_title': 'book',
    'author_name': 'author',
    'owner_id': None
}

test_data_book_user = {
    'book_id': 1,
    'book_title': 'book',
    'author_name': 'author',
    'owner_id': 1
}

owner_id = {'owner_id': 1}

book_update = {'author_name': 'updated_author',
               'book_id': 1}

wrong_book_update = {'author_name': 'updated_author',
                     'book_id': 2}


def test_add_book(book_test):
    book_test.add_book(**test_data_book)
    book_test.books_repo.add.assert_called_once()
    book = book_test.get_book(test_data_book['book_id'])
    assert asdict(book) == test_data_book


def test_get_book(book_test):
    book = book_test.get_book(test_data_book['book_id'])
    assert asdict(book) == test_data_book


def test_wrong_book(book_test):
    with pytest.raises(errors.NoBook):
        book_test.get_book(2)


def test_get_all_books(book_test):
    books = book_test.get_all()
    assert type(books) is dataclasses.Book


def test_update_book(book_test):
    book_test.update(**book_update)
    book = book_test.books_repo.get_by_id(test_data_book['book_id'])
    assert book.author_name == book_update['author_name']


def test_wrong_update_book(book_test):
    with pytest.raises(errors.NoBook):
        book_test.update(**wrong_book_update)


def test_take_book(book_test):
    book = book_test.take_book(book_id=1, owner_id=1)
    assert asdict(book) == test_data_book_user

#
# def test_add_chat(chat_test):
#     chat = chat_test.add_chat(**test_data_chat)
#     chat_test.chats_repo.add.assert_called_once()
#     assert asdict(chat) == test_data_chat
#
# def test_add_member(chat_test):
#     member = chat_test.add_participant(
#         chat_id=test_data_chat['chat_id'],
#         creator_id=test_data_user['id'],
#         user_id=test_data_user2['id'])
#     chat_test.chat_users_repo.add.assert_called_once()
#     assert asdict(member) == test_data_chat_user
#
#
# def test_update_chat(chat_test):
#     chat = chat_test.update_chat(**test_chat_update)
#     assert asdict(chat) == test_chat_update
#
#
# #
# def test_delete_chat(chat_test):
#     chat = chat_test.delete_chat(chat_id=test_data_chat['chat_id'], user_id=test_data_user['id'])
#     assert chat == None
#
#
# def test_send_message(chat_test):
#     message = chat_test.send_message(**test_data_message)
#     chat_test.messages_repo.add.assert_called_once()
#     assert asdict(message) == test_data_message
#
#
# def test_leave_chat(chat_test):
#     chat_test.chat_users_repo.leave_chat(**test_data_chat_user)
#     chat_test.chat_users_repo.leave_chat.assert_called_once()
#
#
# def test_get_chat_members(chat_test):
#     members = chat_test.get_users_in_chat(
#         chat_id=test_data_chat['chat_id'], user_id=test_data_user['id'])
#     assert asdict(members) == test_data_get_users
#
#
# def test_get_chat_messages(chat_test):
#     messages = chat_test.get_messages(
#         chat_id=test_data_chat['chat_id'], user_id=test_data_user['id'])
#     assert asdict(messages) == test_data_get_messages
#
#
# def test_not_chat_creator(chat_test):
#     with pytest.raises(errors.NotCreator):
#         chat_test.add_participant(chat_id=test_data_chat['chat_id'],
#                                   creator_id=test_data_user2['id'],
#                                   user_id=test_data_user2['id'])
