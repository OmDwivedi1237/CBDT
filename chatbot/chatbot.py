import random
import random
from chatbot.decision_tree import DecisionTree

class Chatbot:
    def __init__(self):
        self.tree = DecisionTree()
        self.current_node = self.tree.root

    def start(self):
        print("Hi! I'm your chatbot. Type 'exit' to end the conversation.")
        while True:
            question = self.current_node['question']
            user_input = input(f"Chatbot: {question} (yes/no): ").strip()
            if user_input.lower() == 'exit':
                print("Chatbot: Goodbye!")
                break
            response = self.traverse_and_learn(user_input)
            if response:
                print(f"Chatbot: {response}")
            else:
                self.learn_from_user(user_input)

    def generate_response(self, user_input):
        # This is a simple implementation; you might want to use NLP for better response generation
        responses = ["That's interesting!", "Can you tell me more?", "I see. What do you think about it?"]
        return random.choice(responses)

    def traverse_and_learn(self, user_input):
        next_question = self.tree.traverse_tree(user_input)
        if next_question:
            return next_question
        return None

    def learn_from_user(self, user_input):
        feedback = input("Chatbot: I didn't quite understand. Can you tell me more about that? (yes/no): ").strip()
        self.tree.learn(user_input, feedback)
        print("Chatbot: Thanks for your input!")

    def reset_tree(self):
        self.tree.reset_tree()

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

    def learn(self):
        current = self.current_node
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
class Chatbot:
    def __init__(self):
        self.tree = DecisionTree()
        self.current_node = self.tree.root

    def start(self):
        print("Hi! I'm your chatbot. Type 'exit' to end the conversation.")
        while True:
            user_input = input("You: ").strip().lower()
            if user_input == 'exit':
                print("Chatbot: Goodbye!")
                break
            elif user_input == 'view tree':
                self.view_tree()
            elif user_input == 'learn':
                self.learn()
            else:
                response = self.generate_response(user_input)
                print(f"Chatbot: {response}")

    def generate_response(self, user_input):
        # This is a simple implementation; you might want to use NLP for better response generation
        responses = ["That's interesting!", "Can you tell me more?", "I see. What do you think about it?"]
        return random.choice(responses)
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

    def learn(self):
        current = self.current_node
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