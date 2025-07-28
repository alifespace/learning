import threading
import time
def worker():
    print(f"Worker started: {threading.current_thread().name}\n")
    time.sleep(3)
    print(f"Worker finished: {threading.current_thread().name}\n")

thread1 = threading.Thread(target=worker, name="Thread1")
thread2 = threading.Thread(target=worker, name="Thread2")
thread3 = threading.Thread(target=worker, name="Thread3")
thread1.start()
thread1.join()
thread2.start()
thread3.start()
print("Main thread ends")