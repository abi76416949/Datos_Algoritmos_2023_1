from alumno import Alumno
from docente import Docente
from cursos import Curso

# Crear instancias de cursos
lista_cursos = []
curso_algebra = Curso('C001', 'Algebra')
curso_matematica = Curso('C002', 'Matematica')
curso_filosofia = Curso('C003', 'Filosofia')

lista_cursos.append(curso_algebra)
lista_cursos.append(curso_matematica)
lista_cursos.append(curso_filosofia)

# Crear instancias de alumnos
lista_alumnos = []
for i in range(3):
    alumno1 = Alumno('nombre', 'apellido 1', 'apellido 2', 'dni','codigo', 'Informatica y Sistemas', 2023)
    lista_alumnos.append(alumno1)

    # Inscribir alumnos en los cursos correspondientes
    for curso in lista_cursos:
        inscripcion = input(f"¿Inscribir al alumno en el curso {curso.get_nombre()}? (s/n): ")
        if inscripcion.lower() == 's':
            alumno1.agregar_curso(curso)

# Mostrar los cursos inscritos por los alumnos
    cursos_inscritos = alumno1.mostrar_cursos_inscritos()
    print(f"Cursos inscritos por el alumno:")
    for curso in cursos_inscritos:
        print(curso)

print("Este programa funciona correctamente")

input("Presiona Enter para salir...")
