print("Calculemos algo!")

operator = input('¿Qué operación quieres realizar? (+,-,*,/): ')

if operator == '+' or operator == '-' or operator == '*':

    first_operand = int(input('Ingresa el primer valor: '))
    second_operand = int(input('Ingresa el segundo valor: '))

    if operator == '+':
        print('El resultado es: ')
        print(first_operand + second_operand)
    if operator == '-':
        print('El resultado es: ')
        print(first_operand - second_operand)
    if operator == '*':
        print('El resultado es: ')
        print(first_operand * second_operand)

if operator == '/':

    divider = int(input('Ingresa el numerador: '))
    dividend = int(input('ingresa el denominador: '))

    if dividend == 0:
        print('Tal parece que no estudias ingeniería... intenta de nuevo ingresando otro valor')
    else:
        print('El resultado es: ')
        print(divider/dividend)
else:
    print('No te pases de listo, ingresa una de las operaciones sugeridas')
# Ya me di cuenta que para ese último mensaje tenia que haber usado otra condicional de la forma: if operator != '+' and operator != '-' and operator != '*' and operator != '/'. Ya que el mensaje se ejecuta siempre que la operación sea distinta de '/'
