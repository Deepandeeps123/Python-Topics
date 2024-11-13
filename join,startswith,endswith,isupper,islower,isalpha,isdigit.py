Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='hello'
s.join()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s.join()
TypeError: str.join() takes exactly one argument (0 given)
s.join('')
''
s.join(' ')
' '
s.join('_')
'_'
'_'.join(s)
'h_e_l_l_o'
s.join('a')
'a'
s='hello everu one'
'-'.join(s)
'h-e-l-l-o- -e-v-e-r-u- -o-n-e'
s='the question of the element'
''.join(s)
'the question of the element'
'_'.join()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    '_'.join()
TypeError: str.join() takes exactly one argument (0 given)
'_'.join(s)
't_h_e_ _q_u_e_s_t_i_o_n_ _o_f_ _t_h_e_ _e_l_e_m_e_n_t'
s='hello','every','one'
''.join(s)
'helloeveryone'
' '.join(s)
'hello every one'
s='hello''every''one'

' '.join(s)
'h e l l o e v e r y o n e'
''.join(s)
'helloeveryone'
s='hello','123'
' '.join(s)
'hello 123'
s='hello123'
' '.join(s)
'h e l l o 1 2 3'






#startswith





s='programming'
s.startswith('p')
True
s.startswith('r')
False
s.startswith('pro')
True
s.startswith('gram',3,6)
False
s.startswith('ro',1)
True
s.startswith('ram',4,7)
True
s.startswith('ram',4,-4)
True
s.startswith('ram',-7)
True
s.startswith('ram',-7,-1)
True
s.startswith('ram')
False
s,startswith('zz')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    s,startswith('zz')
NameError: name 'startswith' is not defined
s.startswith('z')
False
s.startswith('z',1,7)
False






#endwith




s='programming'
s.endwith('e')
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    s.endwith('e')
AttributeError: 'str' object has no attribute 'endwith'. Did you mean: 'endswith'?
s.endswith('e')
False
s.endswith('age')
False
s.endswith('gua',0,len(s))
False
s.endswith('ang',0,3)
False
s.endswith('ing',0,3)
False
s='hello'
s.endswith('ing',1,8)
False
s='morning'
s.endswith('ing',-5)
True

s='hello every one'
s,endswith('ery',0,8)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    s,endswith('ery',0,8)
NameError: name 'endswith' is not defined
s.endswith('ery',0,8)
False
s.endswith('ery',0,11)
True
s.endswith('ery')
False
s.endswith('ery',8,11)
True
s.endswith('ery',-14,-4)
True







#isupper()
s='helllo'
s.isupper()
False
s='HELLO'
s.isupper()
True
s='Hello'
s.isupper()
False
s='HeLlO EvErY OnE'
s.isupper()
False
s.isupper('s')
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    s.isupper('s')
TypeError: str.isupper() takes no arguments (1 given)
s='hello123'
s.isupper()
False
s='deepanvinayagam@gmail.com'
s.isupper()
False
s.upper()
'DEEPANVINAYAGAM@GMAIL.COM'





#islower()



s='hello'
s.islower()
True
s='Hello'
s.islower()
False
s='hello@123'
s.islower()
True
s='happy.123'
s.islower()
True
s='Hello.123'
s.islower()
False
>>> 
>>> 

... 
>>> 
>>> #isalpha
>>> 
>>> 
>>> 
>>> s='Hello'
>>> s.isalpha()
True
>>> s='hello123.'
>>> s.isalpha()
False
>>> s='hello.......@'
>>> s.isalpha()
False
>>> 
>>> 
>>> 
>>> 
>>> #isdigit()
>>> 
>>> 
>>> 
>>> s='Hello.123'
>>> s.isdigit()
False
>>> s='123'
>>> s.isdigit()
True
>>> s='52.33'
>>> s.isdigit()
False
>>> 
>>> 
>>> 
>>> 
>>> 
