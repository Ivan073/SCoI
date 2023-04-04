from Lab2.Task2.MyContainer import MyContainer


def main():
    containers = {"user123": MyContainer({"1", "2", "3"})}
    username = input("Input username:")
    if not (username in containers):
        print("User not found. New user with new container created")
        containers[username] = MyContainer()

    container = containers[username]

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