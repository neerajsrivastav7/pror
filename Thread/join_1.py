import threading
import time

def worker():
    print("Worker thread starting")
    time.sleep(2)
    print("Worker thread finished")

# Create a new thread
thread = threading.Thread(target=worker)

# Start the thread
thread.start()

# Wait for the thread to complete
thread.join()

print("Main thread continues after worker thread has finished")
