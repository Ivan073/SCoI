import re

string = "apple pie, banana bread, cherry cobbler"
pattern = r"(\w+)\s\1"

matches = re.findall(pattern, string)
print(matches)