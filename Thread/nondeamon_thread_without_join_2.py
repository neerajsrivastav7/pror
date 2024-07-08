import threading
import time

def non_daemon_task():
    for i in range(5):
        print(f"Non-daemon task iteration {i+1}")
        time.sleep(1)
    print("Non-daemon task completed.")

# Create a non-daemon thread
non_daemon_thread = threading.Thread(target=non_daemon_task)

# Start the thread
non_daemon_thread.start()

# The main program will continue to run and will not wait for the non-daemon thread explicitly.
print("Main program is running...")

# The main program won't exit until the non-daemon thread has finished.
print("Main program has finished execution.")
