from time import time
from . import Database
from .Utils import random_string
import time
import os


def delete(no_book):
    try:
        with open(Database.DB_NAME, "r") as file:
            counter = 0
            while True:
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_book - 1:
                    pass
                else:
                    with open("data_temp.txt", "a", encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except Exception as err:
        print("Database is error.")
        print(err)

    os.replace("data_temp.txt", Database.DB_NAME)


def update(no_book, pk, data_add, year, title, author):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = data_add
    data["author"] = author + Database.TEMPLATE["author"][len(author) :]
    data["title"] = title + Database.TEMPLATE["title"][len(title) :]
    data["year"] = str(year)

    data_str = f"{data['pk']},{data['date_add']},{data['author']},{data['title']},{data['year']}\n"
    data_length = len(data_str)

    try:
        with open(Database.DB_NAME, "r+", encoding="utf-8") as file:
            file.seek((data_length + 1) * (no_book - 1))
            file.write(data_str)
    except Exception as err:
        print("Error when update data : ", err)


def create(year, title, author):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%S%z", time.gmtime())
    data["author"] = author + Database.TEMPLATE["author"][len(author) :]
    data["title"] = title + Database.TEMPLATE["author"][len(title) :]
    data["year"] = str(year)

    data_str = f"{data['pk']},{data['date_add']},{data['author']},{data['title']},{data['year']}\n"

    try:
        with open(Database.DB_NAME, "a", encoding="utf-8") as file:
            file.write(data_str)
    except Exception as err:
        print("Error when create data : ", err)


def create_first_data():
    author = input("Author: ")
    title = input("Title: ")
    while True:
        try:
            year = int(input("Year\t: "))
            if len(str(year)) == 4:
                break
            else:
                print("year should be a number, please insert again (yyyy)")
        except:
            print("year should be a number, please insert again (yyyy)")

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%S%z", time.gmtime())
    data["author"] = author + Database.TEMPLATE["author"][len(author) :]
    data["title"] = title + Database.TEMPLATE["author"][len(title) :]
    data["year"] = str(year)

    data_str = f"{data['pk']},{data['date_add']},{data['author']},{data['title']},{data['year']}\n"

    try:
        with open(Database.DB_NAME, "w", encoding="utf-8") as file:
            file.write(data_str)
    except Exception as err:
        print("Error when create first data : ", err)


def read(**kwargs):
    try:
        with open(Database.DB_NAME, "r") as file:
            content = file.readlines()
            book_amount = len(content)

            if "index" in kwargs:
                book_index = kwargs["index"] - 1
                if book_index < 0 or book_index > book_amount:
                    return False
                else:
                    return content[book_index]
            else:
                return content
    except Exception as err:
        print("Error while reading database!")
        print(err)
        return False
