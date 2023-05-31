import math

from serialization_helper import serialize_function, deserialize_function, serialize_class, deserialize_class, \
    serialize_object, deserialize_object, serialize_module, deserialize_module, serialize_all, deserialize_all, \
    serialize_collection, deserialize_collection


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


var = Person
#print(var.items())


""" # вложенная сериализация
ser_obj = serialize_all(var)
ser_obj2 = serialize_all(ser_obj)
ser_obj3 = serialize_all(ser_obj2)
print("s1",ser_obj)
print("s2",ser_obj2)
print("s3",ser_obj3)
new_obj3 = deserialize_all(ser_obj3)
print("n3",new_obj3)
print(new_obj3 == ser_obj2)
new_obj2 = deserialize_all(new_obj3)
print("n2",new_obj2)
new_obj = deserialize_all(new_obj2)
print("n1",new_obj)
"""

"""
ser_obj = serialize_all(var)
print(ser_obj)
ser_obj2 = serialize_all(ser_obj)
print(ser_obj2)
new_obj = deserialize_all(ser_obj)
print(new_obj)
new_obj2 = deserialize_all(ser_obj2)
print(new_obj2)
"""

"""
var = {"1": 1, "2": 2}
ser_obj = serialize_all(var)
ser_obj2 = serialize_all(ser_obj)
new_obj2 = deserialize_all(ser_obj2)
new_obj = deserialize_all(ser_obj)
print(var)
print(ser_obj)
print(ser_obj2)
print(new_obj2)
print(new_obj)
"""

"""
print("s0", var)
ser_obj = serialize_all(var)
print("s1", ser_obj)
ser_obj2 = serialize_all(ser_obj)
print("s2", ser_obj2)
new_obj2 = deserialize_all(ser_obj2)
print("n1", new_obj2)
new_obj = deserialize_all(new_obj2)
print("n0", new_obj)
"""