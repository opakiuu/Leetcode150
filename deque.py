from collections import deque

# Create a queue
my_queue = deque()

# Enqueue (add items to the back)
my_queue.append('a')
my_queue.append('b')
my_queue.append('c')
print(f"Queue after adding items: {my_queue}")

# Dequeue (remove items from the front)
front_item = my_queue.popleft()
print(f"Removed item: {front_item}")
print(f"Queue after removing an item: {my_queue}")

# Peek (view the front item without removing it)
if my_queue:
    peek_item = my_queue[0]
    print(f"Front item (peek): {peek_item}")

# Check if empty
print(f"Is the queue empty? {not bool(my_queue)}")
