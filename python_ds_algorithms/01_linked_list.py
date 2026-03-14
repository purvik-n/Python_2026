"""
==========================================================
  Python DS & Algorithms — Day 1: Linked List
  Author  : Purvik
  Date    : 2026-03-14
  Topic   : Singly & Doubly Linked Lists from scratch
==========================================================
"""

# ──────────────────────────────────────────────
#  NODE
# ──────────────────────────────────────────────
class Node:
    """A single node that holds data and a pointer to the next node."""
    def __init__(self, data):
        self.data = data
        self.next = None   # pointer to next node
        self.prev = None   # pointer to previous node (for doubly linked list)

    def __repr__(self):
        return f"Node({self.data})"


# ──────────────────────────────────────────────
#  SINGLY LINKED LIST
# ──────────────────────────────────────────────
class SinglyLinkedList:
    """Singly Linked List – each node points only to next."""

    def __init__(self):
        self.head = None
        self.size = 0

    # ── Insert ──────────────────────────────
    def prepend(self, data):
        """O(1) – insert at beginning."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def append(self, data):
        """O(n) – insert at end."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def insert_at(self, index, data):
        """O(n) – insert at a specific index."""
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if index == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    # ── Delete ──────────────────────────────
    def delete(self, data):
        """O(n) – delete first occurrence of data."""
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next
            self.size -= 1

    # ── Search ──────────────────────────────
    def search(self, data):
        """O(n) – return index of data or -1 if not found."""
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    # ── Reverse ─────────────────────────────
    def reverse(self):
        """O(n) – reverse the list in-place."""
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    # ── Detect Cycle ────────────────────────
    def has_cycle(self):
        """O(n) – Floyd's tortoise-and-hare algorithm."""
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    # ── Helpers ─────────────────────────────
    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __len__(self):
        return self.size

    def __repr__(self):
        return " -> ".join(str(v) for v in self.to_list()) + " -> None"


# ──────────────────────────────────────────────
#  DOUBLY LINKED LIST
# ──────────────────────────────────────────────
class DoublyLinkedList:
    """Doubly Linked List – each node has prev & next pointers."""

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        """O(1) – insert at end."""
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, data):
        """O(1) – insert at beginning."""
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def delete(self, data):
        """O(n) – delete first occurrence of data."""
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self.size -= 1
                return
            current = current.next

    def to_list_forward(self):
        result, current = [], self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def to_list_backward(self):
        result, current = [], self.tail
        while current:
            result.append(current.data)
            current = current.prev
        return result

    def __len__(self):
        return self.size

    def __repr__(self):
        return "None <-> " + " <-> ".join(str(v) for v in self.to_list_forward()) + " <-> None"


# ──────────────────────────────────────────────
#  DEMO
# ──────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 50)
    print("  SINGLY LINKED LIST DEMO")
    print("=" * 50)

    sll = SinglyLinkedList()
    for val in [10, 20, 30, 40, 50]:
        sll.append(val)
    print(f"List          : {sll}")
    print(f"Size          : {len(sll)}")
    print(f"Search 30     : index {sll.search(30)}")
    sll.prepend(5)
    print(f"After prepend5: {sll}")
    sll.insert_at(3, 25)
    print(f"Insert 25 @3  : {sll}")
    sll.delete(25)
    print(f"Delete 25     : {sll}")
    sll.reverse()
    print(f"Reversed      : {sll}")
    print(f"Has cycle?    : {sll.has_cycle()}")

    print()
    print("=" * 50)
    print("  DOUBLY LINKED LIST DEMO")
    print("=" * 50)

    dll = DoublyLinkedList()
    for val in [100, 200, 300, 400]:
        dll.append(val)
    dll.prepend(50)
    print(f"DLL            : {dll}")
    print(f"Forward        : {dll.to_list_forward()}")
    print(f"Backward       : {dll.to_list_backward()}")
    dll.delete(200)
    print(f"After del 200  : {dll}")
    print(f"Size           : {len(dll)}")
