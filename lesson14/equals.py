class Bottle:
    def __init__(self, color, capacity, material, brand):  # конструктор класу
        self.color = color
        self.capacity = capacity
        self.material = material
        self.brand = brand

        self.opened = False
        self.contains = None

    def __str__(self):
        return f'{self.brand} bottle with {self.contains or "nothing"} inside'

    def __eq__(self, another):  # magic method [eq]uals
        return isinstance(another, Bottle) and all(
            (
                self.color == another.color,
                self.capacity == another.capacity,
                self.material == another.material,
                self.brand == another.brand,
            )
        )

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
    another_dopper = Bottle('white', 500, 'steel', 'Dopper')
    morsh = Bottle('transparent', 330, 'plastic', 'Morshinska')

    print('dopper == morsh', dopper == morsh)

    print('dopper == another_dopper', dopper == another_dopper)
    print('dopper == dopper', dopper == dopper)

    print('dopper is another_dopper', dopper is another_dopper)
    print('dopper is dopper', dopper is dopper)

    print('dopper == 42', dopper == 42)

