Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
lst=[1,2,3,4,5,6,7,8,9,10]
type(lst)
<class 'list'>
lst2=[1,1.1,true,1+2j],'hi',[1,2,3]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    lst2=[1,1.1,true,1+2j],'hi',[1,2,3]
NameError: name 'true' is not defined. Did you mean: 'True'?
lst2=[1,1.1,True,1+2j],'hi',[1,2,3]
type(lst2)
<class 'tuple'>
lst2=[1,1.1,True,1+2j],'hi',[1,2,3]]
SyntaxError: unmatched ']'
lst=[1,1.1,True,'hi']
type(lst2)
<class 'tuple'>
type(lst)
<class 'list'>
lst=[1,1,1,1,1,1,1,1,'hi','hi']
type(lst)
<class 'list'>
lst
[1, 1, 1, 1, 1, 1, 1, 1, 'hi', 'hi']
a=10

a
10
lst=list(1,2,3,4,5,6,7,8)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    lst=list(1,2,3,4,5,6,7,8)
TypeError: list expected at most 1 argument, got 8
lst=list((1,2,3,4,5,6,7))
lst
[1, 2, 3, 4, 5, 6, 7]
lst=list((1,2,3,4,5,6),(7,8,9,10))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    lst=list((1,2,3,4,5,6),(7,8,9,10))
TypeError: list expected at most 1 argument, got 2
lst=list()
lst
[]




lst=[1,2,3,'hello']
id(lst)
1557052355008
id(lst[0])
140735468276152
is(lst[1])
SyntaxError: invalid syntax
id(lst[1])
140735468276184
id(lst[2])
140735468276216
id(lst[3])
1557044715536
id(lst[4])
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    id(lst[4])
IndexError: list index out of range
lst=[1,2,3,1,2,3]
lst[0]
1
id(lst[0])
140735468276152
id(lst[1])
140735468276184
id(lst[2])
140735468276216
id(lst[3])
140735468276152
id(lst[4])
140735468276184
id(lst[5])
140735468276216
lst=[1,2,3[4,5,6]]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    lst=[1,2,3[4,5,6]]
TypeError: 'int' object is not subscriptable
lst=[1,2,3,[4,5,6]]
lst[0]
1
lst[1]
2
lst[3]
[4, 5, 6]
lst=[1,2,3]
id(lst[0]
   )
140735468276152
id(lst[1])
140735468276184
id(lst[2])
140735468276216
id(lst[4])
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    id(lst[4])
IndexError: list index out of range


#index


lst=[1,2,3,4,'hello','hi']
lst[3]
4
lst[1]
2
lst[0]
1
lst[2]
3
lst[3]
4
lst[5]
'hi'
lst[4]
'hello'
lst[6]
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    lst[6]
IndexError: list index out of range
lst[4][0]
'h'
lst[4][1]
'e'
lst[4][2]
'l'
lst[4][3]
'l'
lst[4][4]
'o'
lst[4][5]
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    lst[4][5]
IndexError: string index out of range
lst[-8]
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    lst[-8]
IndexError: list index out of range
lst=[1,2,3,[4,5,6]]
lst[3]
[4, 5, 6]
lst[0]
1
lst[1]
2
lst[3]
[4, 5, 6]
lst[3][0]
4
lst[3][1]
5
lst[3][2]
6
lst[3].[0]
SyntaxError: invalid syntax
lst=[1,2,3,[4,5,6,[7,8,9]]]
lst[0]
1
lst[1]
2
lst[2]
3
lst[3]
[4, 5, 6, [7, 8, 9]]
lst[3][0]
4
lst[3][1]
5
lst[3][2]
6
lst[3][3]
[7, 8, 9]
lst[3][3][0]
7
lst[3][3][1]
8
lst=[1,2,3,4,[5,6,7,8],[9,10,11]]
lst[0]
1
lst=[1,2,3,4,[5,6,7,8],[9,10,11]]      #10
lst[1]
2
lst[2]
3
lst[3]
4
lst[4]
[5, 6, 7, 8]
lst[5]
[9, 10, 11]
lst[5][0]
9
lst[5][1]
10

lst[2]
3
lst[3]
4
lst[4]
[5, 6, 7, 8]
lst[4]      #7
[5, 6, 7, 8]
lst[4][0]
5
lst[4][1]
6
lst[4][2]
7
lst=[1,2,3,['hello','hi',['bye','good']]]
#i
lst[0]
1
lst[1]
2
lst[2]
3
lst[3]
['hello', 'hi', ['bye', 'good']]
lst[3][0]
'hello'
lst[3][1]
'hi'
lst[3][1][0]
'h'
lst[3][1][1]
'i'
# i upper
lst[3][1][1].upper()
'I'
lst=[1,2,3,4,[5,6,7,8,[9,10,11,12,[13,14,15]]]]
lst[0]
1
lst[1]
2
lst[2]
3
lst[3]
4
lst[4]
[5, 6, 7, 8, [9, 10, 11, 12, [13, 14, 15]]]
#15
lst[4][0]
5
lst[4][1]
6
lst[4][2]
7
lst[4][3]
8
lst[4][4]
[9, 10, 11, 12, [13, 14, 15]]
lst[4][4][0]
9
lst[4][4][1]
10
lst[4][4][2]
11
lst[4][4][3]
12
lst[4][4][4]
[13, 14, 15]
lst[4][4][4][0]
13
lst[4][4][4][1]
14
lst[4][4][4][2]
15


lst =list('hello','hi',['bye'],['python'])
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    lst =list('hello','hi',['bye'],['python'])
TypeError: list expected at most 1 argument, got 4
lst =list(('hello','hi',['bye'],['python']))
#python
lst[0]
'hello'
lst[1]
'hi'
lst[2]
['bye']
lst[3]
['python']
lst[3][0]
'python'
lst[3][0][0]
'p'
#pto
lst[3]
['python']
lst[3][0]
'python'
lst[3][0][::2]
'pto'
#ptO
lst[3][0][::2].replace('o','O')
'ptO'
lst[3][0][::2][::-1]
'otp'
lst[3][0][::2][::-1].title()[::-1]
'ptO'





#SLicing


lst=[1,2,3,4,5,6,7,8,9]
lst[0]
1
lst[0:1]
[1]
lst[0:0]
[]
#1234
lst[2]
3
lst[3]
4
lst[:4]
[1, 2, 3, 4]
lst[:5]
[1, 2, 3, 4, 5]
lst[::]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
lst[::-1]
[9, 8, 7, 6, 5, 4, 3, 2, 1]
lst[-1]
9
lst[-1:5]
[]
lst[-1:5:-1]
[9, 8, 7]
lst[4:]
[5, 6, 7, 8, 9]
lst[:4]
[1, 2, 3, 4]
lst[len(lst) | 2]
Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    lst[len(lst) | 2]
IndexError: list index out of range
lst[:len(lst) | 2]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
lst{:lemn(lst) || 2]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
lst[:len(lst) || 2]
SyntaxError: invalid syntax
lst[:len(lst) / 2]
Traceback (most recent call last):
  File "<pyshell#190>", line 1, in <module>
    lst[:len(lst) / 2]
TypeError: slice indices must be integers or None or have an __index__ method
lst[len(lst) || 2]
SyntaxError: invalid syntax
len(lst)
9
len(lst)|2
11
len)lst)/2
SyntaxError: unmatched ')'
len(lst)/2
4.5
len(lst)//2
4
lst[len(lst) //2]
5
lst[:len(lst) // 2]
[1, 2, 3, 4]
lst=['hello','hi','good','bye','apple','orange','bannana','neem','orange']
lst[0]
'hello'
lst[1]
'hi'
lst[2]
'good'
lst[3]
'bye'
lst[4]
'apple'
lst[5]
'orange'
lst[6]
'bannana'
lst[7]
'neem'
lst[8]
'orange'
lst[9]
Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    lst[9]
IndexError: list index out of range
#index 02468
lst[::2]
['hello', 'good', 'apple', 'bannana', 'orange']
#replace a z
lst[::].replace('a','z')
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    lst[::].replace('a','z')
AttributeError: 'list' object has no attribute 'replace'
lst[::2]
['hello', 'good', 'apple', 'bannana', 'orange']
lst[::2][::1]
['hello', 'good', 'apple', 'bannana', 'orange']
lst[::2][::2]
['hello', 'apple', 'orange']
lst[::2][::2]
['hello', 'apple', 'orange']
lst[::2][:2][::2]
['hello']
lst[::2][::2][::2][::-1]
['orange', 'hello']
lst[::2][::2][1]
'apple'
lst[::2][::2][1].replace('p','')
'ale'
lst[::2][::2][1].replace('p',' ')
'a  le'
#nam
#nan
lst[4]
'apple'
lst[5]
'orange'
lst[6]
'bannana'
lst[6][::2]
'bnaa'
lst[6][0:6]
'bannan'
lst[6][3:]
'nana'
lst[6][3:6]
'nan'
lst[6][-3]
'a'
lst=['apple','qspiders',['jspiders','pyspiders','prospyiders',['tarmarind','jasmine']]]
lst[0]
'apple'
lst[1]
'qspiders'
lst[2]
['jspiders', 'pyspiders', 'prospyiders', ['tarmarind', 'jasmine']]
lst[3]
Traceback (most recent call last):
  File "<pyshell#237>", line 1, in <module>
    lst[3]
IndexError: list index out of range
#marind

lst[2]
['jspiders', 'pyspiders', 'prospyiders', ['tarmarind', 'jasmine']]
lst[0]
'apple'
lst[2]
['jspiders', 'pyspiders', 'prospyiders', ['tarmarind', 'jasmine']]
lst[2][1]
'pyspiders'
lst[2][2]
'prospyiders'
lst[2][3]
['tarmarind', 'jasmine']
lst[2][3][0]
'tarmarind'
lst[2][3][0][3]
'm'
lst[2][3][0][3:]
'marind'
#opsi

lst[2]
['jspiders', 'pyspiders', 'prospyiders', ['tarmarind', 'jasmine']]
lst[2][1]
'pyspiders'
lst[2][1][:5:2]
'psi'
lst[2][1][:5:2].join('o')
'o'
'o'.join(lst[2][1][:5:2])
'posoi'
'o '.join(lst[2][1][:5:2])
'po so i'
>>> lst[2][1][:5:2].join('o ')
'opsi '
>>> lst[2][1][:5:2].join(' o')
' psio'
>>> lst[6]
Traceback (most recent call last):
  File "<pyshell#258>", line 1, in <module>
    lst[6]
IndexError: list index out of range
>>> lst[5]
Traceback (most recent call last):
  File "<pyshell#259>", line 1, in <module>
    lst[5]
IndexError: list index out of range
>>> lst[3]
Traceback (most recent call last):
  File "<pyshell#260>", line 1, in <module>
    lst[3]
IndexError: list index out of range
>>> lst[2]
['jspiders', 'pyspiders', 'prospyiders', ['tarmarind', 'jasmine']]
>>> lst=['hello','hi','good','bye','apple','orange','bannana','neem','orange']   #xna
>>> lst[2]
'good'
>>> lst[7]
'neem'
>>> lst[6]
'bannana'
>>> lst[6][-1]
'a'
>>> lst[6][-2]
'n'
>>> lst[6][5:]
'na'
>>> lst[6][5:].join('x ')
'xna '
>>> lst[6][5:]+'x'
'nax'
>>> 'x'+lst[6][5:]
'xna'
