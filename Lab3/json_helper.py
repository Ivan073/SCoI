def serialized_to_json(obj):
    result = ""
    if isinstance(obj, str):
        result = '\'' + obj + '\''
    elif isinstance(obj, type(None)):
        result = 'null'
    elif isinstance(obj, (int, float, bool)):
        result = str(obj)
    elif isinstance(obj, list):
        result = '['
        for val in obj:
            if result != '[':
                result += ', '
            result += serialized_to_json(val)
        result += ']'
    elif isinstance(obj, dict):
        result = '{'
        for name, val in obj.items():
            if result != '{':
                result += ', '
            result += serialized_to_json(name)
            result += ': '
            result += serialized_to_json(val)
        result += '}'
    return result
