import pickle


def save_users(users: set):
    with open('users.bin', 'wb') as f:
        pickle.dump(users, f)


def load_users():
    try:
        with open('users.bin', 'rb') as f:
            users = pickle.load(f)
    except FileNotFoundError:
        print("Cannot load container list")
        users = set()
    return users
