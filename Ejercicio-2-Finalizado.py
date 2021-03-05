"""
Diego quiere salir a carretear con sus amigos este fin 
de semana por lo cual debe tener el permiso de su madre 
o su padre, su madre le digo que no, pero su padre le 
dijo que sí. ¿Diego puede ir a carretear?
"""

# IMPORTACIONES

# VARIABLES QUE CONOCEMOS

permiso_madre = False
permiso_padre = True

# DESARROLLO
# ahora construimos la operacion logica necesaria, para este en donde uno de los permiso es necesario
# para poder salir a carretear ocuparemos el comando "or".

permiso_final = permiso_madre or permiso_padre

# RESULTADO
print('¿Diego puede salir a carretear?')
print('R: ', permiso_final, '\n')