""" 
Make a program that calculates the value of π by developing the series, the program must ask the user for a number M, which will be the number of terms in that series. 

"""
from functions import integerValidation
print("\n")
NUMBER_OF_TERMS = integerValidation(
    input("Enter an integer (represents the number of terms in the series): "))

sumTerms = []
sum = 0

for index in range(1, NUMBER_OF_TERMS + 1):

    item = 1/(index**6)
    if index % 2 == 0:
        item *= -1
    sumTerms.append(item)

for term in range(len(sumTerms)):
    sum += sumTerms[term]

PI = (sum * (30240/31))**(1/6)
print(
    "The approximation to the value of PI according to the number of terms specified is: {:.50f}".format(PI))
print("\n")
