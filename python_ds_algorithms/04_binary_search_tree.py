"""
==========================================================
  Python DS & Algorithms — Day 4: Binary Search Tree (BST)
  Author  : Purvik
  Date    : 2026-03-14
  Topic   : BST insert, search, delete, traversals, height
==========================================================
"""


# ──────────────────────────────────────────────
#  BST NODE
# ──────────────────────────────────────────────
class BSTNode:
    def __init__(self, key):
        self.key   = key
        self.left  = None
        self.right = None

    def __repr__(self):
        return f"BSTNode({self.key})"


# ──────────────────────────────────────────────
#  BINARY SEARCH TREE
# ──────────────────────────────────────────────
class BinarySearchTree:
    """
    BST where left.key < root.key < right.key.
    Average-case O(log n) for search / insert / delete.
    Worst-case O(n) for skewed tree.
    """

    def __init__(self):
        self.root = None

    # ── Insert ──────────────────────────────
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        # duplicate keys are ignored
        return node

    # ── Search ──────────────────────────────
    def search(self, key) -> bool:
        return self._search(self.root, key)

    def _search(self, node, key) -> bool:
        if node is None:
            return False
        if key == node.key:
            return True
        return self._search(node.left if key < node.key else node.right, key)

    # ── Delete ──────────────────────────────
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Node to delete found
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Node has two children: replace with in-order successor
            successor = self._min_node(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)
        return node

    def _min_node(self, node):
        while node.left:
            node = node.left
        return node

    # ── Traversals ──────────────────────────
    def inorder(self) -> list:
        """Left → Root → Right  (gives sorted order for BST)."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

    def preorder(self) -> list:
        """Root → Left → Right."""
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(node.key)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder(self) -> list:
        """Left → Right → Root."""
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.key)

    def level_order(self) -> list:
        """Breadth-first traversal using a queue."""
        if not self.root:
            return []
        from collections import deque
        result, queue = [], deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.key)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        return result

    # ── Height & Size ───────────────────────
    def height(self) -> int:
        return self._height(self.root)

    def _height(self, node) -> int:
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def size(self) -> int:
        return self._size(self.root)

    def _size(self, node) -> int:
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

    # ── Validation ──────────────────────────
    def is_valid_bst(self) -> bool:
        return self._is_valid(self.root, float('-inf'), float('inf'))

    def _is_valid(self, node, min_val, max_val) -> bool:
        if node is None:
            return True
        if not (min_val < node.key < max_val):
            return False
        return (self._is_valid(node.left, min_val, node.key) and
                self._is_valid(node.right, node.key, max_val))

    # ── Min / Max ───────────────────────────
    def minimum(self):
        if not self.root:
            return None
        return self._min_node(self.root).key

    def maximum(self):
        if not self.root:
            return None
        node = self.root
        while node.right:
            node = node.right
        return node.key


# ──────────────────────────────────────────────
#  DEMO
# ──────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 50)
    print("  BINARY SEARCH TREE DEMO")
    print("=" * 50)

    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
    for v in values:
        bst.insert(v)

    print(f"Inserted       : {values}")
    print(f"In-order       : {bst.inorder()}  ← sorted!")
    print(f"Pre-order      : {bst.preorder()}")
    print(f"Post-order     : {bst.postorder()}")
    print(f"Level-order    : {bst.level_order()}")
    print(f"Height         : {bst.height()}")
    print(f"Size           : {bst.size()}")
    print(f"Min            : {bst.minimum()}")
    print(f"Max            : {bst.maximum()}")
    print(f"Search 40      : {bst.search(40)}")
    print(f"Search 99      : {bst.search(99)}")
    print(f"Valid BST?     : {bst.is_valid_bst()}")

    bst.delete(30)
    print(f"\nAfter delete 30: {bst.inorder()}")
    bst.delete(50)
    print(f"After delete 50: {bst.inorder()}")
    print(f"Still valid BST: {bst.is_valid_bst()}")
