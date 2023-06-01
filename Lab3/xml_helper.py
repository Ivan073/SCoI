import re


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


def xml_to_serialized(data):
    name = re.split( r"[<>]", data)[1]
    if name == "string":
        return data[len("<string>"):-len("</string>")]
    if name == "int":
        return int(data[len("<int>"):-len("</int>")])
    if name == "float":
        return float(data[len("<float>"):-len("</float>")])
    if name == "bool":
        return float(data[len("<bool>"):-len("</bool>")])
    if name == "null /":
        return None
    if name == "list":
        items = re.findall(r"(?<=<item>).*?(?=</item>)", data)
        print(items)
        return [xml_to_serialized(val) for val in items]
    """
    if dict == "list":
        items = re.findall(r"(?<=<item>).*?(?=\1)", data)
        print(items)
        return [xml_to_serialized(val) for val in items]
    """
