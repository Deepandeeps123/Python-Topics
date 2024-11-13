Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#add()



s={1,2,3,4}
s.append(5)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s.append(5)
AttributeError: 'set' object has no attribute 'append'
s=(1,2,3,4)
s.append(5)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s.append(5)
AttributeError: 'tuple' object has no attribute 'append'
s=[1,2,3,4]
s.append(5)
s
[1, 2, 3, 4, 5]


s={1,2,3,4}
s.add(5)
s
{1, 2, 3, 4, 5}
s={1,2,3,'hello')
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
s={1,2,3,'hello'}
s.add('bye')
s
{'bye', 2, 3, 1, 'hello'}
s={1,2,3,5,4,6,7,8,9,10}
s.add(11)
s
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
s={1,3,2}
s.add('hello')
s
{1, 2, 3, 'hello'}
s={1,3,4,5,2,9,6,7,8}
s.add('bye')
s
{1, 2, 3, 4, 5, 6, 7, 8, 9, 'bye'}
s.add(True)
s
{1, 2, 3, 4, 5, 6, 7, 8, 9, 'bye'}
s.add(0)
s
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'bye'}
s.add(0.0)
s
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'bye'}
s.add(10+3j)
s
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'bye', (10+3j)}
s.add('hi')
s
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'bye', (10+3j), 'hi'}
s.add(['hi'])
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    s.add(['hi'])
TypeError: unhashable type: 'list'
s.add(('good'))
s
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'bye', 'good', (10+3j), 'hi'}
s.add({'hi'})
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    s.add({'hi'})
TypeError: unhashable type: 'set'




#update()
s={1,2,3,4}
s.update(1)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    s.update(1)
TypeError: 'int' object is not iterable

s.update({1})
s
{1, 2, 3, 4}
s.add(4)
s
{1, 2, 3, 4}
s.update(5)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    s.update(5)
TypeError: 'int' object is not iterable
s.update('5')
s
{1, 2, 3, 4, '5'}
s.update({5})
s
{1, 2, 3, 4, '5', 5}



#remove()
s=[1,2,3,4]
s.remove()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    s.remove()
TypeError: list.remove() takes exactly one argument (0 given)
s.remove(4)
s
[1, 2, 3]

s={1,2,3,4}
s.remove(4)
s
{1, 2, 3}




#discord()

s={1,2,3,4,5}
s.add(6)
s
{1, 2, 3, 4, 5, 6}
s.update(7)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    s.update(7)
TypeError: 'int' object is not iterable
s.update({7})
s
{1, 2, 3, 4, 5, 6, 7}
s.remove(1,2)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    s.remove(1,2)
TypeError: set.remove() takes exactly one argument (2 given)
s.remove(7)
s
{1, 2, 3, 4, 5, 6}
s.discord(6)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    s.discord(6)
AttributeError: 'set' object has no attribute 'discord'. Did you mean: 'discard'?
s.discard(6)
s
{1, 2, 3, 4, 5}
s.discard(0)
s
{1, 2, 3, 4, 5}
s.add(0)
s
{0, 1, 2, 3, 4, 5}
s.update({1000})
s
{0, 1, 2, 3, 4, 5, 1000}
s.remove(10000)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    s.remove(10000)
KeyError: 10000
s.discard(1000000)
s
{0, 1, 2, 3, 4, 5, 1000}




#pop()



s=[1,2,3,4,5]
s.pop(4)
5
s
[1, 2, 3, 4]
s={1,2,3,4}
s.pop(4)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    s.pop(4)
TypeError: set.pop() takes no arguments (1 given)
s
s.pop()
1
s.pop()
2
s.pop(100)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    s.pop(100)
TypeError: set.pop() takes no arguments (1 given)
lst=[1,2,3]
lst.pop(100)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    lst.pop(100)
IndexError: pop index out of range
lst.pop()
3
lst.pop()
2
lst.pop()
1
lst.pop(0
        )
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    lst.pop(0
IndexError: pop from empty list
s={1,2,3,4}
            
s.pop()
            
1
s.pop()
            
2

s.pop()
            
3
s.pop()
            
4
s.pop()
            
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    s.pop()
KeyError: 'pop from an empty set'


#clear()
            


s=[1,2,3,4,5]
            
s.clear(0)
            
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    s.clear(0)
TypeError: list.clear() takes no arguments (1 given)
s.clear()
            
s
            
[]
s={1,2,3,4,5}
            
s.clear()
            
s
            
set()
s={1,2,3,4,5}
            
s.clear(100)
            
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    s.clear(100)
TypeError: set.clear() takes no arguments (1 given)
s={1,2,3,4]
            
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
s={1,2,3,4}
            
s.update(1)
            
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    s.update(1)
TypeError: 'int' object is not iterable
s1={6}
            
s.update(s2)
            
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    s.update(s2)
NameError: name 's2' is not defined. Did you mean: 's'?
s.update(s1)
            
s
            
{1, 2, 3, 4, 6}




#issuperset()
            
s={1,2,3,4}
            
s1={10,11}
            
s.superset(s1)
...             
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    s.superset(s1)
AttributeError: 'set' object has no attribute 'superset'. Did you mean: 'issuperset'?
>>> s.issuperset(s1)
...             
False
>>> 
>>> 
>>> 
>>> 
>>> #issubset()
...             
>>> s={1,2,3,4}
...             
>>> s1={1}
...             
>>> s.issubset(s1)
...             
False
>>> 
>>> 
>>> 

>>> #isdisjoint()
...             
>>> 
>>> s1={1,2,3}
...             
>>> s2={1,2,3}
...             
>>> s1.isdisjoint(s2)
...             
False
>>> s2={100,200,300}
...             
>>> s1.isdisjoint(s2)
...             
True
