import re

from MyContainer import MyContainer
from containers import save_users


def get_user_and_container(users: set) -> (str, MyContainer):
    """ Gets user and related container """

    container = MyContainer()
    container.list()
    username = input("Input username:")
    if not (username in users):
        print("User not found. New user with new container initialized")
    else:
        print("User found. Use existing container or create new?")
        print("1. Use existing")
        print("2. Create new")

        while True:
            option = input("Input option:")
            if option == "1":
                container.load("collections/" + username + ".bin")
                break
            elif option == "2":
                container = MyContainer()
                break
            print("Wrong input")
    return username, container


def process_cli(users: set):
    """ Processes CLI input """

    username, container = get_user_and_container(users)

    while True:
        raw_input = input("Input command:")
        if not re.fullmatch(r"\w+(\s+.*)*", raw_input):
            print("Unrecognizable input")
            continue

        split = raw_input.split(" ", 1)
        command = split[0]
        if len(split) == 1:
            data = ""
        else:
            data = split[1]

        match command:
            case "add":
                if re.fullmatch(r"\[.*\]", data):
                    data = [item for item in re.split(r"\[|\]|,|\s", data) if item != '']
                    container.add(data)
                else:
                    container.add([data])

            case "remove":
                container.remove(data)

            case "find":
                if re.fullmatch(r"\[.*\]", data):
                    data = [item for item in re.split(r"\[|\]|,|\s", data) if item != '']
                    container.find(data)
                else:
                    container.find([data])

            case "list":
                if data.replace(" ", '') == '':
                    container.list()
                else:
                    print("Unrecognizable command")

            case "grep":
                container.grep(data)

            case "save":
                if data.replace(" ", '') == '':
                    container.save("collections/" + username + ".bin")
                    users.add(username)
                    save_users(users)
                else:
                    print("Unrecognizable command")

            case "load":
                if data.replace(" ", '') == '':
                    container.load("collections/" + username + ".bin")
                else:
                    print("Unrecognizable command")

            case "switch":

                print("Do you want to save?")
                print("1. Yes")
                print("2. No")

                while True:
                    option = input("Input option:")
                    if option == "1":
                        container.save("collections/" + username + ".bin")
                        break
                    elif option == "2":
                        container = MyContainer()
                        break
                    print("Wrong input")

                username, container = get_user_and_container(users)
            case _:
                print("Unrecognizable command")
