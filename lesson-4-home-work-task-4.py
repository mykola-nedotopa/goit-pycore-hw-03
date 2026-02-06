from datetime import datetime, timedelta
from typing import Dict, List


def get_upcoming_birthdays(users: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Повертає список привітань на наступні 7 днів (включно з сьогодні), переносячи вихідні на понеділок."""
    today = datetime.today().date()
    birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        try:
            birthday_this_year = birthday.replace(year=today.year)
        except ValueError:
            # якщо 29 лютого і рік не високосний - замінюємо на 28 лютого
            birthday_this_year = birthday.replace(year=today.year, day=28)
        

        if birthday_this_year < today:
            try:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            except ValueError:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1, day=28)

        days_diff = (birthday_this_year - today).days

        if 0 <= days_diff <= 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:      # субота
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:    # неділя
                congratulation_date += timedelta(days=1)

            birthdays.append(
                {
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                }
            )

    return birthdays


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.02.07"},
        {"name": "Jane Smith", "birthday": "1990.02.10"},
        {"name": "Maria Maria", "birthday": "2000.02.29"},
    ]
    print("Список привітань на цьому тижні", get_upcoming_birthdays(users))