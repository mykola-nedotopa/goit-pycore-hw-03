from datetime import datetime

def get_days_from_today(date):
    target_date = datetime.strptime(date, "%Y-%m-%d")
    today = datetime.now()
    return (today - target_date).days

# Перевірка коду
print(get_days_from_today("2026-01-01")) # Обраховує кількість днів з минулого до сьогоднішнього дня
print(get_days_from_today("2026-12-31")) # Обраховує кількість днів з майбутнього від сьогоднішнього дня (значення буде від'ємним в таком разі)