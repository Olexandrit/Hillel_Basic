# import random
#
#
# class Cucumber:
#     _SIZES = {
#         3: 'tiny',
#         5: 'small',
#         10: 'medium',
#         17: 'large',
#         25: 'huge',
#     }
#     _COLORS = ('light-green', 'green', 'yellow')
#     _TASTES = ('sweet', 'sour', 'bitter', 'salty')
#
#     def __init__(self, size, color, taste):
#         self.size = size
#         self.color = color
#         self.taste = taste
#
#     def __str__(self):
#         return f'This Cucumber is {self.color}, {self.text_size} size and tastes {self.taste}'
#
#     @property
#     def text_size(self):
#         for size, text in reversed(self._SIZES.items()):
#             if self.size >= size:
#                 return text
#
#         return next(iter(self._SIZES.values()))
#
#     @property
#     def size(self):
#         return self._size
#
#     @color.setter
#     def size(self, value):
#         assert value > 1, f'size {value}cm is too small'
#         self._size = value
#
#     @property
#     def color(self):
#         return self._color
#
#     @color.setter
#     def color(self, color):
#         assert color in self._COLORS, f'{color} is not a valid color'
#         self._color = color
#
#     @classmethod
#     def generate(cls):
#         return cls(random.randint(2, 30), *self.multichoice(cls._COLORS, cls._TASTES))
#
#     @staticmethod
#     def multichoice(*iterables):
#         return tuple(random.choice(iterable) for iterable in iterables)
#
#
# if __name__ == '__main__':
#     cucumber = Cucumber(10, 'green', 'bitter')
#     cucumber.color = 'red'
#
#     print(cucumber)

listss = [1,2,3,4,5]


print('Concatenated String using join() =', "".join([ str(i) for i in listss]))

