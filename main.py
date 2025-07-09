from SerhiiVyzolmyrskyi_SystemMapy import GameMap

def main():
    game_map = GameMap(width=10, height=10)
    game_map.generate_terrain()

    while True:
        print("\nWybierz akcję:")
        print("1. Сгенерировать новый террейн")
        print("2. Tworzenie nowego terenu")
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
            break
        else:
            print("Zły wybór!")

if __name__ == "__main__":
    main()