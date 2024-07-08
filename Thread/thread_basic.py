import threading

# Define a function for the threads
def print_numbers(name, start, end):
    for i in range(start, end):
        print(f"{name}: {i}")

# Create two threads
thread1 = threading.Thread(target=print_numbers, args=("Thread 1", 1, 6), name="Thread1", daemon=True)
thread2 = threading.Thread(target=print_numbers, args=("Thread 2", 6, 11), name="Thread2", daemon=True)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both threads have finished execution.")
