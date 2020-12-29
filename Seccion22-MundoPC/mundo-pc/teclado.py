from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    
    contadorTeclados = 0
    
    def __init__(self, marca, tipoEntrada):
        Teclado.contadorTeclados += 1
        self.__idTeclado = Teclado.contadorTeclados
        #Accedemos a los atributos protected heredados de la clase padre
        self._marca = marca
        self._tipoEntrada = tipoEntrada
    
    def __str__(self):
        return (
            f"Id:  {self.__idTeclado}, " 
            f"marca: {self._marca}, "    
            f"tipoEntrada: {self._tipoEntrada}"    
            )