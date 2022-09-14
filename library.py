class Libreria:
    def __init__(self, libros:list, cantidad_libros:int) -> None:
        self.libros = libros
        self.cantidad_libros = cantidad_libros

    def mostrar(self):
        for mostrar in self.libros:
            print("Los libros que se encuentran disponibles actualmente son: ", self.libros)

    def cargar(self):
        self.libros.append()
        for cargar in self.libros:
            print("Los libros que se encuentran disponibles actualmente son: ", self.libros)
            self.cantidad_libros = self.cantidad_libros + 1
            print("La cantidad de libros disponibles es de: ", self.cantidad_libros)

    def retirar(self):
        self.libros.pop()
        for retirar in self.libros:
            print("Los libros que se encuentran disponibles actualmente son: ", self.libros)
            self.cantidad_libros = self.cantidad_libros - 1
            print("La cantidad de libros disponibles es de: ", self.cantidad_libros)

class Usuario:
    def __init__(self, usuario:str) -> None:
        self.nombre_usuario = usuario

    def prestamo(self, tipo_libro:str, libreria:Libreria):
        self.tipo_libro = tipo_libro
        if (self.tipo_libro == libreria.libros):
            libreria.libros.remove(libreria.libros[self.tipo_libro])

    def devolucion(self, libreria:Libreria):
        libreria.libros.append(libreria.libros[i])