from datetime import datetime
from typing import Optional


def get_days_from_today(date: str) -> Optional[int]:
    """Повертає кількість днів між заданою датою (YYYY-MM-DD) і сьогодні.
    Якщо формат неправильний — повертає None.
    """

    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return None
    
    today = datetime.today().date()
    return (today - target_date).days


if __name__ == "__main__":
    print(get_days_from_today("2026-01-01"))
    print(get_days_from_today("2026-12-31"))
    print(get_days_from_today("2026/12/31")) # None