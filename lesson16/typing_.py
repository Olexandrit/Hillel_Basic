from typing import TextIO, Optional, Union


class Duck:
    _ducks = []

    def __init__(self, name: Optional[Union[str, int]] = None):
        Duck._ducks.append(self)
        self.name = name or f'Duck #{len(Duck._ducks)}'

    def __str__(self) -> str:
        return f'{self.name} the Duck'

    def quack(self):
        print(f'{self.name}: Quaaack!')

    @classmethod
    def from_file(cls, file: TextIO) -> list['Duck']:  # tuple['Duck', ...]
        ducks = []
        for line in file:
            duck = Duck(line.strip())
            ducks.append(duck)

        return ducks

    @classmethod
    def all_ducks(cls) -> list['Duck']:
        return cls._ducks


if __name__ == '__main__':
    with open('ducks.txt') as f:
        Duck.from_file(f)

    Duck(42)

    for _ in range(10):
        Duck()

    for duck in Duck.all_ducks():
        duck.quack()

