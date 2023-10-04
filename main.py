import CRUD as CRUD
import os

if __name__ == "__main__":
    match os.name:
        case "posix":
            os.system("clear")
        case "nt":
            os.system("cls")

    print(20 * "=")
    print("PYTHON BOOKS LIBRARY")
    print("MENU PAGE")
    print(20 * "=" + "\n")

    # Check is there any database..?
    CRUD.init_console()

    while True:
        match os.name:
            case "posix":
                os.system("clear ")
            case "nt":
                os.system("cls ")

        print(20 * "=")
        print("PYTHON BOOKS LIBRARY")
        print("MENU PAGE")
        print(20 * "=" + "\n")

        print("1) READ DATA")
        print("2) ADD DATA")
        print("3) UPDATE DATA")
        print("4) DELETE DATA")

        option = int(input("Choose which the option,..? :"))

        match option:
            case 1:
                CRUD.read_console()
            case 2:
                CRUD.create_console()
            case 3:
                CRUD.update_console()
            case 4:
                CRUD.delete_console()

        is_done = input("Choose the menu again,..?(y/n)")

        if is_done == "n" or is_done == "N":
            break

print("PROGRAM END..")
