player = {
    "name": "name",
    "health": 100,
    "coins": 50,
    "turns": 0,
    "gender": "male",
    "inventory": [],
}


def get_pronoun(gender: str, **values) -> str:
    return values.get(gender, "...")


def show_status(player):
    print("твои характеристики:")
    for key, values in player.items():
        print(key, "-", values)


def start():
    print("\nТы зашла в город. Твои действия:")
    print("  1. Идти вперёд")
    print("  2. Выйти")
    choice = input("\nТвой выбор: ").lower().strip()
    return choice


def city_center():
    word = get_pronoun(player["gender"], male="пришел", female="пришла")
    print(f"\nТы {word} к центру города, куда двинешься дальше?")
    print("  1. Отдохнуть в гостинице")
    print("  2. Подкрепиться в местном кафе")
    print("  3. Осмотреться (фонтан)")
    print("  4. Выйти из игры")
    print("  5. Показать статистику")
    choice = input("\nТвой выбор: ").lower().strip()
    return choice


def fountain(player):
    while 1:
        word = input("введи слово палиндром: ").lower().strip()
        if word == "выйти":
            break
        reversed_word = word[::-1]
        if word == reversed_word and len(word) > 2:
            word = get_pronoun(player["gender"], male="получил", female="получила")
            print(f"молодец! ты {word} бутылочку живой воды!")
            player["inventory"].append("Бутылочка воды")
            break
        print("попробуй еще раз")

    return player


def motel(player):
    pass


def cafe(player):
    pass


def main():
    print()
    print("Добро пожаловать в Твинкс!")
    print()

    choice = start()
    if choice == "выйти":
        print("Ты покидаешь Твинкс")
        return

    while player["health"] > 0 and player["coins"] >= 0:
        player["turns"] += 1
        loc = player.get("location")

        # старт
        if loc is None or loc == "центр":
            player["location"] = "центр"
            choice = city_center()
            match choice:
                case "1":  # идти в гостиницу
                    player["location"] = "гостиница"
                case "2":  # идти в кафе
                    player["location"] = "кафе"
                case "3":  # идти в фонтан
                    player["location"] = "фонтан"
                case "4":
                    word = get_pronoun(player["gender"], male="решил", female="решила")
                    print(f"\nТы {word} уйти. Спасибо за игру!")
                    return
                case "5":  # показать статистику
                    show_status(player)
                case _:
                    print("Неверный выбор.")

            continue
        # логика гостиницы
        elif loc == "гостинциа":
            motel(player)
            player["location"] = "центр"
        # логика кафе
        elif loc == "кафе":
            cafe(player)
            player["location"] = "центр"
        # логика фонтана
        elif loc == "фонтан":
            fountain(player)
            player["location"] = "центр"


if __name__ == "__main__":
    main()
