# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese tres palabras y arme un acrónimo con ellas
# Si desea puede modificar el código para ingresar más palabras
print('Ingrese palabra 1:')
palabra_1 = str(input())                    # Ej: Club

print('Ingrese palabra 2:')
palabra_2 = str(input())                    # Ej: Atletico

print('Ingrese palabra 3:')
palabra_3 = str(input())                    # Ej: San

print('Ingrese palabra 4:')
palabra_4 = str(input())                    # Ej: Lorenzo

print('Ingrese palabra 5:')
palabra_5 = str(input())                    # Ej: Almagro

print('Ud ingreso:', palabra_1, palabra_2, palabra_3, palabra_4, palabra_5)   # Muestra en pantalla la frase formada con las palabras elegidas

# De cada palabra debe tomar la primera letra y armar el acrónimo
# Ejemplo: Alumbrado, barrido y limpieza --> ABL
# Imprimir el resultado en pantalla

print('Su acronimo es:', palabra_1[0], palabra_2[0], palabra_3[0], palabra_4[0], palabra_5[0])
