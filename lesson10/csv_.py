
import csv


# Reading CSV
with open('cars.csv') as csvfile:
    cars_reader = csv.reader(csvfile)
    print(cars_reader)
    for row in cars_reader:
        print(row)

        
with open('cars.csv') as csvfile:
    cars_reader = csv.reader(csvfile)
    for row_n, row in enumerate(cars_reader):
        if row_n == 0:  # пропускаємо рядок із заголовком
            continue
        print('{} owns {} {}, year {}. VIN code: {}'.format(*row))
        

MSG_TEMPLATE = '{owner_name} owns {car_brand} {car_model}, year {car_year}. VIN code: {car_vin}'
MSG_TEMPLATE = '{car_brand} {car_model} owned by {owner_name}. VIN code: {car_vin}'
with open('cars.csv') as csvfile:
    cars_reader = csv.DictReader(csvfile)
    for row in cars_reader:
        print(MSG_TEMPLATE.format(**row))


# Writing CSV
from utils import generate_cucumber


with open('cucumbers.csv', 'w') as csvfile:
    cucumbers_writer = csv.writer(csvfile)
    cucumbers_writer.writerow(['cucumber', 'another_cucumber', 'one_more', 'and_again'])
    for _ in range(10):
        cucumbers_writer.writerow([generate_cucumber() for _ in range(4)])
        
        
fruits_data = [
    {
        'icon': '🍏',
        'name': 'Apple',
    },
    {
        'icon': '🍓',
        'name': 'Strawberry',
    },
    {
        'icon': '🍑',
        'name': 'Peach',
    },
    {
        'icon': '🍌',
        'name': 'Banana',
    },
    {
        'icon': '🍊',
        'name': 'Orange',
        # 'size': 'medium',
    },
]

with open('fruits.csv', 'w') as csvfile:
    fruits_writer = csv.DictWriter(csvfile, fieldnames=fruits_data[0].keys())
    
    fruits_writer.writeheader()
    for fruit in fruits_data:
        fruits_writer.writerow(fruit)
