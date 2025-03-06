import tkinter as tk
from chatbot.chatbot import Chatbot

class ChatbotGUI:
    def __init__(self):
        self.chatbot = Chatbot()
        self.window = tk.Tk()
        self.window.title("Chatbot")
        self.label = tk.Label(self.window, text="Chatbot: Ask me something!", font=("Arial", 14))
        self.label.pack()

        self.entry = tk.Entry(self.window, width=50)
        self.entry.pack()

        self.send_button = tk.Button(self.window, text="Send", command=self.get_response)
        self.send_button.pack()

        self.tree_button = tk.Button(self.window, text="View Tree", command=self.show_tree)
        self.tree_button.pack()

    def get_response(self):
        user_input = self.entry.get()
        response = self.chatbot.start()
        self.label.config(text=response)
        self.entry.delete(0, tk.END)

    def show_tree(self):
        self.chatbot.view_tree()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = ChatbotGUI()
    gui.run()
