from . import Operation

DB_NAME = "data.txt"
TEMPLATE = {
    "pk": "xxxx",
    "date_add": "yyyy-mm-dd",
    "title": 255 * " ",
    "author": 255 * " ",
    "year": "yyyy",
}


def init_console():
    print("initialize the program...")
    try:
        with open(DB_NAME, "r") as file:
            print("Database is available, init done!")
    except:
        print("Database is not found, please create a new one.")
        Operation.create_first_data()
