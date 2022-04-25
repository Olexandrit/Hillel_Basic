fruits = ('🍑', '🍌', '🍏')
# fruits = ['🍑', '🍌', '🍏']
peach, banana, apple = fruits

print(peach)
print(banana)
print(apple)

fruits = ('🍑', '🍌', '🍏', '🍊')
peach, banana, apple, _ = fruits

print(peach)
print(banana)
print(apple)

fruits = ('🍑', '🍌', '🍏', '🍊', '🍉')
peach, banana, apple, *other_fruits = fruits

print(peach)
print(banana)
print(apple)
print(other_fruits)

peach, banana = banana, peach
peach, banana = (banana, peach)
print(peach, banana)
fruits = banana, peach
print(fruits)