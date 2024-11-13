Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dic = {'a':1,'b':2,'c':3,'d':4}
dic
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
dic['a']=11
dic
{'a': 11, 'b': 2, 'c': 3, 'd': 4}
dic.update('a')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    dic.update('a')
ValueError: dictionary update sequence element #0 has length 1; 2 is required
dic.update({'a'})
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    dic.update({'a'})
ValueError: dictionary update sequence element #0 has length 1; 2 is required
dic.update({100})
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    dic.update({100})
TypeError: cannot convert dictionary update sequence element #0 to a sequence
dic.update({'e':5})
dic
{'a': 11, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dic.setdefault('a')
11
dic={'iphone':15,'iqoo':7,'readme':9}
>>> dic
{'iphone': 15, 'iqoo': 7, 'readme': 9}
>>> dic.setdefault(7)
>>> dic
{'iphone': 15, 'iqoo': 7, 'readme': 9, 7: None}
>>> lst=[1,2,3,4,5,6,7,8]
>>> n=lst.pop(),lst.append()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    n=lst.pop(),lst.append()
TypeError: list.append() takes exactly one argument (0 given)
>>> n=lst.pop(),lst.append(len(lst))
>>> n
(7, None)
>>> lst.append(lst.extend(lst[::2]))
>>> lst
[1, 2, 3, 4, 5, 6, 6, 1, 3, 5, 6, None]
>>> lst.append(lst.pop(lst[0]))
>>> lst
[1, 3, 4, 5, 6, 6, 1, 3, 5, 6, None, 2]
>>> dic={'iphone':15,'iqoo':7,'readme':9}
>>> dic
{'iphone': 15, 'iqoo': 7, 'readme': 9}
>>> 
>>> 
>>> 
>>> #fromkeys()
>>> 
>>> lst={'pubg','freefire','cod','ludo','coc'}
>>> lst
{'pubg', 'cod', 'ludo', 'coc', 'freefire'}
>>> dict.fromkeys()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    dict.fromkeys()
TypeError: fromkeys expected at least 1 argument, got 0
>>> dict.fromkeys('none')
{'n': None, 'o': None, 'e': None}
>>> dict.fromkeys(lst)
{'pubg': None, 'cod': None, 'ludo': None, 'coc': None, 'freefire': None}
