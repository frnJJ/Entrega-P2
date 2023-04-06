nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

def comprimir_notas (nombres, nota1, nota2): 
    """esta funcion retorna el nombre del alumno con sus respectivas notas"""
    aux = nombres.split(",")
    aux = ([n.split("'")[1] for n in aux])
    est_notas = list(zip(aux,nota1,nota2))
    return est_notas



def calcular_promedio (datos):
    """Esta funcion retorna una Tupla con los nombres y promedios de los alumnos"""
    promedios = tuple(map(lambda x: (x[0],(x[1]+x[2])/2),datos))
    return(promedios)

def promedio_general (datos):
    """Esta funcion retorna el promedio general de todo el curso"""
    prom_general = calcular_promedio(datos)
    prom_general = sum([i[1] for i in prom_general])
    prom_general = prom_general / len(datos)
    return (prom_general)

def max_promedio(datos_alu):
    """esta funcion retorna una tupla del alumno con mayor promedio"""
    aux = list(calcular_promedio(datos_alu))
    return(max(aux,key= lambda x: x[1]))


def min_nota(datos_alu):
    """Esta funcion retorna una tupla del alumno con menor nota"""
    minnota = map(lambda x:((x[0],x[1]) if x[1] <= x[2] else (x[0],x[2])),datos_alu)
    return min(minnota,key= lambda x: x[1])


datos_alumnos = comprimir_notas(nombres, notas_1, notas_2)
promedios = calcular_promedio(datos_alumnos)
prom_general = promedio_general(datos_alumnos)
alumno_maxprom = max_promedio(datos_alumnos)
alumno_minnota = min_nota(datos_alumnos)

print(datos_alumnos)
for i in promedios:
    print(f" NOMBRE= {i[0]} PROMEDIO= {i[1]} ")
print(f"El promedio general es {prom_general} ")
print(f"El alumno con mayor promedio es {alumno_maxprom[0]} con un promedio de {alumno_maxprom[1]}")
print(f"El alumno con menor nota es {alumno_minnota[0]} con una nota de {alumno_minnota[1]}")
