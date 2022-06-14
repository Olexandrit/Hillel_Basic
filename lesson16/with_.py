# import time
#
#
# with open('ducks.txt', 'r') as ducksfile:
#     print(ducksfile.read())
#
#
# # --
#
#
# class Timer:
#     def __init__(self):
#         self.start = 0
#         self.end = 0
#
#     @property
#     def time_spent(self):
#         return self.end - self.start
#
#     def __enter__(self):
#         self.start = time.time()
#         return self
#
#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         self.end = time.time()
#
#
# with Timer() as timer:
#     for i in range(10000):
#         _ = i ** i
#
# print(f'Spent: {timer.time_spent}s')
#
#
# # --


class AssertationHandler:
    def __init__(self):
        self.assert_count = 0

    def __enter__(self):
        print(self)
        pass

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_value:
            print(f'{exc_value}')
        return exc_type == AssertionError


salmon = input('Хочу лосося: ')
with AssertationHandler():
    assert salmon == '🐟', 'Ні, хочу рибку'
    print('Дяк ;3')

