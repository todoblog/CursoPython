""" Las variables Globales se crean fuera de una función, pero se pueden usar fuera como dentro de una función"""
a='genial'
def funcion():
	print('python es ' + a)
funcion()
"""Puede crear una variable dentro de una función con el mismo nombre que la variable global, esta solo se ejecutara dentro de la función """
b ='genial'
def funcion2():
	b='increible'
	print('python es ' + b)
print(b)
funcion2()
"""Crea una variable global dentro de una función y poder usarla dentro y fuera de la función """
def funcion3():
	global c
	c='increible'
	print(c)
funcion3()
print('python es ' + c)
""" Puede cambiar el valor de una variable global dentro de la función"""
d='increible'
def funcion4():
	global d
	d='genial'
	print(d)
print(d)
funcion4()
