import threading
import time

def worker():
    print(f"Worker thread {threading.current_thread().name} starting.")
    time.sleep(2)
    print(f"Worker thread {threading.current_thread().name} ending.")

# Creating a daemon thread
daemon_thread = threading.Thread(target=worker, name="DaemonWorker")
daemon_thread.setDaemon(True)

# Creating non-daemon threads
threads = []
for i in range(3):
    t = threading.Thread(target=worker, name=f"Worker-{i+1}")
    t.start()
    threads.append(t)

# Start the daemon thread
daemon_thread.start()

# Print the number of active threads
print("Active threads count:", threading.active_count())

# Wait for non-daemon threads to complete
for t in threads:
    t.join()

# Print the number of active threads after non-daemon threads complete
print("Active threads count after non-daemon threads joined:", threading.active_count())


'''
Worker thread Worker-1 starting.
Worker thread Worker-2 starting.
Worker thread Worker-3 starting.
Worker thread DaemonWorker starting.
Active threads count: 5
Worker thread Worker-1 ending.
Worker thread Worker-2 ending.
Worker thread Worker-3 ending.
Worker thread DaemonWorker ending.
Active threads count after non-daemon threads joined: 1
'''