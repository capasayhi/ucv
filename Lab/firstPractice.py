list1 = ["gatos", "", "perros", "ratones", ""]
list1.pop(1)
''
list1
['gatos', 'perros', 'ratones', '']
list1.pop(3)
''
list1
['gatos', 'perros', 'ratones']
list2 = [1, 2, [200, 400, [1000, 6000], 800], 30, 40]
list2[2][2].insert(2, 5000)
list2
[1, 2, [200, 400, [1000, 6000, 5000], 800], 30, 40]
list2[2][2].pop(2)
5000
list2clear
[1, 2, [200, 400, [1000, 6000], 800], 30, 40]
list2[2][2].insert(1, 5000)
list2
[1, 2, [200, 400, [1000, 5000, 6000], 800], 30, 40]
str = "Después de la tempestad, viene la calma"
str_2 = str[0] + str[2] + str[-1]
str_2
'Dsa'
celsiusTemp = 20
fahrenheitTemp = celsiusTemp * 1.8 + 32
fahrenheitTemp
68.0
dict1 = {'Diez': 10, 'Veinte': 20, 'Treinta': 30}
dict2 = {'Treinta': 30, 'Cuarenta': 40, 'Cincuenta': 50}
dict1.update(dict2)
dict1
{'Diez': 10, 'Veinte': 20, 'Treinta': 30, 'Cuarenta': 40, 'Cincuenta': 50}
studentDict = {"clase": {"estudiante": {
    "nombre": "Mike", "marcas": {"física": 70, "historia": 80}}}}
print(studentDict['clase']['estudiante']['marcas']['historia'])
80
dict3 = {"nombre": 'Platón', 'país': 'Antigua Grecia',
         'fecha_de_nacimiento': -427, "maestro": "Sócrates", "alumno": "Aristóteles", }
dict3["fecha_de_nacimiento"] = -428
dict3
{'nombre': 'Platón', 'país': 'Antigua Grecia', 'fecha_de_nacimiento': -
    428, 'maestro': 'Sócrates', 'alumno': 'Aristóteles'}
