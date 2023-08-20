Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Dictionaries are Python’s implementation of a data structure, generally known as associative arrays, hashes, or hashmaps.

# You can think of a dictionary as a mapping between a set of indexes (known as keys) and a set of values. Each key maps to a value. The association of a key and a value is called a key:value pair or sometimes an item.

# Create a dictionar to store employee record.
emp = {'name':'Bob','Age':30,'job':'Dev','city':'NY','email':'bob@web.com'}

emp
{'name': 'Bob', 'Age': 30, 'job': 'Dev', 'city': 'NY', 'email': 'bob@web.com'}

# The Dict() constructor.

# we can convert two-value sequences into a dictionary with python's dict() constructor.

# create a dict with a list of two-item tuples.
L = [('name','Bob'),
     ('age',23),
     ('job','Dev')]
D = dict(L)
print(D)
{'name': 'Bob', 'age': 23, 'job': 'Dev'}


# Create a dict with a tuple of two-item lists.
T = (['name','Bob'),
     
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
T = (['name','Bob'),
     
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
T = (['name','Bob'],['age',34],['job','Dev'])
     
T
     
(['name', 'Bob'], ['age', 34], ['job', 'Dev'])
Dict = dict(T)
     
print(Dict)
     
{'name': 'Bob', 'age': 34, 'job': 'Dev'}


# Others ways to create Dictionaries
     
# Using zip() function
     
keys = ['name','age','job']
     
values = ['Bob',25,'Dev']
     
D = dict(zip(keys,values))
     
D
     
{'name': 'Bob', 'age': 25, 'job': 'Dev'}

# Access dict items
     
print(D['name'])
     
Bob

# if you refer to a key that is not in the dictionary , you'll get an exception.
     
print(D['Salary'])
     
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    print(D['Salary'])
KeyError: 'Salary'
# To avoid such exception, you can use the special dictioary get() method. This method returns the value for key if key in the dictionary, else None, so that this method never raises a KeyError.
     
print(D['name']) #when key is present
     
Bob
print(D.get('salary')] # when key is absent.
     
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
print(D.get('salary')) # when key is absent.
     
None
# Add or update dict items
     
D['name'] = 'sam'
     
print(D)
     
{'name': 'sam', 'age': 25, 'job': 'Dev'}
D['salary'] = 23000
     
print(D)
     
{'name': 'sam', 'age': 25, 'job': 'Dev', 'salary': 23000}

# Merge two dictionaries.
     
D1 = {'name':'Bob', 'age':23, 'job':'Dev'}
     
D2 = {'age':29, 'city':'NY', 'email':'bob@mail.com'}
     
D1.update(D2)
     
print(D1)
     
{'name': 'Bob', 'age': 29, 'job': 'Dev', 'city': 'NY', 'email': 'bob@mail.com'}

# Remove Dict items
     
D
     
{'name': 'sam', 'age': 25, 'job': 'Dev', 'salary': 23000}
x = D.pop('age')
     
x
     
25
D
     
{'name': 'sam', 'job': 'Dev', 'salary': 23000}
# if you don't need the removed value, use the del statement.
     
del D['name']
     
D
     
{'job': 'Dev', 'salary': 23000}
# Remove last inserted item.
     
x = D.popitem()
     
print(D)
     
{'job': 'Dev'}
print(x)
     
('salary', 23000)
D.clear()
     
D
     
{}

# Get All keys, values and key:Value Pairs
     
D = {'name':'Bob', 'age':34, 'salary':30000}
     
print(list(D.keys()))
     
['name', 'age', 'salary']
print(list(D.values()))
     
['Bob', 34, 30000]
print(list(D.items()))
     
[('name', 'Bob'), ('age', 34), ('salary', 30000)]

# iterate through a dict
     
D
     
{'name': 'Bob', 'age': 34, 'salary': 30000}
for x in D:
     print(x)

name
age
salary
for x in D:
     print(D[x])

Bob
34
30000

# check if a key or value exists
     
D
     
{'name': 'Bob', 'age': 34, 'salary': 30000}
print('name' in D)
     
True
print('class' in D)
     
False
# for values
     
print('Bob' in D.values())
     
True


# ---- Nested Dictionary -----#
     

D = {'emp1':{'name':'BOb','job':'Mgr'},
     'emp2':{'name':'Kim','job':'Dev'},
     'emp3':{'name':'Sam','job':'Dev'}}
     
D
     
{'emp1': {'name': 'BOb', 'job': 'Mgr'}, 'emp2': {'name': 'Kim', 'job': 'Dev'}, 'emp3': {'name': 'Sam', 'job': 'Dev'}}

# Access Nested Dictionary Items.
     
print(D['emp1']['name'])
     
BOb
print(D['emp2']['name'])
...      
Kim
>>> print(D['emp1']['job'])
...      
Mgr
>>> 
>>> 
>>> # Change Nested Dictionary items.
...      
>>> D['emp3']['name'] = 'max'
...      
>>> D['emp3']['job'] = 'Janitor'
...      
>>> print(D)
...      
{'emp1': {'name': 'BOb', 'job': 'Mgr'}, 'emp2': {'name': 'Kim', 'job': 'Dev'}, 'emp3': {'name': 'max', 'job': 'Janitor'}}
>>> print(D['emp3'])
...      
{'name': 'max', 'job': 'Janitor'}
>>> 
>>> # iterate through a nested dictionary
...      
>>> for id,info in D.items():
...      print("\nEmployee ID:", id)
...      for key in info:
...      print(key + ':', info[key])
...      
SyntaxError: expected an indented block after 'for' statement on line 3
>>> for id,info in D.items():
...      print("\nEmployee ID:", id)
...      for key in info:
...          print(key + ':', info[key])
... 

Employee ID: emp1
name: BOb
job: Mgr

Employee ID: emp2
name: Kim
job: Dev

Employee ID: emp3
name: max
job: Janitor
