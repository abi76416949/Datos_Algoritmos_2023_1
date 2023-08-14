from persona import Persona
from cursos import Curso

class Alumno(Persona):
    codigo = ''
    facultad = ''
    año_ingreso = 0

    def __init__(self, nombre, ap_paterno, ap_materno, dni, codigo, facultad, año_ingreso):
        super().__init__(nombre, ap_paterno, ap_materno, dni)
        self.codigo = codigo
        self.facultad = facultad
        self.año_ingreso = año_ingreso

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_facultad(self):
        return self.facultad

    def set_facultad(self, facultad):
        self.facultad = facultad

    def get_anio_ingreso(self):
        return self.año_ingreso

    def set_anio_ingreso(self, anio):
        self.año_ingreso = anio
    #Funcion para imprimir los datos del alumno
    def imprimir(self):
        per_data = super().imprimir()
        codigo = self.codigo
        facultad = self.facultad
        año = self.año_ingreso
        return f'datos del alumno es : {per_data}, codigo de ingreso {codigo}, {facultad=}, el año de ingreso es: {año}'
    
    """###FUNCION PARA REGISTRAR ALUMNO 
        
        def registrarAlumno(self):
            Persona.set_nombre=("ingrese su nombre: ")
            Persona.set_ap_materno =input("ingresar el apellido materno")
            Persona.set_ap_paterno = input("Ingrese su apellido paterno")
            Persona.set_dni = int(input("ingre el dni de la persona"))
            
    """

    def agregar_curso(self, curso):
            self.Curso.append(curso)
    def remover_curso(self, curso_eliminar):
            
            for curso in self.Curso:
                if curso_eliminar.get_codigo() ==  curso.get_codigo():
                    self.Curso.remove(curso)
                else:
                    print('No se encuentra registrado el curso a eliminar')
                   

# Mostramos los cursos en la lista
for curso in Curso.curso:
    print(curso.nombre)
"""Curso = Curso
        nuevo_curso = input("ingrese nuevo curso")
        curso_nuevo = Curso(nuevo_curso)
        curso.curso.append(curso_nuevo) 
        agregarCursos()"""