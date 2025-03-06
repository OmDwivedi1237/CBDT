import tkinter as tk
from tkinter import messagebox
from chatbot.decision_tree import DecisionTree  # Assuming the correct path is chatbot.decision_tree

class ChatbotGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Chatbot")
        self.tree = DecisionTree()
        self.current_node = self.tree.root
        self.setup_ui()
        self.root.mainloop()

    def setup_ui(self):
        self.conversation_text = tk.Text(self.root, height=20, width=60)
        self.conversation_text.pack()
        self.user_input = tk.Entry(self.root, width=60)
        self.user_input.pack()
        self.user_input.bind("<Return>", self.send_message)  # Binding Enter key to send_message
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack()

    def send_message(self, event=None):
        user_input = self.user_input.get().strip()
        self.conversation_text.insert(tk.END, f"You: {user_input}\n")
        if user_input.lower() == 'exit':
            self.conversation_text.insert(tk.END, "Chatbot: Goodbye!\n")
            self.root.quit()
        else:
            response = self.generate_response(user_input)
            self.conversation_text.insert(tk.END, f"Chatbot: {response}\n")
        self.user_input.delete(0, tk.END)

    def generate_response(self, user_input):
        # This is a simple implementation; you might want to use NLP for better response generation
        return self.tree.get_response(user_input)  # Assuming DecisionTree has a get_response method

if __name__ == "__main__":
    gui = ChatbotGUI()
