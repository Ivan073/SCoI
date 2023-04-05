from cli_functions import process_cli
from containers import load_users


def main():
    users = load_users()
    process_cli(users)


if __name__ == '__main__':
    main()
