import threading
import time

def worker():
    print("Worker thread starting")
    time.sleep(5)
    print("Worker thread finished")

# Create a new thread
thread = threading.Thread(target=worker)

# Start the thread
thread.start()

# Wait for the thread to complete with a timeout of 2 seconds
thread.join(timeout=2)

if thread.is_alive():
    print("Worker thread is still running after timeout")
else:
    print("Worker thread has finished")

print("Main thread continues")

# This line marks the end of the main thread
print("Main thread finished")

# The program will not terminate until the worker thread (non-daemon) has finished

'''
Worker thread starting
Worker thread is still running after timeout
Main thread continues
Main thread finished
Worker thread finished

'''