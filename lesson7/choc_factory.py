
cocoa = 'cocoa beans'
sugar = ['sugar', 'sugar', 'sugar', 'sugar', 'sugar', 'sugar']


def grind(beans):
    return 'grinded ' + beans


def weight(pack):
    if isinstance(pack, list):
        return pack.pop(0)
    else:
        return pack


def mix(ingridient_a, ingridient_b):
    return ingridient_a + ' and ' + ingridient_b


def mold(mixture):
    return 'brick of ' + mixture


def mix_and_mold(ingridient_a, ingridient_b):
    return mold(mix(ingridient_a, ingridient_b))


def wrap(chocolate):
    return 'wrapped ' + chocolate


coffee = 'coffee beans'
milk = ['milk', 'milk', 'milk']

# conveyor_a = cocoa
conveyor_a = coffee
conveyor_b = sugar
conveyor_c = milk

conveyor_a = grind(conveyor_a)
conveyor_b = weight('sugar')
conveyor_c = weight(conveyor_c)

conveyor_z = mix(mix(conveyor_a, conveyor_b), conveyor_c)

conveyor_z = wrap(conveyor_z)

print(conveyor_z)