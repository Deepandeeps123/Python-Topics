Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s= 'programming'
len(s)
11
s=[2]
s
[2]
s[2]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s[2]
IndexError: list index out of range
s[0]
2
s='programming'
s[0]
'p'
s[1]
'r'
s[2]
'o'
s[3]
'g'
s[4]
'r'
s[5]
'a'
s[6]
'm'
s[7]
'm'
len(s)
11
s[8]
'i'
s[9]
'n'
s[10]
'g'
s[11]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s[11]
IndexError: string index out of range
s=hello every one
SyntaxError: invalid syntax
s=hello
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s=hello
NameError: name 'hello' is not defined. Did you mean: 'help'?
s="""hello"""
s[10]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s[10]
IndexError: string index out of range
s[1]
'e'
s[]
SyntaxError: invalid syntax
s[]
SyntaxError: invalid syntax
s[:]
'hello'
s[::]
'hello'
s[-2]
'l'
s= 'programming'
s[-3]
'i'
s[-2,-2]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s[-2,-2]
TypeError: string indices must be integers, not 'tuple'
s[-17]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s[-17]
IndexError: string index out of range
s[-8]
'g'
s[-:]
SyntaxError: invalid syntax
s[-]
SyntaxError: invalid syntax
s[:]
'programming'
s[-:]
SyntaxError: invalid syntax
s[-4]
'm'
s[0]
'p'
s[-1]
'g'
s[-2]
'n'
s[-3]
'i'
s[-4]
'm'
s[-5]
'm'
s[-6]
'a'
s[-7]
'r'
s[-8]
'g'
s[-9]
'o'
s[-10]
'r'
s[-11]
'p'
s[0:0]
''
s[0:1]
'p'
s='hello'
s[0:2]
'he'
s='programming'
s[0:1]
'p'
s[0:2]
'pr'
s[0:3]
'pro'
s[0:4]
'prog'
s[0:5]
'progr'
s[0:6]
'progra'
s[0:7]
'program'
s[0:8]
'programm'
s[0:9]
'programmi'
s[0:10]
'programmin'
s[0:11]
'programming'
s[0:12]
'programming'
s[0:18]
'programming'
s[6:7]
'm'
s[0:19:1]
'programming'
s[0:11:2]
'pormig'
s[0:11:3]
'pgmn'
s[0:11:4]
'pri'
s[0:11:5]
'pag'
s[0:11:6]
'pm'
s[0:11:7]
'pm'
s[4:11:7]
'r'
s[2:11:7]
'on'
s[2:11:8]
'og'
s[2:11:9]
'o'
s[4:11:10]
'r'
s[4:11:11]
'r'
s[11:11:!1]
SyntaxError: invalid syntax
s[11:11:11]
''
10:11:11]
SyntaxError: unmatched ']'
s[10:11:11]
'g'
s[::]
'programming'
s[1::]
'rogramming'
s()
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    s()
TypeError: 'str' object is not callable
s[2:2];
''
s[2:2]:
    
SyntaxError: invalid syntax
s[2,2]
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    s[2,2]
TypeError: string indices must be integers, not 'tuple'
s[2.2]
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    s[2.2]
TypeError: string indices must be integers, not 'float'
s[2:2];
''
s[2:2]:
    
SyntaxError: invalid syntax
s[2::]
'ogramming'
s[2::4]
'omg'
s[1:-3]
'rogramm'
s[-11:8]
'programm'
s[11:0]
''
s[11:-1]
''
s[11:-2]
''
s[0:-2]
'programmi'
s[0:-10]
'p'
s[0:-9]
'pr'
s[0:-8]
'pro'
s[0:-7]
'prog'
s[0:-6]
'progr'
S[0:-5]
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    S[0:-5]
NameError: name 'S' is not defined. Did you mean: 's'?
s=[0:-5]
SyntaxError: invalid syntax
s[0:-5]
'progra'
s[0:-4]
'program'
s[0:-3]
'programm'
s[0:-2]
'programmi'
s[0:-1]
'programmin'
s[0:]
'programming'
s[0:10:-1]
''
s[0:5:-5]
''
s[-1:5]
''
s[-1:-1]
''
s[-1:-2]
''
s[-1:-2:-1]
'g'
s[-1:-3:-1]
'gn'
s[-1:-4:-1]
'gni'
s[-1:-5:-1]
'gnim'
s[-1:-6:-1]
'gnimm'
s[-1:-7:-1]
'gnimma'
s[-1:-8:-1]
'gnimmar'
s[-1:-9:-1]
'gnimmarg'
s[-1:-10:-1]
'gnimmargo'
s[-1:-11:-1]
'gnimmargor'
s[-1:-12:-1]
'gnimmargorp'
s[10:-11:-1]
'gnimmargor'
s[10:-12:-1]
'gnimmargorp'
s[8:-11:-4]
'ir'
s[-11:-1:-2]
''
s[-12:-1:-2]
''
s[-1:-11:-2]
'gimro'
s[-1:-11:-3]
'gmrr'
s[-1:-11:-4]
'gmo'
s[-1:-11:-5]
'ga'
s[-1:-11:-6]
'gr'
s[-1:-12:-7]
'gg'
s[-1:-12:-8]
'go'
s[-1:-12:-9]
'gr'
>>> s[-1:-12:-10]
'gp'
>>> s[-1:-12:-11]
'g'
>>> s[-1:-12:-12]
'g'
>>> s[0:11:-1]
''
>>> s[0:11:1]
'programming'
>>> s[-1:-11:-3]
'gmrr'
>>> s[-1:-12:-1]
'gnimmargorp'
>>> s[::-1]
'gnimmargorp'
>>> s[:::]
SyntaxError: invalid syntax
>>> s[::]
'programming'
>>> s[:]
'programming'
>>> s[0:0:0]
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    s[0:0:0]
ValueError: slice step cannot be zero
>>> s[0:0]
''
>>> s[:0]
''
>>> s[0:]
'programming'
>>> s[0:0:1]
''
>>> s[0:10:1]
'programmin'
>>> s[10:11:11]
'g'
