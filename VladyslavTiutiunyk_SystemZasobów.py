class Resource:
    """Klasa reprezentująca zasób"""
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def consume(self, amount):
        # Zmniejsz ilość zasobu, zwróć True jeśli się udało
        if self.quantity >= amount:
            self.quantity -= amount
            return True
        return False

    def add(self, amount):
        # Dodaj zasoby
        self.quantity += amount

class ResourceManager:
    """Manager zarządzający wszystkimi zasobami w grze"""
    def __init__(self):
        # Stwórz słownik zasobów
        self.resources = {
            "food": Resource("food", 100),
            "water": Resource("water", 100),
            "medicine": Resource("medicine", 20),
            "ammo": Resource("ammo", 50),
            "materials": Resource("materials", 30)
        }

    def add_resource(self, resource_type, amount):
        # Dodaj zasób do puli
        if resource_type in self.resources:
            self.resources[resource_type].add(amount)
        else:
            self.resources[resource_type] = Resource(resource_type, amount)

    def consume_resource(self, resource_type, amount):
        # Spróbuj użyć zasobu, zwróć True/False
        if resource_type in self.resources:
            return self.resources[resource_type].consume(amount)
        return False

    def get_status(self):
        # Zwróć słownik z aktualnym stanem zasobów
        return {name: res.quantity for name, res in self.resources.items()}

    def daily_consumption(self, population):
        # Oblicz i zastosuj dzienne zużycie zasobów
        food_needed = 2 * population
        water_needed = 3 * population
        self.consume_resource("food", food_needed)
        self.consume_resource("water", water_needed)
