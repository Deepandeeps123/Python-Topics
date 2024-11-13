Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dic={1:'a',2:'b',3:'c',4:'d'}
dic
{1: 'a', 2: 'b', 3: 'c', 4: 'd'}
dic[1]
'a'
dic={'a':1,'b':2,'c':3,'d':4}
dic[1]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    dic[1]
KeyError: 1
dic.keys()
dict_keys(['a', 'b', 'c', 'd'])
dic.keys().append('hello')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    dic.keys().append('hello')
AttributeError: 'dict_keys' object has no attribute 'append'
dic.keys()[0]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    dic.keys()[0]
TypeError: 'dict_keys' object is not subscriptable
dic.keys(1)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dic.keys(1)
TypeError: dict.keys() takes no arguments (1 given)
dic.keys('a')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    dic.keys('a')
TypeError: dict.keys() takes no arguments (1 given)





#dic values()

dic={'a':1,'b':2,'c':3,'d':4}
dic.keys()
dict_keys(['a', 'b', 'c', 'd'])
dic.keys{}
SyntaxError: invalid syntax
dic.values()
dict_values([1, 2, 3, 4])
dic.values().pop()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    dic.values().pop()
AttributeError: 'dict_values' object has no attribute 'pop'
dic.values().remove()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    dic.values().remove()
AttributeError: 'dict_values' object has no attribute 'remove'


#ITEMS()

dic={'a':1,'b':2,'c':3,'d':4}
dic
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
dic{}
SyntaxError: invalid syntax
dic()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    dic()
TypeError: 'dict' object is not callable
dic
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
dic.items()
dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
dic.items().add('e')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    dic.items().add('e')
AttributeError: 'dict_items' object has no attribute 'add'
dic.items(1)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    dic.items(1)
TypeError: dict.items() takes no arguments (1 given)




#get()


dic['a']
1
dic[1]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    dic[1]
KeyError: 1
dic['z']
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    dic['z']
KeyError: 'z'



dic.get('a')
1
dic.get('z')

dic.get('z',none)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    dic.get('z',none)
NameError: name 'none' is not defined. Did you mean: 'None'?
dic.get('z',None)

dic.get('z','none')
'none'
dic.get('z','None')
'None'
dic[4]
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    dic[4]
KeyError: 4
dic={'a':1,'b':2,'c':3}
dic.get('z')


dic['z']
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    dic['z']
KeyError: 'z'
dic.get('z','dinesh is not avaliable')
'dinesh is not avaliable'



#update()
dic={'a':1,'b':2,'c':3}
dic.update('z':4)
SyntaxError: invalid syntax
dic={'a':1,'b':2,'c':3,'d':4}
dic
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
dic.pop()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    dic.pop()
TypeError: pop expected at least 1 argument, got 0
dic.update()
dic
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
dic['a']=22
dic
{'a': 22, 'b': 2, 'c': 3, 'd': 4}
dic()=11
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
dic[]=11
SyntaxError: invalid syntax
dic('a')=11
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
dic.update({})
dic
{'a': 22, 'b': 2, 'c': 3, 'd': 4}
dic.update('a':'a')
SyntaxError: invalid syntax
dic.update({'a':'a'})
dic
{'a': 'a', 'b': 2, 'c': 3, 'd': 4}
dic={'a':1,'b':2}
dic.update({'a':11,'b':22,'c':33,'d':44,'e':55})
dic
{'a': 11, 'b': 22, 'c': 33, 'd': 44, 'e': 55}



#pop()
dic.pop()
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    dic.pop()
TypeError: pop expected at least 1 argument, got 0
dic.pop('e')
55
dic.pop('z')
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    dic.pop('z')
KeyError: 'z'
dic.pop(1)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    dic.pop(1)
KeyError: 1





#popitem()

dic
{'a': 11, 'b': 22, 'c': 33, 'd': 44}
dic={'a': 11, 'b': 22, 'c': 33, 'd': 44}
dic
{'a': 11, 'b': 22, 'c': 33, 'd': 44}
dic.popitem()
('d', 44)
dic.popitem()
('c', 33)
dic.popitem(1)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    dic.popitem(1)
TypeError: dict.popitem() takes no arguments (1 given)
dic.pop()
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    dic.pop()
TypeError: pop expected at least 1 argument, got 0
dic.pop()
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    dic.pop()
TypeError: pop expected at least 1 argument, got 0
dic.popitem()
('b', 22)

dic.popitem()
('a', 11)
dic.popitem()
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    dic.popitem()
KeyError: 'popitem(): dictionary is empty'




>>> 
>>> #clear()
>>> 
>>> 
>>> 
>>> dic={'a':1,'b':2,'c':3}
>>> dic
{'a': 1, 'b': 2, 'c': 3}
>>> dic.clear(1)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    dic.clear(1)
TypeError: dict.clear() takes no arguments (1 given)
>>> dic.clear()
>>> dic
{}
>>> 
>>> 
>>> 
>>> 
>>> dic={'chennai':['vadapalani','marina beach'],'madurai':['temple','porota'],'thoothukudi':['salt','beach']}
>>> dic
{'chennai': ['vadapalani', 'marina beach'], 'madurai': ['temple', 'porota'], 'thoothukudi': ['salt', 'beach']}
>>> dic['chennai']
['vadapalani', 'marina beach']
>>> dic['chennai'].append(['arumbakkam'])
>>> dic
{'chennai': ['vadapalani', 'marina beach', ['arumbakkam']], 'madurai': ['temple', 'porota'], 'thoothukudi': ['salt', 'beach']}
>>> dic['chennai'].append('arumbakkam')
>>> dic
{'chennai': ['vadapalani', 'marina beach', ['arumbakkam'], 'arumbakkam'], 'madurai': ['temple', 'porota'], 'thoothukudi': ['salt', 'beach']}
>>> dic['m,adurai']
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    dic['m,adurai']
KeyError: 'm,adurai'
>>> dic['madurai']
['temple', 'porota']
>>> dic['madurai'].popitem()
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    dic['madurai'].popitem()
AttributeError: 'list' object has no attribute 'popitem'
dic['madurai'][0]
'temple'
dic['madurai'][0].pop()
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    dic['madurai'][0].pop()
AttributeError: 'str' object has no attribute 'pop'
#tmpl


dic['madurai'][0].replace('e','')
'tmpl'
