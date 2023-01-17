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
    '\nOps! , you\'re missing one or more digits, try again',
    '\nRemaining attempts {}... Take advantage of them well',
    '\nOne last chance',
    '\nI give up, self-destruction in 3,2,1... BOOM!'
]
inputs = [
    'Enter an integer of at least 4 digits: ',
    'At least four digits must been enter: ',
    'Come on, it\'s not complicated, just enter 4 or more integers: ',

]

userInput = integerValidation(input(inputs[0]))

validUserInput = fourDigitsValidation(userInput, alerts, inputs)
amountOfRandomValues = integerValidation(
    input("\nHow many random values do you want to calculate?: "))
randomNumberList = []


def generateRandomValue(num):

    global squareNum
    squareNum = num**2
    randomNumber = squareNum/10**(len(str(squareNum)))
    return randomNumber


if validUserInput:
    num = userInput
    for n in range(amountOfRandomValues):
        randomNumberList.append(generateRandomValue(num))

        # To update the num variable used in the cycle
        start = int(len(str(squareNum)) / 2 - 2)
        end = start + 4
        num = int(str(squareNum)[start: end])

print("\n\nA list with the generated random values is shown below\n", randomNumberList)
print()
