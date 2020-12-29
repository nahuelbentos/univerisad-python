class Computadora:
    contadorComputadoras = 0
    
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contadorComputadoras += 1
        self.__idComputadora = Computadora.contadorComputadoras
        self.__nombre = nombre
        self.__monitor = monitor
        self.__teclado = teclado
        self.__raton = raton
    
    def __str__(self):
        return (
            f"""
            {self.__nombre}: {self.__idComputadora} 
                Monitor: {self.__monitor}
                Teclado: {self.__teclado} 
                Ratón: {self.__raton}
                """
        )