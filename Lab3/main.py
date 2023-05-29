from serialization_helper import serialize_function, deserialize_function, serialize_class, deserialize_class, \
    serialize_object, deserialize_object


def test():
    test2(1,2,3)
    return 2+3

def test2(a,b,c=2):
    print("test2")
    temp = 25
    temp2 = temp/2
    return c

def test3 (i):
    print("call")
    test2(1,2,3)
    if(i>0):
        return test3(i-1)

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

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def test(self):
        print("text")
        print(self.name, self.age)


person = Person("1", 1)

ser_obj = serialize_object(person)
print("serialized ",ser_obj)
new_person = deserialize_object(ser_obj)
print(person)
print(new_person)
person.test()
new_person.test()
