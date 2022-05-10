# імпорти завжди йдуть на початку та поділяються на 3 категорії, які відокремлюються пустим рядком
# 1. модулі які вбудовані в python (наприклад random, time)
# 2. модулі які були встановлені ззовні (бібліотеки, фреймворки, тощо)
# 3. ваші модулі, ті що є частиною проєкту
from utils_file import extract_cucumber, generate_cucumber
# from utils import *  # так робити не треба, це робить код неявним


texts = (
    'Here is my CuCuMbEr',
    'My cucuMber looks like this',
    'Nothing here',
    'Another usual cucumber',
)


for text in texts:
    cucumber = extract_cucumber(text)
    if cucumber:
        print(cucumber)
        
        
for i in range(10):
    print(generate_cucumber())

# --------- інший спосіб --------------

import utils_file

texts = (
    'Here is my CuCuMbEr',
    'My cucuMber looks like this',
    'Nothing here',
    'Another usual cucumber',
)


for text in texts:
    cucumber = utils_file.extract_cucumber(text)
    if cucumber:
        print(cucumber)
        
        
for _ in range(10):  # _ - коли значення не потрібне
    print(utils_file.generate_cucumber())
    

# ----------- в директоріях ------------

from utils import cucumbers
from utils.cucumbers import generate_cucumber


texts = (
    'Here is my CuCuMbEr',
    'My cucuMber looks like this',
    'Nothing here',
    'Another usual cucumber',
)


for text in texts:
    cucumber = cucumbers.extract_cucumber(text)
    if cucumber:
        print(cucumber)
        
        
for _ in range(10):  # _ - коли значення не потрібне
    print(generate_cucumber())
  
