"""
Para aprobar la asignatura de Python Camila tiene que tener un promedio 
mayor o igual a 4.0 y tener una asistencia igual o mayor al 75%. 
Revisando sus datos Camila obtuvo un promedio final de 5.3 y una 
asistencia de 68%. ¿Puede pasar la asignatura Camila?
"""
# IMPORTACIONES

# VARIABLES QUE CONOCEMOS
promedio_minimo = 4.0
promedio_camila = 5.3

asistencia_minima = 0.75
asistencia_camila = 0.68

resultado = None

# DESARROLLO

# verificamos si el promedio de Camila es superior o igual a 4.0 y guardamos su valor.
promedio_valido = promedio_camila >= promedio_minimo

# verificamos si la asistencia de Camila es superor o igual a 75% y guardamos su valor.
asistencia_valida = asistencia_minima >= asistencia_camila

# ahora construimos la operacion logica necesaria, para este caso en donde promedio "Y" asistencia son necesarias
# para pasar ocuparemos el comando "and".

resultado = promedio_valido and asistencia_valida

# RESULTADO
print('¿Logro pasar la asignatura camila?')
print('R:', resultado, '\n')