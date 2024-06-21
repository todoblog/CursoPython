#Multiples valores para multiples variables
x,y,z='naranja', 'banana', 'guinda'
print(x)
print(y)
print(z)
"""Asegurese que la cantidad de varables coincida con la cantidad de valores, de lo contrario obtendra un error """
#Un valor para multiple variables
a=b=c='naranja'
print(a,b,c)
"""Desmpaquetar una coleccion.
    Si una coleccion de valores en una lista ,tupla, etc. Python le permite extraer los valores en variables. A esto se le llama desempaquetar """
lista_frutas=['uvas','peras','guinda']
d,e,f=lista_frutas
print(d,e,f)