"""
Con respecto al problema anterior el padre de Diego 
luego de haber hablado con su esposa decide cambiar 
su opinión, en esta nueva situación 
¿Puede salir a carretear Diego?
"""

# IMPORTACIONES

# VARIABLES QUE CONOCEMOS

permiso_madre = False
# tras cambiar de opinion podemos negar el permiso anterior con el comando not
permiso_padre = not True

# DESARROLLO
# ahora construimos la operacion logica necesaria, para este en donde uno de los permiso es necesario
# para poder salir a carretear ocuparemos el comando "or".

permiso_final = permiso_madre or permiso_padre

# RESULTADO
print('¿Diego puede salir a carretear?')
print('R: ', permiso_final, '\n')