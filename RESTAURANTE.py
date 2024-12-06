class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Beverage(MenuItem):
    def __init__(self, name, price, size, is_cold, has_ice):
        super().__init__(name, price)
        self.size = size
        self.is_cold = is_cold
        self.has_ice = has_ice

    def __str__(self):
        return (
            f"{self.name} (Price: {self.price}, Size: {self.size}, "
            f"Cold: {self.is_cold}, Ice: {self.has_ice})"
        )


class Appetizer(MenuItem):
    def __init__(self, name, price, appetizer_type):
        super().__init__(name, price)
        self.appetizer_type = appetizer_type

    def __str__(self):
        return f"{self.name} (Price: {self.price}, Type: {self.appetizer_type})"


class MainCourse(MenuItem):
    def __init__(self, name, price, ingredients, salad):
        super().__init__(name, price)
        self.ingredients = ingredients
        self.salad = salad

    def __str__(self):
        return (
            f"{self.name} (Price: {self.price}, Ingredients: {self.ingredients}, "
            f"Salad: {self.salad})"
        )


class Order:
    def __init__(self):
        self.plates = []

    def add_plate(self, plate):
        self.plates.append(plate)

    def remove_plate(self, plate):
        self.plates.remove(plate)

    def total(self):
        return sum(plate.price for plate in self.plates)

    def get_plate_details(self):
        return [str(plate) for plate in self.plates]

    def __str__(self):
        plate_details = '\n'.join(self.get_plate_details())
        return f"Order:\n{plate_details}\nTotal: {self.total()}"


def display_menu(menu_items):
    appetizers = [item for item in menu_items if isinstance(item, Appetizer)]
    main_courses = [item for item in menu_items if isinstance(item, MainCourse)]
    beverages = [item for item in menu_items if isinstance(item, Beverage)]

    print("Appetizers:")
    for item in appetizers:
        print(f"  {item.name}: {item}")

    print("\nMain Courses:")
    for item in main_courses:
        print(f"  {item.name}: {item}")

    print("\nBeverages:")
    for item in beverages:
        print(f"  {item.name}: {item}")



cocacola = Beverage(
    name="Coca Cola",
    price=2000, size="B",
    is_cold=True,
    has_ice=True
    )
orange_juice = Beverage(
    name="Orange Juice",
    price=2000, size="S",
    is_cold=True,
    has_ice=False
    )
pepsi = Beverage(
    name="Pepsi",
    price=2000, size="B",
    is_cold=True,
    has_ice=True
    )

nachos = Appetizer(
    name="Nachos",
    price=12000,
    appetizer_type="Shared"
    )
onion_rings = Appetizer(
    name="Onion Rings",
    price=10000,
    appetizer_type="Shared"
    )
french_fries = Appetizer(
    name="French Fries",
    price=9000,
    appetizer_type="Single"
    )
patacones = Appetizer(
    name="Patacones",
    price=9000,
    appetizer_type="Single"
    )

beef_steak = MainCourse(
    name="Beef Steak",
    price=30000,
    ingredients="Smoked beef seasoned with salt, pepper, paprika, and garlic.",
    salad=False
)
spaghetti = MainCourse(
    name="Spaghetti",
    price=25000,
    ingredients="Spaghetti with ground beef, tomato sauce, onion, garlic, and Parmesan cheese",
    salad=False
)
bandeja_paisa = MainCourse(
    name="Bandeja Paisa",
    price=33000,
    ingredients="Red beans, white rice, grilled steak, fried pork belly, sausage, "
               "fried egg, plantain, avocado, and arepa.",
    salad=False
)
pechuga = MainCourse(
    name="Pechuga a la Plancha",
    price=20000,
    ingredients="Grilled chicken breast with lentils, white rice, and boiled potatoes.",
    salad=False
)


menu_items = [
    cocacola, orange_juice, pepsi,
    nachos, onion_rings, french_fries, patacones,
    beef_steak, spaghetti, bandeja_paisa, pechuga
]


display_menu(menu_items)


order = Order()
order.add_plate(nachos)
order.add_plate(cocacola)
order.add_plate(beef_steak)
order.add_plate(spaghetti)
order.remove_plate(nachos)


print(order)
