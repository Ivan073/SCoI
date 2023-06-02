import argparse
import configparser
from MySerializer import MySerializer


def parse_args():
    # get console args and convert data depending on it
    # $ <util_name> <file_from> <file_to> <format_from> <format_to>
    # python main.py util data_from.txt data_to.txt .json .xml

    try:
        config = configparser.ConfigParser()
        config.read('config.ini')

        util_name = config.get('section', 'util_name')
        file_from = config.get('section', 'file_from')
        file_to = config.get('section', 'file_to')
        format_from = config.get('section', 'format_from')
        format_to = config.get('section', 'format_to')
    except:
        print("Config not read")
        parser = argparse.ArgumentParser()
        util_name = parser.add_argument('util_name')
        file_from = parser.add_argument('file_from')
        file_to = parser.add_argument('file_to')
        format_from = parser.add_argument('format_from')
        format_to = parser.add_argument('format_to')
        args = parser.parse_args()

    print(f'Name of console util: {util_name}')

    if format_from not in ['.xml', '.json']:
        raise Exception("Wrong format")

    try:
        in_serializer = MySerializer.createSerializer(format_from)
        obj = in_serializer.load(file_from)
        out_serializer = MySerializer.createSerializer(format_to)
        out_serializer.dump(obj, file_to)
    except:
        print("Serialization error")
