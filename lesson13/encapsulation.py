class Car:
    def __init__(self):
        self.__key = '🔑'  # private атрибут. Доступний лише в межах цього ж класу

    def __check_key(self, key):  # private метод. Доступний лише в межах цього ж класу
        assert key == self.__key, 'Wrong key'

    def _connect_battery(self):  # protected метод. Доступний в межах цього ж класу та всіх нащадків
        print('Connecting battery')

    def _connect_starter(self):
        print('Connecting starter')

    def _inject_fuel(self):
        print('Injecting fuel')

    def _ignite_fuel(self):
        print('Igniting fuel')

    def start_engine(self, key):
        self.__check_key(key)

        self._connect_battery()
        self._connect_starter()
        self._inject_fuel()
        self._ignite_fuel()

        print('Car is ready to go!')


class ElectricCar(Car):
    def _load_AI(self):
        print('Loading AI')

    def start_engine(self, key):
        # self.__check_key(key)  # приватний метод не можна викликати з дочірнього классу
        self._connect_battery()  # захищений метод можна викликати з дочірнього классу
        self._load_AI()
        print('Car is ready to go!')


if __name__ == '__main__':
    my_car = Car()
    my_car.start_engine('🔑')
    
    my_car = ElectricCar()
    my_car.start_engine('🔑')

    # protected метод все ще можна викликати поза класом
    my_car._connect_starter()  # Але _ на початку каже нам що робити так не треба

    # private метод не можна викликати, так само, не можна отримати доступ до таких атрибутів
    # print(my_car.__key)

