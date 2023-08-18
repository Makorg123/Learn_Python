Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('Hello world')
Hello world
squares = [1,4,9,16,25]
squares
[1, 4, 9, 16, 25]
squares[0]
1
squares[-1]
25
cube = [2,3,4,5,6,7]
cube[0] = 1
cube
[1, 3, 4, 5, 6, 7]
cube.append(231)
cube
[1, 3, 4, 5, 6, 7, 231]
cube.insert(0,123)
cube
[123, 1, 3, 4, 5, 6, 7, 231]
cube.insert(3,500)
cube
[123, 1, 3, 500, 4, 5, 6, 7, 231]
cube[2:4]
[3, 500]
cube[2:4] = ['A','B
             
SyntaxError: incomplete input
cube[2:4] = ['A','B']
             
cube
             
[123, 1, 'A', 'B', 4, 5, 6, 7, 231]
cube[2:4] = []
             
cube
             
[123, 1, 4, 5, 6, 7, 231]
cube[:]
             
[123, 1, 4, 5, 6, 7, 231]
cube
             
[123, 1, 4, 5, 6, 7, 231]
cube[:] =[]
             
cube
             
[]
a = [1,2,3,4,5]
             
b = ['a','b']
             
c = [a,b]
             
c
             
[[1, 2, 3, 4, 5], ['a', 'b']]
c[0][1]
             
2
c[1][1]
             
'b'
L = ['a','b',['cc','dd',['eee','fff']],'g','h]
     
SyntaxError: incomplete input
L = ['a','b',['cc','dd',['eee','fff']],'g','h']
     
L[0][1][0]
     
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    L[0][1][0]
IndexError: string index out of range
L[-3][-1][-1]
     
'fff'
L[3][1][1]
     
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    L[3][1][1]
IndexError: string index out of range
L[3][0][0]
     
'g'
L[3]
     
'g'
L[0]
     
'a'
L
     
['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
L[1]
     
'b'
L[2]
     
['cc', 'dd', ['eee', 'fff']]
L[2][0]
     
'cc'
L[2]
     
['cc', 'dd', ['eee', 'fff']]
L[2][2]
     
['eee', 'fff']
L[2][2][0]
     
'eee'
number = [3,4,5,[56,67,"name",45,66]]
     
number[0]
     
3
number[3]
     
[56, 67, 'name', 45, 66]
number[3][2]
     
'name'
number[3][2][1:3]
     
'am'
L = l
     
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    L = l
NameError: name 'l' is not defined. Did you mean: 'L'?
l = L
     
l
     
['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
l[2]
     
['cc', 'dd', ['eee', 'fff']]
l[3]
     
'g'
l[2][1]
     
'dd'
l.append('xx')
     
l
     
['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h', 'xx']
l[0].append('b')
     
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    l[0].append('b')
AttributeError: 'str' object has no attribute 'append'
l[1].append('c')
     
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    l[1].append('c')
AttributeError: 'str' object has no attribute 'append'
l[1].insert(0,12)
     
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    l[1].insert(0,12)
AttributeError: 'str' object has no attribute 'insert'
l[2].insert(0,'x')
     
l
     
['a', 'b', ['x', 'cc', 'dd', ['eee', 'fff']], 'g', 'h', 'xx']
l[5].insert(1,'GGG')
     
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    l[5].insert(1,'GGG')
AttributeError: 'str' object has no attribute 'insert'
l[6].insert(0,'GGG')
     
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    l[6].insert(0,'GGG')
IndexError: list index out of range
l
     
['a', 'b', ['x', 'cc', 'dd', ['eee', 'fff']], 'g', 'h', 'xx']
l[5][0].insert(0,'hhhh')
     
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    l[5][0].insert(0,'hhhh')
AttributeError: 'str' object has no attribute 'insert'
>>> l[2][3].insert(0,12)
...      
>>> l
...      
['a', 'b', ['x', 'cc', 'dd', [12, 'eee', 'fff']], 'g', 'h', 'xx']
>>> l[1].extend([1,2,3,4])
...      
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    l[1].extend([1,2,3,4])
AttributeError: 'str' object has no attribute 'extend'
>>> l[2].extend([1,2,4,6,7])
...      
>>> l
...      
['a', 'b', ['x', 'cc', 'dd', [12, 'eee', 'fff'], 1, 2, 4, 6, 7], 'g', 'h', 'xx']
>>> # Convet list items to absolute values.
...      
>>> vec = [-4,-3,-5,-2,0]
...      
>>> l = [abx(x) for x in vec]
...      
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    l = [abx(x) for x in vec]
  File "<pyshell#75>", line 1, in <listcomp>
    l = [abx(x) for x in vec]
NameError: name 'abx' is not defined. Did you mean: 'abs'?
>>> l = [abs(x) for x in vec]
...      
>>> l
...      
[4, 3, 5, 2, 0]
>>> # removes whitespaces of list items.
...      
>>> colors = [' green', '  blue', ' red ']
...      
>>> l = [color.strip() for color in colors]
...      
>>> l
...      
['green', 'blue', 'red']
