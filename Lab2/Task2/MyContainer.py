import re


class MyContainer:
    def __init__(self, collection=set()):
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



