Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='hello'
s.upper(s)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s.upper(s)
TypeError: str.upper() takes no arguments (1 given)
upper(s)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    upper(s)
NameError: name 'upper' is not defined. Did you mean: 'super'?
s.upper()
'HELLO'
s='hElLo'
s.upper()
'HELLO'
s.upper
<built-in method upper of str object at 0x0000017E6B93DC50>
s.upper()
'HELLO'
s[4].upper;
<built-in method upper of str object at 0x00007FFF64D003A8>
s.[4].upper()
SyntaxError: invalid syntax
s[4].upper()
'O'
s[::].upper()
'HELLO'
s[:3],s[4].upper()
('hEl', 'O')
s='hello'
s
'hello'
s[:4][4].upper()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s[:4][4].upper()
IndexError: string index out of range
s[:3]s[4].upper()
SyntaxError: invalid syntax
s[:3],s[4].upper()
('hel', 'O')
s= 'he22o'
s.upper()
'HE22O'
s='@pple'
s.upper()
'@PPLE'
s='hell1232@'
s.upper()
'HELL1232@'
s[6]
'3'
s[0]
'h'
s[1:1:1]
''
s[1:2:3]
'e'
s[1:10:2]
'el22'






# lower ()



s='HELLO'
S.LOWER()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    S.LOWER()
NameError: name 'S' is not defined. Did you mean: 's'?
s='HELLO'
s.lower()
'hello'

s='hello'
s.lower()
'hello'
s= 'HeLlO'
s.lower()
'hello'
s='@#$$%^^^&HeLlO'
s.lower()
'@#$$%^^^&hello'
s='PYTHON'
s.lower()
'python'
s[1:4:3]
'Y'
s.lower()
'python'




# swapcase




s='HELLO'
s.swapcase()
'hello'
s='HeLlO'
s.swapcase()
'hElLo'
s='PyThOn EvErY OnE'
s.swapcase()
'pYtHoN eVeRy oNe'
s[1:6:1].swapcase()
'YtHoN'
s= '@#$$%^^HeLlo^&*&***(F4566767788hhhhh**&*('
s.swapcase()
'@#$$%^^hElLO^&*&***(f4566767788HHHHH**&*('







# capitalize



s='hello'
s.capitalize()
'Hello'
s='HELlo'
s.captilize()
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    s.captilize()
AttributeError: 'str' object has no attribute 'captilize'. Did you mean: 'capitalize'?
s.capitalize()
'Hello'
s='hello every one'
s.capitalize()
'Hello every one'
s[1:10:3].capitalize()
'Eov'
s[-1:-10:-2].capitalize()
'Eoyee'
s='@hello'
s.capitalize()
'@hello'
s='12Hello'
s.capitalize()
'12hello'
s='the question'
s.capitalize()
'The question'





#title()






s='hello'
s.title()
'Hello'
s='Hello'
s.title()
'Hello'
s='!@##$$$hello'
s.title()
'!@##$$$Hello'
s='@#Hello'
s.title()
'@#Hello'
s= 'in the program question is very difficult to solve the answer in apptitue question in interview'
s.title()
'In The Program Question Is Very Difficult To Solve The Answer In Apptitue Question In Interview'





#assignment




question = 'hello'
s[::]
'in the program question is very difficult to solve the answer in apptitue question in interview'
question[]
SyntaxError: invalid syntax
question[::]
'hello'
question[::-1]
'olleh'
question[::-1].
SyntaxError: invalid syntax
question[::-1].title()
'Olleh'



s='hello'
s[::-1].title()[::-1]
'hellO'
s[::-1].title()[::-1].title()
'Hello'




s='python'
s[::]
'python'
s[::-1]
'nohtyp'
s[::-1].title()[::-1]
'pythoN'




s='python programming'
s[::]
'python programming'
s[::-1]
'gnimmargorp nohtyp'
s[::-1].title()
'Gnimmargorp Nohtyp'
s[::-1].title s[::-1]
SyntaxError: invalid syntax
s[::-1].title() s[::-1]
SyntaxError: invalid syntax
s[::-1].title()[::-1]
'pythoN programminG'




s='heLlo pyThOn'
s.swapcase()
'HElLO PYtHoN'
s='heLlO pyThOn
SyntaxError: unterminated string literal (detected at line 1)
s='heLlO pyThOn'
s.swaocase()
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    s.swaocase()
AttributeError: 'str' object has no attribute 'swaocase'. Did you mean: 'swapcase'?
s.swapcase()
'HElLo PYtHoN'
s[0:11:2].swapcase()
'HloPto'




s='apple'
s.upper()
'APPLE'
s[::-1].upper()
'ELPPA'
s[::-1].upper()[2:6:2]
'PA'
a[::-1].upper()[3:6:2]
Traceback (most recent call last):
  File "<pyshell#182>", line 1, in <module>
    a[::-1].upper()[3:6:2]
NameError: name 'a' is not defined
>>> s[::-1].upper()[3:6:2]
'P'
>>> 
>>> 
>>> 
>>> s='mango'
>>> s[3:5]
'go'
>>> s[3:5].title()
'Go'
>>> 
>>> 
>>> 
>>> 
>>> s='hey dinga how are you'
>>> s.upper()
'HEY DINGA HOW ARE YOU'
>>> s[0:5:2]
'hyd'
>>> s[0:5:2].upper()
'HYD'
>>> 
>>> 
>>> 
>>> 
>>> s='india'
>>> s.upper()
'INDIA'
>>> s[0:3:2]
'id'
>>> s[0:4:2]
'id'
>>> s[0:5:2]
'ida'
>>> s[0:5:2].upper()
'IDA'
>>> 
>>> 
>>> 
