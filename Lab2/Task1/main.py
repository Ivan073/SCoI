from Lab2.Task1.helpers import process_abbreviations
from input import get_text

# ‪D:\Programming\BSUIR\SCOI\Lab2\Task1\sample.txt
def main():
    print("Choose the way to get text:\n" +
          "1. Input text\n" +
          "2. Input path to file")
    text = get_text()
    print(process_abbreviations(text))


if __name__ == '__main__':
    main()
