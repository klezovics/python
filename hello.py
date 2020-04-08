""" 
#1 Base

def print_greeting(name):
  print("Hello, "+name)

# Execution starts here
name=input('Enter your name\n')

for i in range(1,4):
  print_greeting(name) """

# outer="This is an outer var"

""" 
#2 Use and define globals locally

def defineGlobalLocally():
    global globalVar
    globalVar="I am global!"
    print("Inside function:"+globalVar)

defineGlobalLocally()
print("Outside function:"+globalVar) """

""" 
#3 Read envionment variables
import os
print(os.environ['TEST_VAR']) """

"""
#4 Read in a file and split string

f=open("input.txt")
Lines=f.readlines()

for line in Lines:
    print(line)
"""

""" 
#5 Write lines to file

f=open("input.txt",'w')
f.write('New line1\n')
 """

"""
#6 Do system calls

import os
os.system("ls -l")
"""

""" 
#7 Get type of variable

x=5
print(type(x))
"""

"""
Working with strings 
str="abcde"
# print(str[1])
# print(str[-1])
# print(str[0:2])
# print(str[-2:len(str)])

#8 Check if substring
res = "man" in "fireman"
if res: 
    print("Sexist!")
# print("This is a string".split(" "))

#9 Use formatting
format_str="Hello, {}"
print(format_str.format("Arthur"))

### Let's use data structures ###

#10 Lists
l=[1,2,3]
print(l)
l=[1,2,3]

l[0]=0
print(l[0])
l=[1,2,3]

for list_item in l: 
    print(list_item)

l=[1,2,3]
if 2 in l:
    print("in")

l=[1,2]
l.append(3)
print(l)

l=[1,2,3]
l.insert(1,99)
print(l)

l=[1,3,2]
l.remove(2)
print(l)

l=[1,2,3]
l.pop()
print(l)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

l=[1,2]
cl=l.copy()
print(cl)

l=[1,2]
l1=[3,4]
lr=l+l1
print(lr)
"""



