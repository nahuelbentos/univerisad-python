class Monitor:
    contadorMonitores = 0
    
    def __init__(self, marca, tamanio):
        Monitor.contadorMonitores += 1
        self.__idMonitor = Monitor.contadorMonitores
        self.__marca = marca
        self.__tamanio = tamanio
    
    def __str__(self):
        return (
            f"Id:  {self.__idMonitor}, " 
            f"marca: {self.__marca}, " 
            f"tamaño:  {self.__tamanio} "
            )