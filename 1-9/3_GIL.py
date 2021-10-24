import random
import threading
import time


def working():
    # 10000000개의 랜덤 숫자를 생성한 후, 그 중에서 최대값을 찾는다.
    max([random.random() for i in range(10000000)])


def sleep_working():
    time.sleep(0.1)
    max([random.random() for i in range(100000)])
    time.sleep(0.1)
    max([random.random() for i in range(100000)])
    time.sleep(0.1)
    max([random.random() for i in range(100000)])
    time.sleep(0.1)
    max([random.random() for i in range(100000)])
    time.sleep(0.1)
    max([random.random() for i in range(100000)])
    time.sleep(0.1)


if __name__ == '__main__':
    print("\n 1. 단일 쓰레드 작업 완료 시간")
    print("\n 2. 멀티 쓰레드 작업 완료 시간")
    print("\n 3. 단일 & 멀티 쓰레드 (1) 작업 완료 시간")
    print("\n 4. 단일 & 멀티 쓰레드 (2) 작업 완료 시간")
    select = input("\n선택 : ")

    if select == "1":  # 단일 쓰레드
        s_time = time.time()
        working()
        working()
        e_time = time.time()
        print("Thread-1 : ", f'{e_time - s_time:.5f}')
    elif select == "2":  # 멀티 쓰레드
        s_time = time.time()
        threads = []
        for i in range(2):
            threads.append(threading.Thread(target=working))
            threads[-1].start()

        for t in threads:
            t.join()

        e_time = time.time()
        print("Thread-2 : ", f'{e_time - s_time:.5f}')
    elif select == "3":  # 단일 & 멀티 쓰레드
        # 단일 쓰레드
        s_time = time.time()
        working()
        working()
        e_time = time.time()
        print("Thread-1 : ", f'{e_time - s_time:.5f}')

        # 멀티 쓰레드
        s_time = time.time()
        threads = []
        for i in range(2):
            threads.append(threading.Thread(target=working))
            threads[-1].start()

        for t in threads:
            t.join()

        e_time = time.time()
        print("Thread-2 : ", f'{e_time - s_time:.5f}')
    elif select == "4":  # 단일 & 멀티 쓰레드
        # 단일 쓰레드
        s_time = time.time()
        sleep_working()
        sleep_working()
        e_time = time.time()
        print("Thread-1 : ", f'{e_time - s_time:.5f}')

        # 멀티 쓰레드
        s_time = time.time()
        threads = []
        for i in range(2):
            threads.append(threading.Thread(target=sleep_working))
            threads[-1].start()

        for t in threads:
            t.join()

        e_time = time.time()
        print("Thread-2 : ", f'{e_time - s_time:.5f}')
    else:
        input("\n올바른 값을 입력해주세요")
