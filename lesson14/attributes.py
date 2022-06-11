class Dog:
    species = 'Canis familiaris'  # Атрибут класу

    def __init__(self, name, age):
        self.name = name  # Атрибут екземпляру
        self.age = age  # Атрибут екземпляру


if __name__ == '__main__':
    buddy = Dog('Buddy', 9)
    miles = Dog('Miles', 4)
    print(buddy.name, buddy.age)
    print(miles.name, miles.age)

    print(buddy.species)
    print(miles.species)

    miles.species = 'Felis silvestris'

    print(buddy.species)
    print(miles.species)

    print(Dog.species)

    Dog.species = 'Canis lupus'

    print(buddy.species)
    print(miles.species)
    print(miles.__class__.species)
    
