from abc import abstractmethod, ABC  # Abstract Base Class


class Animal(ABC):
    def __init__(self, color, heigt, weight, paws):
        self.color = color
        self.heigt = heigt
        self.weight = weight
        self.paws = paws

    def __str__(self):
        return f'{self.color}; {self.heigt} cm; {self.weight} kg; {len(self.paws)} paws'

    @abstractmethod
    def make_sound(self):
        raise NotImplementedError


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
    animals = [
        Dog('black+white', 55, 34, ['paw', 'paw', 'paw', 'paw']),
        Cat('...', 20, 4, ['paw', 'paw', 'paw', 'paw']),
        Animal('wierdo', 100, 100, ['paw', 'paw', 'paw', 'paw']),
    ]

    for animal in animals:
        animal.make_sound()  # Викликається метод make_sound з різних класів
