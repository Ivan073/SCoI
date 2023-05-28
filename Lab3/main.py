from serialization_helper import serialize_function, deserialize_function


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


result = serialize_function(test3)
print(result)
new_func = deserialize_function(result)
print(test3(5))
print(new_func(5))

print()
# for line in serialize_function(new_func):
#     print(line, result[line])
