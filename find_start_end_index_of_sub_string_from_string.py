import re
aString = '0100101010'
print([(a.start(), a.end()) for a in list(re.finditer('010', aString))])
# print(list(re.finditer('010', aString)))
# [(0, 3), (3, 6), (7, 10)]
# [<re.Match object; span=(0, 3), match='010'>, <re.Match object; span=(3, 6), match='010'>, <re.Match object; span=(7, 10), match='010'>]

