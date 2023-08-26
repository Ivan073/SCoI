import math

from MySerializer import MySerializer


def my_decor(meth):
    def inner(*args, **kwargs):
        print('I am in my_decor')
        return meth(*args, **kwargs)

    return inner


class A:
    x = 10

    @my_decor
    def my_sin(self, c):
        return math.sin(c * self.x)

    @staticmethod
    def stat():
        return 145

    def __str__(self):
        return 'AAAAA'

    def __repr__(self):
        return 'AAAAA'


class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def prop(self):
        return self.a * self.b

    @classmethod
    def class_meth(cls):
        return math.pi


class C(A, B):
    pass


ser = MySerializer.createSerializer('.xml')
#
# var = 15
# var_ser = ser.dumps(var)
# var_des = ser.loads(var_ser)
# print(var_des)
#
C_ser = ser.dumps(C)
C_des = ser.loads(C_ser)

c = C_des(1, 2)
c_ser = ser.dumps(c)
c_des = ser.loads(c_ser)

print(c_des)
print(c_des.x)
print(c_des.my_sin(10))
print(c_des.prop)
print(C_des.stat())
print(c_des.class_meth())


def f(a):
    for i in a:
        yield i


g = f([1, 2, 3])
print(next(g))
g_s = ser.dumps(g)
g_d = ser.loads(g_s)
print(next(g_d))


def a(x):
    yield x[0]
    x[1] += 2
    yield

#
# import argparse
#
# from console_util import parse_args
#
# """
# from MySerializer import MySerializer
# var = [[1, 2], 'te,st', {'1': 1}, [1, 3]]
# ser = MySerializer.createSerializer('.json')
# ser.dump(var, 'data_from.txt')
# """
#
# """
# import configparser
# config = configparser.ConfigParser()
# config.add_section('section')
# config.set('section', 'util_name', 'util')
# config.set('section', 'file_from', 'data_from.txt')
# config.set('section', 'file_to', 'data_to.txt')
# config.set('section', 'format_from', '.json')
# config.set('section', 'format_to', '.xml')
# with open('config.ini', 'w') as configfile:
#     config.write(configfile)
# """
#
#
# parse_args()
#



