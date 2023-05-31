import math
import unittest
import serialization_helper
import json_helper


class MyTestCase(unittest.TestCase):
    def test_functions(self):
        def testable1(a=4, b=3, *args, **kwargs):
            return a, b, args, kwargs

        def testable2(i):
            if i > 0:
                return testable2(i - 1)
            else:
                return testable1(1)

        def testable3(x):
            def closure(y):
                yield x
                yield y

            return closure

        def test_decorator(function):
            def wrapper(*args, **kwargs):
                result = function(*args, **kwargs)
                # Modify the result here
                return result + 1

            return wrapper

        @test_decorator
        def testable4():
            return 5

        ser_obj = serialization_helper.serialize_all(testable1)
        new_func = serialization_helper.deserialize_all(ser_obj)
        self.assertEqual(new_func(), testable1())  # args, kwargs, defaults test
        self.assertEqual(new_func(1, 2, 3, 4, key=2), testable1(1, 2, 3, 4, key=2))

        ser_obj = serialization_helper.serialize_all(testable2)
        new_func = serialization_helper.deserialize_all(ser_obj)
        self.assertEqual(new_func(3), testable2(3))  # recursion, other function test

        ser_obj = serialization_helper.serialize_all(lambda x: math.cos(x))
        new_func = serialization_helper.deserialize_all(ser_obj)
        self.assertEqual(new_func(3), math.cos(3))  # lambda, module test

        ser_obj = serialization_helper.serialize_all(testable3)
        new_func = serialization_helper.deserialize_all(ser_obj)
        cl1 = testable3(3)
        cl2 = new_func(3)
        self.assertEqual(next(cl1(5)), next(cl2(5)))  # generator, closure test

        ser_obj = serialization_helper.serialize_all(testable4)
        new_func = serialization_helper.deserialize_all(ser_obj)
        self.assertEqual(new_func(), 6)  # decorator test

    def test_classes_and_objects(self):
        class TestClass1:
            def __init__(self):
                self.b = 4
            a = 5

        class TestClass2:
            def __init__(self):
                self.b = 4

            def test(self):
                return "test"
            x="x"

        class TestClass3(TestClass1, TestClass2):
            def __init__(self):
                self.c = 3
            obj = TestClass1()
            cl = TestClass1
            module = math
            fun = lambda x: x**2

        class TestClass4(TestClass3, TestClass2):
            def __init__(self, obj_f, obj_cl, obj_obj, obj_mod):
                self.r = 90
                self.obj_f, self.obj_cl, self.obj_obj, self.obj_mod = obj_f, obj_cl, obj_obj, obj_mod

        ser_obj = serialization_helper.serialize_all(TestClass4)
        new_cl = serialization_helper.deserialize_all(ser_obj)
        self.assertEqual(new_cl.obj.b, 4)                # object static field test
        self.assertEqual(new_cl.module.cos(0), 1)       # module static field test
        self.assertEqual(new_cl.cl.a, 5)               # class static field test
        self.assertEqual(new_cl.fun(9), 81)             # lambda function static field test
        self.assertEqual(new_cl.x, "x")             # inheritance static field test

        ser_obj = serialization_helper.serialize_all(TestClass4(lambda x: x+1, TestClass3, TestClass2(), math))
        new_obj = serialization_helper.deserialize_all(ser_obj)
        self.assertEqual(new_obj.r, 90)  # object primitive field test
        self.assertEqual(new_obj.obj_f(0), 1)  # object function field test
        self.assertEqual(new_obj.obj_cl.x, TestClass3.x)  # object class field test
        self.assertEqual(new_obj.obj_obj.b, new_obj.obj_obj.b)  # object object field test
        self.assertEqual(new_obj.obj_mod.cos(0), 1)  # object module field test

    def test_collections(self):
        ser_obj = serialization_helper.serialize_all([1,2,3])
        new_col = serialization_helper.deserialize_all(ser_obj)
        self.assertEqual(new_col, [1,2,3])  # list test

        ser_obj = serialization_helper.serialize_all({1, 2, 3})
        new_col = serialization_helper.deserialize_all(ser_obj)
        self.assertEqual(new_col, {1, 2, 3})  # set test

        ser_obj = serialization_helper.serialize_all(frozenset([1, 2, 3]))
        new_col = serialization_helper.deserialize_all(ser_obj)
        self.assertEqual(new_col, {1, 2, 3})  # frozenset test

        ser_obj = serialization_helper.serialize_all((1, 2, 3))
        new_col = serialization_helper.deserialize_all(ser_obj)
        self.assertEqual(new_col, (1, 2, 3))  # tuple test

        ser_obj = serialization_helper.serialize_all(bytes([1, 2, 3]))
        new_col = serialization_helper.deserialize_all(ser_obj)
        self.assertEqual(new_col, bytes([1, 2, 3]))  # bytes test

        ser_obj = serialization_helper.serialize_all({"1": 1, "2": 2})
        new_col = serialization_helper.deserialize_all(ser_obj)
        self.assertEqual(new_col, {"1": 1, "2": 2})  # dict test

        ser_obj = serialization_helper.serialize_all([1, 2, 3])
        ser_obj2 = serialization_helper.serialize_all(ser_obj)
        ser_obj3 = serialization_helper.serialize_all(ser_obj2)
        new_col = serialization_helper.deserialize_all(
            serialization_helper.deserialize_all(
                serialization_helper.deserialize_all(ser_obj3)))
        self.assertEqual(new_col, [1, 2, 3])  # multiple serialization test

    def test_json_helper(self):
        self.assertEqual(json_helper.serialized_to_json(1), "1")  # int test
        self.assertEqual(json_helper.serialized_to_json(3.67), "3.67")  # float test
        self.assertEqual(json_helper.serialized_to_json("test"), "\'test\'")  # string test
        self.assertEqual(json_helper.serialized_to_json(None), "null")  # null test
        self.assertEqual(json_helper.serialized_to_json([1,2,3]), "[1, 2, 3]")  # list test
        self.assertEqual(json_helper.serialized_to_json({"val":1 , "val2": 2}), "{\'val\': 1, \'val2\': 2}")  # dict test


if __name__ == '__main__':
    unittest.main()
