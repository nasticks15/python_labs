def is_palindrome(text: str) -> bool:
    """
    Перевіряє, чи є рядок паліндромом (без урахування регістру)
    """
    text = text.lower()
    return text == text[::-1]


if __name__ == "__main__":
    user_input = input("Введіть рядок: ")
    if is_palindrome(user_input):
        print("Рядок є паліндромом")
    else:
        print("Рядок не є паліндромом")
