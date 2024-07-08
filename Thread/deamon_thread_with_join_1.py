import threading
import time

def daemon_task():
    for i in range(3):
        print(f"Daemon task iteration {i+1}")
        time.sleep(1)
    print("Daemon task completed.")

def non_daemon_task():
    for i in range(5):
        print(f"Non-daemon task iteration {i+1}")
        time.sleep(1)
    print("Non-daemon task completed.")

# Create a daemon thread
daemon_thread = threading.Thread(target=daemon_task, daemon=True)

# Create a non-daemon thread
non_daemon_thread = threading.Thread(target=non_daemon_task)

# Start both threads
daemon_thread.start()
non_daemon_thread.start()

# Wait for both threads to complete
daemon_thread.join()  # This will wait for the daemon thread to complete
non_daemon_thread.join()  # This will wait for the non-daemon thread to complete

print("Main program has finished execution.")
