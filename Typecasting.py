Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#type casting


#int

a=10
in(a)]
SyntaxError: unmatched ']'
int(a)
10
float(a)
10.0
boolean(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    boolean(a)
NameError: name 'boolean' is not defined
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
a=10,20
int(a)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
list(a)
[10, 20]
type(a)
<class 'tuple'>
int(a)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(a)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(a)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    complex(a)
TypeError: complex() first argument must be a string or a number, not 'tuple'
bool(a)
True
str(a)
'(10, 20)'
list(a)
[10, 20]
set(a)
{10, 20}
tuple(a)
(10, 20)
dict(a)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    dict(a)
TypeError: cannot convert dictionary update sequence element #0 to a sequence


a=10
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable





#float



f=10.23
type(f)
<class 'float'>
int(a)
10
int(f)
10
float(f)
10.23
bool(f)
True
complex(f)
(10.23+0j)
c0mplex(a,a)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    c0mplex(a,a)
NameError: name 'c0mplex' is not defined. Did you mean: 'complex'?
complex(f,f)
(10.23+10.23j)
complex(f,f,f)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    complex(f,f,f)
TypeError: complex() takes at most 2 arguments (3 given)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
str(f)
'10.23'
list(f)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    list(f)
TypeError: 'float' object is not iterable
set(f)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    set(f)
TypeError: 'float' object is not iterable
tuple(f)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    tuple(f)
TypeError: 'float' object is not iterable
dict(f)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    dict(f)
TypeError: 'float' object is not iterable



a=10.23,10.46
a
(10.23, 10.46)
type(a)
<class 'tuple'>
int(a)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(a)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(a)]
SyntaxError: unmatched ']'
complex(a)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    complex(a)
TypeError: complex() first argument must be a string or a number, not 'tuple'
bool(a)
True
str(a)
'(10.23, 10.46)'
list(a)
[10.23, 10.46]
tuple(a)
(10.23, 10.46)
set(a)
{10.23, 10.46}
dict(a)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    dict(a)
TypeError: cannot convert dictionary update sequence element #0 to a sequence




#boolean


a=True
int(a)
1
a=False
int(a)
0
a=None
int(a)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'
a=True
int(a)
1
float(a)
1.0
bool(a)
True
complex(a)
(1+0j)
complex(100,100)
(100+100j)



str(a)
'True'
list(a)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    list(a)
TypeError: 'bool' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    set(a)
TypeError: 'bool' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    tuple(a)
TypeError: 'bool' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    dict(a)
TypeError: 'bool' object is not iterable
a=True,True
int(a)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(a)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(a)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    complex(a)
TypeError: complex() first argument must be a string or a number, not 'tuple'
bool(a)
True
str(a)
'(True, True)'
list(a)
[True, True]
set(a)
{True}
tuple(a)
(True, True)
dict(a)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    dict(a)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
type(a)
<class 'tuple'>



#complex



a=10
complex(a)
(10+0j)
int(a)
10
a=10+2j
type(a)
<class 'complex'>
int(a)
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(a)
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'complex'
complex(a)
(10+2j)
bool(a)
True
str(a)
'(10+2j)'
list(a)
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    list(a)
TypeError: 'complex' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    set(a)
TypeError: 'complex' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    tuple(a)
TypeError: 'complex' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    dict(a)
TypeError: 'complex' object is not iterable





a=10+2j,20+4j
type(a)
<class 'tuple'>
int(a)
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(a)
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'tuple'
bool(a)
True
str(a)
'((10+2j), (20+4j))'
list(a)
[(10+2j), (20+4j)]
set(a)
{(10+2j), (20+4j)}
tuple(a)
((10+2j), (20+4j))
dict(a)
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    dict(a)
TypeError: cannot convert dictionary update sequence element #0 to a sequence





#string()

a='hello'
int(a)
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    int(a)
ValueError: invalid literal for int() with base 10: 'hello'
float(a)
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    float(a)
ValueError: could not convert string to float: 'hello'
complex(a)
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    complex(a)
ValueError: complex() arg is a malformed string
bool(a)
True
list(a)
['h', 'e', 'l', 'l', 'o']



a='10'
int(a)
10
float(a)
10.0
complex(a)
(10+0j)
bool(a)
True
complex(a,a)
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    complex(a,a)
TypeError: complex() can't take second arg if first is a string
complex(a,10)
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    complex(a,10)
TypeError: complex() can't take second arg if first is a string
complex(10,a)
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    complex(10,a)
TypeError: complex() second arg can't be a string
a='10','10'
complex(a)
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    complex(a)
TypeError: complex() first argument must be a string or a number, not 'tuple'
complex(a,a)
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    complex(a,a)
TypeError: complex() first argument must be a string or a number, not 'tuple'
a='hi'
complex(a)
Traceback (most recent call last):
  File "<pyshell#178>", line 1, in <module>
    complex(a)
ValueError: complex() arg is a malformed string
s='
SyntaxError: unterminated string literal (detected at line 1)
s='10.23'
int(s)
Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: '10.23'
complex(a)
Traceback (most recent call last):
  File "<pyshell#182>", line 1, in <module>
    complex(a)
ValueError: complex() arg is a malformed string
bool(a)
True
str(a)
'hi'
a='10.23'
int(a)
Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    int(a)
ValueError: invalid literal for int() with base 10: '10.23'
complex(a)
(10.23+0j)
>>> complex(s,s)
Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    complex(s,s)
TypeError: complex() can't take second arg if first is a string
>>> bool(a)
True
>>> s='hello'
>>> str(a)
'10.23'
>>> list(a)
['1', '0', '.', '2', '3']
>>> tuple(a)
('1', '0', '.', '2', '3')
>>> set(a)
{'1', '3', '0', '2', '.'}
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#195>", line 1, in <module>
    dict(a)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> 
>>> 
>>> 
>>> 
>>> a='hello'
>>> list(a)
['h', 'e', 'l', 'l', 'o']
>>> set(a)
{'e', 'l', 'h', 'o'}
>>> tuple(a)
('h', 'e', 'l', 'l', 'o')
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#204>", line 1, in <module>
    dict(a)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> s='1234'
>>> list(s)
['1', '2', '3', '4']
