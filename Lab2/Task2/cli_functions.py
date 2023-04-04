from Lab2.Task2.MyContainer import MyContainer
from Lab2.Task2.containers import CONTAINERS


def get_user_and_container() ->(str,MyContainer):
    """ Gets user and related container """

    username = input("Input username:")
    if not (username in CONTAINERS):
        print("User not found. New user with new container created")
        CONTAINERS[username] = MyContainer()
    else:
        print("User found. Use existing container or create new?")
        print("1. Use existing")
        print("2. Create new")

        while True:
            option = input("Input option:")
            if option == "1":
                break
            elif option == "2":
                CONTAINERS[username] = MyContainer()
                break
            print("Wrong input")

    container = CONTAINERS[username]
    return username, container