# -*- coding: utf-8 -*-
"""

@author: Michael Don Corleone

Thing to remember about lists is that when passed to
a function, a reference is really passed to it
we will create a few manipulation functions
!!!!Things to remember:
    - append function modifies the current list
    - + operator creates a new list

"""
#We make sure the list referenced contains at least
#one element before executing a deletion
def deleteHead(listManipulated):
    if len(listManipulated) > 0:
        del listManipulated[0]

def printContents(listToPrint):
    print(listToPrint)

def 
#We created a list of numbers
#We delete the head and then we print the
#list. As expected the functions manipulate the
#original list
numbers = [1,2,3,4,5]
while len(numbers) > 0:
    printContents(numbers)
    deleteHead(numbers)
printContents(numbers)
    
