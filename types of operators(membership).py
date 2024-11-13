Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#in




s='qspiders'
s='Qspiders'
s[4].lower() in 'd'
True
s[4] in [d]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s[4] in [d]
NameError: name 'd' is not defined. Did you mean: 'id'?
s[4] in ['d]
         
SyntaxError: unterminated string literal (detected at line 1)
s[4] in ['d']
         
True
s[4] in s
         
True
s[4] in [s]
         
False
s[4].lower() in [s]
         
False
s.lower in s
         
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s.lower in s
TypeError: 'in <string>' requires string as left operand, not builtin_function_or_method
s[4].lower() in s
         
True


s[4] in {s}
         
False
s='hello'
         
s
         
'hello'
len(s)
         
5
s=['hello']
         
len(s)
         
1
s={'hello'}
         
len(s)
         
1
]
s=('hello')
len(s)
5
s[4] in (s)
True
s={'hello'}
len(s)
1
s[4] in s
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s[4] in s
TypeError: 'set' object is not subscriptable
s[4] in {s{
    
SyntaxError: '{' was never closed
s[4] in {s}
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s[4] in {s}
TypeError: 'set' object is not subscriptable






#is




a='hello'
b='hi'
c='good'
d='bye'
e='hello'
a is b
False
b is c
False
a is c
False
a is d
False
>>> a is e
True
>>> a= 10
>>> b=10
>>> a is b
True
>>> c= 100
>>> a is c
False
>>> b is c
False
>>> a is b
True
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #is not
>>> a= 10
>>> b=10
>>> c= 100
>>> a is b
True
>>> a is not b
False
>>> a is c
False
>>> a is c
False
>>> a is not c
True
>>> 
>>> 
>>> 10=10
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> 10==10
True
