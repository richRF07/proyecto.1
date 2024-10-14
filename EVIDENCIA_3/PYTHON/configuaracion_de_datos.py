import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

# Crear las tablas
cursor.execute('''
CREATE TABLE IF NOT EXISTS autores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS libros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor_id INTEGER,
    FOREIGN KEY (autor_id) REFERENCES autores (id)
)
''')

conn.commit()
def agregar_autor(nombre):
    cursor.execute("INSERT INTO autores (nombre) VALUES (?)", (nombre,))
    conn.commit()

def listar_autores():
    cursor.execute("SELECT * FROM autores")
    return cursor.fetchall()

def agregar_libro(titulo, autor_id):
    cursor.execute("INSERT INTO libros (titulo, autor_id) VALUES (?, ?)", (titulo, autor_id))
    conn.commit()

def listar_libros():
    cursor.execute("SELECT * FROM libros")
    return cursor.fetchall()

def buscar_libros_por_autor(autor_id):
    cursor.execute("SELECT * FROM libros WHERE autor_id = ?", (autor_id,))
    return cursor.fetchall()

def listar_libros_con_autores():
    cursor.execute('''
    SELECT libros.titulo, autores.nombre 
    FROM libros 
    INNER JOIN autores ON libros.autor_id = autores.id
    ''')
    return cursor.fetchall()
def menu():
    while True:
        print("\nMenu:")
        print("1. Agregar Autor")
        print("2. Listar Autores")
        print("3. Agregar Libro")
        print("4. Listar Libros")
        print("5. Buscar Libros por Autor")
        print("6. Listar Libros con Autores")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del autor: ")
            agregar_autor(nombre)
            print("Autor agregado.")

        elif opcion == '2':
            autores = listar_autores()
            print("Autores:")
            for autor in autores:
                print(autor)

        elif opcion == '3':
            titulo = input("Ingrese el título del libro: ")
            autor_id = input("Ingrese el ID del autor: ")
            agregar_libro(titulo, autor_id)
            print("Libro agregado.")

        elif opcion == '4':
            libros = listar_libros()
            print("Libros:")
            for libro in libros:
                print(libro)

        elif opcion == '5':
            autor_id = input("Ingrese el ID del autor: ")
            libros = buscar_libros_por_autor(autor_id)
            print("Libros del autor:")
            for libro in libros:
                print(libro)

        elif opcion == '6':
            libros_autores = listar_libros_con_autores()
            print("Libros con Autores:")
            for item in libros_autores:
                print(item)

        elif opcion == '7':
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()

# Cerrar la conexión al final
conn.close()