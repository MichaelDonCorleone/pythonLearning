"""

    @author: MichaelCorleone
    
    This script will read numbers from the keyboard and return 
    them to the user. We are going to use the built in functions of lists to
    print the maximum of the numbers, minimum, sum, the average and 
    how many numbers the list contains. We can easily write our own
    min and max functions.

"""
#function returns 'invalid' if not a valid float number
#function to check if a valid float number was given

def checkNumber(potentialNumber):
    try:
        return float(potentialNumber)
    except:
        return 'invalid'

def readNumbers():
    numbers = []
    while True:
        read = input('Please give a number to be added to the list : ')
        print('You have given',read,'as your input.')
        if read == 'done':
            break
        if checkNumber(read) == 'invalid':
            print('You have given an invalid number. Please try again or enter \'done\' to enter the program.')
        else:
            numbers.append(float(read))   
    return numbers

numbers = readNumbers()
print('List of numbers entered: ', numbers)
if len(numbers) == 0:
    print('The number list is empty. An average, sum, min and max cannot be calculated.')
else:
    print('The list contains :', len(numbers),'numbers.')
    print('The sums of the numbers in the list is :', sum(numbers))
    print('The maximum number in the list is:', max(numbers))
    print('The minimum number in the list is:', min(numbers))
    print('The average of the numbers contained in the list is equal to', sum(numbers)/len(numbers), '.')
