import math

print('Este programa transforma puntos en coordenadas cartesianas a coordenadas polares')

x = float(input('Ingresa un valor numerico para la absisa \n'))
y = float(input('Ingresa un valor numerico para la ordenada \n'))

print('El punto ingresado es ({}, {})'.format(x, y))

r = math.sqrt(pow(x, 2) + pow(y, 2))

angle = math.degrees(math.atan(y/x))
if x < 0 or y < 0:
    angle = angle + 180

print('El punto en polares es ({:.2f}, {:.2f})'.format(r, angle))


# 2 Excercise
