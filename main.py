from SerhiiVyzolmyrskyi_SystemMapy import GameMap
from VladyslavTiutiunyk_SystemZasobów import ResourceManager
from AndriiZakordonskyi_SystemJednostek import Human, Zombie


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

def menu_human(human, game_map, resource_manager):
    menu_Human = True
    while menu_Human:
        print("\n--- Ustawienia human ---")
        print("1. Przenieś jednostkę")
        print("2. Zadaj obrażenia")
        print("3. Spożyj zasoby")
        print("4. Zmień rolę")
        print("0. Back")
        choice = input("Twój wybór: ")

        if choice == "1":
            try:
                new_x = int(input("Nowe X: "))
                new_y = int(input("Nowe Y: "))
                tile = game_map.get_tile(new_x, new_y)
                if tile is None:
                    print("Nie ma takiej komórki.")
                elif tile.terrain_type == "water":
                    print("Nie możesz wejść do wody!")
                else:
                    human.move(new_x, new_y)
            except Exception as e:
                print("Błąd wprowadzania:", e)
        elif choice == "2":
            try:
                dmg = int(input("Ile obrażeń zadać: "))
                human.take_damage(dmg)
            except Exception as e:
                print("Błąd wprowadzania:", e)
        elif choice == "3":
            food_needed = 1
            water_needed = 1
            food_ok = resource_manager.consume_resource("food", food_needed)
            water_ok = resource_manager.consume_resource("water", water_needed)
            human.consume_resources(1 if food_ok else 0, 1 if water_ok else 0)
            if food_ok and water_ok:
                print("Człowiek spożył zasoby z magazynu.")
            else:
                print("Brak zasobów w magazynie! Morale spada.")
        elif choice == "4":
            print("Dostępne role: warrior, scavenger, medic, builder, leader")
            new_role = input("Podaj nową rolę: ")
            human.role = new_role
            print(f"Rola zmieniona na: {human.role}")
        elif choice == "0":
            menu_Human = False
        else:
            print("Niewłaściwy wybór. Spróbuj jeszcze raz.")

def menu_units(units, game_map, resource_manager):
    while True:
        print("\n--- Zarządzanie jednostkami ---")
        print("1. Wybierz jednostkę po współrzędnych")
        print("0. Powrót")
        choice = input("Twój wybór: ")

        if choice == "1":
            try:
                x = int(input("Podaj X jednostki: "))
                y = int(input("Podaj Y jednostki: "))
                found = None
                for unit in units:
                    if unit.x == x and unit.y == y:
                        found = unit
                        break
                if not found:
                    print("Nie znaleziono jednostki na tych współrzędnych.")
                    continue

                print(f"Wybrano: {'Człowiek' if isinstance(found, Human) else 'Zombie'} na ({found.x}, {found.y})")
                print("1. Przenieś jednostkę")
                if isinstance(found, Human):
                    print("2. Zadaj obrażenia")
                    print("3. Spożyj zasoby")
                    print("4. Zmień rolę")
                print("0. Powrót")
                sub_choice = input("Twój wybór: ")
                if sub_choice == "1":
                    new_x = int(input("Nowe X: "))
                    new_y = int(input("Nowe Y: "))
                    tile = game_map.get_tile(new_x, new_y)
                    if tile is None:
                        print("Nie ma takiej komórki.")
                    elif tile.terrain_type == "water":
                        print("Nie możesz wejść do wody!")
                    else:
                        other = None
                        for unit in units:
                            if unit != found and unit.x == new_x and unit.y == new_y:
                                other = unit
                                break
                        prev_x, prev_y = found.x, found.y
                        found.move(new_x, new_y)
                        if other:
                            if isinstance(found, Human) and isinstance(other, Zombie):
                                print("Zombie atakuje człowieka!")
                                found.take_damage(20)
                                if found.hp > 0:
                                    other.move(prev_x, prev_y)
                            elif isinstance(found, Zombie) and isinstance(other, Human):
                                print("Zombie atakuje człowieka!")
                                other.take_damage(20)
                                if other.hp > 0:
                                    found.move(prev_x, prev_y)
                elif sub_choice == "2" and isinstance(found, Human):
                    try:
                        dmg = int(input("Ile obrażeń zadać: "))
                        found.take_damage(dmg)
                    except Exception as e:
                        print("Błąd wprowadzania:", e)
                elif sub_choice == "3" and isinstance(found, Human):
                    food_needed = 1
                    water_needed = 1
                    food_ok = resource_manager.consume_resource("food", food_needed)
                    water_ok = resource_manager.consume_resource("water", water_needed)
                    found.consume_resources(1 if food_ok else 0, 1 if water_ok else 0)
                    if food_ok and water_ok:
                        print("Człowiek spożył zasoby z magazynu.")
                    else:
                        print("Brak zasobów w magazynie! Morale spada.")
                elif sub_choice == "4" and isinstance(found, Human):
                    print("Dostępne role: warrior, scavenger, medic, builder, leader")
                    new_role = input("Podaj nową rolę: ")
                    found.role = new_role
                    print(f"Rola zmieniona na: {found.role}")
                elif sub_choice == "0":
                    continue
                else:
                    print("Niewłaściwy wybór.")
            except Exception as e:
                print("Błąd:", e)
        elif choice == "0":
            break
        else:
            print("Niewłaściwy wybór. Spróbuj jeszcze raz.")

def main():
    game_map = GameMap()
    game_map.generate_terrain()
    resource_manager = ResourceManager()
    human1 = Human(0, 0, "warrior")
    human2 = Human(2, 2, "medic")
    zombie1 = Zombie(1, 1, "runner")
    zombie2 = Zombie(3, 3, "normal")
    units = [human1, human2, zombie1, zombie2]


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
        elif choice == "4":
            menu_units(units, game_map, resource_manager)
        elif choice == "0":
            print("Exit.")
            break
        else:
            print("Zły wybór!")

if __name__ == "__main__":
    main()