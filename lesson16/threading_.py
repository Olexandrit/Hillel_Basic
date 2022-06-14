import threading
import time


def first_sleeper():
    print('Sleeping for next 5 seconds 😴')
    time.sleep(5)
    print('I slept well for this 5 seconds')


def second_sleeper():
    print('Sleeping for next 2 seconds 😴')
    time.sleep(2)
    print('I slept well for this 2 seconds')


first_sleeper()
second_sleeper()


first_thread = threading.Thread(target=first_sleeper)
second_thread = threading.Thread(target=second_sleeper)
first_thread.start()
second_thread.start()


# ---


import threading
import time


def sleeper(duration):
    print(f'Sleeping for next {duration} seconds 😴')
    time.sleep(duration)
    print(f'I slept well for this {duration} seconds')


first_thread = threading.Thread(target=sleeper, args=(5,))
second_thread = threading.Thread(target=sleeper, args=(3,))
first_thread.start()
second_thread.start()
print('Sleepers are done sleeping')
first_thread.join()
second_thread.join()
print('Sleepers are done sleeping')


# ---


import threading
import random

import requests


def request_some_important_data(number):
    delay = random.randint(1, 10)
    print(f'Requesting very important data #{number} from server')
    requests.get(f'https://httpbin.org/delay/{delay}')
    print(f'Very important data #{number} received')


for i in range(1, 11):
    thread = threading.Thread(target=request_some_important_data, args=(i,))
    thread.start()


with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(request_some_important_data, range(1, 11))
