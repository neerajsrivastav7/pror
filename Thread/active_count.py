import threading
import time

def worker():
    time.sleep(2)

# Create multiple threads
threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

# Print the number of active threads
print("Active threads count before join:", threading.active_count())

# Wait for all threads to complete
for t in threads:
    t.join()

# Print the number of active threads after join
print("Active threads count after join:", threading.active_count())

'''
Active threads count before join: 6
Active threads count after join: 1
'''