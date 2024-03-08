seconds = int(input("Введіть секунди (0 <= seconds < 8640000): "))
if 0 <= seconds < 8640000:
    days = seconds // 86400
    remaining_seconds = seconds % 86400
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    remaining_seconds %= 60
    days_word = "день" if days == 1 else "дні" if 1 < days < 5 else "днів"
    days_str = f"{days} {days_word}, " if days > 0 else ""
    hours_str = f"{hours:02d}"
    minutes_str = f":{minutes:02d}"
    seconds_str = f":{remaining_seconds:02d}"

    result = days_str + hours_str + minutes_str + seconds_str
    print(result)
else:
    print("Введене число не відповідає умовам задачі.")