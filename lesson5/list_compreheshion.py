temperatures = [10, -10, 23, -5, 0, 13, -25, 14, 6, 2, -7, 4]
good_temperatures = []

for temperature in temperatures:
    if temperature > 0:
        good_temperatures.append(temperature)

print(good_temperatures)

print([temp for temp in temperatures if temp > 0])

destinations = ['49003', 'aaaaa', '', '49033', '490490', None, '49050', 'Urkposhta', '49005']
valid_destinations = []

for destination in destinations:
    if destination and destination.isdigit() and len(destination) == 5:
        valid_destinations.append(destination)
    else:
        valid_destinations.append('INVALID')

print(valid_destinations)

print([dest if dest and dest.isdigit() and len(dest) == 5 else 'INVALID' for dest in destinations])