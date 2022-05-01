import time


print(time.time())  # timestamp
print(1970 + time.time() / 60 / 60 / 24 / 365)

print('Hi')
start = time.time()
time.sleep(5)
slept = time.time() - start
print(f'I slept {slept}s')