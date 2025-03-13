import nltk
from nltk.tokenize import word_tokenize

class TodoAgent:
    def __init__(self):
        self.todo_list = []

    def process_input(self, user_input):
        tokens = word_tokenize(user_input.lower())
        if "add" in tokens:
            self.add_item(user_input)
        elif "what" in tokens and "list" in tokens:
            self.show_list()
        elif "mark" in tokens and "done" in tokens:
            self.mark_done(user_input)
        else:
            print("I don't understand that command.")

    def add_item(self, user_input):
        try:
            item = user_input.lower().split("add")[1].strip().split("to")[0].strip()
            self.todo_list.append({"item": item, "done": False})
            print(f"Added '{item}' to your to-do list.")
        except IndexError:
            print("Invalid add command")

    def show_list(self):
        if not self.todo_list:
            print("Your to-do list is empty.")
        else:
            print("Your to-do list:")
            for i, item in enumerate(self.todo_list):
                status = "[X]" if item["done"] else "[ ]"
                print(f"{i + 1}. {status} {item['item']}")

    def mark_done(self, user_input):
        try:
            item_to_mark = user_input.lower().split("mark")[1].split("done")[0].strip()
            for item in self.todo_list:
                if item["item"] in item_to_mark:
                    item["done"] = True
                    print(f"Marked '{item['item']}' as done.")
                    return
            print(f"Item '{item_to_mark}' not found in your to-do list.")
        except IndexError:
            print("Invalid mark done command")

if __name__ == "__main__":
    agent = TodoAgent()
    print("Welcome to the Simple To-Do List Manager!")
    while True:
        user_input = input("> ")
        if user_input.lower() == "exit":
            break
        agent.process_input(user_input)