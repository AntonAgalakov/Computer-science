# Лабораторная работа 8
# Задание C: Кулинарные меры

def reduce_measure(amount, unit):
    """
    Преобразует меры объема
    """
    # Ваша реализация здесь
    pass

if __name__ == "__main__":
    print("59 teaspoons (корректный):", reduce_measure(59, "teaspoons"))
    print("16 tablespoons (корректный):", reduce_measure(16, "tablespoons"))
    print("3 teaspoons (корректный):", reduce_measure(3, "teaspoons"))
    print("-5 cups (некорректный):", reduce_measure(-5, "cups"))
    print("0 teaspoons (корректный):", reduce_measure(0, "teaspoons"))
    print("3.5 cups (некорректный):", reduce_measure(3.5, "cups"))
    print("2 liters (некорректная единица):", reduce_measure(2, "liters"))