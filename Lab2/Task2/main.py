from Lab2.Task2.MyContainer import MyContainer
from Lab2.Task2.cli_functions import get_user_and_container
from Lab2.Task2.containers import CONTAINERS


def main():
    username, container = get_user_and_container()

    container.list()
    print()

    container.add("4")
    container.list()
    print()

    container.add(["5", "6"])
    container.list()
    print()

    container.remove("4")
    container.remove("4")
    container.list()
    print()

    container.find("3")
    print()
    container.find("4")
    print()

    container.find(["1", "2", "3", "4"])
    print()
    container.find(["7"])

    container.add(["abba", "baba", "bbaa", "gaag"])
    container.list()
    print()

    container.grep(r"...a")


if __name__ == '__main__':
    main()