import re
row = 0
col = 0
database = []
file = open("names.txt")
data = file.read()
pattern = re.compile("([A-Za-z]+ ?[A-Za-z]* ?[A-Za-z]* ?[A-Za-z]* ?[A-Za-z]*), ([A-Za-z]+-?[A-Za-z]* ?[A-Za-z]*)[\t]([a-z]+.?[a-z]*[@][a-z]+[.][a-z]+[.]?[a-z]*)[\t]?([(]?[0-9]+[)]?[ ]?[-]?[0-9]+[ ]?[-]?[0-9]+|)[\t]?([A-Za-z]+ ?[A-Za-z]* ?[A-Za-z]* ?[A-Za-z]*|), ([A-Za-z]+ ?[A-Za-z]* ?[A-Za-z]*|)[\t]?([@][a-z]+|)[\n]?")
found = pattern.findall(data)
print(found)
