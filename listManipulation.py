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
"""
    Function returns a slice of the list from valid token position 
    (including the token postion) to the end of the list and it does not 
    modify the original one. If token is greater than the index of the 
    last element function will return an empty list. If empty list is given,
    an empty list will be returned. 
"""
def returnSlicedList(toBeSliced, token):
    if len(toBeSliced) > 0:
        if len(toBeSliced)-1 >= token:
            return toBeSliced[token:]
        else:
            return []
    else:
        return []
#We created a list of numbers
#We delete the head and then we print the
#list. As expected the functions manipulate the
#original list
numbers = [1,2,3,4,5]
print(returnSlicedList(numbers, 2))
print('Here is the numbers list after a slice of it was returned', numbers)
#Wrong way to attempt to delete head
#this creates a new list referenced by numbersDeletedHead
#without affecting the intial list
numbersDeletedHead = numbers[1:]
while len(numbers) > 0:
    printContents(numbers)
    deleteHead(numbers)
printContents(numbers)
