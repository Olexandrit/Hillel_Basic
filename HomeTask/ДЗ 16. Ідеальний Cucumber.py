# ВАЖЛИВО: Не можна користуватись конструкцією `if`


# 1. Привітатися та запросити користувача ввести слово "Cucumber"
# 2. Перевірити, чи:
#   1. Слово написано з великої літери
#   2. Чи всі літери, окрім першої, маленькі
#   3. Чи нема зайвих пробілів у тексті
#   4. Чи це саме слово Cucumber, а не щось інше
# 3. У разі порушення будь-якої з перевірок, обуритись та вивести користувачу помилку
# з текстом який зрозуміло описує йому проблему.
# _Наприклад, якщо користувач ввів cucumber вивести помилку про те що слово написано з маленької літери._
# 4. У разі помилки запросити користувача ввести слово "Cucumber" ще раз.
# У іншому разі - подякувати та завершити програму.


COME_I_BELIVE = 'Давай, я в тебе вірю: '


def intro_cucumber():
    print("Привіт! Мені дуже потрібен Cucumber прямо зараз, введи мені Cucumber будь ласка!\n"
          "Але будь уважним, неймовірно важливо щоб Cucumber гарний та без помилок!")


def check_cucumber():
    str_cucumber = input(COME_I_BELIVE)

    # 1. Слово написано з великої літери
    assert str_cucumber[0].isupper(), 'Що ні! Ну хто ж так робить! Твій Cucumber починається з маленької літери, виправляй швиденько 😡'

    # 2. Чи всі літери, окрім першої, маленькі
    assert str_cucumber == str_cucumber.capitalize(), 'Що за кривий Cucumber? А ну вирівнюй! 😡'

    # 3. Чи нема зайвих пробілів у тексті
    assert str_cucumber.find(' ') == -1, 'Щось я не памʼятаю щоб у Cucumber були пробіли. Буду вважати що це випадковість... 😡'

    # 4. Чи це саме слово Cucumber, а не щось інше
    assert str_cucumber.lower() == 'cucumber', 'Тут взагалі нема Cucumber! 😡'

    return str_cucumber


def well_done_cucumber(str_cucumber):
    print(f'{str_cucumber}!!! Відмінно! Дуже дякую! Ти, буквально, врятував всесвіт 😊! ')


def start_cucumber():
    str_cucumber = ''
    intro_cucumber()

    try:
        str_cucumber = check_cucumber()
        well_done_cucumber(str_cucumber)
    except AssertionError as error:
        print(error)

    try:
        str_cucumber = check_cucumber()
        well_done_cucumber(str_cucumber)
    except AssertionError as error:
        print(error)
        print("\nВ тебе не вишло. Дякую")


start_cucumber()