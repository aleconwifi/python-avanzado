from threading import Thread
import os 
import time

def square_numbers():
    for i in range(200):
        i*i
        time.sleep(0.1)


threads = []
num_threads = 10

if __name__ == '__main__':
    
    for i in range(num_threads):
        p = Thread(target=square_numbers)
        threads.append(p)

    for p in threads:
        p.start()

    for p in threads:
        p.join()

    print('end')
