import json

class DecisionTree:
    class Node:
        def __init__(self, question, yes=None, no=None):
            self.question = question
            self.yes = yes
            self.no = no

    def __init__(self, filename="data/tree.json"):
        self.filename = filename
        self.root = self.load_tree()

    def load_tree(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return self._build_tree(data)
        except (FileNotFoundError, json.JSONDecodeError):
            return self.Node("Are you interested in technology?")

    def _build_tree(self, data):
        if isinstance(data, str):
            return self.Node(data)
        return self.Node(
            data["question"],
            self._build_tree(data["yes"]) if "yes" in data else None,
            self._build_tree(data["no"]) if "no" in data else None,
        )

    def save_tree(self):
        def to_dict(node):
            if node is None:
                return None
            return {"question": node.question, "yes": to_dict(node.yes), "no": to_dict(node.no)}

        with open(self.filename, "w") as file:
            json.dump(to_dict(self.root), file, indent=4)

    def insert(self, current_node, question, yes_answer, no_answer):
        if not current_node.yes and not current_node.no:
            current_node.question = question
            current_node.yes = self.Node(yes_answer)
            current_node.no = self.Node(no_answer)
        return current_node

    def traverse(self, order="inorder"):
        def inorder(node):
            return inorder(node.yes) + [node.question] + inorder(node.no) if node else []

        def preorder(node):
            return [node.question] + preorder(node.yes) + preorder(node.no) if node else []

        def postorder(node):
            return postorder(node.yes) + postorder(node.no) + [node.question] if node else []

        if order == "preorder":
            return preorder(self.root)
        elif order == "postorder":
            return postorder(self.root)
        return inorder(self.root)
