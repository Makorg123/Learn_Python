Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Tuples is an ordered collection of values, tuples are immutable(unchangeable).
T = (1, 'abc', 1.23, True)
T
(1, 'abc', 1.23, True)
# Singleton Tuple
T = (3,)
type(T)
<class 'tuple'>
T = (3)
type(T)
<class 'int'>

#Tuple constructor
T = tuple([1,2,3])
type(T)
<class 'tuple'>
print(T)
(1, 2, 3)
#Convert a string into tuple
T = tuple('abc')
print(T)
('a', 'b', 'c')
type(T)
<class 'tuple'>

#Nested Tuples
T = ('red',('green','blue'),'yellow')
T
('red', ('green', 'blue'), 'yellow')
T(0)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    T(0)
TypeError: 'tuple' object is not callable

# Tuple packing & unpacking.
T = ('red','green','blue')
a,b,c = T
print(a)
red
print(b)
green
print(c)
blue

#Tuple usage. Split an email into a user name and a domain.
addr = 'bob@python.org'
user,domain = add.split('@')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    user,domain = add.split('@')
NameError: name 'add' is not defined. Did you mean: 'addr'?
user,domain = addr.split('@')
print(user)
bob
print(domain)
python.org


add = 'anas@gmail.com'
user,domain = add.split('@')
user
'anas'
domain
'gmail.com'

# Access tuple
T
('red', 'green', 'blue')
T = ('red','green','blue','yellow','orange')
print(T[0])
red
(T[1])
'green'
print(T[2])
blue
T = ('red',('green','blue'),'yellow')
print(T[0][1])
e
print(T)
('red', ('green', 'blue'), 'yellow')
print(T[0])
red
print(T[0][0][1])
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(T[0][0][1])
IndexError: string index out of range
print(T[0][2])
d
print(T[1])
('green', 'blue')
print(T[1][2])
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    print(T[1][2])
IndexError: tuple index out of range
print(T[1][0])
green
print(T[1][1])
blue
print(T[1][1][0:2])
bl

# Change tuple itmes [Tuples are immutable(unchangeable) onece a tuple is created, it cannot be modified.
T = ('red','green','blue')
T[0] = 'black'
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    T[0] = 'black'
TypeError: 'tuple' object does not support item assignment

# Tuple immutability is applicable only to the top level of the tuple itself, not to its contents. For example, a list inside a tuple can be changed as usual.

T = (1,[2,3],4)
print(T)
(1, [2, 3], 4)
T[1][0] = 'xx'
print(T)
(1, ['xx', 3], 4)


# Delete a tuple.
T = ('red','green','blue')
del T

print(T)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    print(T)
NameError: name 'T' is not defined


# Tuple Concatenation & Repetition.
T = ('red','green','blue') + (1,2,4)
T
('red', 'green', 'blue', 1, 2, 4)

T = ('red',) * 3
T
('red', 'red', 'red')


# find tuple length
T
('red', 'red', 'red')
len(T)
3
>>> 
>>> # Check if item exists in a tuple.
>>> 
>>> T = ('red','green','blue')
>>> if 'red' in T:
...     print('yes')
... 
yes
>>> # check for absence.
>>> 
>>> if 'yellow' not in T:
...     print('Yes')
... 
Yes
>>> 
>>> # iterate through a tuple.
>>> 
>>> T = ('red','green','blue')
>>> for item in T:
...     print(item)
... 
red
green
blue
>>> 
>>> 
>>> # Tuple sorting.
>>> 
>>> # Method 1:
>>> T = ('cc','aa','dd','bb')
>>> print(tuple(sorted(T)))
('aa', 'bb', 'cc', 'dd')
>>> 
>>> # Method 2:
>>> T = ('ee','aa','hh','oo')
>>> tmp = lsit(T)
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    tmp = lsit(T)
NameError: name 'lsit' is not defined
>>> tmp = list(T)
>>> tmp.sort()
>>> T = tuple(tmp)
>>> print(T)
('aa', 'ee', 'hh', 'oo')
>>> 
