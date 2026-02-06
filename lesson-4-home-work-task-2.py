import random
from typing import List


def get_numbers_ticket(min_value: int, max_value: int, quantity: int) -> List[int]:
    """Повертає відсортований список унікальних випадкових чисел або [] при невалідних параметрах."""
    # 1) перевірка обмежень
    if min_value < 1 or max_value > 1000 or min_value > max_value:
        return []
    if quantity < 1 or quantity > (max_value - min_value + 1):
        return []

    # 2) беремо унікальні випадкові числа (без повторів)
    nums = random.sample(range(min_value, max_value + 1), quantity)

    # 3) сортуємо і повертаємо
    return sorted(nums)


if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print(lottery_numbers)