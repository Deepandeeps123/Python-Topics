Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='python'
s.index('o')
4
s.index(1)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s.index(1)
TypeError: must be str, not int
1='python'
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
=='python'
SyntaxError: invalid syntax
s.index(1)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s.index(1)
TypeError: must be str, not int
s.index('p')
0
s.index('y')
1
s.index('t')
2
s.index('h')
3
s.index()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s.index()
TypeError: index() takes at least 1 argument (0 given)
s.index()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s.index()
TypeError: index() takes at least 1 argument (0 given)
s.index('python')
0
s[::].index('y')
1
s.index('o',5,6)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s.index('o',5,6)
ValueError: substring not found
s.index('o',5,6)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s.index('o',5,6)
ValueError: substring not found
s.index('e',0)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s.index('e',0)
ValueError: substring not found
s.index('o',2)
4
s.index('l')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s.index('l')
ValueError: substring not found
s='hello python'
s.index('l')
2
s.index('h')
0
s.index('e')
1
s,index('l')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s,index('l')
NameError: name 'index' is not defined
s.index('l')
2
s.index('l',3)
3
s.index('o'0
        
SyntaxError: '(' was never closed
s.index('o'0
        
SyntaxError: '(' was never closed

s.index('o')
        
4
s.index('p')
        
6
s.index('y')
        
7

s.index('t')
        
8
s.index('h')
        
0
s.index('h',1)
        
9
s.index('o',3)
        
4
s.index('o
        
SyntaxError: unterminated string literal (detected at line 1)
s.index('o',6)
        
10
s.index('n')
        
11





#rindex()
        

s='hello every one'
        
s[:12].index('o')
        
4
s[12:].index('o')
        
0
s.index('o',12)
        
12
s.rindex('o')
        
12
s.index('y')
        
10
s.index('y')
        
10
s.rindex('e',4,8)
        
6
s.index('z')
        
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    s.index('z')
ValueError: substring not found
s.rindex('z')
        
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    s.rindex('z')
ValueError: substring not found







#find()
        



s='hello'
        
s.find('e')
        
1
s.index('e')
        
1
s.rindex('e')
        
1
s.index('o')
        
4
s.rindex('o')
        
4
s.find('o')
        
4
s='the question of the values'
        
s.index('s')
        
7
s.rindex('s')
        
25
s='hello;
        
SyntaxError: unterminated string literal (detected at line 1)
s='hello'
        
4
s.find('z')
        
-1
s.find('')
        
0
s.find()
        
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    s.find()
TypeError: find() takes at least 1 argument (0 given)


s='hello every one'
        
s.find('o')
        
4
s.index('o')
        
4
s.rindex('o')
        
12
s.rfind('o')
        
12


s.index('
        
SyntaxError: unterminated string literal (detected at line 1)
s.index('x')
        
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    s.index('x')
ValueError: substring not found
s.rindex('x')
        
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    s.rindex('x')
ValueError: substring not found
s.find('x')
        
-1
s.rfind('x')
        
-1
s.rfind('e')
        
14
s.rindex('2')
        
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    s.rindex('2')
ValueError: substring not found
s.rfind('y')
        
10





#count()
        

s='malayalam'
        
s.index('a')
        
1
s.rindex('a')
        
7
s.find('a')
        
1
s.rfind('a')
        
7
s.count('a')
        
4
s.count('a',2,7)
        
2
s.count('e')
        
0
s.count('la')
        
2
s.count('lam')
        
1
s.count('aaaa')
        
0
s.count('a'),2)
        
SyntaxError: unmatched ')'
s,count('a',2)
        
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    s,count('a',2)
NameError: name 'count' is not defined. Did you mean: 'round'?
s.count('a',2)
        
3
s.count('a',len(s)-3)
        
1
s.count('a',len(s))
        
0
s.count('a',0,len(s))
        
4
s.count('a',0,8,len(s)-2)
        
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    s.count('a',0,8,len(s)-2)
TypeError: count() takes at most 3 arguments (4 given)
s.count('a',0.len(s)-2)
        
SyntaxError: invalid decimal literal
s.count('a',0,len(s)-2)
        
3
s.count('la')
        
2





#replace()
        



s='malayalam'
        

s.replace('m','M')
        
'MalayalaM'
s.replace('a','A')
        
'mAlAyAlAm'
s.replace('l','L')
        
'maLayaLam'
>>> s.replace('s','w')
...         
'malayalam'
>>> s.replace('e')
...         
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    s.replace('e')
TypeError: replace expected at least 2 arguments, got 1
>>> s.replace('a','e',1)
...         
'melayalam'
>>> s.replace('a','e',2)
...         
'meleyalam'
>>> s.replace('a','e',3)
...         
'meleyelam'
>>> s.replace('a','e',4)
...         
'meleyelem'
>>> s.replace('a','e',5)
...         
'meleyelem'
>>> s.replace(::-1)
...         
SyntaxError: invalid syntax
>>> s[::-1]
...         
'malayalam'
>>> s.replace('a','e',2)[::-1]
...         
'malayelem'
>>> s.replace('a','A',3)[::-1]
...         
'malAyAlAm'
>>> s.replace('a','A',3)[::-3]
...         
'mAl'
