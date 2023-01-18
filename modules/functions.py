def integerValidation(num):
    variable = num
    if not num.isnumeric():
        raise TypeError("Only integers are allowed")
    else:
        variable = int(num)
    return variable


def fourDigitsValidation(NUM, alertMessages=['1 attempt', '2 attempt', '3 attempt', '4 attempt'], inputMessages=["input 1", "input 2", "input 3"]):
    valid_NUM = False
    tries = 4
    while tries >= 0 and (not valid_NUM):
        tries -= 1

        if len(str(NUM)) < 4 and tries == 3:
            print(alertMessages[0].format(tries))
            NUM = integerValidation(input(inputMessages[0]))

        if len(str(NUM)) < 4 and tries == 2:
            print(alertMessages[1].format(tries))
            NUM = integerValidation(input(inputMessages[1]))

        if len(str(NUM)) < 4 and tries == 1:
            print(alertMessages[2])
            NUM = integerValidation(input(inputMessages[2]))

        if len(str(NUM)) < 4 and tries == 0:
            print(alertMessages[3])
            break

        if len(str(NUM)) >= 4:
            valid_NUM = True
            break
    return valid_NUM


def createBaseMatrix(rows):
    matriz = []
    # generates the amount of rows in the matriz
    for row in range(rows):
        matriz.append([])
    return matriz
