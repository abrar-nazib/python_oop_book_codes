from queue import Queue

lineup = Queue(maxsize=3)
# lineup.get(block=False)  # Don't wait for element to arrive, raise exception


lineup.put("one")
lineup.put("two")
lineup.put("three")

# lineup.put("four", timeout=1) # Raises full after 1 second of waiting to be free

print(lineup.full())

print(lineup.get())

print(lineup.get())

print(lineup.get())

print(lineup.empty())
