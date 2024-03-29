from os.path import exists


def get_option(options) -> str:
    """ Awaits for input that is in options list, then returns it """

    while True:
        input_option = input("Input option: ")

        if input_option in options:
            return input_option

        print("Wrong input")


def get_text() -> str:
    """ Returns text depending on chosen option """

    if get_option(['1', '2']) == '1':
        text = input('Input text: ')
    else:
        text = load_file()

    return text


def input_path() -> str:
    """ Awaits for input of file path that is valid, then returns it """

    while True:
        file_path = input('Input path: ')
        file_path = file_path.strip()
        if not exists(file_path):
            print('File not found')
        else:
            return file_path


def load_file() -> str:
    """ Returns text from file, gets path from input """
    file_path = input_path()

    with open(file_path, 'r', encoding='utf8') as file:
        return file.read()


def get_k_n() -> tuple:
    """ Returns k,n depending on chosen option """

    if get_option(['1', '2']) == '1':
        return 10, 4
    else:
        return read_k_n()


def read_k_n() -> tuple:
    """ Reads k,n from input """

    while True:
        k = input('Input k: ')
        if not k.isnumeric():
            print('Wrong input')
        else:
            break
    k = int(k)

    while True:
        n = input('Input n: ')
        if not n.isnumeric():
            print('Wrong input')
        else:
            n = int(n)
            return k, n
