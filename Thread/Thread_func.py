import threading as th

print(dir(th))

Result 

# Method Use in Thread
# ['Barrier', 'BoundedSemaphore', 'BrokenBarrierError', 'Condition', 'Event', 'ExceptHookArgs', 
# 'Lock', 'RLock', 'Semaphore', 'TIMEOUT_MAX', 'Thread', 'ThreadError', 'Timer', 'WeakSet', 
# '_CRLock', '_DummyThread', '_HAVE_THREAD_NATIVE_ID', '_MainThread', '_PyRLock', '_RLock', 
# '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__',
#  '__spec__', '_active', '_active_limbo_lock', '_after_fork', '_allocate_lock', '_count', '_counter',
#   '_dangling', '_deque', '_enumerate', '_islice', '_limbo', '_main_thread', '_make_invoke_excepthook', 
#   '_newname', '_os', '_profile_hook', '_set_sentinel', '_shutdown', '_shutdown_locks', 
#   '_shutdown_locks_lock', '_start_new_thread', '_sys', '_time', '_trace_hook', 'activeCount', 
#   'active_count', 'currentThread', 'current_thread', 'enumerate', 'excepthook', 'get_ident', 
#   'get_native_id', 'local', 'main_thread', 'setprofile', 'settrace', 'stack_size']