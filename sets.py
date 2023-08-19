Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# python sets: unordered collection of unique items. commonly used for computing mathematical opeation such as union, intersection, difference, and symmetric difference.

# Sets are: unordered, changeable(mutable), unindexed, items are unique.

s = {'red','green','blue'}
s
{'red', 'blue', 'green'}

# set constructor.
s = set('abc')
print(s)
{'c', 'a', 'b'}
s
{'c', 'a', 'b'}

S = set(range(0,4))
print(S)
{0, 1, 2, 3}

#convert list into set
s = set([1,2,3])
print(s)
{1, 2, 3}


# add items to a set

S = {'red','green','blue'}
S.add('yellow')
print(S)
{'red', 'blue', 'green', 'yellow'}
S.add(0,'pink')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    S.add(0,'pink')
TypeError: set.add() takes exactly one argument (2 given)
S.insert(0,'pink')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    S.insert(0,'pink')
AttributeError: 'set' object has no attribute 'insert'


# update
S = {'red','green','blue'}
S.update(['yellow','orange']}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
S.update(['yellow','orange'])
print(S)
{'green', 'yellow', 'red', 'orange', 'blue'}

# remove items from a sets.

S = {'red','green','blue'}
S.remove('red')

print(S)
{'blue', 'green'}

#with discard() method
S = {'red','green','blue'}
S.discard('red')
print(S)
{'blue', 'green'}

#remove() vs discard()
# Both methods work exactly the same. The only difference is that If specified item is not present in a set:

# remove() method raises KeyError
# discard() method does nothing

S.remove('red')
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    S.remove('red')
KeyError: 'red'
S.discard('red')

print(S)
{'blue', 'green'}

# The pop() method removes random item from a set and returns it.

S = {'red','blue','green'}
x = S.pop()
print(x)
red
S
{'blue', 'green'}

# clear() method to remove all items from the set.
S = {'red','green','blue'}
S.clear()
pritn(S)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    pritn(S)
NameError: name 'pritn' is not defined. Did you mean: 'print'?

S
set()
S = {'red','green','blue'}
for item in S:
    print(item):
        
SyntaxError: incomplete input
for item in S:
    print(item)

red
blue
green

if 'red' in S:
    print('Yes')

Yes

if 'red' not in S:
    print('Yes')

if 'red' not in S:
    print('Yes')
else:
    print('No')

No

# Set operations.
# Set Union

A = {'red','green','blue'}
B = {'yellow','red','orange'}
>>> 
>>> print(A|B)
{'green', 'yellow', 'red', 'orange', 'blue'}
>>> # By method
>>> print(A.union(B))
{'green', 'yellow', 'red', 'orange', 'blue'}
>>> 
>>> 
>>> # Set Intersection.
>>> # by operator
>>> print(A&B)
{'red'}
>>> 
>>> # by method.
>>> print(A.intersection(B))
{'red'}
>>> 
>>> # Set Difference.
>>> 
>>> #by operator
>>> print(A-B)
{'green', 'blue'}
>>> #by method
>>> print(A.difference(B))
{'green', 'blue'}
>>> 
>>> 
>>> # Set Symmetric difference
>>> # by operator
>>> print(A^B)
{'blue', 'yellow', 'orange', 'green'}
>>> # by method
>>> print(A.symmetric_difference(B))
{'blue', 'yellow', 'orange', 'green'}
>>> 
>>> 
>>> 
>>> # Python Frozenset.
>>> 
>>> S = frozenset({'red','green','blue'})
>>> print(S)
frozenset({'red', 'blue', 'green'})
>>> 
>>> # frozenset are unchangeable, we can perform non-modifying operations on them.
>>> print(S | {'yellow'})
frozenset({'red', 'blue', 'green', 'yellow'})
