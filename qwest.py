def show_status(health, coins, turns):
    print(f"твое здоровье {health}, у тебя {coins} монет")
    print(f"твой ход {turns}")

def show_menu():
    print("\nТы зашла в город. Твои действия:")
    print("  1. Идти вперёд")
    print("  2. Осмотреться")
    print("  3. снять комнату в гостинице")
    print("  4. Выйти")
    choice = input("\nТвой выбор: ").lower().strip()
    return choice

def go_forward(health, coins):
    health -= 15
    print("\n Ты пришла к центру города! Но очень устала. ( -15)")
    return health, coins

def look_around(health, coins):
    print("\n👀 Ты осматриваешься и видишь придорожное кафе.")
    action = input("Зайти или пройти мимо? (зайти/мимо): ").lower().strip()
    
    if action == "зайти":
        if coins >= 30:
            print("\n Молодец! Акция: второе кофе бесплатно! ( +50,  -30)")
            health += 50
            coins -= 30
        else:
            print("\nНедостаточно монеток.")
    elif action == "мимо":
        print("\nТы ушла ни с чем.")
    else:
        print("\n Я тебя не понял.")
    
    return health, coins


def hotel(health,coins):
    print("Ты нашла гостиницу")
    if coins >=50:
        health +=30
        coins -=50
        print(f"Ты выспалась у тебя {health} здоровья, твой баланс {coins} монеток")
    else:
        print("У тебя недостаточно денег")
    return health, coins


health = 100
coins = 100
turns = 0

print()
print(" Добро пожаловать в Твинкс!")
print()

while health > 0 and coins >= 0:  
    turns += 1
    print()
    show_status(health,coins,turns)
    choice = show_menu()
    if choice == "1" or choice == "идти вперед":
        health, coins = go_forward(health, coins)     
    elif choice == "2" or choice == "осмотреться":
        health, coins  = look_around(health,coins)     
    elif choice == "3" or choice == "отдохнуть":
        health,coins = hotel(health,coins)        
    elif choice == "4" or choice == "выйти":
        print("\n Ты решила уйти. Спасибо за игру!")
        break 
    else:
        print("\n Неверный выбор. Попробуй ещё раз.")
        continue  

if health <= 0:
    print(f"\n Ты слишком устала. Ходов сделано: {turns}")
elif coins < 0:
    print(f"\n У тебя закончились монетки. Ходов сделано: {turns}")
else:
    print(f"\n Игра завершена. Ходов сделано: {turns}")
