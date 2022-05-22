from pathlib import Path

current_dir = Path('.')
print(current_dir)
print(current_dir.absolute())
file = current_dir / 'garden' / 'cucumber.txt'
print(file.name)

print(current_dir.exists())
print(current_dir.is_dir())  # False якщо не існує
print(file.is_file())  # False якщо не існує

print(file.parent)

temp_dir = Path('/tmp/')
my_dir = temp_dir / 'cucumbers'
print(my_dir.exists())
my_dir.mkdir()
# my_dir.mkdir()  # FileExistsError тому що директорія вже існує
my_dir.mkdir(exist_ok=True)  # ніяких помилок якщо директорія вже існує
print(my_dir.exists())

my_dir = my_dir.rename(temp_dir / 'big_cucumbers')
print(my_dir)
print(my_dir.exists())

my_dir.rmdir()
print(my_dir.exists())

cucumbers_dir = temp_dir / 'storage' / 'cucumbers' / 'big'
print(cucumbers_dir.parent.exists())
cucumbers_dir.mkdir(parents=True)  # створити всі директорії яки наявні у шляху
for parent in cucumbers_dir.parents:
    print(parent, parent.exists())

# cucumbers_dir.parent.rmdir()  # помилка, бо директорія не пуста
cucumbers_dir.rmdir()
cucumbers_dir.parent.rmdir()  # тепер добре
cucumbers_dir.parents[1]  # підчищаємо

for parent in cucumbers_dir.parents:
    print(parent, parent.exists())

    
print(list(current_dir.iterdir()))  # aka list directory

for path in current_dir.iterdir():
    if path.is_dir():
        print(path, 'is a directory')
    elif path.is_file():
        print(path, 'is a file')
    else:
        print('What are you? 😱')
