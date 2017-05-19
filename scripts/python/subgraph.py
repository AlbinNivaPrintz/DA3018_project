from fifoqueue import *

def sub_graph_numberer(self): # Gives all the nodes in each subgraph a number specific to the subgraph
    i = 0
    for node in self.get_nodes():
        if not node.get_graph_number():
            i += 1
            self.bfs_numberer(node, i)
    self.set_number_of_subgraphs(i)

def sub_graph_creater(self): # Takes a graph and returns a list of its connected subgraphs
    l = []
    for i in range(1, self.get_number_of_subgraphs + 1):
        l[i - 1] = Graph()
        for node in self.get_nodes():
            if node.get_graph_number() == i:
                l[i - 1].create_node(node, node.get_length(), node.get_neighbours())
                self.remove(node)
    return l

def bfs_numberer(self, start, number): # Numbers the nodes in a connected graph with number
    undiscovered = []
    for node in self.get_nodes():
        undiscovered.append(node)
    undiscovered.pop(start)
    start.set_graph_number(number)
    Q = fifoqueue(len(self.get_nodes()))
    Q.enqueue(start)
    while Q.len > 0:
        u = Q.dequeue()
        for v in u.get_neighbours():
            if v in undiscovered:
                undiscovered.pop(v)
                v.set_graph_number(number)
                Q.enqueue(v)

def social_node_remover(self, start, no_neighbours): # Removes nodes with number of neighbours equal to or more than no_neighbours

    def social_node_lister(self, start, no_neighbours): # Lists nodes with number of neighbours equal to or more than no_neighbours

        social_nodes = []
        undiscovered = []
        for node in self.get_nodes():
            undiscovered.append(node)
        if len(start.get_neighbours()) >= no_neighbours:
            social_nodes.append(start)
        undiscovered.pop(start)
        Q = fifoqueue(len(self.get_nodes()))
        Q.enqueue(start)
        while Q.len > 0:
            u = Q.dequeue()
            for v in u.get_neighbours():
                if v in undiscovered:
                    undiscovered.pop(v)
                    if len(v.get_neighbours()) >= no_neighbours:
                        social_nodes.append(v)
                    Q.enqueue(v)
        return social_nodes

    social_nodes = social_node_lister(self, start, no_neighbours)
    for node in social_nodes:
        self.remove(node)
