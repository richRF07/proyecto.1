# Cuestionario Geográfico en Python

# Definir las preguntas y respuestas
preguntas = [
    "1. ¿Cuál es la capital de Francia?",
    "2. ¿Cuál es el río más largo del mundo?",
    "3. ¿En qué país se encuentra el Taj Mahal?",
    "4. ¿Cuál es la montaña más alta del mundo?",
    "5. ¿Cuál es el país más grande del mundo por área?",
    "6. ¿Cuál es el océano más grande del mundo?",
    "7. ¿Cuál es el punto más bajo de la Tierra?",
    "8. ¿Qué país es conocido como 'La Tierra del Sol Naciente'?",
    "9. ¿Cuál es la capital de Australia?",
    "10. ¿Cuál es la cordillera más larga del mundo?",
]

respuestas = [
    "París",
    "Amazonas",
    "India",
    "Monte Everest",
    "Rusia",
    "Océano Pacífico",
    "Mar Muerto",
    "Japón",
    "Canberra",
    "Cordillera de los Andes",
]

# Función para administrar el cuestionario
def cuestionario():
    puntuacion = 0
    for i in range(len(preguntas)):
        print(preguntas[i])
        respuesta_usuario = input("Tu respuesta: ").capitalize()
        if respuesta_usuario == respuestas[i]:
            print("¡Correcto!")
            puntuacion += 1
        else:
            print("Incorrecto. La respuesta correcta es:", respuestas[i])
    print("Tu puntuación final es:", puntuacion, "de", len(preguntas))

# Ejecutar el cuestionario
if __name__ == "__main__":
    print("¡Bienvenido al Cuestionario Geográfico!")
    cuestionario()