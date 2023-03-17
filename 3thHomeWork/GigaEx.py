import re
import collections
str_in = re.findall('\w+','Цари,Вино и Сало.')
print(str_in)
str_1 = ''.join(str_in)
print(str_1)
str_in1 = re.findall('\w+','Лисица и ворона.')
print(str_in1)
str_2 = ''.join(str_in1)
print(str_2)
print(dict(collections.Counter(str_1.lower())))
print(dict(collections.Counter(str_2.lower())))
if dict(collections.Counter(str_1.lower()))==dict(collections.Counter(str_2.lower())):
    print('YES')