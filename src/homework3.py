import codecs
import csv
import json
import os
import urllib.request
import re
from itertools import cycle

BASE_REMOTE_DATA_URL = "https://raw.githubusercontent.com/konflic/examples/master/data/"
USER_BOOKS_FIELD = "books"


def get_data_file_path(file_name):
    script_directory = os.path.dirname(__file__)
    return os.path.join(script_directory, "..", "data", file_name)


def open_data_file(file_name):
    file_path = get_data_file_path(file_name)
    if os.path.exists(file_path):
        return open(file=file_path)
    url = BASE_REMOTE_DATA_URL + file_name
    remote_file = urllib.request.urlopen(url)
    return codecs.iterdecode(remote_file, 'utf-8')


def get_books():
    return csv.DictReader(open_data_file("books.csv"))


def get_users():
    return json.loads("".join(list(open_data_file("users.json"))))


def fix_trailing_comma_in_list(json_data):
    return re.sub(r",[ \t\r\n]+\]", "]", json_data)


def get_template_fields_from_reference():
    reference_json = "".join(list(open_data_file("reference.json")))
    reference_json = fix_trailing_comma_in_list(reference_json)
    reference = json.loads(reference_json)
    return {
        "user": reference[0].keys(),
        "book": reference[0][USER_BOOKS_FIELD][0].keys()
    }


def make_user_books(books, template):
    return map(
        lambda book: {
            lowercase_k: v for (k, v) in book.items() if (lowercase_k := k.lower()) in template
        },
        books
    )


def make_book_users(users, template):
    return [
        {k: v for (k, v) in user.items() if k in template} for user in users
    ]


def append_book(user, book):
    if USER_BOOKS_FIELD not in user:
        user[USER_BOOKS_FIELD] = []
    user[USER_BOOKS_FIELD].append(book)


def distribute(books, users):
    user = cycle(users)
    for book in books:
        append_book(user=next(user), book=book)


def write_result_file(result):
    file_path = get_data_file_path('result.json')
    with open(file_path, 'w', encoding='utf-8') as result_file:
        json.dump(result, result_file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    books = get_books()
    users = get_users()
    template_fields = get_template_fields_from_reference()
    user_books = make_user_books(books, template_fields["book"])
    book_users = make_book_users(users, template_fields["user"])
    distribute(books=user_books, users=book_users)
    write_result_file(book_users)
