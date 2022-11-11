print("Calculemos algo!")
operator = input('¿Qué operación quieres realizar? (+,-,*,/): ')

if operator == '+' or operator == '-' or operator == '*':

    first_operand = int(input('Ingresa el primer valor: '))
    second_operand = int(input('Ingresa el segundo valor: '))

    if operator == '+':
        print('El resultado es: ', first_operand + second_operand)
    elif operator == '-':
        print('El resultado es: ', first_operand - second_operand)
    else:
        print('El resultado es: ', first_operand * second_operand)

if operator == '/':

    divider = int(input('Ingresa el numerador: '))
    dividend = int(input('ingresa el denominador: '))

    try:
        print('El resultado es: ', divider/dividend)
    except ZeroDivisionError:
        print('Tal parece que no estudias ingeniería... intenta de nuevo ingresando otro valor al denominador')

if operator != '+' and operator != '-' and operator != '*' and operator != '/':
    print('No te pases de listo, ingresa una de las operaciones sugeridas')
