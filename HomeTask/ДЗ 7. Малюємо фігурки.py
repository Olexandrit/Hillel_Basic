#  ________ _________  ________
# |\   ____\\___   ___\\   __  \
# \ \  \___\|___ \  \_\ \  \|\ /_
#  \ \  \       \ \  \ \ \   __  \
#   \ \  \____   \ \  \ \ \  \|\  \
#    \ \_______\  \ \__\ \ \_______\
#     \|_______|   \|__|  \|_______|
#
# Welcome to Code the blocks, where Lego blocks meet programming
#
# Click the "Run" button above to place your blocks.
# Drag to pan and shift-scroll to zoom in the left-hand "Blocks" area.

from ctb import place

# Квадрат
num = 10
for x in range(num):
    for y in range(num):
        place(x, 0, y)

# пустий квадрат
num = 10
for x in range(num):
    place(x, 0, 0)

for y in range(num):
    place(0, y, 0)
    place(num, y, 0)

for x in range(num):
    place(x, num-1, 0)

# Коло
X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

x = y = 0

for x in X[:4]:
    place(x, 0, 0)

place(4, 1, 0)
place(5, 2, 0)

for y in Y[3:7]:
    place(6, y, 0)

place(5, 7, 0)
place(4, 8, 0)

for x in X[:4]:
    place(x, 9, 0)

place(-1, 8, 0)
place(-2, 7, 0)

for y in Y[6:2:-1]:
    place(-3, y, 0)

place(-2, 2, 0)
place(-1, 1, 0)
