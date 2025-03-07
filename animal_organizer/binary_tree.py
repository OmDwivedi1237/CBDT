class TreeNode:
    def __init__(self, animal):
        self.animal = animal
        self.left = None
        self.right = None

class AnimalTree:
    def __init__(self):
        self.root = None

    def insert(self, animal):
        """Inserts a new animal into the tree."""
        if self.root is None:
            self.root = TreeNode(animal)
        else:
            self._insert_recursive(self.root, animal)

    def _insert_recursive(self, node, animal):
        if animal.name < node.animal.name:
            if node.left is None:
                node.left = TreeNode(animal)
            else:
                self._insert_recursive(node.left, animal)
        else:
            if node.right is None:
                node.right = TreeNode(animal)
            else:
                self._insert_recursive(node.right, animal)

    def search(self, name):
        """Searches for an animal by name."""
        return self._search_recursive(self.root, name)

    def _search_recursive(self, node, name):
        if node is None:
            return None
        if name == node.animal.name:
            return node.animal
        elif name < node.animal.name:
            return self._search_recursive(node.left, name)
        else:
            return self._search_recursive(node.right, name)

    def remove(self, name):
        """Removes an animal by name."""
        self.root = self._remove_recursive(self.root, name)

    def _remove_recursive(self, node, name):
        if node is None:
            return node

        if name < node.animal.name:
            node.left = self._remove_recursive(node.left, name)
        elif name > node.animal.name:
            node.right = self._remove_recursive(node.right, name)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_larger_node = self._get_min(node.right)
            node.animal = min_larger_node.animal
            node.right = self._remove_recursive(node.right, min_larger_node.animal.name)

        return node

    def _get_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def display(self):
        """Displays the tree using in-order traversal."""
        self._in_order_traversal(self.root)

    def _in_order_traversal(self, node):
        if node:
            self._in_order_traversal(node.left)
            print(f"{node.animal.name} - {node.animal.species} ({node.animal.animal_type})")
            self._in_order_traversal(node.right)
