# Szablon startowy dla zadania
class Entity:
    """Bazowa klasa dla wszystkich jednostek w grze"""
    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.hp = hp

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        print(f"Jednostka przeniesiona na ({self.x}, {self.y})")

    def take_damage(self, damage):
        self.hp -= damage
        print(f"Jednostka otrzymała {damage} obrażeń, HP: {self.hp}")
        if self.hp <= 0:
            print("Jednostka nie żyje!")

class Human(Entity):
    """Klasa reprezentująca człowieka"""
    def __init__(self, x, y, role="survivor"):
        super().__init__(x, y, 100)
        self.morale = 85
        self.role = role  # "warrior", "scavenger", "medic", "builder", "leader"

    def consume_resources(self, food, water):
        if food > 0 and water > 0:
            print("Człowiek spożył zasoby.")
        else:
            self.morale -= 10
            print("Brak zasobów! Morale spada do:", self.morale)

class Zombie(Entity):
    """Klasa reprezentująca zombie"""
    def __init__(self, x, y, zombie_type="normal"):
        super().__init__(x, y, 50)
        self.zombie_type = zombie_type
        self.alive = True

    def can_infect(self):
        return self.alive

# Testy do wykonania:
# 1. Stwórz 3 ludzi o różnych rolach
# 2. Stwórz 2 zombie różnych typów
# 3. Przetestuj ruch jednostek
# 4. Przetestuj system obrażeń