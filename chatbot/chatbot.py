from chatbot.interface import ChatbotInterface
from chatbot.decision_tree import DecisionTree

class Chatbot(ChatbotInterface):
    def __init__(self):
        self.tree = DecisionTree()

    def start(self):
        current = self.tree.root
        while current.yes and current.no:
            response = input(current.question + " (yes/no): ").strip().lower()
            if response == "yes":
                current = current.yes
            elif response == "no":
                current = current.no
            else:
                print("Invalid response. Type 'yes' or 'no'.")

        print(f"Chatbot: {current.question}")
        learn = input("Teach me a better response? (yes/no): ").strip().lower()
        if learn == "yes":
            new_question = input("What question should I ask instead? ")
            yes_answer = input("What if they say 'yes'? ")
            no_answer = input("What if they say 'no'? ")
            self.tree.insert(current, new_question, yes_answer, no_answer)
            self.tree.save_tree()
            print("Thanks! I learned something new.")

    def view_tree(self):
        print("\n=== Decision Tree Traversal ===")
        print("1. Preorder")
        print("2. Inorder")
        print("3. Postorder")
        choice = input("Choose (1/2/3): ").strip()

        if choice == "1":
            print("Preorder:", self.tree.traverse("preorder"))
        elif choice == "2":
            print("Inorder:", self.tree.traverse("inorder"))
        elif choice == "3":
            print("Postorder:", self.tree.traverse("postorder"))
        else:
            print("Invalid choice.")
