import random


def extract_cucumber(text):
    cucumber_index = text.lower().find('cucumber')
    if cucumber_index == -1:
        return None

    return text[cucumber_index:cucumber_index + len('cucumber')]


def generate_cucumber():
    base = 'cucumber'
    cucumber = ''

    for char in base:
        if random.getrandbits(1):
            char = char.upper()
        cucumber += char

    return cucumber


print(__name__)  # цей код та код до цього буде виконуватись коли ми імпортуємо файл

if __name__ == '__main__':  # ця частина коду буде виконуватись лише якщо ми запускаємо саме цей файл
    print(__name__)
    print(generate_cucumber())
