from SerhiiVyzolmyrskyi_SystemMapy import GameMap
from VladyslavTiutiunyk_SystemZasobów import ResourceManager
from ViktorSokolov_SystemWalki_Interakcji import CombatSystem
from AndriiZakordonskyi_SystemJednostek import Human


def menu_gamemap(game_map):
    menu_GameMap = True
    while menu_GameMap:
        print("\nWybierz akcję:")
        print("1. Tworzenie nowego terenu")
        print("2. Wizualizacja mapy")
        print("3. Sprawdź drogę pomiędzy dwoma punktami")
        print("4. Wyświetl typ komórki według współrzędnych")
        print("0. wyjść")
        choice = input("Twój wybór: ")

        if choice == "1":
            game_map.generate_terrain()
            print("Teren generowany.")
        elif choice == "2":
            game_map.visualize()
        elif choice == "3":
            try:
                x1 = int(input("Start X: "))
                y1 = int(input("Start Y: "))
                x2 = int(input("End X: "))
                y2 = int(input("End Y: "))
                path_exists = game_map.find_path(x1, y1, x2, y2)
                if path_exists:
                    print(f"Droga istnieje od ({x1}, {y1}) do ({x2}, {y2}).")
                else:
                    print(f"Nie ma drogi od ({x1}, {y1}) do ({x2}, {y2}).")
            except Exception as e:
                print("Błąd wprowadzania:", e)
        elif choice == "4":
            try:
                x = int(input("X: "))
                y = int(input("Y: "))
                tile = game_map.get_tile(x, y)
                if tile:
                    print(f"Komórka ({x}, {y}): {tile.terrain_type}")
                else:
                    print("Nie ma takiej komórki..")
            except Exception as e:
                print("Błąd wprowadzania:", e)
        elif choice == "0":
            print("Exit.")
            menu_GameMap = False
        else:
            print("Zły wybór!")

def menu_resource_manager(resource_manager):
    menu_ResourceManager = True
    while menu_ResourceManager:
        print("\n--- Ustawienia resource_manager ---")
        print("1. Test")
        print("0. Back")
        choice = input("Twój wybór: ")

        if choice == "1":
            resource_manager.test()
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