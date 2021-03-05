# OPERADORES RELACIONALES EN PYTHON 3

# EJEMPLOS
# LA FUNCION LEN() COMO VIMOS ANTERIORMENTE NOS CUENTA LA CANTIDAD DE ELEMENTOS
# SI LA VARIABLE ES UN STRING CONTABILIZA LA CANTIDAD DE LETRAS.


# ¿12 ES MAYOR QUE 16?

valor_1 = 12
valor_2 = 16

print('¿12 es mayor que 16?')
print(valor_1 > valor_2, '\n')

# ¿LA PALABRA 'PERRO' TIENE MENOS LETRAS QUE 'GATO' ?

palabra_1 = 'PERRO'
palabra_2 = 'GATO'

print('¿La palabra "PERRO" tiene menos letras que la palbara "GATO" ?')
print(len(palabra_1) < len(palabra_2), '\n')

# JUAN ESTA EN UNA DIETA PARA LLEGAR A SU PESO IDEAL DE 75 KG, SI PESA
# 70 KG O MENOS HABRA CUMPLIDO CON LA DIETA DEL NUTRICIONISTA.
# ¿JUAN CUMPLIO CON SU DIETA?

peso_maximo  = 75
peso_claudio = 69.9

print('¿Claudio cumplio con la dieta?')
print(peso_maximo >= peso_claudio, '\n')


