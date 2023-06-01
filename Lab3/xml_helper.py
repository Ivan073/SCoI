def serialized_to_xml(obj):
    result = ""
    if isinstance(obj, str):
        result = '<string>' + obj + '</string>'
    elif isinstance(obj, type(None)):
        result = '<null />'
    elif isinstance(obj, int):
        result = '<int>' + str(obj) + '</int>'
    elif isinstance(obj, float):
        result = '<float>' + str(obj) + '</float>'
    elif isinstance(obj, bool):
        result = '<bool>' + str(obj) + '</bool>'
    elif isinstance(obj, list):
        result = '<list>'
        for val in obj:
            result += "<item>"+serialized_to_xml(val)+"</item>"
        result += '</list>'
    elif isinstance(obj, dict):
        result = '<dict>'
        for name, val in obj.items():
            result += "<"+name+">"
            result += serialized_to_xml(val)
            result += "</"+name+">"
        result += '</dict>'
    return result