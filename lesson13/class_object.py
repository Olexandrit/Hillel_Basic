 class Bottle:
    def __init__(self, color, capacity, material, brand):  # конструктор класу
        self.color = color
        self.capacity = capacity
        self.material = material
        self.brand = brand

        self.opened = False
        self.contains = None
        
        # __init__ нічого не повертає

    def __str__(self):
        return f'{self.brand} bottle with {self.contains or "nothing"} inside'

    def open(self):
        self.opened = True
        print('Bottle is open')

    def close(self):
        self.opened = False
        print('Bottle is closed')

    def fill(self, liquid):
        assert self.opened, 'Bottle is closed'

        self.contains = liquid
        print('Bottle is filled with', self.contains)

    def empty(self):
        assert self.opened, 'Bottle is closed'

        contained = self.contains
        self.contains = None
        print('Bottle is empty')

        return contained


if __name__ == '__main__':
    dopper = Bottle('white', 500, 'steel', 'Dopper')
    morsh = Bottle('transparent', 330, 'plastic', 'Morshinska')

    dopper.open()
    dopper.fill('water')
    dopper.close()

    dopper.empty()  # помилка, бо бутилка закрита
    dopper.open()
    morsh.open()
    morsh.fill(dopper.empty())
    dopper.close()
    morsh.close()

    print('Dopper contains', dopper.contains)
    print('Morshinska contains', morsh.contains)
    print(dopper)
    print(morsh)
    
    dopper = Bottle('white', 500, 'steel', 'Dopper')
    dopper_copy = Bottle('white', 500, 'steel', 'Dopper')
    morsh = Bottle('transparent', 330, 'plastic', 'Morshinska')
