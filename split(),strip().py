Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='hello every one'
s.split()
['hello', 'every', 'one']
s.split(,1)
SyntaxError: invalid syntax
s.split('',1)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    s.split('',1)
ValueError: empty separator
s.split(' ',1)
['hello', 'every one']
s.split(' ',2)
['hello', 'every', 'one']
s.split(' ',3)
['hello', 'every', 'one']
s.split(' ',4)
['hello', 'every', 'one']
s.split('o')
['hell', ' every ', 'ne']
s='malayalam'
s.split('ma')
['', 'layalam']
s.split('ma',4)
['', 'layalam']
s.split('a',4)
['m', 'l', 'y', 'l', 'm']
s,split('a',1)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s,split('a',1)
NameError: name 'split' is not defined
s.split('a',1)
['m', 'layalam']
s.split('a',2)
['m', 'l', 'yalam']
s.split('a',3)
['m', 'l', 'y', 'lam']
s.split('3')
['malayalam']
s.split('e',2)
['malayalam']
s.replace('y','Y')[::2]
'mlYlm'
s.replace('y','
          
SyntaxError: unterminated string literal (detected at line 1)
s.replace('y','Y')[::-2]
          
'mlYlm'
s='the question of the answer to be calculate in answer sheet')
SyntaxError: unmatched ')'
s='the question of the answer to be calculate in answer sheet'
s.split(' ')
['the', 'question', 'of', 'the', 'answer', 'to', 'be', 'calculate', 'in', 'answer', 'sheet']





#rsplit()
s='hello every one'
s.split()
['hello', 'every', 'one']
s.rsplit()
['hello', 'every', 'one']
s.split(' ',1)
['hello', 'every one']
\
s.rsplit(' ',1)
['hello every', 'one']
s='python'
s[::2]
'pto'
s[::2].split().swapcase()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s[::2].split().swapcase()
AttributeError: 'list' object has no attribute 'swapcase'
s[::2].split()
['pto']
s.swapcase[::2]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    s.swapcase[::2]
TypeError: 'builtin_function_or_method' object is not subscriptable
s[::2].swapcase()
'PTO'
s.swapcase()[::2]
'PTO'
s='hello every one'
s.upper()
'HELLO EVERY ONE'
s.lower()
'hello every one'
s.swapcase()
'HELLO EVERY ONE'
s.find()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    s.find()
TypeError: find() takes at least 1 argument (0 given)
s.find('e')
1
s.index('e')
1
s.count(' ')
2
s.count('d')
0
s.upper().replace('M','@').count('d')
0











#strip()



s='@@@@@@hello@@@@@@'
s.strip('@')
'hello'
>>> s='@@@@@@@@h@e@l@l@o@@@@@@@@@@'
>>> s.strip('@')
'h@e@l@l@o'
>>> s.strip()
'@@@@@@@@h@e@l@l@o@@@@@@@@@@'
>>> s.strip(' ')
'@@@@@@@@h@e@l@l@o@@@@@@@@@@'
>>> s='______hello________'
>>> s.strip()
'______hello________'
>>> s.strip(' ')
'______hello________'
>>> s.strip('a')
'______hello________'
>>> s.strip('1')
'______hello________'
>>> s.strip()
'______hello________'
>>> s.strip( )
'______hello________'
>>> s.strip('')
'______hello________'
>>> s='__hello__'
>>> s.strip()
'__hello__'
>>> s='@@@@@@@@@@@@hello@@@@@@@@@@'
>>> s.lstrip()
'@@@@@@@@@@@@hello@@@@@@@@@@'
>>> s.lstrip('@')
'hello@@@@@@@@@@'
>>> s='______hello________'
>>> s.strip('_')
'hello'
>>> --s='@@@@@@@@@@@@hello@@@@@@@@@@'
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> s='@@@@@@@@@@@@hello@@@@@@@@@@'
>>> s.rstrip()
'@@@@@@@@@@@@hello@@@@@@@@@@'
>>> s.rstrip('@')
'@@@@@@@@@@@@hello'
