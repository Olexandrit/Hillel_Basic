class Animal:
    def __init__(self, color, heigt, weight, paws):
        self.color = color
        self.heigt = heigt
        self.weight = weight
        self.paws = paws

    def __str__(self):
        return f'{self.color}; {self.heigt} cm; {self.weight} kg; {len(self.paws)} paws'

    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self, color, heigt, weight, paws, is_service_dog=False):
        super().__init__(color, heigt, weight, paws)
        self.is_service_dog = is_service_dog

    def __str__(self):
        return f'Dog: {super().__str__()}'

    def make_sound(self):
        print('Woof!')


class Cat(Animal):
    def __str__(self):
        return f'Cat: {super().__str__()}'

    def make_sound(self):
        print('Meow!')


if __name__ == '__main__':
    katana = Dog('black+white', 55, 34, ['paw', 'paw', 'paw', 'paw'])
    katana.make_sound()

    masyana = Cat('gray', 40, 4, ['paw', 'paw', 'paw', 'paw'])
    masyana.make_sound()

    patron = Dog('ginger+white', 30, 6, ['paw', 'paw', 'paw', 'paw'], True)
    patron.make_sound()

    print(katana)
    print(masyana)
    print(patron)
    
    # Поліморфізм
    animals = [katana, masyana, patron]
    for animal in animals:
        animal.make_sound()
