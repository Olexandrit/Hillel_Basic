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
