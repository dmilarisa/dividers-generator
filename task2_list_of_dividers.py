from time import time
from multiprocessing import cpu_count, Pool


# standard implementation, for using without processes
def factorize(*number):
    res = []
    for n in number:
        res.append([i + 1 for i in range(n) if n % (i + 1) == 0])
    return res


# function-worker for the processes
def factorize_one_number(n):
    return [i + 1 for i in range(n) if n % (i + 1) == 0]


# function which uses processes for the building of lists of numbers
def factorize_processes(*number):
    with Pool(processes=cpu_count()) as pool:
        return pool.map(factorize_one_number, number)


if __name__ == '__main__':
    # Test the standard function
    start = time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]
    end = time()
    print(f"Time for the work of factorize like a function without processes is {end - start} seconds")

    start1 = time()
    a, b, c, d = factorize_processes(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]
    end1 = time()
    print(f"Time for the work of factorize_processes is {end1 - start1} seconds")
