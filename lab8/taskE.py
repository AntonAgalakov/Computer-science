# Лабораторная работа 8
# Задание E: Доставка

def decode_postal_code(code):
    """
    Декодирует четырехзначный почтовый код региона Канадория
    """
    pass

if __name__ == "__main__":
    print("A2N1 (корректный):", decode_postal_code("A2N1"))
    print("E0A7 (корректный):", decode_postal_code("E0A7"))
    print("Z1A2 (некорректная буква):", decode_postal_code("Z1A2"))
    print("A2N (некорректная длина):", decode_postal_code("A2N"))
    print("1234 (некорректный формат):", decode_postal_code("1234"))
    print("A2N12 (некорректная длина):", decode_postal_code("A2N12"))
    print("a2n1 (нижний регистр):", decode_postal_code("a2n1"))
    print(" (пустая строка):", decode_postal_code(""))