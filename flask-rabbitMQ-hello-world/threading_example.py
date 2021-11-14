import os
import threading


def print_cube(num):
    cube = num * num * num
    print(f'Cube: {cube}')
    print('Xxxxxxx')
    print(threading.current_thread().name)
    print(os.getpid())


def print_square(num):
    square = num * num
    print(f'Square: {square}')
    print(threading.current_thread().name)
    print(os.getpid())


if __name__ == '__main__':
    t1 = threading.Thread(target=print_square(10))
    t2 = threading.Thread(target=print_cube(10))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('Done')