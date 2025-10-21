# Лабораторная работа 8
# Задание F: Эрудит - Битва Саши Ш.

def calculate_scrabble_score(word):
    """
    Вычисляет количество очков в игре Эрудит для русского слова
    """
    pass

if __name__ == "__main__":
    print("ПРИВЕТ (корректный):", calculate_scrabble_score("ПРИВЕТ"))
    print("ПИТОН (корректный):", calculate_scrabble_score("ПИТОН"))
    print("ПРОГРАММИРОВАНИЕ (корректный):", calculate_scrabble_score("ПРОГРАММИРОВАНИЕ"))
    print("КОД (корректный):", calculate_scrabble_score("КОД"))
    print("СИЛА (корректный):", calculate_scrabble_score("СИЛА"))
    print(" (пустая строка):", calculate_scrabble_score(""))
    print("привет (нижний регистр):", calculate_scrabble_score("привет"))
    print("ПиТоН (смешанный регистр):", calculate_scrabble_score("ПиТоН"))
    print("Hello (английские буквы):", calculate_scrabble_score("Hello"))
    print("123 (цифры):", calculate_scrabble_score("123"))
    print("Привет! (с восклицательным знаком):", calculate_scrabble_score("Привет!"))
    print("ПРИ-ВЕТ (с дефисом):", calculate_scrabble_score("ПРИ-ВЕТ"))
    print("ПРИВЕТ, МИР (с запятой и пробелом):", calculate_scrabble_score("ПРИВЕТ, МИР"))