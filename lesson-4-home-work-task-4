from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    # 1) поточна дата (без часу)
    today = datetime.today().date()
    birthdays = []  # помістимо  результати сюди

    # 2) проходимо по всіх користувачах
    for user in users:
        # 3) конвертуємо birthday з рядка в дату
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # 4) робимо день народження в поточному році
        birthday_this_year = birthday.replace(year=today.year)

        # 5) якщо вже минув — переносимо на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # 6) різниця в днях між ДН і сьогодні
        days_diff = (birthday_this_year - today).days

        # 7) якщо ДН в наступні 7 днів (включно з сьогодні)
        if 0 <= days_diff <= 7:
            congratulation_date = birthday_this_year

            # 8) якщо вихідний — переносимо на понеділок
            # weekday(): пн=0 ... сб=5, нд=6
            if congratulation_date.weekday() == 5:      # субота
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:    # неділя
                congratulation_date += timedelta(days=1)

            # 9) додаємо в результат
            birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return birthdays


# Перевірка коду
users = [
    {"name": "John Doe", "birthday": "1985.02.07"},
    {"name": "Jane Smith", "birthday": "1990.02.10"},
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)