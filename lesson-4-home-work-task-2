import random

def get_numbers_ticket(min, max, quantity):
    # 1) перевірка обмежень
    if min < 1 or max > 1000 or min > max or quantity < 1 or quantity > (max - min + 1):
        return []
    # 2) беремо унікальні випадкові числа (без повторів)
    nums = random.sample(range(min, max + 1), quantity)
    # 3) сортуємо і повертаємо
    return sorted(nums)

# Перевірка коду
lottery_numbers = get_numbers_ticket(1, 49, 6)
print(lottery_numbers)