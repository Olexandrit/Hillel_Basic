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
