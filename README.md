# RETO-3-POO
En este repositorio encontraras el reto 3 de programacion orientada a objetos
- [RETO 1_1.py](RETO%201_1.py): Operaciones básicas
# DIAGRAMA DE CLASES
El siguiente diagrama de clases muestra la estructura del sistema de gestión de un menú y órdenes para un restaurante.



```mermaid
classDiagram
    class MenuItem {
        -name: str
        -price: float
        +__init__(name, price)
    }

    class Beverage {
        -size: str
        -is_cold: bool
        -has_ice: bool
        +__init__(name, price, size, is_cold, has_ice)
        +__str__()
    }

    class Appetizer {
        -appetizer_type: str
        +__init__(name, price, appetizer_type)
        +__str__()
    }

    class MainCourse {
        -ingredients: str
        -salad: bool
        +__init__(name, price, ingredients, salad)
        +__str__()
    }

    class Order {
        -plates: list
        +__init__()
        +add_plate(plate)
        +remove_plate(plate)
        +total(): float
        +get_plate_details(): list
        +__str__()
    }

    MenuItem <|-- Beverage
    MenuItem <|-- Appetizer
    MenuItem <|-- MainCourse
    Order --> MenuItem

```mermaid

