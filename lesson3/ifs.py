duck = 'eggs'
dog = 'milk'
platypus = 'eggs+milk'

visitor = duck

if visitor == 'eggs':
    print('Go to left corridor')
elif visitor == 'milk':
    print('Go to right corridor')
else:
    print('Go to admin :/')
