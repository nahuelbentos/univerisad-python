class Orden:
    
    contadorOrdenes = 0
    
    def __init__(self, computadoras):
        Orden.contadorOrdenes += 1
        self.__idOrden = Orden.contadorOrdenes
        #Recibe la lista de objetos de tipo Computadora
        self.__computadoras = computadoras        

    def agregar_computadora(self, computadora):
        self.__computadoras.append(computadora) 
    
    def __str__(self):
        computadoras_str = ""
        for computadora in self.__computadoras:
            computadoras_str += computadora.__str__()
        
        return (
            f"Orden: {self.__idOrden}, " 
            f"computadoras: {computadoras_str}"
            )