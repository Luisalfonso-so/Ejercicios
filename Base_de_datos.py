import sqlite3

class creacion_db:
    
    def __init__(self,nombre_base_de_datos):
        self.nombre_base_de_datos=nombre_base_de_datos
        
    def conexion(self):
        self.cursor=sqlite3.connect(self.nombre_base_de_datos)
        return self.cursor
    
    def guardar(self):
        self.cursor.commit()
        
    def cerrar(self):
        self.cursor.close()

class tablas:
    
    def __init__(self,cursor):
        self.cursor=cursor
    
    def tabla_libros(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Libros (libro_id INTEGER PRIMARY KEY,
                Título TEXT VARCHAR(50),
                Autor TEXT VARCHAR(50))''')
        
    def tabla_usuarios(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Usuarios (usuario_id INTEGER PRIMARY KEY,
                Nombre TEXT VARCHAR(50) not null,
                Email TEXT VARCHAR(50) unique)''')
        
    def tabla_prestamos(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Préstamos (id_prestamo INTEGER PRIMARY KEY autoincrement,
                libro_id INTEGER, usuario_id INTEGER,
                foreign key (usuario_id)
                references Usuarios (usuario_id)
                foreign key (libro_id)
                references Libros (libro_id))''')
        
class insertar_en_tablas:
    
    def __init__(self,cursor):
        self.cursor=cursor

    def insert_libros(self,tupla_libros):
        self.cursor.execute('''INSERT INTO Libros VALUES (NULL,?,?)''',tupla_libros)
        
    def insert_usuario(self,tupla_usuario):
        self.cursor.execute('''INSERT INTO Usuarios VALUES(NULL,?,?)''',tupla_usuario)
        
    def insert_prestamo(self,tupla_prestamo):
        self.cursor.execute('''INSERT INTO Préstamos VALUES(NULL,?,?)''',tupla_prestamo)
        
print('\nEste programa permite crear una base de datos básica y también permite insertar algunos datos en las tablas.')

ciclo=True
while ciclo:
    
    inicio=str(input('\n¿Desea comenzar? (si/no): '))
    
    if inicio.lower()=='no':
        input('Presione enter para finalizar.')
        ciclo=False
    
    elif inicio.lower()=='si':
        
        try:
            instancia_creacion_db=creacion_db('Biblioteca')
            instancia_creacion_db.conexion()
            instancia_tablas=tablas(instancia_creacion_db.conexion())
            instancia_tablas.tabla_libros()
            instancia_tablas.tabla_prestamos()
            instancia_tablas.tabla_usuarios()
            
            instancia_insertar=insertar_en_tablas(instancia_creacion_db.conexion())
            libro=str(input('\nIngrese el título de un libro: '))
            autor=str(input('Ingrese el autor: '))
            usuario=str(input('\nIngrese el nombre del usuario: '))
            correo_usuario=str(input('Ingrese el correo del usuario: '))
            id_libro=int(input('\nIngrese el ID del libro (para efectos de esta practica el id inicia en 1 y va aumentado n+1 a medida que se agregan libros: '))
            id_usuario=int(input('Ingrese el ID del usuario (para efectos de esta practica el id inicia en 1 y va aumentado n+1 a medida que se agregan usuarios: '))
            
            instancia_insertar.insert_libros((libro,autor))
            instancia_insertar.insert_usuario((usuario,correo_usuario))
            instancia_insertar.insert_prestamo((id_libro,id_usuario))
            instancia_creacion_db.guardar()
            instancia_creacion_db.cerrar()
            input('\nBase de datos creada con éxito, presione enter para finalizar.')
        
            
        except Exception as error:
            print('\nError en el tipo de dato:',error)
    
    elif inicio.lower()=='no':
        ciclo=False
        input('\nPresione enter para finalizar.')
    
    else:
        print('\nUna de las respuestas es inválida, intente de nuevo.')