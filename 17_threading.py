import time
import threading

def task(task_idx, pause):
    print(f"Starting task {task_idx}")
    for i in range(pause):
        print(f"Task #{task_idx} halted for {pause-i}s")
        time.sleep(1)
    print(f"Ending task {task_idx}")

t1 = threading.Thread(target=task, args=(1, 5))
t2 = threading.Thread(target=task, args=(2, 3))

print("Making threads...")
t1.start()
t2.start()

print("Waiting for threads to end...")
t1.join()
t2.join()