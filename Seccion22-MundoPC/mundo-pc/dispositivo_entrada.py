class DispositivoEntrada:
    def __init__(self, tipoEntrada, marca):
        #Atributos de tipo protected (accesibles desde una subclase)
        self._marca = marca
        self._tipoEntrada = tipoEntrada
    
    def __str__(self):
        return "Dispositivo entrada: marca: " + self._marca + " tipo entrada: "+ self._tipoEntrada
     