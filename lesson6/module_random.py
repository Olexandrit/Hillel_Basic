import random

for _ in range(10):
    print(random.random())

print([random.random() for _ in range(10)])

print([random.randint(0, 100) for _ in range(10)])

print([random.randrange(0, 100, 5) for _ in range(10)])

print([random.uniform(5, 10) for _ in range(10)])

fruits = ['🍊', '🍏', '🍑', '🍌']
fruit = random.choice(fruits)
print(fruit)

smoothie = random.choices(fruits, k=3)
print(smoothie)