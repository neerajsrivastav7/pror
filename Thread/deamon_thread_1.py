import threading
import time

def daemon_task():
    while True:
        print("Daemon thread running...")
        time.sleep(1)
    print("Demon Thread is finished")

def non_daemon_task():
    for i in range(5):
        print("Non-daemon thread running...")
        time.sleep(1)
    print("non deamon thread finished its Execution")

# Create a daemon thread
daemon_thread = threading.Thread(target=daemon_task, daemon=True)

# Create a non-daemon thread
non_daemon_thread = threading.Thread(target=non_daemon_task)

# Start both threads
daemon_thread.start()
non_daemon_thread.start()

# Wait for the non-daemon thread to complete
non_daemon_thread.join()

print("Main program has finished execution.")
