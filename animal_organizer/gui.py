import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import networkx as nx
from .binary_tree import AnimalTree

class TreeVisualizer:
    def __init__(self, tree):
        self.tree = tree
        self.root = tk.Tk()
        self.root.title("Binary Tree Visualizer")
        
        btn_show = tk.Button(self.root, text="Show Tree", command=self.display_tree)
        btn_show.pack(pady=20)
        
        self.root.mainloop()
    
    def add_edges(self, graph, node, pos, x=0, y=0, layer=1):
        if node is not None:
            graph.add_node(node.animal.name, label=node.animal.name)
            pos[node.animal.name] = (x, -y)
            
            if node.left:
                graph.add_edge(node.animal.name, node.left.animal.name)
                self.add_edges(graph, node.left, pos, x - 1 / (layer + 1), y + 1, layer + 1)
            
            if node.right:
                graph.add_edge(node.animal.name, node.right.animal.name)
                self.add_edges(graph, node.right, pos, x + 1 / (layer + 1), y + 1, layer + 1)
    
    def display_tree(self):
        if self.tree.root is None:
            messagebox.showerror("Error", "Tree is empty!")
            return
        
        graph = nx.DiGraph()
        pos = {}
        self.add_edges(graph, self.tree.root, pos)
        
        labels = {node: node for node in graph.nodes()}
        plt.figure(figsize=(12, 8))
        nx.draw(graph, pos, labels=labels, with_labels=True, node_size=3500, node_color="lightgreen", font_size=10, font_weight="bold", edge_color="black")
        plt.title("Animal Binary Tree Structure")
        plt.show()

if __name__ == "__main__":
    from animal_organizer.data_loader import load_animals_from_csv
    
    animal_tree = AnimalTree()
    load_animals_from_csv("animals.csv", animal_tree)
    TreeVisualizer(animal_tree)
