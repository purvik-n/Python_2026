"""
==========================================================
  Python DS & Algorithms — Day 2: Stack & Queue
  Author  : Purvik
  Date    : 2026-03-14
  Topic   : Stack (LIFO) and Queue (FIFO) from scratch
==========================================================
"""

from collections import deque


# ──────────────────────────────────────────────
#  STACK  (Last In, First Out)
# ──────────────────────────────────────────────
class Stack:
    """
    Stack implementation using a Python list.
    Operations:  push O(1)  |  pop O(1)  |  peek O(1)
    """

    def __init__(self):
        self._data = []

    def push(self, item):
        """Push item onto the top of the stack."""
        self._data.append(item)

    def pop(self):
        """Remove and return the top item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"Stack(top -> {self._data[::-1]})"


# Real-world stack use case: balanced parentheses checker
def is_balanced(expression: str) -> bool:
    """Check if brackets in expression are balanced."""
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in expression:
        if ch in '([{':
            stack.push(ch)
        elif ch in ')]}':
            if stack.is_empty() or stack.pop() != pairs[ch]:
                return False
    return stack.is_empty()


# Real-world stack use case: reverse a string
def reverse_string(s: str) -> str:
    stack = Stack()
    for ch in s:
        stack.push(ch)
    return ''.join(stack.pop() for _ in range(len(stack)))


# ──────────────────────────────────────────────
#  QUEUE  (First In, First Out)
# ──────────────────────────────────────────────
class Queue:
    """
    Queue implementation using collections.deque for O(1) enqueue & dequeue.
    """

    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        """Add item to the rear of the queue."""
        self._data.append(item)

    def dequeue(self):
        """Remove and return the front item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def front(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._data[0]

    def rear(self):
        """Return the rear item without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"Queue(front -> {list(self._data)} <- rear)"


# ──────────────────────────────────────────────
#  PRIORITY QUEUE  (min-heap based)
# ──────────────────────────────────────────────
import heapq

class PriorityQueue:
    """
    Min-priority queue: item with smallest priority value dequeues first.
    """

    def __init__(self):
        self._heap = []
        self._counter = 0      # tie-breaker for equal priorities

    def enqueue(self, item, priority: int):
        heapq.heappush(self._heap, (priority, self._counter, item))
        self._counter += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty priority queue")
        _, _, item = heapq.heappop(self._heap)
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty priority queue")
        return self._heap[0][2]

    def is_empty(self):
        return len(self._heap) == 0

    def __len__(self):
        return len(self._heap)

    def __repr__(self):
        items = [(p, i) for p, _, i in sorted(self._heap)]
        return f"PriorityQueue({items})"


# ──────────────────────────────────────────────
#  DEMO
# ──────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 50)
    print("  STACK DEMO")
    print("=" * 50)

    s = Stack()
    for v in [10, 20, 30, 40]:
        s.push(v)
    print(s)
    print(f"Peek     : {s.peek()}")
    print(f"Pop      : {s.pop()}")
    print(f"After pop: {s}")
    print(f"Balanced '{{[()]}}': {is_balanced('{[()]}')}")
    print(f"Balanced '([)]'   : {is_balanced('([)]')}")
    print(f"Reversed 'Python' : {reverse_string('Python')}")

    print()
    print("=" * 50)
    print("  QUEUE DEMO")
    print("=" * 50)
    q = Queue()
    for v in ["Alice", "Bob", "Charlie", "Diana"]:
        q.enqueue(v)
    print(q)
    print(f"Front      : {q.front()}")
    print(f"Dequeue    : {q.dequeue()}")
    print(f"After deq  : {q}")

    print()
    print("=" * 50)
    print("  PRIORITY QUEUE DEMO")
    print("=" * 50)
    pq = PriorityQueue()
    pq.enqueue("low task", 10)
    pq.enqueue("critical task", 1)
    pq.enqueue("medium task", 5)
    pq.enqueue("urgent task", 2)
    print("Dequeuing by priority:")
    while not pq.is_empty():
        print(f"  -> {pq.dequeue()}")
