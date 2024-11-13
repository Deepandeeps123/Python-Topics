Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#modification of list



lst=[1,2,3,4]
lst
[1, 2, 3, 4]

lst.append(5)
'

lst.append()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    lst.append()
TypeError: list.append() takes exactly one argument (0 given)
lst.append(5)
lst
[1, 2, 3, 4, 5, 5]
lst=[1,2,3,4]
lst.append(5)
lst
[1, 2, 3, 4, 5]
lst.append(1)
lst
[1, 2, 3, 4, 5, 1]
lst.append(6)
lst
[1, 2, 3, 4, 5, 1, 6]
lst.append('hello')
lst
[1, 2, 3, 4, 5, 1, 6, 'hello']
lst.append([7,8,9])
lst
[1, 2, 3, 4, 5, 1, 6, 'hello', [7, 8, 9]]
lst=[1,2,3,[4,5,6,[7,8,9]]]
lst[0]
1
#[1,2,3,[4,5,6,[7,8,9,10]]]
lst[3]
[4, 5, 6, [7, 8, 9]]
lst[3][3]
[7, 8, 9]
lst[3][3].append(10)
lst
[1, 2, 3, [4, 5, 6, [7, 8, 9, 10]]]
lst[3][3][0].append(10)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    lst[3][3][0].append(10)
AttributeError: 'int' object has no attribute 'append'
lst[3][3][0]
7
lst.append(10)
lst
[1, 2, 3, [4, 5, 6, [7, 8, 9, 10]], 10]
lst.append(1,1)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    lst.append(1,1)
TypeError: list.append() takes exactly one argument (2 given)



#extend


lst=[1,2,3,4]
lst.append(hello)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    lst.append(hello)
NameError: name 'hello' is not defined. Did you mean: 'help'?
lst.append('hello')
lst
[1, 2, 3, 4, 'hello']
lst=[1,2,3,4]
lst.extend('hello')
lst
[1, 2, 3, 4, 'h', 'e', 'l', 'l', 'o']
lst.extend(100)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    lst.extend(100)
TypeError: 'int' object is not iterable
lst.extend('100')
lst
[1, 2, 3, 4, 'h', 'e', 'l', 'l', 'o', '1', '0', '0']
lst.extend('the question of the python')
lst
[1, 2, 3, 4, 'h', 'e', 'l', 'l', 'o', '1', '0', '0', 't', 'h', 'e', ' ', 'q', 'u', 'e', 's', 't', 'i', 'o', 'n', ' ', 'o', 'f', ' ', 't', 'h', 'e', ' ', 'p', 'y', 't', 'h', 'o', 'n']
lst=[1,2,3,4]
lst.append([5,6,7,8])
lst
[1, 2, 3, 4, [5, 6, 7, 8]]
lst=list((1,2,3,4))
lst.extend(list((5,6,7,8)))
lst
[1, 2, 3, 4, 5, 6, 7, 8]
lst=[1,2,3,5,['helllo']]
lst.extend('hi')
lst
[1, 2, 3, 5, ['helllo'], 'h', 'i']
lst.extend(['hello'])
lst
[1, 2, 3, 5, ['helllo'], 'h', 'i', 'hello']
lst.extend('hello')
lst
[1, 2, 3, 5, ['helllo'], 'h', 'i', 'hello', 'h', 'e', 'l', 'l', 'o']




#insert()

lst=list((1,2,3))
lst[0]
1
lst.insert(2)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    lst.insert(2)
TypeError: insert expected 2 arguments, got 1
lst.insert(0,1000)
lst
[1000, 1, 2, 3]
lst=[1,2,3]
lst.insert(1,22)
lst
[1, 22, 2, 3]
lst.insert(2,22)
lst
[1, 22, 22, 2, 3]
lst.insert(3,22)
lst
[1, 22, 22, 22, 2, 3]
lst.insert(10,22)
lst
[1, 22, 22, 22, 2, 3, 22]
lst[1]
22
lst[2]
22
lst[3]
22
lst[4]
2
lst[5]
3
>>> lst[6]
22
>>> lst=list(('hello','hi','apple']
...          
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> lst=list(('hello','hi','apple'))
...          
>>> lst.insert(0,'neem')
...          
>>> lst
...          
['neem', 'hello', 'hi', 'apple']
>>> lst=list(('hello','hi','apple'))
...          
>>> lst.insert(1,'neem')
...          
>>> lst
...          
['hello', 'neem', 'hi', 'apple']
>>> lst=list(('hello','hi','apple'))
...          
>>> lst.insert(2,'neem')
...          
>>> lst
...          
['hello', 'hi', 'neem', 'apple']
>>> lst.insert(3,'bannana')
...          
>>> lst
...          
['hello', 'hi', 'neem', 'bannana', 'apple']
>>> lst=['hello',['bye','good','python'],'great','java',['apple','bannana']]
...          
>>> lst[1]
...          
['bye', 'good', 'python']
>>> lst[1].insert(2,'qspiders')
...          
>>> lst
...          
['hello', ['bye', 'good', 'qspiders', 'python'], 'great', 'java', ['apple', 'bannana']]
lst.insert(3,'qspoders')
         
lst
         
['hello', ['bye', 'good', 'qspiders', 'python'], 'great', 'qspoders', 'java', ['apple', 'bannana']]
lst[5]
         
['apple', 'bannana']
lst[5].insert(1,'graphs')
         
lst
         
['hello', ['bye', 'good', 'qspiders', 'python'], 'great', 'qspoders', 'java', ['apple', 'graphs', 'bannana']]
lslst=['hello',['bye','good','python'],'great','java',['apple','bannana']]
         
lst[5].insert(0,'graphs')
         
lst
         
['hello', ['bye', 'good', 'qspiders', 'python'], 'great', 'qspoders', 'java', ['graphs', 'apple', 'graphs', 'bannana']]
lst[5][0].insert(0,'graphs')
         
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    lst[5][0].insert(0,'graphs')
AttributeError: 'str' object has no attribute 'insert'
lst[1]
         
['bye', 'good', 'qspiders', 'python']
lst[1][2]
         
'qspiders'
lst[1]
         
['bye', 'good', 'qspiders', 'python']
lst[1].insert(100)
         
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    lst[1].insert(100)
TypeError: insert expected 2 arguments, got 1
lst[1].insert(100,100)
         
lst
         
['hello', ['bye', 'good', 'qspiders', 'python', 100], 'great', 'qspoders', 'java', ['graphs', 'apple', 'graphs', 'bannana']]
