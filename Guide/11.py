import math

# Using Triangle Inequality Theorem which says:

# "The sum of the lengths of any two sides of a triangle is greater than the length of the third side."

# Using Herón's formula : Area = sqrt{s(s-a)(s-b)(s-c)}; where s is the  semiperimeter of the triangle: s = 1/2(a+b+c)

a = int(input("Ingresa un lado \n"))
b = int(input("Ingresa otro lado \n"))
c = int(input("Y el último lado es... \n"))

# if ((abs(a-c) < b) and (b < (a+c))):
if (a+c) > b and (a+b) > c and (b+c) > a:
    s = (a+b+c)/2
    print(s)
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    txt = 'El área del triangulo es {:.2f}'
    print(txt.format(area))
else:
    print("Los lados introducidos no pueden formar un triangulo")
