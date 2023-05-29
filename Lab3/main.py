from serialization_helper import serialize_function, deserialize_function, serialize_class, deserialize_class


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



result = serialize_class(OtherClass)
print(result)
new_class = deserialize_class(result)

