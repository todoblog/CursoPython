""" Los nombres de variables debe comenzar con una letra o un guion bajo.
    Los nombres de variables no pueden comenzar con un número.
    Los nombres de variables solo puede contener caracteres alfanumericos y guiones bajos (az, 09,_).
    Los nombres de variables distinguen entre mayusculas y minusculas (edad, Edad, EDAD son variables diferentes)
 """
myvar='Juan'
my_var='Juan'
_my_var='Juan'
myVar='Juan'
MYVAR='Juan'
myvar2='Juan'
print(myvar, my_var, _my_var, myVar, MYVAR, myvar2)
#variables no legales
#2myvar='Juan' comienza con número
#my-var='Juan' contiene un guión
#my var='Juan' contiene un espacio

"""Los nombres de variables de varias palabras pueden ser dificiles de leer.
    Hay varias tecnicas para hacerlos más facil.
    Caso Carmel; cada palabra excepto la primera comienza con mayusculas."""
miNombreVariable='Juan'
print(miNombreVariable)
"""Caso Pascal; cada nombre comienza con mayuscula"""
MiNombreVariable='Juan'
print(MiNombreVariable)
"""Caso serpiente; cada palabra esta separada con guiones bajos."""
mi_nombre_variable='Juan'
print(mi_nombre_variable)

