# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella
print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

# De la primera palabra tome las primeras tres letras, utilice el operador :

p_1 = palabra_1[:3]
print('Si de la primer palabra se toma:', p_1)

# De la segunda palabra tome las primeras dos letras, utilice el operador :

p_2 = palabra_2[0:2]
print('Y de la segunda:', p_2)

# Formar una nueva palabra con los recortes solicitados

palabra_nueva = p_1 + p_2

# Imprima en pantalla los resultados

print('El resultado de la combinacion es:', palabra_nueva)
