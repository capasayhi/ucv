""" One way to generate random numbers is the so-called middle square technique, which consists of
take a number (seed) of N digits, square it, and use the middle N digits as the next
The element to which the same operation will be applied.

N        N^2           Número Aleatorio
8745     76475025      0;76475025
4750     22562500      0;22562500
5625     31640625      0;31640625

Design a program that asks a user for the value of N to generate random numbers with the technique
of the middle square, the program must verify that such number has at least 4 digits, otherwise
throw an error message and re-request the N number. You must grant the user a maximum of 3
Opportunities to enter the number correctly.

 """

from functions import integerValidation, fourDigitsValidation


alerts = [
    'Ops! , you\'re missing one or more digits, try again',
    'Remaining attempts {}... Take advantage of them well',
    'One last chance',
    'I give up, self-destruction in 3,2,1... BOOM!'
]
inputs = [
    'Enter an integer of at least 4 digits: ',
    'At least four digits must been enter: ',
    'Come on, it\'s not complicated, just enter 4 or more numbers: ',

]

userInput = integerValidation(input(inputs[0]))
# print("NUM", NUM)
amountOfRandomValues = integerValidation(
    input("How many random values do you want to calculate?"))
randomNumberList = []

validUserInput = fourDigitsValidation(userInput, alerts, inputs)
# print("valid_number", valid_number)


def generateRandomValue(num):
    squareNum = num**2
    print(squareNum)
    randomNumber = squareNum/10**(len(str(squareNum)))
    print("random_number", randomNumber)
    return randomNumber


if validUserInput:
    num = userInput
    for n in range(amountOfRandomValues):
        randomNum = generateRandomValue(num)
        randomNumberList.append(generateRandomValue(num))
        num = randomNum[len(str(randomNum))/2 - 2: len(str(randomNum))/2 + 4]

print(randomNumberList)
