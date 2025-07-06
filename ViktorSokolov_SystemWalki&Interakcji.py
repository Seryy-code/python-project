import random

class CombatSystem:
    """System obsługujący walkę między jednostkami"""

    def __init__(self):
        # TODO: Zainicjuj system walki
        # Przechowuj historię walk
        pass

    def calculate_damage(self, attacker_strength, weapon_bonus=0):
        # TODO: Oblicz obrażenia
        # base_damage = attacker_strength + weapon_bonus + random(0,10)
        pass

    def melee_combat(self, attacker, defender):
        # TODO: Przeprowadź walkę wręcz
        # Zwróć słownik z wynikiem walki
        pass

    def ranged_combat(self, attacker, defender, ammo_available):
        # TODO: Przeprowadź walkę dystansową
        # Użyj amunicji jeśli dostępna
        pass

    def group_combat(self, humans_list, zombies_list):
        # TODO: Symuluj walkę grupową
        # Zwróć listę ocalałych i poległych
        pass

class InfectionSystem:
    """System zarażania"""

    def __init__(self):
        # TODO: Zainicjuj system
        pass

    def attempt_infection(self, human, infection_chance=0.3):
        # TODO: Spróbuj zarazić człowieka
        # Zwróć True jeśli zarażony
        pass

    def process_infection(self, infected_human, hours_passed):
        # TODO: Przetwórz postęp infekcji
        # Po 6-12h zmień w zombie
        pass

# Testy do wykonania:
# 1. Symuluj walkę 1v1 człowiek vs zombie
# 2. Symuluj walkę grupową 5 ludzi vs 8 zombie
# 3. Przetestuj system zarażania
# 4. Wygeneruj raport z 10 walk