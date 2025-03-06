import json

class DecisionTree:
    def __init__(self):
        self.root = {'question': 'Do you like the weather today?', 'yes': None, 'no': None}
        self.current_node = self.root
        self.load_tree()

    def load_tree(self):
        try:
            with open('../data/tree.json', 'r') as file:
                self.root = json.load(file)
        except FileNotFoundError:
            pass

    def save_tree(self):
        with open('../data/tree.json', 'w') as file:
            json.dump(self.root, file, indent=4)

    def add_node(self, question, yes_response=None, no_response=None):
        new_node = {'question': question, 'yes': yes_response, 'no': no_response}
        self.save_tree()

    def traverse_tree(self, user_input):
        if user_input.lower() in ['yes', 'y']:
            if self.current_node['yes'] is None:
                return None
            self.current_node = self.current_node['yes']
        elif user_input.lower() in ['no', 'n']:
            if self.current_node['no'] is None:
                return None
            self.current_node = self.current_node['no']
        return self.current_node['question'] if 'question' in self.current_node else None

    def reset_tree(self):
        self.current_node = self.root

    def learn(self, user_input, feedback):
        if feedback == 'yes':
            if self.current_node['yes'] is None:
                self.current_node['yes'] = {'question': user_input, 'yes': None, 'no': None}
        elif feedback == 'no':
            if self.current_node['no'] is None:
                self.current_node['no'] = {'question': user_input, 'yes': None, 'no': None}
        self.save_tree()
