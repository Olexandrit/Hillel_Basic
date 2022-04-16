
string_cucumber = input("Введіть фразу зі словом cucumber \U0001F923: ")

str_find = "cucumber"

len_cucumber = len(str_find)

index_cucumber = string_cucumber.find(str_find)

if index_cucumber == -1:
    print(str_find, "не знайдено ", "\U0001f600")
else:
    print(string_cucumber[index_cucumber+len_cucumber:len(string_cucumber):])
