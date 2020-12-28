class MiClase:
    variable_clase = "Variable de clase"
    
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
        
print(MiClase.variable_clase)  
objeto1 = MiClase("Variable instancia") 
MiClase.variable_instancia = "Modificando variable de instancia"
print(MiClase.variable_instancia) #valores distintos  
print(objeto1.variable_instancia) #valores distintos 

#Podemos acceder a las variables de clase desde los objetos
print(objeto1.variable_clase)
#Podemos acceder a las variables con el nombre de la clase
print(MiClase.variable_clase)

objeto1.variable_clase = "Modificando variable de clase"
print(objeto1.variable_clase)
print(MiClase.variable_clase)

objeto2 = MiClase("Nuevo valor de variable de instancia")
print(objeto2.variable_clase)

objeto3 = MiClase("tercer objeto")

MiClase.variable_clase = "Cambio desde la clase"
print(objeto1.variable_clase)
print(objeto2.variable_clase)
print(objeto3.variable_clase)