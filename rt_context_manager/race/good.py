# race/good.py
from pathlib import Path
import time
import threading

file_lock = threading.Lock()

def accumulate(thread_id):
    path = Path("account.txt")
    for _ in range(5):
        with file_lock:
            with path.open() as f:
                balance = int(f.read())
                print(f"id={thread_id} Read", balance)
                balance += 1

            with path.open(mode="w") as f:
                f.write(str(balance))
                print(f"id={thread_id} Wrote", balance)

        time.sleep(0.01)

threads = []
for index in range(2):
    thread = threading.Thread(target=accumulate, args=(index, ))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
