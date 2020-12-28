try:
    archivo = open("./Seccion20-ManejoArchivo/prueba.txt", "a")
    archivo.write("Agregamos info al archivo\n")
    archivo.write("Adios\n")
except Exception as e:
    print(e)
finally:
    archivo.close()
    #después de close ya no podemos trabajar con el archivo
    #archivo.write("saludos")
    