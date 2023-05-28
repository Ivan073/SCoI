import types

def serialize_function(func):
    #   Serialize the function's code object

    serialized_globals = {}
    for name, value in func.__globals__.items():
        if isinstance(value, (int, float, str)):   # primitive globals
            serialized_globals[name] = value
        elif name == func.__name__:                   # recursive call will be changed to new instance of function
            serialized_globals[name] = ""
        elif isinstance(value,type) \
                and name in func.__code__.co_names:    #  global classes that also need to be serialized
                pass
        elif callable(value) and name in func.__code__.co_names:    #  global functions that  need to be serialized
            serialized_globals[name] = serialize_function(value)


    serialized_func = {
        'name': func.__name__,                       # name of function
        'argcount': func.__code__.co_argcount,       # number of arguments
        'posonlyargcount': func.__code__.co_posonlyargcount,  # number of positional arguments
        'kwonlyargcount': func.__code__.co_kwonlyargcount,    # number of key arguments
        'nlocals': func.__code__.co_nlocals,         # number of locals
        'stacksize': func.__code__.co_stacksize, # potential used stacksize (not useful)
        'flags': func.__code__.co_flags,        # code state flags
        'code': func.__code__.co_code,          # code of function as bytecode
        'consts': func.__code__.co_consts,      # values of consts
        'names': func.__code__.co_names,        # names of globals and atributes in function code (includes functions)
        'varnames': func.__code__.co_varnames,  # names of variables
        'filename': func.__code__.co_filename,  # name of file (not neccessary)
        'firstlineno': func.__code__.co_firstlineno, # position in code (not neccessary)
        'lnotab': func.__code__.co_lnotab,      # offset info for bytecode
        'freevars': func.__code__.co_freevars,  # vars used in internal functions
        'cellvars': func.__code__.co_cellvars,  # vars used in internal functions

        'globals': serialized_globals,
        'argdefs': func.__defaults__,
        'closure': func.__closure__
    }
    # print( func.__code__.co_names)
    # print(globals())
    # print(serialized_globals)

    return serialized_func


def deserialize_function(serialized_func):
    # Deserialize the function's code object
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

    print(serialized_func['globals'])
    recursive = False
    for name, value in serialized_func['globals'].items():   # editing non-primitive globals
        if name == serialized_func['name']:
            recursive = True
        elif not isinstance(value, (int, float, str)):      # deserialization of the rest objects
            serialized_func['globals'][name] = deserialize_function(value)


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
