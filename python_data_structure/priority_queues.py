import heapq

# Create an empty heap
heap = []

# Add elements to the heap with priority
heapq.heappush(heap, (10, "Ten"))
heapq.heappush(heap, (1, "One"))
heapq.heappush(heap, (5, "Five"))

# Print the heap
print("Heap:", heap)

# Pop the smallest element from the heap
smallest = heapq.heappop(heap)
print("Smallest element:", smallest)  # Return 1

# Pop the smallest element again
smallest = heapq.heappop(heap)
print("Smallest element:", smallest)  # Returns 5

# Pop the smallest element again
smallest = heapq.heappop(heap)
print("Smallest element:", smallest)  # Returns 10
