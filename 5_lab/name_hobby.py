class Name:
    def __init__(self, name, hobby) -> None:
        allowed_names = ["Наталя", "Анонім", "Анастасія"]
        if name not in allowed_names:
            raise ValueError(f"Дозволені імена: {allowed_names}")
        if not hobby:
            raise ValueError("Хоббі не може бути пустим")
        self.name = name
        self.hobby = hobby

# Приклади
try:
    a = Name("Наталя", "співати")
except ValueError as e:
    print(e)

b = Name("Анастасія", "малювання")
print(f"Створено об'єкт: {b.name}, хоббі: {b.hobby}")
