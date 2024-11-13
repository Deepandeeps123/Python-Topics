Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
help(key)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    help(key)
NameError: name 'key' is not defined
help('key')
No Python documentation found for 'key'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help('key function')
No Python documentation found for 'key function'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

lst=[1,10,2,20,3,30]
lst.sort()
lst
[1, 2, 3, 10, 20, 30]
lst.sort(reverse=True)
lst
[30, 20, 10, 3, 2, 1]
lst=['apple','Apple','orange','Orange','facebook','Facebook']
lst.sort()
lst
['Apple', 'Facebook', 'Orange', 'apple', 'facebook', 'orange']
lst.sort(reverse=True)
lst
['orange', 'facebook', 'apple', 'Orange', 'Facebook', 'Apple']
lst=['1','2','3','apple','orange','Apple','Orange']
lst.sort()
lst
['1', '2', '3', 'Apple', 'Orange', 'apple', 'orange']
lst.sort(reverse=True)
lst
['orange', 'apple', 'Orange', 'Apple', '3', '2', '1']
lst=[1,2,3,'apple','Apple']
lst.sort()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    lst.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
lst=['aa','bbb','cccc','d']
lst.sort()
lst
['aa', 'bbb', 'cccc', 'd']
lst.sort(reverse=True)
lst
['d', 'cccc', 'bbb', 'aa']
lst.sort(key=len)
lst
['d', 'aa', 'bbb', 'cccc']
lst.sort(key=len,reverse=True)
lst
['cccc', 'bbb', 'aa', 'd']
lst=['apple','Apple','facebook','Facebook']
lst.sort()
lst
['Apple', 'Facebook', 'apple', 'facebook']
lst.sort(reverse=True)
lst
['facebook', 'apple', 'Facebook', 'Apple']
lst.sort(key=len)
lst
['apple', 'Apple', 'facebook', 'Facebook']
lst.sort(upper())
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    lst.sort(upper())
NameError: name 'upper' is not defined. Did you mean: 'super'?
lst.sort(key=len.upper())
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    lst.sort(key=len.upper())
AttributeError: 'builtin_function_or_method' object has no attribute 'upper'
lst.sort(key=str.upper())
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    lst.sort(key=str.upper())
TypeError: unbound method str.upper() needs an argument
lst.sort(key=str.upper)
lst
['apple', 'Apple', 'facebook', 'Facebook']
lst.sort(key=list.upper)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    lst.sort(key=list.upper)
AttributeError: type object 'list' has no attribute 'upper'
lst.sort(key=lst.upper)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    lst.sort(key=lst.upper)
AttributeError: 'list' object has no attribute 'upper'
lst,sort(key=str.lower)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    lst,sort(key=str.lower)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
lst.sort(key=str.lower)
lst
['apple', 'Apple', 'facebook', 'Facebook']
lst=['aPple','apple','Apple','facebook','Facebook']
lst.sort(key=str.upper)
lst
['aPple', 'apple', 'Apple', 'facebook', 'Facebook']
lst.sort(key=str.lower)
lst
['aPple', 'apple', 'Apple', 'facebook', 'Facebook']
lst.sort()
lst
['Apple', 'Facebook', 'aPple', 'apple', 'facebook']
lst.sort(key=str.count)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    lst.sort(key=str.count)
TypeError: count() takes at least 1 argument (0 given)
lst.sort(key=str.count(p))
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    lst.sort(key=str.count(p))
NameError: name 'p' is not defined






#copy


str='1,2,3,4,5'
str2=str
str
'1,2,3,4,5'
str2
'1,2,3,4,5'
str='hello,hi'
str
'hello,hi'
lst['hello,hi']
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    lst['hello,hi']
TypeError: list indices must be integers or slices, not str
lst['hello','hi']
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    lst['hello','hi']
TypeError: list indices must be integers or slices, not tuple
lst=['hello,hi']
lst
['hello,hi']
lst=['hello','hi']
lst
['hello', 'hi']
lst[0]
'hello'
lst=['hello,hi']
lst[0]
'hello,hi'
lst[1]
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    lst[1]
IndexError: list index out of range
+
SyntaxError: invalid syntax




lst=[1,2,3,4,5]
lst2
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    lst2
NameError: name 'lst2' is not defined. Did you mean: 'lst'?
lsr
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    lsr
NameError: name 'lsr' is not defined. Did you mean: 'lst'?
lst
[1, 2, 3, 4, 5]
lst2=lst
lst
[1, 2, 3, 4, 5]
lst2
[1, 2, 3, 4, 5]
lst[0]
1
lst[1]
2
lst[]
SyntaxError: invalid syntax
lst[2]
3
lst[3]
4
lst[4]
5
lst=[1,2,3,[4,5,6]]
lst[1]
2
lst[2]
3
lst[3]
[4, 5, 6]
lst[3][0]
4
lst[3][1]
5
lst[3][2]
6
lst[3].pop()
6
lst2=lst
lst
[1, 2, 3, [4, 5]]
lst2
[1, 2, 3, [4, 5]]
lst=55
lst
55
lst=[1,2,3,[4,5,6]]
lst[3]=33
lst
[1, 2, 3, 33]
lst2
[1, 2, 3, [4, 5]]
lst=[1,2,3,[4,5,6]]
lst2=lst
lst
[1, 2, 3, [4, 5, 6]]
lst2
[1, 2, 3, [4, 5, 6]]
lst[3]=33
lst
[1, 2, 3, 33]
lst2
[1, 2, 3, 33]




#copy()

lst=[1,2,4,5,9]
lst2=lst.copy()
lst
[1, 2, 4, 5, 9]
lst2
[1, 2, 4, 5, 9]
id(list)
140735013529200
id(lst2)
2887000359872
id(lst)
2887000281856
lst[2]=44
lst
[1, 2, 44, 5, 9]
lst2
[1, 2, 4, 5, 9]
lst=[1,2,3,[4,5,6]]
lst2=lst.copy()
lst
[1, 2, 3, [4, 5, 6]]
lst2
[1, 2, 3, [4, 5, 6]]
lst[0]=11
lst
[11, 2, 3, [4, 5, 6]]
lst[1]=22
lst
[11, 22, 3, [4, 5, 6]]
lst[2]
3
lst[2]=33
lst
[11, 22, 33, [4, 5, 6]]
lst2
[1, 2, 3, [4, 5, 6]]
lsy1
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    lsy1
NameError: name 'lsy1' is not defined
lst
[11, 22, 33, [4, 5, 6]]
lst[3]=44
lst
[11, 22, 33, 44]
lst2
[1, 2, 3, [4, 5, 6]]
lst2[3][0]=44
lst2
[1, 2, 3, [44, 5, 6]]
lst
[11, 22, 33, 44]
lst=[1,2,3,[4,5,6]]
lst2[3][0]=44
lst2
[1, 2, 3, [44, 5, 6]]
lst
[1, 2, 3, [4, 5, 6]]
lst=[1,2,3,[4,5,6]]
lst[3][0]=44
lst
[1, 2, 3, [44, 5, 6]]
lst2
[1, 2, 3, [44, 5, 6]]
lst=[1,2,3,[4,5,6]]
lst2[3][0]=44
lst2
[1, 2, 3, [44, 5, 6]]
lst
[1, 2, 3, [4, 5, 6]]
lst=[1,2,3,[4,5,6]]
lst2.lst.copy()
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    lst2.lst.copy()
AttributeError: 'list' object has no attribute 'lst'
lst=lst.copy()
lst2[3][0]=44
lst2
[1, 2, 3, [44, 5, 6]]
lst
[1, 2, 3, [4, 5, 6]]
lst=[1,2,3,[4,5,6]]
lst2=lst.copy()
lst[3][0]=44
lst
[1, 2, 3, [44, 5, 6]]
lst2
[1, 2, 3, [44, 5, 6]]



#deepcopy()

lst=[1,2,3,'hello','hi']
lst2=lst
lst[3]='bye'
lst
[1, 2, 3, 'bye', 'hi']
lst2
[1, 2, 3, 'bye', 'hi']
lst=lst.copy()
lst[3]='hello'
lst
[1, 2, 3, 'hello', 'hi']
lst2
[1, 2, 3, 'bye', 'hi']
lst2=lst.copy()
lst
[1, 2, 3, 'hello', 'hi']
lst2
[1, 2, 3, 'hello', 'hi']
lst[3]='hey'
lst
[1, 2, 3, 'hey', 'hi']
lst2
[1, 2, 3, 'hello', 'hi']
lst=[1,2,['hello','bye']
     ]
lst
[1, 2, ['hello', 'bye']]
lst2
[1, 2, 3, 'hello', 'hi']
lst2=lst.copy()
lst2
[1, 2, ['hello', 'bye']]
lst[2]='hi'
lst
[1, 2, 'hi']
lst2
[1, 2, ['hello', 'bye']]
lst[0]=1111
lst
[1111, 2, 'hi']
lst2
[1, 2, ['hello', 'bye']]
lst=[1,2,['hello','bye']
     ]
lst2=lst.copy()
lst
[1, 2, ['hello', 'bye']]
lst2
[1, 2, ['hello', 'bye']]
id(lst)
2887000363968
id(lst2)
2887000281856
id(lst[1]
   )
140735014701528
id(lst2[1])
140735014701528
id(lst[2])
2887000369728
id(lst[2])
2887000369728
lst=[1,2,3,[4,5,6]]
lst2=lst.copy()
lst
[1, 2, 3, [4, 5, 6]]
lst2
[1, 2, 3, [4, 5, 6]]
lst[3][0]=44
lst
[1, 2, 3, [44, 5, 6]]
lst2
[1, 2, 3, [44, 5, 6]]
lst=[1,2,['hello','hi]]
          
SyntaxError: unterminated string literal (detected at line 1)
lst=[1,2,['hello','hi']]
          
lst2=lst.copy()
          
lst[3][0]='bye'
          
Traceback (most recent call last):
  File "<pyshell#235>", line 1, in <module>
    lst[3][0]='bye'
IndexError: list index out of range
lst[2][0]
          
'hello'
lst[2][0]='bye'
          
lst
          
[1, 2, ['bye', 'hi']]
lst2
          
[1, 2, ['bye', 'hi']]





#deepcopy()
          

lst=[1,2,3,[4,5,6]]
          
lst2=lst.deepcopy()
          
Traceback (most recent call last):
  File "<pyshell#248>", line 1, in <module>
    lst2=lst.deepcopy()
AttributeError: 'list' object has no attribute 'deepcopy'


from i
KeyboardInterrupt
KeyboardInterrupt
from ['orange', 'apple', 'Orange', 'Apple', '3', '2', '1']
          
SyntaxError: invalid syntax




from copy import deepcopy
          
lst=[1,2,3,[4,5,6]]
          
lst2=lst.deepcopy()
          
Traceback (most recent call last):
  File "<pyshell#255>", line 1, in <module>
    lst2=lst.deepcopy()
AttributeError: 'list' object has no attribute 'deepcopy'
lst2=deepcopy(lst)
          
lst
          
[1, 2, 3, [4, 5, 6]]
lst2
          
[1, 2, 3, [4, 5, 6]]
lst[0]=11
          
lst
          
[11, 2, 3, [4, 5, 6]]
lst2
          
[1, 2, 3, [4, 5, 6]]
lst[2]=22
          
lst
          
[11, 2, 22, [4, 5, 6]]
lst2
          
[1, 2, 3, [4, 5, 6]]
lst2[0]=1111
          
lst2
          
[1111, 2, 3, [4, 5, 6]]
lst
          
[11, 2, 22, [4, 5, 6]]
lst[3]=4
          
lst
          
[11, 2, 22, 4]
lst[3]=[4,5,6]
          
lst
          
[11, 2, 22, [4, 5, 6]]
lst[3]=[7,8,9]
          
lst
          
[11, 2, 22, [7, 8, 9]]


lst=[1,2,3,[4,5,6]]
          
lst.append(7)
          
lst
          
[1, 2, 3, [4, 5, 6], 7]
>>> lst2
...           
[1111, 2, 3, [4, 5, 6]]
>>> lst=[1,2,3,[4,5,6]]
...           
>>> from copy import deepcopy
...           
>>> lst=[1,2,3,[4,5,6]]
...           
>>> lst.append(7)
...           
>>> lst
...           
[1, 2, 3, [4, 5, 6], 7]
>>> lst2
...           
[1111, 2, 3, [4, 5, 6]]
>>> lst2=deepcopy(lst)
...           
>>> lst2
...           
[1, 2, 3, [4, 5, 6], 7]
>>> lst.extend(7)
...           
Traceback (most recent call last):
  File "<pyshell#287>", line 1, in <module>
    lst.extend(7)
TypeError: 'int' object is not iterable
>>> lst[3].pop()
...           
6
>>> lst[1]=22
...           
>>> lst
...           
[1, 22, 3, [4, 5], 7]
>>> lst2
...           
[1, 2, 3, [4, 5, 6], 7]
