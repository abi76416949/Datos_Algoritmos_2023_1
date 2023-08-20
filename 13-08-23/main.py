from alumno import Alumno
from docente import Docente
from cursos import Curso

lista_alumnos =[]
#incluir los 5 registros por integrante
for i in range(3):

    alumno1 = Alumno('nombre', 'apellido 1', 'apellido 2', 'dni','codigo', 'Informatica y Sistemas', 2023)
    lista_alumnos.append(alumno1)

lista_docente = []
docente1 = Docente('nombre1', 'paterno', 'materno', 'dni', 'codigo', 'FIIS')
docente2 = Docente('nombre2', 'paterno', 'materno', 'dni', 'codigo', 'FIIS')

lista_docente.append(docente1)
lista_docente.append(docente2)

lista_curso = []
curso1 = Curso('codigo 1', 'nombre 1')
curso2 = Curso('codigo 2', 'nombre 1')
curso3 = Curso('codigo 3', 'nombre 1')
curso4 = Curso('codigo 4', 'nombre 1')

lista_curso.append(curso1)
lista_curso.append(curso2)
lista_curso.append(curso3)
lista_curso.append(curso4)

 

input("Presiona Enter para salir...")

band = 0
for curso in lista_curso:
    if (band < 2):
        curso.asignar_docente(docente1)
    else:
        curso.asignar_docente(docente2)
    band += 1

for curso in lista_curso:
    docente = curso.mostrar_docente()
    print(docente.imprimir())
    

for alumno in lista_alumnos:
    for curso in lista_curso:
        alumno.agregar_curso(curso)

#mostrar los cursos asignados a alumno 
#ingresar notas al alumno
#calcular el promedio