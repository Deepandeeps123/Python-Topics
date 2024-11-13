Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
b=10
a+b
20
s='dinga'
lrn(s)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    lrn(s)
NameError: name 'lrn' is not defined. Did you mean: 'len'?
len(s)
5
len(s)/2
2.5
len(s)//2
2
dinga/2
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dinga/2
NameError: name 'dinga' is not defined
'dinga'/2
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    'dinga'/2
TypeError: unsupported operand type(s) for /: 'str' and 'int'
a-b
0
a*b
100
a/2
5.0
a/b
1.0
a=5
b=2
a%b
1
a=10
b=20
a/b
0.5
a//b
0
a=50
b=20
a/b
2.5
a=40
b=5

a/b
8.0
a=45
b=5
a/b
9.0
a//b
9


#relational




a=20
b=10
a>b
True
a<b
False
a>=b
True
a<=b
False
a!=b
True
a==b
False
20>=10
True
4<=2
False
2<1
False
2<=2
True

3<=2
False
20<=10
False
2>=2
True
1>=2
False
3>=2
True
4>=2
True
20<=10
False
4!=2
True
21=2
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
2!=2
False
1!=2
True
4!=2
True
10==10
True
20==10
False
30==10
False
40==10
False






#logical


#and

10>5 and 10<20
True
10>5 and 10<20 and 100 > 20
True
10>5 and 10<20 and 100< 10
False
10<5 and 10<20 and 100<10
False
12 and 13
13
0 and 10
0
a and 11
11
0 and 11
0
 '' and []
 
SyntaxError: unexpected indent

'' and []
''
'0' and []
[]
1 and set()
set()
0 and false
0
o and False
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    o and False
NameError: name 'o' is not defined
0 and False
0
'o' and False
False





#or


10>20 and 20<10
False
10>20 or 20<10
False
20<10
False
10!=4
True
5!=4
True
6!=4
True
10!=4 and 10<5
False
10<5
False
10!=4 or 10<5
True
10>20 and 20<10
False
10>20
False
10>20 and 20<10
False
0 and 14
0
0 or 14
14
0 or ''
''
[1,2,3] or (1,2,3)
[1, 2, 3]





#Not


10
10
True
True
10>2
True
not 10>2
False
[]
[]
not []
True
not 10>2 and 20>2
False
not 10>2 and not 10<2
False
not 10>2
False
not 10<2
True
10>2
True
10<2
False
True
True








# membership



h in 'hello'
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    h in 'hello'
NameError: name 'h' is not defined
'h' in 'hello'
True
h in hello
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    h in hello
NameError: name 'h' is not defined
'H' in 'hello'
False
'H' in 'helloHELLO'
True
s='Apple'
'a' in 'aeiou'
True
>>> s in 'aeiou'
False
>>> s='Qspiders'
>>> s in 'a'
False
>>> s in 'b'
False
>>> s in 'c'
False
>>> s in 'd'
False
>>> s='apple'
>>> s in 'aeiou'
False
>>> s[2]
'p'
>>> s[4]
'e'
>>> a='qspiders'
>>> s='qspiders'
>>> s
'qspiders'
>>> s[4]
'd'
>>> s[4] in 'a'
False
>>> s[4] in 'b'
False
>>> s[4] in 'c'
False
>>> s[4] in 'd'
True
>>> 
>>> 
>>> 
>>> s[4].upper() in 'd'
False
>>> 
>>> 

... 
























































































































































































































