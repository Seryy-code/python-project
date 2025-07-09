from SerhiiVyzolmyrskyi_SystemMapy import GameMap
from VladyslavTiutiunyk_SystemZasobów import ResourceManager
from ViktorSokolov_SystemWalki_Interakcji import CombatSystem
from AndriiZakordonskyi_SystemJednostek import Human


def menu_gamemap(game_map):
    menu_GameMap = True
    while menu_GameMap:
        print("\n--- Ustawienia karty ---")
        print("1. Test")
        print("0. Back")
        choice = input("Twój wybór: ")
        if choice == "1":
            game_map.test()
        elif choice == "0":
            menu_GameMap = False
        else:
            print("Niewłaściwy wybór. Spróbuj jeszcze raz.")

def menu_resource_manager(resource_manager):
    menu_ResourceManager = True
    while menu_ResourceManager:
        print("\n--- Ustawienia resource_manager ---")
        print("1. Pokaż stan zasobów")
        print("2. Dodać zasób")
        print("3. Korzystać z zasobu")
        print("4. Simułować dzień dla mieszkańców")
        print("0. Back")
        choice = input("Twój wybór: ")

        if choice == "1":
            print(resource_manager.get_status())
        elif choice == "2":
            rtype = input("Typ zasobu: ")
            amount = int(input("Ile dodać: "))
            resource_manager.add_resource(rtype, amount)
            print("Dodane.")
        elif choice == "3":
            rtype = input("Typ zasobu: ")
            amount = int(input("Ile użyć: "))
            if resource_manager.consume_resource(rtype, amount):
                print("Używane.")
            else:
                print("Brak zasobów.")
        elif choice == "4":
            pop = int(input("Wprowadź liczbę osób: "))
            resource_manager.daily_consumption(pop)
            print("Zasoby uaktualnione.")
        elif choice == "0":
            menu_ResourceManager = False
        else:
            print("Niewłaściwy wybór. Spróbuj jeszcze raz.")

def menu_combat(combat_system):
    menu_Combat = True
    while menu_Combat:
        print("\n--- Ustawienia combat_system ---")
        print("1. Test")
        print("0. Back")
        choice = input("Twój wybór: ")

        if choice == "1":
            combat_system.test()
        elif choice == "0":
            menu_Combat = False
        else:
            print("Niewłaściwy wybór. Spróbuj jeszcze raz.")

def menu_human(human):
    menu_Human = True
    while menu_Human:
        print("\n--- Ustawienia human ---")
        print("1. Test")
        print("0. Back")
        choice = input("Twój wybór: ")

        if choice == "1":
            human.test()
        elif choice == "0":
            menu_Human = False
        else:
            print("Niewłaściwy wybór. Spróbuj jeszcze raz.")

def main():
    game_map = GameMap()
    # game_map.generate_terrain()
    resource_manager = ResourceManager()
    combat_system = CombatSystem()
    human = Human(0, 0)


    while True:
        print("\n=== Główne menu ===")
        print("1. Ustawienia i funkcje mapy")
        print("2. Menedżer zasobów")
        print("3. System walki")
        print("4. System jednostek")
        print("0. Exit")
        choice = input("Twój wybór: ")
        if choice == "1":
            menu_gamemap(game_map)
        elif choice == "2":
            menu_resource_manager(resource_manager)
        elif choice == "3":
            menu_combat(combat_system)
        elif choice == "4":
            menu_human(human)
        elif choice == "0":
            print("Exit.")
            break
        else:
            print("Zły wybór!")

if __name__ == "__main__":
    main()