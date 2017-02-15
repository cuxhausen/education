# comment

"""
comments
"""
i = 1
i = 1
>>> i
1
>>> i = 666
>>> i
666
>>> 
>>> i = "hello"
>>> i
'hello'
>>> I = 333
>>> i
'hello'
>>> I
333
>>> a = 8
>>> b = a
>>> a = 9
>>> a
9
>>> b
8
>>> l = [1, 2, 3]
>>> l2 = l
>>> l2.ap
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    l2.ap
AttributeError: 'list' object has no attribute 'ap'
>>> l2 = append(888)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    l2 = append(888)
NameError: name 'append' is not defined
>>> l
[1, 2, 3]
>>> l2
[1, 2, 3]
>>> i = 123
>>> i
123
>>> i = -123
>>> i
-123
>>> i = 0b1101100011
>>> i
867
>>> i = 0o345
>>> i
229
>>> i = 0xFF
>>> i
255
>>> f = 1.5
>>> f
1.5
>>> f = 12e-2
>>> f
0.12
>>> f = 12e-3
>>> f
0.012
>>> f = 12e3
>>> f
12000.0
>>> c = 12.3j
>>> c
12.3j
>>> s = "hello, python!"
>>> ы
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    ы
NameError: name 'ы' is not defined
>>> s
'hello, python!'
>>> s = "hello, \"python!"
>>> s
'hello, "python!'
>>> s = """dfeefefd
...dfdfdd
...efegfbyhg
...dfedce
..."""
>>> print(s)
dfeefefd
...dfdfdd
...efegfbyhg
...dfedce
...
>>> s
'dfeefefd\n...dfdfdd\n...efegfbyhg\n...dfedce\n...'
>>> bs = b"hello"
>>> bs
b'hello'
>>> s = "123456789"
>>> s[1]
'2'
>>> s[1] = w
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    s[1] = w
NameError: name 'w' is not defined
>>> person = ("Name", 26, True, ())
>>> person
('Name', 26, True, ())
>>> person[2]
True
>>> person[2] = 27
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    person[2] = 27
TypeError: 'tuple' object does not support item assignment
>>> list[1, 2, 4, 5]list
SyntaxError: invalid syntax
>>> list
<class 'list'>
>>> lst = [1, 2, 4, 5]
>>> lst
[1, 2, 4, 5]
>>> lst.append(5)
>>> lst
[1, 2, 4, 5, 5]
>>> m = set()
>>> m
set()
>>> m = {1, 5, 1}
>>> m
{1, 5}
>>> d = {"username": "ivan", "password": "123"}
>>> d
{'username': 'ivan', 'password': '123'}
>>> d["password"]
'123'
>>> d["id"] = 1
>>> d
{'username': 'ivan', 'password': '123', 'id': 1}
>>> p = None
>>> p
>>> 
>>> n
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    n
NameError: name 'n' is not defined
>>> type(p)
<class 'NoneType'>
>>> type(m)
<class 'set'>
>>> s
'123456789'
>>> s = "hello"
>>> s.upper()
'HELLO'
>>> type(s)
<class 'str'>
>>> type(s) is str
True
>>> type(s) is bool
False
>>> 2 + "5"
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    2 + "5"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> a = 2
>>> b = "5"
>>> b = int(b)
>>> b
5
>>> type(b)
<class 'int'>
>>> a = int(2)a
SyntaxError: invalid syntax
>>> a
2
>>> b = int("010101", 2)
>>> b
21
>>> b = float(b)
>>> b
21.0
>>> b = str(b)
>>> b
'21.0'
>>> b = list(b)
>>> b
['2', '1', '.', '0']
>>> b = str(b)
>>> b
"['2', '1', '.', '0']"
>>> + - * / % ** //
some = 2
some+=1
some
print(some)
i = 0b1
i << 1
d
SyntaxError: invalid syntax
>>> + - * / % ** //
some = 2
some+=1
some
print(some)
i = 0b1
i << 1
lst
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> type(d) is dict
True
>>> type(d) is not dict
False
>>> d is None
False
>>> d
{'username': 'ivan', 'password': '123', 'id': 1}
>>> lst = [1, 2, 3, 4, 5, 6]
>>> lst
[1, 2, 3, 4, 5, 6]
>>> lst[1:]
[2, 3, 4, 5, 6]
>>> lst[:4]
[1, 2, 3, 4]
>>> lst[1:4]
[2, 3, 4]
>>> lst[1:-4]
[2]
>>> lst[1:-3]
[2, 3]
>>> lst[-3:-1]
[4, 5]
>>> lst[::2]
[1, 3, 5]
>>> lst[::-1]
[6, 5, 4, 3, 2, 1]
>>> s = "hello, python!"
>>> s[::-1]
'!nohtyp ,olleh'
>>> len(s)
14
>>> p = None
>>> if p is not None:
    prin("p существует!")

    
>>> q = 5 ** 2 if p is None else 5 ** 3
>>> q
25
>>> a = "789"
>>> a = int(a) if type(a) is str else 0
>>> a
789
>>> 
