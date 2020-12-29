from dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    
    contadorRatones = 0
    
    def __init__(self, marca, tipoEntrada ):
        Raton.contadorRatones += 1
        self.__idRaton = Raton.contadorRatones
        #Accedemos a los atributos protected heredados de la clase padre
        self._marca = marca
        self._tipoEntrada = tipoEntrada
    
    def __str__(self):
        return (
            f"Id:  {self.__idRaton}, " 
            f"marca: {self._marca}, "
            f"tipoEntrada:  {self._tipoEntrada}"
        )