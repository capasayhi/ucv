""" String numbers are created by continuously adding the square of each digit of a number to form another. For example, if you have the number 44, you proceed to square each of its digits and the sum of them results in 32(42 + 42 = 16 + 16 = 32). Then the same thing is done with the 32, where it turns out 13(32 + 22 = 13) and so on. For example:

                      44 -> 32 -> 13 -> 10 -> 1 -> 1

                      85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

Once the chain reaches 1 or 89, the chain is left in an infinite cycle

It is requested to design a program that allows to know what is the percentage of whole numbers less than
an N-value (read as data) whose string reaches the number 89.

 """

from functions import integerValidation, twoDigitsValidation

alerts = [
    '\nOps! , you\'re missing one or more digits, try again',
    '\nRemaining attempts {}... Take advantage of them well',
    '\nOne last chance',
    '\nI give up, self-destruction in 3,2,1... BOOM!'
]
inputs = [
    '\nEnter an integer of at least 2 digits: ',
    'At least two digits must been enter: ',
    'Come on, it\'s not complicated, just enter 2 or more integers: ',
]


def generateValue(num):
    sum = 0
    iterableList = list(str(num))
    for count, item in enumerate(iterableList):
        sum += int(item)**2
    return sum


N = twoDigitsValidation(
    integerValidation(input("Enter an integer of at least 2 digits: "), str),
    alerts, inputs, str)

valuesList = []
valuesList.append(int(N))
comparator = int(N)

condition_1 = comparator != 1
condition_2 = comparator != 89

# Generates the string numbers
while condition_1 or condition_2:
    value = generateValue(valuesList[-1])
    valuesList.append(value)
    comparator = value
    if comparator == 1 or comparator == 89:
        break


# Filter all elements < N
filterList = [s for s in valuesList if s < int(N)]
# percentage of whole numbers less than N
percentage = len(filterList)/len(valuesList)*100


# Manage the output for the user
if comparator == 1:
    print("The string of numbers ends in 1")
elif comparator == 89:
    print(" the percentage of whole numbers less than {} is {}%".format(N, percentage))
