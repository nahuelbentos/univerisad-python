from dominio.pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas

opcion = None
while opcion != "4":
    print("Opciones:")
    print("1. Agregar película")
    print("2. Listar películas")
    print("3. Eliminar catálogo de películas")
    print("4. Salir")
    opcion = input("Escribe tu opción (1-4): ")
    
else:
    print("Salimos del programa...")