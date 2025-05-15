# Juego de la Serpiente con Función de Rebobinado - Implementación de Estructuras de Datos

## 1. Descripción del Proyecto y Caso de Uso

Este proyecto implementa el clásico juego Snake, enriquecido con una funcionalidad de rewind basada en estructuras de datos personalizadas. La serpiente y sus movimientos se gestionan a través de objetos `Snake` y la historia de movimientos y estados se almacena con stacks y queue-stacks.

**Motivación:**
- La naturaleza secuencial del movimiento se adapta bien al manejo con stacks.
- Se demuestra el uso práctico de estructuras como `Stack` y `QueueStack` para almacenar estados y movimientos.
- La funcionalidad de rewind se implementa almacenando un historial limitado de estados para revertir el juego en caso de colisiones.
- La función "ghost snake" predice movimientos y mejora la experiencia visual.

## 2. Características Principales y Estructuras de Datos

### Mecánicas del Juego

- Control direccional usando teclado (WASD o flechas).
- Crecimiento de la serpiente al comer fruta.
- Detección de colisiones con paredes, con el cuerpo propio y con el "ghost snake".
- Contador de colisiones; tras dos colisiones el juego termina.
- Registro del score y entrada de nombre al finalizar.

### Funciones Avanzadas

1. **Historial de movimientos y estados:**
   - `QueueStack` almacena las últimas 10 posiciones del cuerpo de la serpiente (`frames_history`).
   - `QueueStack` también almacena las últimas 10 direcciones (`movement_history`).
   - `Stack` gestiona los movimientos del ghost snake (`ghost_moves`).

2. **Rewind Temporal:**
   - Cuando ocurre una colisión, se reproduce una "repetición" (`show_replay`) de los últimos movimientos utilizando el historial.
   - Se puede reconstruir el estado previo y reiniciar el juego desde ahí.

3. **Ghost Snake:**
   - Se mueve siguiendo la historia invertida de movimientos.
   - Se muestra solo si no colisiona con límites ni consigo mismo.

4. **Estructuras `Stack` y `QueueStack`:**
   - Ambos implementan un arreglo fijo con tamaño máximo.
   - Cuando el stack está lleno, desplazan los elementos a la izquierda para hacer espacio (desplazamiento FIFO para `QueueStack`).
   - Métodos: `Push`, `Pop` y `Peek` que manejan el stack de manera eficiente, ignorando valores `None`.

### Clases y Métodos Clave

- **`Snake`**:
  - `move(direction)`: mueve la cabeza y actualiza el cuerpo.
  - `reverse(direction)`: mueve la cola hacia una dirección para la función de rewind.
  - `check_collision(min_coord, max_coord, other_snake)`: verifica colisiones.
  - `eats(fruit_pos)`: detecta si la serpiente come la fruta.
  - `draw(screen)`: dibuja la serpiente en pantalla.

- **`Stack` y `QueueStack`**:
  - Almacenan valores con un tope (`Top`) y tamaño máximo (`Max`).
  - Realizan desplazamiento para mantener tamaño limitado.
  - Usadas para almacenar posiciones y movimientos.

## 3. Estructura de Archivos

```

📂 SnakeGame/
├── Stack.py           # Implementación del stack con desplazamiento FIFO
├── QueueStack.py      # Implementación tipo queue con comportamiento similar a stack limitado
├── Snake.py           # Clase Snake con métodos de movimiento, dibujo y colisión
├── BasicSnake.py      # Código principal del juego con funcionalidades completas y rewind
├── scores.txt         # Archivo para almacenar puntuaciones
├── README.md          # Documentación del proyecto

````

## 4. Descripción del Flujo de Juego

- El juego inicia con una serpiente blanca y un ghost snake azul.
- La serpiente principal se mueve con las teclas de dirección, y sus movimientos y posiciones se almacenan en `movement_history` y `frames_history`.
- El ghost snake repite en orden inverso los movimientos almacenados.
- Si la serpiente colisiona con paredes, consigo misma o con el ghost snake, se inicia la reproducción de los últimos 10 estados (`show_replay`).
- Tras la repetición, el estado vuelve a un punto seguro y el jugador puede continuar.
- El score se incrementa al comer fruta, y al perder se puede ingresar nombre para guardar la puntuación.
- El juego maneja hasta dos colisiones antes de terminar.

## 5. Instalación y Ejecución

### Requisitos

- Python 3.6 o superior
- Pygame 2.0+

### Instalación

```bash
pip install pygame
````

### Ejecución

```bash
python BasicSnake.py
```

### Controles

| Acción                 | Tecla                          |
| ---------------------- | ------------------------------ |
| Mover Arriba           | W o Flecha ↑                   |
| Mover Abajo            | S o Flecha ↓                   |
| Mover Izquierda        | A o Flecha ←                   |
| Mover Derecha          | D o Flecha →                   |
| Reinicio (tras muerte) | Enter para guardar y reiniciar |
| Salir                  | Q                              |

## 6. Ventajas de la Implementación

* Uso eficiente de estructuras de datos para manejo limitado de historial.
* Función rewind con visualización de estados anteriores.
* Código modular, reutilizable y mantenible.
* Visualización clara mediante colores y animaciones.
* Control intuitivo y experiencia de usuario mejorada con ghost snake.

---

Este proyecto ejemplifica cómo implementar estructuras de datos clásicas (stack, queue) para agregar funcionalidades avanzadas a un juego clásico, logrando un balance entre complejidad, rendimiento y usabilidad.

```
