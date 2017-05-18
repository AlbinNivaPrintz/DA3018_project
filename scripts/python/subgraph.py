from fifoqueue import *

def bfs_numberer(self, start, number): # Numbers all the nodes in connected graph
    pass

def sub_graph_numberer(self): # Gives all the nodes in each subgraph a number specific to the subgraph
    i = 0
    for node in self.get_nodes(): # Need self.get_nodes()
        if  not node.get_graph_number(): # Need node.get_graph_number()
            i += 1
            self.bfs_numberer(node, i)
    self.set_number_of_subgraphs(i) # Need self.set_number_of_subgraphs(i)

def sub_graph_creater(self): # Takes a graph and returns a list of its connected subgraphs
    l = []
    for i in range(1, self.get_number_of_subgraphs + 1): # Need self.get_number_of_subgraphs()
        l[i - 1] = GraphClass() # To be replaced
        for node in self.get_nodes(): 
            if node.get_graph_number() == i:
                l[i - 1].insert(node)
                self.remove(node) # Need self.remove()
    return l

def bfs_numberer(self, start, number):
    start.set_color("Gray") # Need node.set_color(color)
    start.set_graph_number(number) # Need node.set_graph_number(number)
    Q = fifoqueue(len(self.get_nodes())) # Need self.get_nodes()
    Q.enqueue(start)
    while Q.len > 0:
        u = Q.dequeue()
        for v in u.get_edges(): # Need node.get_edges()
            if v.get_color() == "White": # Need node.get_color()
                Q.enqueue(v)
        u.set_color("Black")
