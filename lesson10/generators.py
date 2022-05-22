def float_range(end, start=0.0, step=1.0):
    current = start
    while current < end:
        print(f'Before yield {current}')
        yield current
        print(f'After yield {current}')
        current += step
        
        
print(float_range(10))


for i in float_range(10):
    print(i)
    if i > 5:
        break

square_range = (i ** 2 for i in range(10))
print(square_range)
print(list(square_range))

print(range(10))  # range - це також генератор
print(list(range(10)))


def weird_gen():
    yield 1
    yield 2
    yield 3


for i in weird_gen():
    print(i)
