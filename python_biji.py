Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 8-1
7
>>> def say_hello(name):
	print("hello {}".format(name))
	for i in range(3):
		print(name)

		
>>> say_hello('ming')
hello ming
ming
ming
ming
>>> say_hello('ming')
hello ming
ming
ming
ming
>>> def say_hello(name):
	print("hello {}".format(name))
	for i in range(3):
		print(name)

		
>>> def say_hello(name):
	print("hello {}".format(name))
	for i in range(3):
		print(name)

		
>>> say_hello('ming')
hello ming
ming
ming
ming
>>> 77+1
78
>>> score=77
>>> print(score)
77
>>> score
77
>>> _score=88
>>> _score
88
>>> ss
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    ss
NameError: name 'ss' is not defined
>>> _score=88
>>> score
77
>>> myScore=100
>>> myScore
100
>>> ss=''
>>> ss
''
>>> ss=
SyntaxError: invalid syntax
>>> ss=1
>>> ss
1
>>> name='tom'
>>> x=20
>>> y='tom'
>>> id(y)
53898632
>>> z='tom'
>>> in(z)
SyntaxError: invalid syntax
>>> id(z)
53898632
>>> a=50
>>> b=50
>>> a==b
True
>>> a===b
SyntaxError: invalid syntax
>>> id(a)
1412355344
>>> id(b)
1412355344
>>> a is b
True
>>> mike=8000
>>> peter=8000
>>> mike=peter
>>> mike==peter
True
>>> id(mike)
53879664
>>> id(peter)
53879664
>>> typr(2)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    typr(2)
NameError: name 'typr' is not defined
>>> type(222)
<class 'int'>
>>> type(1.11)
<class 'float'>
>>> type('222')
<class 'str'>
>>> type()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    type()
TypeError: type() takes 1 or 3 arguments
>>> list=[1,3,2]
>>> x = list.sort()
>>> x
>>> print(x)
None
>>> x is None
True
>>> x == None
True
>>> 5>3
True
>>> 5<3
False
>>> type(5<3)
<class 'bool'>
>>> 
>>> 3=2
SyntaxError: can't assign to literal
>>> 3=2
SyntaxError: can't assign to literal
>>> 3+2
5
>>> 8_2
SyntaxError: invalid syntax
>>> 8-2
6
>>> 21*7
147
>>> 23/7
3.2857142857142856
>>> 23//7
3
>>> 2**3
8
>>> 22%7
1
>>> 25%7
4
>>> 10 + "30"
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    10 + "30"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 10 + int("30")
40
>>> 10+int("1101")
1111
>>> 10+int("1101",2)
23
>>> int('222',8)
146
>>> int("177",8)
127
>>> "2.14"*2
'2.142.14'
>>> int("3.14")*2
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    int("3.14")*2
ValueError: invalid literal for int() with base 10: '3.14'
>>> float("3.14")*2
6.28
>>> bin(10)
'0b1010'
>>> hex(8)
'0x8'
>>> oct(10)
'0o12'
>>> 21/7
3.0
>>> 22/7
3.142857142857143
>>> 22//7
3
>>> import math
>>> math.floor
<built-in function floor>
>>> math.floor(3.14)
3
>>> math.floor(-3.14)
-4
>>> math.trunc(3.99)
3
>>> math.trunc(-3.99)
-3
>>> math.ceil(3.14)
4
>>> math.ceil(-13.14)
-13
>>> math.ceil(-3.14)
-3
>>> round(3.14)
3
>>> round(3.9)
4
>>> round(-3.9)
-4
>>> math.pi
3.141592653589793
>>> pow(2,4)
16
>>> import decimal
>>> decimal.Decimal('0.1')+decimal.D
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    decimal.Decimal('0.1')+decimal.D
AttributeError: module 'decimal' has no attribute 'D'
>>> decimal.Decimal('0.1')+decimal.Decimal
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    decimal.Decimal('0.1')+decimal.Decimal
TypeError: unsupported operand type(s) for +: 'decimal.Decimal' and 'type'
>>> decimal.Decimal('0.1')+decimal.Decimal('0.1')-de
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    decimal.Decimal('0.1')+decimal.Decimal('0.1')-de
NameError: name 'de' is not defined
>>> decimal.Decimal('0.1')+decimal.Decimal('0.1')-decimal.Decimal('0.2')
Decimal('0.0')
>>> from decimal import Decimal
>>> Decimal('0.1')+Decimal('0.1')
Decimal('0.2')
>>> Decimal(0.1)+Decimal(0.1)-Decimal(0.2)
Decimal('4.8434595763683319091796875E-29')
>>> True == 1
True
>>> 1
1
>>> 2
2
>>> True ==3
False
>>> False == 0
True
>>> False == 1
False
>>> x=3+True
>>> x
4
>>> x=99-True
>>> x
98
>>> 98
98
>>> bool(1)
True
>>> bool(false)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    bool(false)
NameError: name 'false' is not defined
>>> bool(0)
False
>>> bool(2)
True
>>> bool(-3)
True
>>> bool('222')
True
>>> bool([])
False
>>> bool('')
False
>>> bool()
False
>>> x=()
>>> bool(x)
False
>>> x=[]x=()
SyntaxError: invalid syntax
>>> x={}
>>> bool(x)
False
>>> if x:
	print 1
	
SyntaxError: Missing parentheses in call to 'print'
>>> if x:
	print(1)

	
>>> if !x:
	
SyntaxError: invalid syntax
>>> if !x:
	
SyntaxError: invalid syntax
>>> x=1
>>> if x:
	print(222)

	
222
>>> score=80
>>> score
80
>>> score=[80,90,100]
>>> score
[80, 90, 100]
>>> score=[80,90,99.3]
>>> type(score)
<class 'list'>
>>> score
[80, 90, 99.3]
>>> x=[50,60,66.6,'tom']
>>> score[0]
80
>>> score[2]
99.3
>>> score[-1]
99.3
>>> score[0:2]
[80, 90]
>>> score[0:3]
[80, 90, 99.3]
>>> score[0:3=9]
SyntaxError: invalid syntax
>>> score[0:9]
[80, 90, 99.3]
>>> score.append(78)
>>> score
[80, 90, 99.3, 78]
>>> score.append(79)
>>> score
[80, 90, 99.3, 78, 79]
>>> score[]=22
SyntaxError: invalid syntax
>>> y=[1,2,3,['tom','ming']]
>>> y
[1, 2, 3, ['tom', 'ming']]
>>> score
[80, 90, 99.3, 78, 79]
>>> score[0]=85.2
>>> score
[85.2, 90, 99.3, 78, 79]
>>> x=[1,2,3]
>>> x
[1, 2, 3]
>>> x[1]
2
>>> name=list('刘黎明')
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    name=list('刘黎明')
TypeError: 'list' object is not callable
>>> name=list(1,32)
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    name=list(1,32)
TypeError: 'list' object is not callable
>>> range(5)
range(0, 5)
>>> list(range(0,5))
Traceback (most recent call last):
  File "<pyshell#179>", line 1, in <module>
    list(range(0,5))
TypeError: 'list' object is not callable
>>> list(range(5))
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    list(range(5))
TypeError: 'list' object is not callable
>>> list(range(2))
Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    list(range(2))
TypeError: 'list' object is not callable
>>> names=['tom','jerry','mike']
>>> 'tome' in names
False
>>> 'tom' in names
True
>>> 'tom' not in names
False
>>> 'tome' not in names
True
>>> range(5)
range(0, 5)
>>> range(0,5)
range(0, 5)
>>> x=list(range(0,4))
Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    x=list(range(0,4))
TypeError: 'list' object is not callable
>>> list
[1, 2, 3]
>>> list
[1, 2, 3]
>>> score
[85.2, 90, 99.3, 78, 79]
>>> name[-1]
'm'
>>> citys=['北京','上海','广州','深圳','上海']
>>> citys[0,2]
Traceback (most recent call last):
  File "<pyshell#195>", line 1, in <module>
    citys[0,2]
TypeError: list indices must be integers or slices, not tuple
>>> citys[0:2]
['北京', '上海']
>>> citys[0:3]
['北京', '上海', '广州']
>>> citys[0:4]
['北京', '上海', '广州', '深圳']
>>> citys[5]
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    citys[5]
IndexError: list index out of range
>>> citys[-1]
'上海'
>>> citys[4]
'上海'
>>> citys[-5,-3]
Traceback (most recent call last):
  File "<pyshell#202>", line 1, in <module>
    citys[-5,-3]
TypeError: list indices must be integers or slices, not tuple
>>> citys[-5:-3]
['北京', '上海']
>>> citys[:3]
['北京', '上海', '广州']
>>> citys[0:4]
['北京', '上海', '广州', '深圳']
>>> citys[0:-1]
['北京', '上海', '广州', '深圳']
>>> citys[0:]
['北京', '上海', '广州', '深圳', '上海']
>>> citys[:]
['北京', '上海', '广州', '深圳', '上海']
>>> citys[::]
['北京', '上海', '广州', '深圳', '上海']
>>> len(citys)
5
>>> min(score)
78
>>> score
[85.2, 90, 99.3, 78, 79]
>>> max(score)
99.3
>>> sum(scores)
Traceback (most recent call last):
  File "<pyshell#214>", line 1, in <module>
    sum(scores)
NameError: name 'scores' is not defined
>>> sum(score)
431.5
>>> citys.index('北京')
0
>>> score.index(78)
3
>>> citys.count(78)
0
>>> l=[1,2,3,2,2,2,3,4,3,2]
>>> l.count(2)
5
>>> s=[1,2,3,4,5,6,7,8,9,10]
>>> s
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> s[0]=99
>>> s
[99, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> s[:3]=[98,99,100]
>>> s
[98, 99, 100, 4, 5, 6, 7, 8, 9, 10]
>>> s[:3]=[98,99,100,101,102]
>>> s
[98, 99, 100, 101, 102, 4, 5, 6, 7, 8, 9, 10]
>>> s[:5]=[999]
>>> s
[999, 4, 5, 6, 7, 8, 9, 10]
>>> l=list(range(1,11))
Traceback (most recent call last):
  File "<pyshell#231>", line 1, in <module>
    l=list(range(1,11))
TypeError: 'list' object is not callable
>>> l
[1, 2, 3, 2, 2, 2, 3, 4, 3, 2]
>>> l
[1, 2, 3, 2, 2, 2, 3, 4, 3, 2]
>>> l=[1,2,3,4,5,6,7,8,9,10]
>>> l
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> l[::2]=[99,99,9,99,9]
>>> l
[99, 2, 99, 4, 9, 6, 99, 8, 9, 10]
>>> del l[0]
>>> l
[2, 99, 4, 9, 6, 99, 8, 9, 10]
>>> l=[1,2,3,4,5,6,7,8,9,10]
>>> l
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> l.r
Traceback (most recent call last):
  File "<pyshell#242>", line 1, in <module>
    l.r
AttributeError: 'list' object has no attribute 'r'
>>> l.remove(2)
>>> l
[1, 3, 4, 5, 6, 7, 8, 9, 10]
>>> l.remove(9)
>>> l
[1, 3, 4, 5, 6, 7, 8, 10]
>>> x=[1,2,3,4,3,2,1,2,3]
>>> x.remove(2)
>>> x
[1, 3, 4, 3, 2, 1, 2, 3]
>>> x.clear()
>>> x
[]
>>> x.append(5)
>>> x
[5]
>>> x.append(6)
>>> x
[5, 6]
>>> x.append([7,8])
>>> x
[5, 6, [7, 8]]
>>> x.extend([9,10])
>>> xx
Traceback (most recent call last):
  File "<pyshell#259>", line 1, in <module>
    xx
NameError: name 'xx' is not defined
>>> x
[5, 6, [7, 8], 9, 10]
>>> x
[5, 6, [7, 8], 9, 10]
>>> x.insert(0.99)
Traceback (most recent call last):
  File "<pyshell#262>", line 1, in <module>
    x.insert(0.99)
TypeError: insert() takes exactly 2 arguments (1 given)
>>> x.insert(0,99)
>>> x
[99, 5, 6, [7, 8], 9, 10]
>>> x.insert(3,100)
>>> x
[99, 5, 6, 100, [7, 8], 9, 10]
>>> x.insert(2,101)
>>> x
[99, 5, 101, 6, 100, [7, 8], 9, 10]
>>> x[2:2]=[101]
>>> x
[99, 5, 101, 101, 6, 100, [7, 8], 9, 10]
>>> x.pop()
10
>>> x
[99, 5, 101, 101, 6, 100, [7, 8], 9]
>>> x.pop
<built-in method pop of list object at 0x000000000337E908>
>>> x.pop()
9
>>> x
[99, 5, 101, 101, 6, 100, [7, 8]]
>>> result=x.pop()
>>> x
[99, 5, 101, 101, 6, 100]
>>> esult
Traceback (most recent call last):
  File "<pyshell#278>", line 1, in <module>
    esult
NameError: name 'esult' is not defined
>>> result
[7, 8]
>>> x
[99, 5, 101, 101, 6, 100]
>>> x.reverse()
>>> x
[100, 6, 101, 101, 5, 99]
>>> y=x.reverse()
>>> x
[99, 5, 101, 101, 6, 100]
>>> y
>>> s=[0,1,2,3,4,5,6,7,8,9,10]
>>> s
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> k=l
>>> k[0]=99
>>> k
[99, 3, 4, 5, 6, 7, 8, 10]
>>> s
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> l
[99, 3, 4, 5, 6, 7, 8, 10]
>>> k=s
>>> k[0]=99
>>> k
[99, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> s
[99, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> l = list(range(11))
Traceback (most recent call last):
  File "<pyshell#298>", line 1, in <module>
    l = list(range(11))
TypeError: 'list' object is not callable
>>> 
>>> 
>>> l=[0,1,2,3,4,5,6,7,8,9,10]
>>> l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> s=l[:]
>>> s
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> s[0]=99
>>> s
[99, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> x=l.copy()
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> x[-1]=101
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 101]
>>> l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> l.sort()
>>> l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> scort.sort()
Traceback (most recent call last):
  File "<pyshell#315>", line 1, in <module>
    scort.sort()
NameError: name 'scort' is not defined
>>> score
[85.2, 90, 99.3, 78, 79]
>>> score.sort()
>>> score
[78, 79, 85.2, 90, 99.3]
>>> score.reverse()
>>> score
[99.3, 90, 85.2, 79, 78]
>>> people=['tom','jerry','mike','peter','join']
>>> people
['tom', 'jerry', 'mike', 'peter', 'join']
>>> people.sort()
>>> people
['jerry', 'join', 'mike', 'peter', 'tom']
>>> sorted(score)
[78, 79, 85.2, 90, 99.3]
>>> sorted(people,key=lambda n:n[1])
['jerry', 'peter', 'mike', 'join', 'tom']
>>> 
