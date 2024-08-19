import threading
import time

# Define a simple function that each thread will run
def func_name(thread_id):
    print(f"Thread {thread_id} is starting.")
    time.sleep(2)  # Simulate some work with sleep
    print(f"Thread {thread_id} is finishing.")

# Create and start multiple threads
threads = []
for i in range(10):
    th = threading.Thread(target=func_name, args=(i,))
    th.start()
    threads.append(th)

# Print the total number of active threads
print(f"Total active threads: {threading.active_count()}")

# Wait for all threads to complete
for th in threads:
    th.join()
print(f"Total active threads: {threading.active_count()}")
print("All threads have finished.")
