from queue import LifoQueue

stack = LifoQueue(maxsize=3)

stack.put("one")
stack.put("two")
stack.put("three")

# stack.put("four", block=False) # Don't block the process. Raise exception
# stack.put("four", timeout=2) # Don't  block the process. After 2 seconds, raise exception

stack.get()
stack.get()
stack.get()

# stack.get(timeout=1) # Raise empty after 1 second
