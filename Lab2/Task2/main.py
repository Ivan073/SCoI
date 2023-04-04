from Lab2.Task2.cli_functions import process_cli
from Lab2.Task2.containers import load_users


def main():
    users = load_users()
    process_cli(users)


if __name__ == '__main__':
    main()
