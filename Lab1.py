def validate_credit_card(card_number):
    # Убрать пробелы и перевернуть номер карты
    card_number = card_number.replace(" ", "")[::-1]
    
    # Проверка на то, что в номере только цифры
    if not card_number.isdigit():
        return False
    
    # Проверка длины номера карты (обычно 13, 15 или 16 цифр)
    if not 13 <= len(card_number) <= 16:
        return False
    
    # Вычисление контрольной суммы по алгоритму Луна
    total = 0
    for i, digit in enumerate(card_number):
        if i % 2 == 1:
            digit = int(digit) * 2
            if digit > 9:
                digit -= 9
        total += int(digit)
    
    # Проверка на кратность 10 (контрольная сумма должна быть кратна 10)
    return total % 10 == 0

def card_type(card_number):
    if card_number.startswith('4'):
        return "Visa"
    elif card_number.startswith(('51', '52', '53', '54', '55')):
        return "Mastercard"
    elif card_number.startswith(('34', '37')):
        return "American Express"
    elif card_number.startswith('6'):
        return "Discover"
    elif card_number.startswith(('2')):
        return "Mir"
    else:
        return "Unknown"

# Пример использования функций
card_number = input("Введите номер карты: ")
if validate_credit_card(card_number):
    print("Номер карты является действительным.")
    print("Тип карты:", card_type(card_number))
else:
    print("Номер карты не является действительным.")