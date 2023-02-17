tickets = int(input("Введите количество билетов: "))
sum_ = 0

for i in range(tickets):
    age = int(input(f"Введите возраст {i+1} участника: "))
    if 18 <= age < 25:
        sum_ += 990
    elif age >= 25:
        sum_ += 1390

print("Сумма к оплате:", sum_ if tickets < 4 else int(sum_ - (sum_ * 0.1)), "рублей")
