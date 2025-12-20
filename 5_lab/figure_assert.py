class Figure:
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in ["квадрат", "прямокутник", "трикутник"], \
            "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length


try:
    a = Figure("трапеція", 12) 
except AssertionError as e:
    print(e)

try:
    b = Figure("квадрат", 0)  
except AssertionError as e:
    print(e)

c = Figure("квадрат", 1)  
print(f"Створено об'єкт: {c.type}, довжина: {c.length}")


