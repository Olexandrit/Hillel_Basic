import time
from multiprocessing import Process
from threading import Thread


def heavy_func(x):
    return x ** x


if __name__ == '__main__':
    start = time.time()
    for i in range(500_000, 500_000 + 10):
        heavy_func(i)
    end = time.time()

    print(f'Simple loop took: {end - start}s')

    threads = []
    start = time.time()
    for i in range(500_000, 500_000 + 10):
        thread = Thread(target=heavy_func, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    end = time.time()

    print(f'Threading took: {end - start}s')

    processes = []
    start = time.time()
    for i in range(500_000, 500_000 + 10):
        process = Process(target=heavy_func, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    end = time.time()

    print(f'Multiprocessing took: {end - start}s')
