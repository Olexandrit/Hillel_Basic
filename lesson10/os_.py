import os

print(os.cpu_count())  # count of CPU cores

print(os.listdir())  # list directory (old way)
print(list(os.scandir()))  # list directory (modern way)
print(os.getcwd())  # get [c]urrent [w]orking [d]irectory

print(os.path.join('/cucumber/', 'yeah', 'hello/text.txt'))
print(os.path.dirname('pond/ducks/hanry.duck'))
print(os.path.basename('pond/ducks/hanry.duck'))
print(os.path.abspath('pond/ducks/hanry.duck'))
print(os.path.abspath('/pond/ducks/hanry.duck'))

print(os.path.exists('/pond/ducks/hanry.duck'))
print(os.path.exists('/tmp'))

print(os.path.isfile('pond/ducks/hanry.duck'))  # False якщо файл не існує
print(os.path.isdir('pond/ducks/'))  # False якщо директорія не існує
print(os.path.isdir('/tmp'))

print(os.path.exists('here'))
os.mkdir('here')
# os.mkdir('here')  # FileExistsError тому що директорія вже існує
print(os.path.exists('here'))

os.rename('here', 'there')
print(os.path.exists('here'))
print(os.path.exists('there'))

os.rmdir('there')
print(os.path.exists('there'))
