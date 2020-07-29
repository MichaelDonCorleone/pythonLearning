# -*- coding: utf-8 -*-
"""


@author: PCuser

Chapter 8 : Difference between strings and lists of characters

"""
#function takes a string and then appends its contents
#to a character list
def stringToCharacters(string):
    converted = []
    for i in range(len(string)):
        converted.append(string[i])
    return converted
#function to convert a string to a list of words
#using a delimeter
def stringToWordsDelimeter(string, delimeter):
    words = []
    word = ''
    for i in range(len(string)):
        #strips spaces by ignoring extra spaces in between words
        if string[i] == delimeter:
            if len(word) > 0:
                words.append(word)
                word = ''
        else:
            word = word + string[i]
    #check if there was a last word to be added after we exited the
    #loop that traverses the string
    if len(word) > 0:
        words.append(word)
    return words
#function to convert a string to a list of words without
#a delimeter
def stringToWords(string):
    words = []
    word = ''
    for i in range(len(string)):
        #strips spaces by ignoring extra spaces in between words
        if string[i] == ' ':
            if len(word) > 0:
                words.append(word)
                word = ''
        else:
            word = word + string[i]
    #check if there was a last word to be added after we exited the
    #loop that traverses the string
    if len(word) > 0:
        words.append(word)
    return words
#Here we will explore manipulation of strings
#we will also create our own functions to manipulate strings
wordTest = 'spam-spam-spam'
word = 'test'
wordConvertedToList = list(word)
print(wordConvertedToList)
converted = stringToCharacters(word)
print(converted)
string = 'Hunt for deer in the woods'
words = string.split()
print(words)
convertedWords = stringToWords(string)
#We can also split a string into words let's see
print(convertedWords)
print(stringToWordsDelimeter(wordTest, '-'))
#join can be invoked on a delimeter to create a string from
#a list of words
delimeter = ' '
print(delimeter.join(convertedWords))