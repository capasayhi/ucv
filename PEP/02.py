""" A snail falls into a pit H meters deep. This snail during the day ascends a distance
Ld meters, but during the night, when falling asleep, slips and ascends Ln meters. Design a program
than simulating the movement of the snail for H, Ld and Ln given by the user. The program must yield
As a result in how many days the snail comes out of the pit (if at all). """


from functions import integerValidation

H = integerValidation(
    input("Enter the depth of the pit into which the snail falls: "))
print(H)
LD = integerValidation(
    input("How much do you expect the snail to climb during the day?: "))
print(LD)

LN = integerValidation(
    input("And how much do you think it falls during the night?: "))
print(LN)

height = H
days = 0


if LD < LN:
    print("Oh no, it looks like the snail will DIE buried")
else:
    while height > 0:
        height = height - LD + LN
        days += 1
        print(height)
    if height <= 0:
        print("The snail managed to get out of the hole after {} days but... A bird was waiting.".format(days))
