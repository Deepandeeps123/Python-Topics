Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# TUPLE()


a=1,2,3,4
a
(1, 2, 3, 4)
type(a)
<class 'tuple'>
a='hello'
a
'hello'
type(a)
<class 'str'>
a=hello
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a=hello
NameError: name 'hello' is not defined. Did you mean: 'help'?
a=1,2,3,4,5,1,2,3,4,5
a
(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
type(a)
<class 'tuple'>
s=
SyntaxError: invalid syntax
s=()
s
()
type(s)
<class 'tuple'>
a=1,2,3,'hello'
a
(1, 2, 3, 'hello')
s='hello
SyntaxError: unterminated string literal (detected at line 1)
s='hello'
s
'hello'
s=(1,2,3,'hello','good',10+2j)
s
(1, 2, 3, 'hello', 'good', (10+2j))
type(s)
<class 'tuple'>
s[1]
2
s[0]
1
s[3
]
'hello'
s[0]
1
s[1]
2
s[2]
3
s[3]
'hello'
s[4]
'good'
s[5]
(10+2j)
s[6]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    s[6]
IndexError: tuple index out of range
s[2]=33
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s[2]=33
TypeError: 'tuple' object does not support item assignment
s[1:5:2]
(2, 'hello')
s[3][2].swapcae().islower
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s[3][2].swapcae().islower
AttributeError: 'str' object has no attribute 'swapcae'. Did you mean: 'swapcase'?
s[3][2].swapcae().islower()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    s[3][2].swapcae().islower()
AttributeError: 'str' object has no attribute 'swapcae'. Did you mean: 'swapcase'?
a[3][2].swapcase().islower()
False
a[4].split()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a[4].split()
IndexError: tuple index out of range
s[4].split()
['good']
a[4]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a[4]
IndexError: tuple index out of range
s[4]
'good'
s[4].split()
['good']
s[4].split().append(100)

s
(1, 2, 3, 'hello', 'good', (10+2j))
b=a[4].split().append(100)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    b=a[4].split().append(100)
IndexError: tuple index out of range





#method tuple


s=('1,2,3,4,5)
   
SyntaxError: unterminated string literal (detected at line 1)
s=1,2,3,4,5
   
s
   
(1, 2, 3, 4, 5)
s.index(2)
   
1
s.index(10)
   
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    s.index(10)
ValueError: tuple.index(x): x not in tuple
a=(1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9)
   
s.index()]
SyntaxError: unmatched ']'
s.index()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    s.index()
TypeError: index expected at least 1 argument, got 0
s.index(1,6)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    s.index(1,6)
ValueError: tuple.index(x): x not in tuple
s.index(1)
0
s.index(1,6)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    s.index(1,6)
ValueError: tuple.index(x): x not in tuple
a.index(10)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a.index(10)
ValueError: tuple.index(x): x not in tuple
a.index(1,6)
9
a[::2]
(1, 3, 5, 7, 9, 2, 4, 6, 8)
a[::2].index(1)
0
a.index(1,6,6)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a.index(1,6,6)
ValueError: tuple.index(x): x not in tuple
a.index(1,6,16)
9
a.index(8,8,16)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a.index(8,8,16)
ValueError: tuple.index(x): x not in tuple
a.index(5,3,16)
4
a[3:13].index(5)
1





#count()
s=('apple','orangr',['tamarind','facebook'],3,4,5,6)
s.count(3)
1
s.count('a')
0
s.count()
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    s.count()
TypeError: tuple.count() takes exactly one argument (0 given)
s.count('facebook',2,4)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    s.count('facebook',2,4)
TypeError: tuple.count() takes exactly one argument (3 given)
s.count('facebook')
0
s[1].count('facebook')
0
s[2].count('facebook')
1
lst[10]
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    lst[10]
NameError: name 'lst' is not defined. Did you mean: 'list'?
lst=[10]
lst
[10]
type(lst)
<class 'list'>
a=(10)
a
10
typ(a)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    typ(a)
NameError: name 'typ' is not defined. Did you mean: 'type'?
type(a)
<class 'int'>
a=(10,)
a
(10,)
type(a)
<class 'tuple'>
a=(hello)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    a=(hello)
NameError: name 'hello' is not defined. Did you mean: 'help'?
a='hello',
a
('hello',)
type(a)
<class 'tuple'>
a='hello'
a
'hello'
type(a)
<class 'str'>
a={10}
a
{10}
type(a)
<class 'set'>






#set



s={1,10.2,True,10+2j,'hello',(4,5,6)}
s
{(10+2j), 1, (4, 5, 6), 'hello', 10.2}
s[1]
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    s[1]
TypeError: 'set' object is not subscriptable
s[0]
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
s={1,2,3,6,7}
s
{1, 2, 3, 6, 7}
s{1}
SyntaxError: invalid syntax
s[1]
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    s[1]
TypeError: 'set' object is not subscriptable
s={1,2,3,[4,5,6]}
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    s={1,2,3,[4,5,6]}
TypeError: unhashable type: 'list'
s={1,2,3,{4,5,6}}
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    s={1,2,3,{4,5,6}}
TypeError: unhashable type: 'set'
s={10}
s
{10}
s={1,true}
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    s={1,true}
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> s={1,True}
>>> s
{1}
>>> s={True,1}
>>> s
{True}
>>> s={1,False,0,True}
>>> s
{False, 1}
>>> s=set()
>>> s
set()
>>> s={1,False,0,True}
>>> s()
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    s()
TypeError: 'set' object is not callable
>>> s=()
>>> s
()
>>> type(s)
<class 'tuple'>
>>> s={}
>>> s
{}
>>> type(a)
<class 'set'>
>>> a=str()
>>> a
''
>>> b=list()
>>> b
[]
>>> c=tuple()
>>> c
()
>>> d=set()
>>> d
set()
