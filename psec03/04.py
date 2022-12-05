# First Excercise
# Imprima los primeros 10 números naturales usando while

counter = 0
while counter < 10:
    print(counter)
    counter += 1

# Second Excercise
# Calcule la suma de todos los números entre 1 y un número dado

user_input = input("Ingresa un valor: ")

if user_input.isnumeric():
    terms = 0
    value = 0
    user_input = int(user_input)

    while terms < user_input:
        terms += 1
        value += terms
        # print("Término a sumar", terms)
    print(value)
else:
    print("Intenta de nuevo ingresando un valor válido")
