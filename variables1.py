#Una variable es un contenedor para almacenar valores de datos.
#Una variable se crea cuando se le asigna un valor
x=55
y='John'
print(f'Mi nombre es {y} y tengon {x} años de edad ')
"""No es necesario declarar las variables con ningun tipo, incluso puede cambiar el valor"""
x=45 # es de tipo int(entero)
x='gustav'#ahora cambio a tipo str(string)
print(x)
#haga una conversión para especificar el tipo de dato
x=str(3)
y=int(3)
z=float(3)
#obtener el tipo de dato
print(type(x))
print(type(y))
print(type(z))
""" Las variables string pueden llevar comillas simples o dobles"""
x="Juan"
x='Juan'
print(x)
"""Los nombres de variables distinguen entre mayusculas y minusculas"""
a='hola'
A='chau'
print(a,A)