import threading
import time
import random

def producer_consumer():
    buffer = []
    capacity = 5
    mutex = threading.Semaphore(1)
    empty = threading.Semaphore(capacity)
    full = threading.Semaphore(0)
    item_no = 0

    def producer():
        nonlocal item_no
        for i in range(10):
            time.sleep(random.uniform(0.1, 0.5))
            empty.acquire()
            mutex.acquire()
            item_no += 1
            buffer.append(item_no)
            print(f"Producer produced item {item_no} | Buffer: {buffer}")
            mutex.release()
            full.release()

    def consumer():
        for i in range(10):
            time.sleep(random.uniform(0.2, 0.7))
            full.acquire()
            mutex.acquire()
            item = buffer.pop(0)
            print(f"Consumer consumed item {item} | Buffer: {buffer}")
            mutex.release()
            empty.release()

    print("\nProducer-Consumer Problem (Bounded Buffer)\n" + "-"*50)
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Producer-Consumer Completed.\n")

def dining_philosophers():
    forks = [threading.Semaphore(1) for _ in range(5)]
    philosophers = ["P0", "P1", "P2", "P3", "P4"]

    def philosopher(i):
        left = i
        right = (i + 1) % 5
        for _ in range(3):
            print(f"{philosophers[i]} is thinking...")
            time.sleep(random.uniform(0.5, 1.5))
            forks[left].acquire()
            forks[right].acquire()
            print(f"{philosophers[i]} is eating (Forks {left}-{right})")
            time.sleep(random.uniform(0.5, 1))
            forks[left].release()
            forks[right].release()

    print("\nDining Philosophers Problem\n" + "-"*50)
    threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("Dining Philosophers Completed.\n")

def readers_writers():
    read_count = 0
    mutex = threading.Semaphore(1)
    room_empty = threading.Semaphore(1)
    data = "Shared Data: Initial Value"

    def reader(i):
        nonlocal read_count
        for _ in range(2):
            time.sleep(random.uniform(0.3, 0.8))
            mutex.acquire()
            read_count += 1
            if read_count == 1:
                room_empty.acquire()
            mutex.release()

            print(f"Reader {i} is reading: {data} | Active Readers: {read_count}")
            time.sleep(0.5)

            mutex.acquire()
            read_count -= 1
            if read_count == 0:
                room_empty.release()
            mutex.release()

    def writer(i):
        global data
        for j in range(2):
            time.sleep(random.uniform(0.5, 1.2))
            room_empty.acquire()
            data = f"Shared Data: Updated by Writer {i} (v{j+1})"
            print(f"Writer {i} is writing: {data}")
            time.sleep(0.7)
            room_empty.release()

    print("\nReaders-Writers Problem\n" + "-"*50)
    threads = []
    for i in range(3):
        threads.append(threading.Thread(target=reader, args=(i,)))
    for i in range(2):
        threads.append(threading.Thread(target=writer, args=(i,)))

    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("Readers-Writers Completed.\n")

def main():
    while True:
        print("1. Producer-Consumer Problem")
        print("2. Dining Philosophers Problem")
        print("3. Readers-Writers Problem")
        print("4. Exit")
        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            producer_consumer()
        elif choice == '2':
            dining_philosophers()
        elif choice == '3':
            readers_writers()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!\n")

        time.sleep(1)

if __name__ == "__main__":
    main()
