"""
clases 
class class_name:
    <atributos>
"""
#Crear una clase calculadora


class calculadora:
    numero1 = 0
    numero2 = 0 

    #definir constructor
    def _init_(self):
        self.numero1 = 0
        self.numero2 = 0
        self.resultado = 0
        
        

    def sumar(self, numero_a, numero_d):  #def para crear funciones
        return numero_a + numero_d
    def resta(self, num,num2):
        return num-num2
    def multi(self, num, num2):
        return num*num2
    
    def div(self, numero1,numero2):
        return numero1 / numero2
    
    def sumarAreglos(self,arreglo):
        suma = 0                     
        for x in arreglo:
            suma += x
            
        return suma
        
    def promedio(self,arreglo,anchoDeArreglo):
              
        return arreglo / anchoDeArreglo
      

arreglo = [1,2,3,4,5]
ancho = len(arreglo)
calc = calculadora()
print (calc.sumar(25,30))
print (calc.div(6,3))
print (calc.resta(5,2))
print(calc.multi(5,4))

sumaArreglos = calc.sumarAreglos(arreglo)
print (sumaArreglos) 

print(calc.promedio(sumaArreglos,ancho))    




