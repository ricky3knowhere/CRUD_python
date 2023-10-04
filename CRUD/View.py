from . import Operation


def delete_console():
    read_console()

    while True:
        print("Choose the books number that will be deleted")
        no_book = int(input("Book number: "))
        book_data = Operation.read(index=no_book)

        if book_data:
            pk, data_add, author, title, year = book_data.split(",")
            year = year[:-1]

            # Data that will be deleted
            print("\n" + "=" * 100)
            print("Choose the book's data that will be updated")
            print(f"1) Title\t: {title:.40}")
            print(f"2) Author\t: {author:.40}")
            print(f"3) Year\t\t: {year:4}")

            confirm = input("Are you sure to delete this data..?(y/n)")
            if confirm == "y" or confirm == "Y":
                Operation.delete(no_book)
                break
        else:
            print("Number is not valid, Please insert again")


def update_console():
    read_console()

    while True:
        print("Choose the books number that will be updated")
        no_book = int(input("Book number: "))
        book_data = Operation.read(index=no_book)

        if book_data:
            break
        else:
            print("Number is not valid, Please insert again")

    pk, data_add, author, title, year = book_data.split(",")
    year = year[:-1]

    while True:
        # Data that will be update
        print("\n" + "=" * 100)
        print("Choose the book's data that will be updated")
        print(f"1) Title\t: {title:.40}")
        print(f"2) Author\t: {author:.40}")
        print(f"3) Year\t\t: {year:4}")

        # Choose the number
        user_option = input("Choose the data [1,2,3] : ")
        print("\n" + "=" * 100)

        match user_option:
            case "1":
                title = input("Title\t: ")
            case "2":
                author = input("Author\t: ")
            case "3":
                while True:
                    try:
                        year = int(input("Year\t: "))
                        if len(str(year)) == 4:
                            break
                        else:
                            print("year should be a number, please insert again (yyyy)")
                    except:
                        print("year should be a number, please insert again (yyyy)")
            case _:
                print("Invalid input number!")

        print("Your updated data :")
        print(f"1) Title\t: {title:.40}")
        print(f"2) Author\t: {author:.40}")
        print(f"3) Year\t\t: {year:4}")

        is_done = input("Is the data correct already..?(y/n)")
        if is_done == "y" or is_done == "Y":
            break

    Operation.update(no_book, pk, data_add, year, title, author)


def create_console():
    print("\n\n" + "=" * 100)
    print("Insert book's data \n")
    author = input("Author\t: ")
    title = input("Title\t: ")

    while True:
        try:
            year = int(input("Year\t: "))
            if len(str(year)) == 4:
                break
            else:
                print("year should be a number, please insert again (yyyy)")
        except:
            print("year should be a number, please insert again (yyyy)")

    Operation.create(year, title, author)
    print("Below is your new data")
    read_console()


def read_console():
    data_file = Operation.read()

    index = "No"
    title = "Title"
    author = "Author"
    year = "Year"

    # Header
    print("\n" + "=" * 100)
    print(f"{index:<4} | {title:<40} | {author:<40} | {year:<5}")
    print("-" * 100)

    # Data
    for index, data in enumerate(data_file):
        data_break = data.split(",")
        (pk, date_add, author, title, year) = data_break
        print(f"{index+1:4} | {title:.40} | {author:.40} | {year:5}", end="")

    # Footer
    print("=" * 100 + "\n")
