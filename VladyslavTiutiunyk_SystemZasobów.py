class Resource:
    """Klasa reprezentująca zasób"""
    def __init__(self, name, quantity):
        # TODO: Zaimplementuj konstruktor
        pass

    def consume(self, amount):
        # TODO: Zmniejsz ilość zasobu, zwróć True jeśli się udało
        pass

    def add(self, amount):
        # TODO: Dodaj zasoby
        pass

class ResourceManager:
    def test(self):
        print("Test ResourceManager")
    """Manager zarządzający wszystkimi zasobami w grze"""
    def __init__(self):
        # TODO: Stwórz słownik zasobów
        # Podstawowe zasoby: food, water, medicine, ammo, materials
        pass

    def add_resource(self, resource_type, amount):
        # TODO: Dodaj zasób do puli
        pass

    def consume_resource(self, resource_type, amount):
        # TODO: Spróbuj użyć zasobu, zwróć True/False
        pass

    def get_status(self):
        # TODO: Zwróć słownik z aktualnym stanem zasobów
        pass

    def daily_consumption(self, population):
        # TODO: Oblicz i zastosuj dzienne zużycie zasobów
        # 1 człowiek = 2 food, 3 water dziennie
        pass

# Testy do wykonania:
# 1. Stwórz manager z początkowymi zasobami
# 2. Symuluj 5 dni konsumpcji dla 10 osób
# 3. Dodaj znalezione zasoby
# 4. Wyświetl raport o stanie zasobów