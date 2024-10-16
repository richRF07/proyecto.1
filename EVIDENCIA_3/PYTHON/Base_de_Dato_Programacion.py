import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('cuestionario_geografico.db')
cursor = conn.cursor()

# Crear la tabla de preguntas
cursor.execute('''
CREATE TABLE IF NOT EXISTS preguntas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pregunta TEXT NOT NULL,
    respuesta TEXT NOT NULL
)
''')

conn.commit()

# Agregar preguntas geográficas predefinidas
def agregar_preguntas_iniciales():
    preguntas = [
        ("¿Cuál es la capital de Francia?", "París"),
        ("¿Cuál es el río más largo del mundo?", "Amazonas"),
        ("¿En qué país se encuentra el Taj Mahal?", "India"),
        ("¿Cuál es la montaña más alta del mundo?", "Monte Everest"),
        ("¿Cuál es el país más grande del mundo por área?", "Rusia"),
        ("¿Cuál es el océano más grande del mundo?", "Océano Pacífico"),
        ("¿Cuál es el punto más bajo de la Tierra?", "Mar Muerto"),
        ("¿Qué país es conocido como 'La Tierra del Sol Naciente'?", "Japón"),
        ("¿Cuál es la capital de Australia?", "Canberra"),
        ("¿Cuál es la cordillera más larga del mundo?", "Cordillera de los Andes"),
    ]
    for pregunta, respuesta in preguntas:
        cursor.execute("INSERT INTO preguntas (pregunta, respuesta) VALUES (?, ?)", (pregunta, respuesta))
    conn.commit()

def listar_preguntas():
    cursor.execute("SELECT * FROM preguntas")
    return cursor.fetchall()

def iniciar_cuestionario():
    puntuacion = 0
    cursor.execute("SELECT * FROM preguntas")
    preguntas = cursor.fetchall()
    
    for pregunta in preguntas:
        print(pregunta[1])  # Mostrar la pregunta
        respuesta_usuario = input("Tu respuesta: ").capitalize()
        if respuesta_usuario == pregunta[2]:  # Comparar con la respuesta correcta
            print("¡Correcto!")
            puntuacion += 1
        else:
            print("Incorrecto. La respuesta correcta es:", pregunta[2])
    
    print("Tu puntuación final es:", puntuacion, "de", len(preguntas))

def menu():
    agregar_preguntas_iniciales()  # Agregar preguntas solo si no existen

    while True:
        print("\nMenu:")
        print("1. Listar Preguntas")
        print("2. Iniciar Cuestionario Geográfico")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            preguntas = listar_preguntas()
            print("Preguntas:")
            for pregunta in preguntas:
                print(f"{pregunta[0]}. {pregunta[1]}")  # Mostrar ID y pregunta

        elif opcion == '2':
            iniciar_cuestionario()

        elif opcion == '3':
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()

# Cerrar la conexión al final
conn.close()