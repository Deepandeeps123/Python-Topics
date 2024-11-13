Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
$set()
SyntaxError: invalid syntax
#set(()
s={}
s
{}
s={1,2,3,4}
s
{1, 2, 3, 4}
s{}
SyntaxError: invalid syntax
s1=(1,2,3,4)
s2=(3,4,5,6)
s1.union(s2)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s1.union(s2)
AttributeError: 'tuple' object has no attribute 'union'
s1={1,2,3,4}
s2={3,4,5,6}
s1.union(s2)
{1, 2, 3, 4, 5, 6}
s3={5,6,7,8}
s4={5,6,7,8}
s5={7,8,9,0}
s1.union(s1)(s2)(s3)(s4)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s1.union(s1)(s2)(s3)(s4)
TypeError: 'set' object is not callable
s1.union(s1,s2,s3,s4,s5)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
s1.union(s2,s3,s4,s5)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
s1={1,2,3,4}
s1.union{'3456'}
SyntaxError: invalid syntax
s1.union('3456')
{1, 2, 3, 4, '3', '4', '5', '6'}
s1{'1','2','3','4'}
SyntaxError: invalid syntax
s1={'1','2','3','4'}
s1.union('3,4,5,6)
         
SyntaxError: unterminated string literal (detected at line 1)
s1.union('3,4,5,6')
         
{'3', '4', '5', '1', ',', '2', '6'}
s1={1,2,3,4}
         
s2={3,4,5,6}
         
s1
         
{1, 2, 3, 4}
s2
         
{3, 4, 5, 6}
s1.union(s2)
         
{1, 2, 3, 4, 5, 6}
s2.union(s1)
         
{1, 2, 3, 4, 5, 6}
s1.union(s1)
         
{1, 2, 3, 4}
s2.union(s2)
         
{3, 4, 5, 6}
s1={'hello','hi'}
         
s2={'hello'}
         
s1.union(s2)
         
{'hello', 'hi'}
s1.union(hello)
         
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    s1.union(hello)
NameError: name 'hello' is not defined. Did you mean: 'help'?
s1.union('hello')
         
{'h', 'hello', 'l', 'e', 'o', 'hi'}
s1.union['hello']
         
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    s1.union['hello']
TypeError: 'builtin_function_or_method' object is not subscriptable
s1.union([hello])
         
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    s1.union([hello])
NameError: name 'hello' is not defined. Did you mean: 'help'?
s1.union(['hello'])
         
{'hello', 'hi'}
s1.union(('hello'))
         
{'h', 'hello', 'l', 'e', 'o', 'hi'}
s1.union(('hello',['bye']))
         
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    s1.union(('hello',['bye']))
TypeError: unhashable type: 'list'
s1.union(s2,{'hello'})
         
{'hello', 'hi'}
s1.union({'hello'},['bye'],'good')
         
{'hello', 'bye', 'd', 'o', 'g', 'hi'}
s1.union(['hello'],'hello','good','bye')
         
{'y', 'h', 'hello', 'd', 'l', 'e', 'o', 'g', 'b', 'hi'}
s2.union(['hello'],'hello','good','bye')
         
{'y', 'h', 'hello', 'd', 'l', 'e', 'o', 'g', 'b'}
s1.union(['hello'],'hello','good','bye')
         
{'y', 'h', 'hello', 'd', 'l', 'e', 'o', 'g', 'b', 'hi'}
a=10,20,30,40
         
a
         
(10, 20, 30, 40)
a.union('hello')
         
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a.union('hello')
AttributeError: 'tuple' object has no attribute 'union'
a.union(['hello'])
         
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a.union(['hello'])
AttributeError: 'tuple' object has no attribute 'union'





#update()
         
s1={1,2,3,4}
         
s2={3,4,5,6}
         
s1.union(s2)
         
{1, 2, 3, 4, 5, 6}
s1
         
{1, 2, 3, 4}
s2
         
{3, 4, 5, 6}
s1.update(s2)
         
s1
         
{1, 2, 3, 4, 5, 6}
s2
         
{3, 4, 5, 6}
s2.update(s1)
         
s1
         
{1, 2, 3, 4, 5, 6}
s2
         
{1, 2, 3, 4, 5, 6}
s1.update(s1)
         
s1
         
{1, 2, 3, 4, 5, 6}
s1.update('hello')
         
s1
         
{1, 2, 3, 4, 5, 6, 'h', 'l', 'e', 'o'}
s1.update(['hello'])
         
s1
         
{1, 2, 3, 4, 5, 6, 'h', 'hello', 'l', 'e', 'o'}





#intersection()
         

s1={1,2,3,4}
         
s2={3,4,5,6}
         
s1.union(s2)]
SyntaxError: unmatched ']'
s1.union(s1)
{1, 2, 3, 4}
s1.update(s1)
s1
{1, 2, 3, 4}
s1.union(s2)
{1, 2, 3, 4, 5, 6}
s1.update(s2)
s1
{1, 2, 3, 4, 5, 6}
s1.indtersection(s2)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    s1.indtersection(s2)
AttributeError: 'set' object has no attribute 'indtersection'. Did you mean: 'intersection'?
s1.intersection(s2)
{3, 4, 5, 6}
s1={1,2,3,4}
s2={3,4,5,6}
s1.intersection(s2)
{3, 4}
s1.intersection(s2,(4,5,6,7))
{4}
s1.intersection(s2,[4,5,6,7])
{4}
s1.intersection(s2,{4,5,6,7})
{4}
s1.intersection(s2,(10,11))
set()
s1.intersection(6,5,6)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    s1.intersection(6,5,6)
TypeError: 'int' object is not iterable
s1.intersection('6,7,8')
set()
s1={'the best programming language is python'}
s2={'the best programming language is java'}
s1.union(s2)
{'the best programming language is python', 'the best programming language is java'}
s1.intersection(s2)
set()
s1.difference(s2)
{'the best programming language is python'}
s1
{'the best programming language is python'}
s2
{'the best programming language is java'}
s1.update(s2)
s1
{'the best programming language is python', 'the best programming language is java'}
s2
{'the best programming language is java'}
s1
{'the best programming language is python', 'the best programming language is java'}





#intersection_update()
s1.intersection(s2)
{'the best programming language is java'}
s1={1,2,3,4}
s2={3,4,5,6}
s1.intersection(s2)
{3, 4}
s1
{1, 2, 3, 4}
s2
{3, 4, 5, 6}
s1.intersection_update(s2)
s1
{3, 4}
s2
{3, 4, 5, 6}
s2.intersection_update(s1)
s1
{3, 4}
s2
{3, 4}





#difference()
s={1,2,3,4}
s1={1,2,3,4}
s2={3,4,5,6}
s1.difference(s2)
{1, 2}
s1.difference(s1)
set()
s2.difference(s1)
{5, 6}
s1
{1, 2, 3, 4}
s2
{3, 4, 5, 6}
s1.union()
{1, 2, 3, 4}
s1.
SyntaxError: invalid syntax
s1.difference()
{1, 2, 3, 4}
s2.difference()
{3, 4, 5, 6}
s1.difference(s2,'hello')
{1, 2}
s1.difference(s1,s2,s1)
set()
sq.difference(s1,s2)
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    sq.difference(s1,s2)
NameError: name 'sq' is not defined. Did you mean: 's'?
s1.difference(s1,s2)
set()




#difference_update()
s1={1,2,3,4}
s2={3,4,5,6}
s1.difference(s2)
{1, 2}
s1.difference_update(s2)
s1
{1, 2}
s2
{3, 4, 5, 6}
s1.difference_update(s1)
s1
set()
s2.difference(s1)
{3, 4, 5, 6}
s2.difference_update(s1)
s1
set()
s2
{3, 4, 5, 6}
s2.difference_update(s2)
s2
set()
s1
set()
s1={1,2,3,4}
s2={3,4,5,6}
s2.difference(s1)
{5, 6}
s2.difference_update(s1)
s2
{5, 6}
s1
{1, 2, 3, 4}










#symmertric_difference()



s1={1,2,3,4}
s2={3,4,5,6}
s1.symmertic(s2)
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    s1.symmertic(s2)
AttributeError: 'set' object has no attribute 'symmertic'
s1.symmertic difference(s2)
SyntaxError: invalid syntax
s1.symmertic _ difference(s2)
SyntaxError: invalid syntax
s1.symmetric_difference(s2)
{1, 2, 5, 6}
s1
{1, 2, 3, 4}
s2
{3, 4, 5, 6}
s1.difference(s2)
{1, 2}
s1={'hello','hi','bye','good'}
s2={'welcome','python'}
s1.union(s2)
{'good', 'welcome', 'hello', 'bye', 'python', 'hi'}
s1.intersection(s2)
set()
s1.difference(s2)
{'good', 'hello', 'bye', 'hi'}
s1.symmertic_difference()
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    s1.symmertic_difference()
AttributeError: 'set' object has no attribute 'symmertic_difference'. Did you mean: 'symmetric_difference'?
s1.symmertic_difference(s2)
Traceback (most recent call last):
  File "<pyshell#208>", line 1, in <module>
    s1.symmertic_difference(s2)
AttributeError: 'set' object has no attribute 'symmertic_difference'. Did you mean: 'symmetric_difference'?
>>> s1.symmertric_difference(s2)
Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    s1.symmertric_difference(s2)
AttributeError: 'set' object has no attribute 'symmertric_difference'. Did you mean: 'symmetric_difference'?
>>> s1.symmetric_difference(s2)
{'hello', 'bye', 'python', 'good', 'welcome', 'hi'}
>>> s1={'hello','python'}
>>> s2={'hi','hello','python'}
>>> s1.symmetric_difference(s2)
{'hi'}
>>> 
>>> 
>>> 

>>> #symmetric_difference_update()\
>>> 
>>> s1={1,2,3,4}
>>> s2={3,4,5,6}
>>> s1.symmetric_difference(s2)
{1, 2, 5, 6}
>>> s1
{1, 2, 3, 4}
>>> s2
{3, 4, 5, 6}
>>> s1.symmetric_difference_update(s2)
>>> s1
{1, 2, 5, 6}
>>> s2
{3, 4, 5, 6}
>>> s1.symmertic_difference_update(s1)
Traceback (most recent call last):
  File "<pyshell#227>", line 1, in <module>
    s1.symmertic_difference_update(s1)
AttributeError: 'set' object has no attribute 'symmertic_difference_update'. Did you mean: 'symmetric_difference_update'?
>>> s1.symmetric_difference_update(s1)
>>> s1
set()
>>> s2
{3, 4, 5, 6}
