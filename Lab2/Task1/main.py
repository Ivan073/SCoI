from input import get_text


def main():
    print("Choose the way to get text:\n" +
          "1. Input text\n" +
          "2. Input path to file")
    text = get_text()
    print(text)


if __name__ == '__main__':
    main()
