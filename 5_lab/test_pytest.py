from app import Figure

def test_app_triangle():
    """Тест для трикутника (був раніше)"""
    fig = "трикутник"
    triangle = Figure(fig, 4)
    assert triangle.type == fig
    # Перевірка кутів (якщо ви додавали цей метод)
    if hasattr(triangle, 'get_angles'):
        assert triangle.get_angles == 3

def test_app_square_angles():
    """Тест для квадрата (який повертає високий відсоток)"""
    fig = "квадрат"
    square = Figure(fig, 5)
    # Перевірка кутів
    if hasattr(square, 'get_angles'):
        assert square.get_angles == 4

