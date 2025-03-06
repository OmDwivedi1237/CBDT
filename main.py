from chatbot import Chatbot, ChatbotGUI

def main():
    print("=== Welcome to the Chatbot System ===")
    print("1. Run Chatbot in Console Mode")
    print("2. Run Chatbot with GUI")
    choice = input("Choose an option (1/2): ").strip()

    if choice == "1":
        bot = Chatbot()
        bot.start()
    elif choice == "2":
        gui = ChatbotGUI()
        gui.run()
    else:
        print("Invalid choice. Please restart the program.")

if __name__ == "__main__":
    main()
