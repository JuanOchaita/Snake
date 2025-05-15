# Snake Game — Proyecto con Estructuras de Datos

## 1. Caso de uso

Este proyecto consiste en una versión extendida del clásico juego **Snake**, utilizando las estructuras de datos `Stack` y `QueueStack`. El objetivo principal fue aplicar estas estructuras para agregar funcionalidades avanzadas como:

* **Sistema de repetición (replay)** después de una colisión.
* **Visualización de una "serpiente fantasma"** que simula los movimientos previos del jugador.

La elección del juego Snake surge por ser un entorno controlado y visual donde se pueden demostrar claramente los beneficios de las estructuras de datos, especialmente en el manejo de historial de movimientos y estados.

## 2. Funcionalidades

La aplicación permite realizar las siguientes operaciones:

### a. Movimiento de la serpiente principal

* La serpiente se mueve con las teclas `WASD` o flechas direccionales.
* Cada movimiento válido se almacena en un `QueueStack` (`movement_history`) para poder ser utilizado luego por la serpiente fantasma (`ghost`).

### b. Sistema de repetición (replay)

* Cuando ocurre una colisión, se activa un modo “replay” que muestra los últimos 10 estados de la serpiente (`frames_history`), utilizando un `QueueStack`.
* Estos estados se reproducen visualmente con una breve pausa entre cuadros para simular una repetición animada.

### c. Serpiente fantasma

* Al iniciar el replay, se crea una serpiente “fantasma” (`ghost`) que sigue los mismos movimientos del jugador en orden inverso, almacenados en un `Stack` (`ghost_moves`).
* Esta estructura permite que la serpiente fantasma siga exactamente el camino recorrido, ya que la pila conserva el orden inverso de inserción.

### d. Control de colisiones

* Se permiten hasta 2 colisiones antes de finalizar el juego.
* Cada colisión resetea parcialmente el estado de la serpiente mediante la función `reverse`, que intenta restaurar su posición anterior.

### e. Sistema de puntaje

* El jugador gana 1 punto por cada fruta comida.
* Al finalizar el juego, el puntaje se puede guardar junto con un nombre en un archivo `scores.txt`.

## 3. Diagrama de archivos

```plaintext
📁 ProyectoSnake/
├── BasicSnake.py         # Archivo principal que contiene la lógica del juego.
├── Snake.py              # Clase que representa la serpiente (jugador y fantasma).
├── Stack.py              # Estructura de datos tipo pila (LIFO).
├── QueueStack.py         # Variante de pila con comportamiento de cola al llenarse.
├── scores.txt            # Archivo donde se guardan los puntajes.
└── README.md             # Documentación del proyecto.
```

* **BasicSnake.py**: Punto de entrada de la aplicación. Coordina lógica de entrada, dibujo y actualización de estado.
* **Snake.py**: Contiene la clase `Snake` con lógica de movimiento, dibujo, colisiones y crecimiento.
* **Stack.py**: Pila clásica con desplazamiento circular al alcanzar su capacidad máxima.
* **QueueStack.py**: Variante que simula una cola limitada mediante una pila, útil para mantener histórico reciente.
* **scores.txt**: Registro persistente de puntajes de los jugadores.
* **README.md**: Documento explicativo del proyecto.

## 4. Versión alterna primitiva

Antes de integrar estructuras de datos, se desarrolló una versión básica del juego donde:

* El movimiento no se almacenaba.
* No existía la serpiente fantasma ni la funcionalidad de replay.
* Toda la lógica era secuencial y sin recuperación de estado.

**Implicaciones**:

* No había posibilidad de simular “retroceso” o ver errores cometidos.
* Dificultad para extender la funcionalidad sin sobrecargar la lógica principal.
* Menor reutilización de código y alta dependencia de variables globales.

La implementación de estructuras permitió modularizar el diseño y dar una base sólida para futuras mejoras (como “deshacer movimiento”, múltiples vidas o más IA).

## 5. Instrucciones para ejecutar la aplicación

### Requisitos:

* Python 3.7+
* Pygame

### Instalación de dependencias:

```bash
pip install pygame
```

### Ejecutar el juego:

```bash
python BasicSnake.py
```

### Controles:

* Mover la serpiente: `W`, `A`, `S`, `D` o flechas direccionales
* Guardar puntaje al perder: `Enter`
* Salir sin guardar: `Q`
* Borrar letra del nombre: `Backspace`


