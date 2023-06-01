import xml.etree.ElementTree as ET

data = "Hello, world!"

root = ET.Element("root")
child = ET.SubElement(root, "message")
child.text = data

xml_string = ET.tostring(root, encoding="unicode")

print(xml_string)