
import sys


print(sys.platform)

print(sys.version)

print(sys.argv)

# print(f'Привіт, {sys.argv[1]}')

if len(sys.argv) > 1:
    print(f'Привіт, {sys.argv[1]}')
else:
    print('О ні, ти забув ввести імʼя')
    
