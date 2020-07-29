# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:12:01 2020

@author: PCuser
"""

#Differentiation between objects, values and variables.
a = 'banana'
b = 'banana'
#A string is an object. But do a and b refer to the same object?
#Let's tray the is operator
if a is b:
    print('a and b refer to the same object')
#How about integers?
c = 5
d = 5
#two list with same elements. Are they the same object?
#Answer is no, they are equivalent, their elements have the same
#values
e = [1, 2, 3]
f = [1, 2, 3]
if e is f:
    print('e and f are the same object')
else:
    print('e and f are not the same object')
#e and f in this case are just equivalent
#e and f have the same values so we have two objects
#now if you make a variable equal to another they will refer
#to the same object
a = [1, 2, 3]
b = a
a[0] = 5
print('a[0] value is', a[0],'and b[0] value is', b[0],'.')
if a is b:
    print('a and b refer to the same object')
#We basically aliased a with b
#so a change to a made a change to b
#for strings since they are immutable it doesn't really make
#a difference if a and b would refer to the same object or not