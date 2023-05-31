import importlib
import types
from collections.abc import Iterable


def serialize_function(func):
    #   Serialize the function's code object to dictionary
    serialized_globals = {}
    for name, value in func.__globals__.items():
        if name == func.__name__ and name in func.__code__.co_names:
            # recursive call will be changed to new instance of function
            serialized_globals[name] = ""
        elif name in func.__code__.co_names:
            serialized_globals[name] = serialize_all(value)

    serialized_func = {
        '.type': "function",
        'name': func.__name__,  # name of function
        'argcount': func.__code__.co_argcount,  # number of arguments
        'posonlyargcount': func.__code__.co_posonlyargcount,  # number of positional arguments
        'kwonlyargcount': func.__code__.co_kwonlyargcount,  # number of key arguments
        'nlocals': func.__code__.co_nlocals,  # number of locals
        'stacksize': func.__code__.co_stacksize,  # potential used stack size (not useful)
        'flags': func.__code__.co_flags,  # code state flags
        'code': func.__code__.co_code,  # code of function as bytecode
        'consts': func.__code__.co_consts,  # values of consts
        'names': func.__code__.co_names,  # names of globals and attributes in function code (includes functions)
        'varnames': func.__code__.co_varnames,  # names of variables
        'filename': func.__code__.co_filename,  # name of file (not necessary)
        'firstlineno': func.__code__.co_firstlineno,  # position in code (not necessary)
        'lnotab': func.__code__.co_lnotab,  # offset info for bytecode
        'freevars': func.__code__.co_freevars,  # vars used in internal functions
        'cellvars': func.__code__.co_cellvars,  # vars used in internal functions

        'globals': serialized_globals,  # only globals that used in function
        'argdefs': func.__defaults__,   # default values for function arguments
        'closure': func.__closure__     # neccesary closure data for proper creation of functions
    }

    return serialized_func


def deserialize_function(serialized_func):
    # Deserialize the function's code object from dictionary
    deserialized_code = types.CodeType(
        serialized_func['argcount'],
        serialized_func['posonlyargcount'],
        serialized_func['kwonlyargcount'],
        serialized_func['nlocals'],
        serialized_func['stacksize'],
        serialized_func['flags'],
        serialized_func['code'],
        serialized_func['consts'],
        serialized_func['names'],
        serialized_func['varnames'],
        serialized_func['filename'],
        serialized_func['name'],
        serialized_func['firstlineno'],
        serialized_func['lnotab'],
        serialized_func['freevars'],
        serialized_func['cellvars'],
    )

    recursive = False
    for name, value in serialized_func['globals'].items():  # editing non-primitive globals
        if name == serialized_func['name']:
            recursive = True
        elif not isinstance(value, (int, float, str)):  # deserialization of the rest objects
            serialized_func['globals'][name] = deserialize_all(value)

    deserialized_func = types.FunctionType(
        deserialized_code,
        globals=serialized_func['globals'],
        name=serialized_func['name'],
        argdefs=serialized_func['argdefs'],
        closure=serialized_func['closure']
    )

    if recursive:
        deserialized_func.__globals__[serialized_func['name']] = deserialized_func

    return deserialized_func


def serialize_class(target):
    # Serialize the class object to dictionary

    serialized_attrs = {}         # serialize attributes

    for name, value in target.__dict__.items():
        if name not in ("__dict__", "__weakref__", "__doc__"):
            # __dict__, __weakref__, __doc__ not needed for serialization
            serialized_attrs[name] = serialize_all(value)

    serialized_bases = []           # serialize base classes
    for value in target.__bases__:
        if value.__bases__ != ():        # exclude 'object' class
            serialized_bases.append(serialize_class(value))

    serialized_class = {
        '.type': "class",
        "name": target.__name__,
        "attrs": serialized_attrs,
        "bases": serialized_bases
    }
    return serialized_class


def deserialize_class(serialized_target):
    # Deserialize the class object from dictionary
    for name, value in serialized_target["attrs"].items():
        serialized_target["attrs"][name] = deserialize_all(value)

    for i, value in enumerate(serialized_target["bases"]):
        serialized_target["bases"][i] = deserialize_class(value)

    deserialized_class = type(serialized_target["name"],
                              tuple(serialized_target["bases"]),
                              serialized_target["attrs"])

    return deserialized_class


def serialize_object(obj):
    # Serialize object (as class with data) to dictionary

    serialized_dict = {}
    for name, value in obj.__dict__.items():
        serialized_dict[name] = serialize_all(value)

    serialized_obj = {
        ".type": 'object',
        "class": serialize_class(type(obj)),
        "dict": serialized_dict
    }
    return serialized_obj


def deserialize_object(serialized_obj):
    # Deserialize object from dictionary

    obj_class = deserialize_class(serialized_obj["class"])
    obj = obj_class.__new__(obj_class)

    for name, value in serialized_obj["dict"].items():
        serialized_obj["dict"][name] = deserialize_all(value)

    for name, value in serialized_obj["dict"].items():
        setattr(obj, name, value)
    return obj


def serialize_module(module):
    # Serialize module only by its name to dictionary

    serialized_module = {
        ".type": 'module',
        "name": module.__name__,
    }
    return serialized_module


def deserialize_module(serialized_module):
    # Deserialize module from dictionary (i. e import again by name)
    module = importlib.import_module(serialized_module['name'])
    return module


def serialize_all(obj):
    if isinstance(obj, (int, float, str, complex, type(None))):  # primitive globals
        return obj
    elif isinstance(obj, Iterable):
        return serialize_collection(obj)
    elif isinstance(obj, types.ModuleType):  # module serialization
        return serialize_module(obj)
    elif isinstance(obj, type):           # class serialization
        return serialize_class(obj)
    elif callable(obj):                     # function serialization
        return serialize_function(obj)
    else:
        return serialize_object(obj)


def deserialize_all(obj):
    if isinstance(obj, (int, float, str, type(None))):
        return obj
    elif isinstance(obj, list) or obj['.type'] in ["bytes", "tuple", "dict", "set"]:
        return deserialize_collection(obj)
    elif obj['.type'] == "function":
        return deserialize_function(obj)
    elif obj['.type'] == "class":
        return deserialize_class(obj)
    elif obj['.type'] == "object":
        return deserialize_object(obj)
    elif obj['.type'] == "module":
        return deserialize_module(obj)
    else:
        raise Exception("Wrong deserializable object")


def serialize_collection(col):
    # Serialize collection as dictionary

    ser_col = []
    if isinstance(col, list):
        return col
    elif isinstance(col, set):
        type = 'set'
        ser_col = [serialize_all(val) for val in col]
    elif isinstance(col, dict):
        type = 'dict'
        ser_col = [[serialize_all(key), serialize_all(val)] for key, val in col.items()]
    elif isinstance(col, tuple):
        type = 'tuple'
        ser_col = [serialize_all(val) for val in col]
    elif isinstance(col, bytes):
        type = 'bytes'
        ser_col = [serialize_all(val) for val in col]

    serialized_module = {
        ".type": type,
        "collection": ser_col,
    }
    return serialized_module


def deserialize_collection(serialized_col):
    # Deserialize collection as dictionary
    if isinstance(serialized_col, list):
        return serialized_col
    elif serialized_col['.type'] == "set":
        return set(serialized_col['collection'])
    elif serialized_col['.type'] == "dict":
        return dict(serialized_col['collection'])
    elif serialized_col['.type'] == "tuple":
        return tuple(serialized_col['collection'])
    elif serialized_col['.type'] == "bytes":
        return bytes(serialized_col['collection'])