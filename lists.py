# -*- coding: utf-8 -*-
"""
    Created on Mon Jul 27 16:42:29 2020
    
    @author: Michael Corleone
    List - Chapter 8: Python for Everyone
    
    Lists don't have to be the same type. Lists can be nested(one in another one).
    Each item is called an element. Examples:
    [0, 1, 2, 3], ['test', 1, 2.3, [2, 3, 'pest']]
    Empty List => []
    List values can be assigned to variables.
    Lists are mutable
    In operator works on lists. Negative indexes start counting from the end of the list
    if an index is out of bounds you get an IndexError
    
"""

list1 = ['Test', 'Spam', 'Best']
integers = [0,1,2,3,4]
print(integers)
print(list1)
#change the 2nd element of integers to 123
integers[1] = 123
cheeses = ['Gouda', 'Mozzarella','Cheddar', 'Feta', 'Goat Cheese']
cheesesToSearchFor = ['Edam', 'Cow Cheese', 'Old Cheddar', 'Gouda','Mozzarella', 'Feta']
countHits = 0
countMisses = 0
for i in range(len(cheesesToSearchFor)):
    print(i)
    if cheesesToSearchFor[i] in cheeses:
        print(cheesesToSearchFor[i], 'is in :', cheeses)
        countHits = countHits + 1
    else:
        print(cheesesToSearchFor[i], 'is not in :', cheeses)
        countMisses = countMisses + 1
print('Hits : ', countHits, '. Misses : ', countMisses, '.')
#range returns a list of indices 0 to length-1
print(range(len(cheesesToSearchFor)))
#You can add lists with the plus operations
a = [0, 1, 2, 3, 4, 5]
b = [6, 7, 8, 9 , 10]
c = a + b
print(c)
#2 different ways to traverse list 'c'
for i in range(len(c)):
    print (c[i])

for integer in c:
    print (integer)
#if a list is nested the length of the parent is not affected by the length of the nested list
#Multiplication * repeats the list as many times d = [1, 2, 3]*4 => d = [1,2,3,1,2,3,1,2,3,1,2,3]
d = a*2
print(d)
#functions that can be used with lists :
print('List before appending elements.')
numberList = [1,2,3,4]
print(numberList)
element = 5
numberList.append(element)
print('List after appending', element,'.')
print(numberList)
secondList = [6,7,8]
numberList.extend(secondList)
print('List after extending the following list :', secondList,'.')
print(numberList)
numberList.append(-9)
print(numberList)
print('List after sorting with the new additon of -9 from low to high:')
numberList.sort()
print(numberList)
#There are different methods to remove items from lists
#If you know the index
indexToRemove = 1
print('Index :', indexToRemove, 'to be removed from list. Element to be removed using pop function : ', numberList.pop(indexToRemove),'.')
print('The list currently is :', numberList)
print('Using remove function we will delete an element that has a specific value, but we do not know where it is.')
numberList.remove(5)
print(numberList)
#remove function returns None as a value
#also can use the del operator if you don't need the value that you are removing
print('We will removed',numberList[1],'with the delete operator from the list.')
del numberList[1]
print(numberList)
print('We can also view a slice of a list : let\'s view from element 1 to element 3 not including 3 by doing numberList[1:3] whice gives :', numberList[1:3])
del numberList[1:3]
print('We deleted that slice and now the list is:', numberList)