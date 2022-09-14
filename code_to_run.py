from Library import Libreria, Usuario

libreria = Libreria(libros = ["Libro1", "Libro2"], cantidad_libros = (2))
nombre_usuario = Usuario(usuario = "Daniel")
libreria.mostrar()
nombre_usuario.prestamo(tipo_libro = "Libro2", Libreria = libreria)
libreria.retirar()