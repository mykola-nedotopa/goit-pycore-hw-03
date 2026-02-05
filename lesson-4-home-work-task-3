import re

def normalize_phone(phone_number):
    # 1) прибираємо все, крім цифр
    digits = re.sub(r"\D", "", phone_number)

    # 2) якщо номер вже починається з 380 (є код України) — додаємо лише "+"
    if digits.startswith("380"):
        return "+" + digits
    
    # 3) якщо коду немає — додаємо "+38" попереду
    return "+38" + digits

# приклад перевірки
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
sanitized_numbers = []
for num in raw_numbers:
    sanitized_numbers.append(normalize_phone(num))
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)