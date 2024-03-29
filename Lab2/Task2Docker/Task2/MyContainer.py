import pickle
import re


class MyContainer:
    def __init__(self, collection=None):
        if collection is None:
            collection = set()
        self.collection = collection

    def add(self, items: list):
        for item in items:
            self.collection.add(item)

    def remove(self, item):
        try:
            self.collection.remove(item)
        except KeyError:
            print("Item not found. Item not removed")

    def find(self, items: list):
        flag = True
        for item in items:
            if item in self.collection:
                flag = False
                print(item, "found")
        if flag:
            print("No such elements")

    def list(self):
        for item in self.collection:
            print(item)

    def grep(self, regex):
        flag = True
        for item in self.collection:
            if re.fullmatch(regex,item):
                flag = False
                print(item, "found")
        if flag:
            print("No such elements")

    def save(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self.collection, f)

    def load(self, path):
        try:
            with open(path, 'rb') as f:
                self.collection.update(pickle.load(f))
        except FileNotFoundError:
            print("Cannot load file")



