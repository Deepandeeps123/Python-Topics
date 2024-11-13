Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
lst=[1,2,3,4]
lst[3]
4
lst[3]=44
lst
[1, 2, 3, 44]
lst=[1,2,3,4]
lst.append(100)
lst
[1, 2, 3, 4, 100]
lst=[1,2,3,4]
lst.extend(100)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    lst.extend(100)
TypeError: 'int' object is not iterable
lst.extend('100')
lst
[1, 2, 3, 4, '1', '0', '0']
lst=[1,2,3,4]
lst.insert(4,100)

lst
[1, 2, 3, 4, 100]
lst=[1,2,3,4]
lst[4]=100
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    lst[4]=100
IndexError: list assignment index out of range
lst[3]
4
lst[3]=100
lst
[1, 2, 3, 100]
lst=[1,2,3,4,100]
ls[3]=100
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    ls[3]=100
NameError: name 'ls' is not defined. Did you mean: 'lst'?
lst[3]=100
lst
[1, 2, 3, 100, 100]






#index()

lst=[1,2,3,4,5,6,7,8,9,10]
lst.index(0]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
lst.index(0)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    lst.index(0)
ValueError: 0 is not in list
lst.index(1)
0
lst.index[2]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    lst.index[2]
TypeError: 'builtin_function_or_method' object is not subscriptable
lst.index(2)
1
lst.index(3)
2
lst.index(4)
3
lst.index(5)
4
]
lst.index(5)
4
lst.index(6)
5
lst.index(7)
6
lst.index(8)
7
lst.index(9)
8
lst.index(10)
9
lst.index(11)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    lst.index(11)
ValueError: 11 is not in list
lst.index(-3)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    lst.index(-3)
ValueError: -3 is not in list
lst=[1,2,1,2,1,2,1,2,3,4,5,6,1]
lst.index(2,3)
3
lst.index(1,8,12)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    lst.index(1,8,12)
ValueError: 1 is not in list
lst.index(1,8)
12
lst.index(1)
0
lst=[1,2,3,[4,5,6,[7,8,9]]]
lst[1]
2
lst[2]
3
lst[3]
[4, 5, 6, [7, 8, 9]]
lst[4]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    lst[4]
IndexError: list index out of range
#9

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
lst[3][3].index(9)
2
lst.index(9)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    lst.index(9)
ValueError: 9 is not in list
lst[3].index(5)
1




#remove()



lst=[1,2,3,4,1,2,3]
lst.remove(1)
lst
[2, 3, 4, 1, 2, 3]
lst.remove(100)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    lst.remove(100)
ValueError: list.remove(x): x not in list
lst.remove('100')
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    lst.remove('100')
ValueError: list.remove(x): x not in list
lst.remove()
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    lst.remove()
TypeError: list.remove() takes exactly one argument (0 given)
lst=[1,2,3,[4,5,6,[7,8,9],9]]
lst.remove(9)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    lst.remove(9)
ValueError: list.remove(x): x not in list
# 9 remove
lst[1]
2

lst[2]
3
lat[3]
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    lat[3]
NameError: name 'lat' is not defined. Did you mean: 'lst'?
lst[3]
[4, 5, 6, [7, 8, 9], 9]
lst[3][0]
4
lst[3][1]
5
lst[3][3]
[7, 8, 9]
lst[3][4]
9
lst[3][4].remove(9)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    lst[3][4].remove(9)
AttributeError: 'int' object has no attribute 'remove'
lst[3].remove(9)
lst
[1, 2, 3, [4, 5, 6, [7, 8, 9]]]




#pop


lst=[1,2,3,1,2,3]
lst.remove(1)
lst
[2, 3, 1, 2, 3]
lst=[1,2,3,1,2,3]
lst.pop(3)
1
lst.pop(2)
3
lst.remove()
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    lst.remove()
TypeError: list.remove() takes exactly one argument (0 given)
lst.pop()
3
lst=[1,2,3,1,2,3]
lst.pop(2)
3
lst.remove(1)
lst
[2, 1, 2, 3]
lst.pop()
3
lst.pop()
2
lst.pop()
1
lst.pop()
2
lst.pop()
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    lst.pop()
IndexError: pop from empty list





#clear()

lst=[1,2,3,4,5,8]
lst.clear()
lst
[]
lst=[1,2,3,[4,5,6]]
lst.clear()
lst
[]
lst[3].clear()
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    lst[3].clear()
IndexError: list index out of range
lst=list((1,2,3,[4,5,6]))
lst[1].clear()
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    lst[1].clear()
AttributeError: 'int' object has no attribute 'clear'
lst[2].clear()
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    lst[2].clear()
AttributeError: 'int' object has no attribute 'clear'
lst[3].clear()
lst
[1, 2, 3, []]



#count()


lst=[1,2,3,4,1,1,11,11,11,1,1,1,1,1]
lst.count(1)
8
lst.count(11)
3
lst.count(1,2)
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    lst.count(1,2)
TypeError: list.count() takes exactly one argument (2 given)
lst=[1,2,3,[1,2,3,[1,2,3],1],1]
lst.count(1)
2
lst.count(2)
1
lst.count(3)
1
lst[3].count(1)
2
>>> lst[3].count(2)
1
>>> lst[3].count(3)
1
>>> lst[3][3].count(1)
1
>>> lst[3][3].count(2_
...                 
SyntaxError: invalid decimal literal
>>> lst[3][3].count(2)
...                 
1
>>> lst[3][3].count(3)
...                 
1
>>> 
>>> 
>>> 
>>> 
>>> 
>>> lst=[1,2,3,4,5,6]
...                 
>>> lst[::-1]
...                 
[6, 5, 4, 3, 2, 1]
>>> lst.reverse()
...                 
>>> lst
...                 
[6, 5, 4, 3, 2, 1]
>>> lst=[1,2,3,4,[1,2,3,[2,3,5]]]
...                 
>>> lst[::-1]
...                 
[[1, 2, 3, [2, 3, 5]], 4, 3, 2, 1]
>>> lst.reverse()
...                 
>>> lst
...                 
[[1, 2, 3, [2, 3, 5]], 4, 3, 2, 1]
