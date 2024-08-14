Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

  
1
2
4
5
6
i = 0
while i < 6:
  i += 1
  if i < 4:
    continue
  print(i)

  
4
5
6
i = 1
while i > 20
SyntaxError: expected ':'
i = 1
i = 40
while i > 20:
    print(i)
    i -= 1
    else print ("i is now less than 20)
                
SyntaxError: unterminated string literal (detected at line 4)

i = 40
                
while i > 20:
    print(i)
    i -= 1
    else print ("i is now less than 20")
    
SyntaxError: invalid syntax
i = 40
while i > 20:
    print(i)
    i -= 1
    else: print ("i is now less than 20")
    
SyntaxError: invalid syntax
i = 40
while i > 20:
    print(i)
    i -= 1
else: print ("i is now less than 20")

40
39
38
37
36
35
34
33
32
31
30
29
28
27
26
25
24
23
22
21
i is now less than 20

for x in "Jumanji":
    print(x)

    
J
u
m
a
n
j
i
for x in "Jumanji":
    print(x)
    if x == "Jum":
        break

    
J
u
m
a
n
j
i

berry = ["raspberry", "blackberry", "strawberry"]
for x in berry:
    print(berry)
    if x == "blackberry":
        break

    
['raspberry', 'blackberry', 'strawberry']
['raspberry', 'blackberry', 'strawberry']
berry = ["raspberry", "blackberry", "strawberry"]

berry = ["raspberry", "blackberry", "strawberry"]
for x in berry:
    print(x)
    if x == "blackberry":
        break
    
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> berry = ["raspberry", "blackberry", "strawberry"]
>>> berry = ["raspberry", "blackberry", "strawberry"]
... for x in berry:
...     print(x)
...     if x == "blackberry":
...         break
...     
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> berry = ["raspberry", "blackberry", "strawberry"]
>>> 
... for x in berry:
...     print(x)
...     if x == "blackberry":
...         break
... 
...     
raspberry
blackberry
>>> berry = ["raspberry", "blackberry", "strawberry"]
>>> for x in berry:
...     if x == "blackberry":
...     continue
...     print(x)
... 
...     
SyntaxError: expected an indented block after 'if' statement on line 2
>>> 
>>> berry = ["raspberry", "blackberry", "strawberry"]
>>> for x in berry:
...     if x == "blackberry":
...         continue
...     print(x)
... 
...     
raspberry
strawberry
>>> for five in range(0, 50, 5):
...     print(five)

    
0
5
10
15
20
25
30
35
40
45
for five in range(0, 50, 5):
    print(five)
    else:
        
SyntaxError: invalid syntax
for five in range(0, 50, 5):
    print(five)
else:
    print("we made it!!!")

    
0
5
10
15
20
25
30
35
40
45
we made it!!!

name = 'Python'
print(len(name))
6
for i in enumerate(name):
    print(i)

    
(0, 'P')
(1, 'y')
(2, 't')
(3, 'h')
(4, 'o')
(5, 'n')

