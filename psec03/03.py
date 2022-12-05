tries = 4
alerts = [
    'Ups! algo hiciste mal, te quedan {} intentos',
    'Intentos restantes {}... aprovéchalos bién',
    'Una última oportunidad',
    'Te has quedado sin intentos',
    'Intentar dividir entre 0 me ha dañado los circuitos, me autodestuiré en 3, 2, 1 ',
    'Tal parece que no estudias ingeniería... intenta de nuevo ingresando otro valor al denominador',
    'La división por 0 no está definida, prueba con otro valor'
]
inputs = [
    '¿Qué operación quieres realizar? (+,-,*,/):\n ',
    'Elije una de las siguientes operacion= (+ - * /)\n',
    'Asegurate de estar ingresando una de las operaciones sugeridas\n',
    'Operaciones admitidas: (+,-,*,/)\n'
]

print('Calculemos algo!')
operator = input(inputs[0])

while operator != '+' and operator != '-' and operator != '*' and operator != '/' and tries != 0:

    tries -= 1

    if tries == 3:
        print(alerts[0].format(tries))
        operator = input(inputs[1])

    if tries == 2:
        print(alerts[1].format(tries))
        operator = input(inputs[2])
    if tries == 1:
        print(alerts[2])
        operator = input(inputs[3])

    if tries == 0:
        print(alerts[3])
        break


if operator == '+' or operator == '-' or operator == '*':

    first_operand = int(input('Ingresa el primer valor: '))
    second_operand = int(input('Ingresa el segundo valor: '))

    if operator == '+':
        print('El resultado es:'.format(first_operand, second_operand),
              first_operand + second_operand)
    elif operator == '-':
        print('El resultado es:'.format(first_operand, second_operand),
              first_operand - second_operand)
    else:
        print('El resultado es: '.format(first_operand, second_operand),
              first_operand * second_operand)

if operator == '/':

    divisionErrors = 0
    divider = int(input('Ingresa el numerador: '))

    while divisionErrors < 3:

        if divisionErrors == 0:
            dividend = int(input('ingresa el denominador: '))
        if divisionErrors == 1:
            dividend = int(input('Ingresa otro denominador: '))
        if divisionErrors == 2:
            dividend = int(input('denominador ( > 0 ): '))

        try:
            print('{} / {} = '.format(divider, dividend), divider/dividend)
            break
        except ZeroDivisionError:

            divisionErrors += 1

            if divisionErrors == 1:
                print(alerts[5])
            if divisionErrors == 2:
                print(alerts[6])

    if divisionErrors == 3:
        print(alerts[4])
