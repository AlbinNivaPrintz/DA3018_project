def bfs_numberer(self, start, number): # Numbers all the nodes in connected graph
    pass

def sub_graph_numberer(self): # Gives all the nodes in each subgraph a number specific to the subgraph
    i = 0
    for node in self.get_nodes(): # Need self.get_nodes()
        if  not node.get_graph_number(): # Need node.get_graph_number()
            i += 1
            self.bfs_numberer(node, i)
    self.set_number_of_subgraphs = i # Need self.set_number_of_subgraphs()

def sub_graph_creater(self): # Takes a graph and returns a list of its connected subgraphs
    l = []
    for i in range(1, self.get_number_of_subgraphs + 1): # Need self.get_number_of_subgraphs()
        l[i - 1] = GraphClass() # To be replaced
        for node in self.get_nodes(): # Need self.get_nodes()
            if node.get_graph_number() == i: # Need node.get_graph_number()
                l[i - 1].insert(node)
                self.remove(node) # Need self.remove()
    return l
