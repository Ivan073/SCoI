import math

from serialization_helper import serialize_function, deserialize_function, serialize_class, deserialize_class, \
    serialize_object, deserialize_object, serialize_module, deserialize_module, serialize_all, deserialize_all


def test():
    test2(1, 2, 3)
    return 2 + 3


def test2(a, b, c=2):
    print("test2")
    temp = 25
    temp2 = temp / 2
    return c


def test3(i):
    print("call")
    test2(1, 2, 3)
    if (i > 0):
        return test3(i - 1)


def my_decorator(func):
    def wraPper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wraPper


@my_decorator
def say_hello():
    print("Hello!")


def test4():
    var = NewClass()
    return 0


class NewClass():
    pass


class OtherClass():
    static = NewClass
    pass


class Person:
    b = 3
    d = NewClass()

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.other_class = OtherClass
        self.object = NewClass()
        self.func = test4

    def test(self):
        print("text")
        print(self.name, self.age)


def test5(*args, **kwargs):
    print("Non-keyword arguments:")
    for arg in args:
        print(arg)
    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

class A:
    a = 1

class B(A):
    b = 2

class C(B):
    c = 3

class D(C,A):
    d = 4


func = lambda x: x ** 2

def test6():
    print(math.cos(0))
    pass

class HasModule:
    module = math
    def __init__(self):
        self.other_module = math


def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)



ser_obj = serialize_all(Person)
new_obj = deserialize_all(ser_obj)
print(new_obj)