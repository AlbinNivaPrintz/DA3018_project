class Graph:
    def __init__(self):
        self._nodes = {}
        self._number_of_subgraphs = None

    @classmethod
    def parse(cls, filename: str, n_lines=-1):
        """

        Creates a graph object from file
        :param filename: name of the file where the graph is
        :param n_lines: how many lines of the file do you want to read, optional
        :return: graph object
        """
        G = Graph()
        fileObject = open(filename, 'r')
        n = 0
        for line in fileObject:
            if n == n_lines:
                break
            if not n % 1000000:
                print(n)
            n += 1
            out = line.split()
            nodeA = out[0]
            nodeB = out[1]
            G.connect(nodeA, nodeB)
        return G

    def create_node(self, name: str, neighbours=[]):
        """
        Creates a node object, and puts it in the graph
        :param name: Name of the node
        :param neighbours: Optional list of the neighbours
        """
        self._nodes[name] = neighbours
        for n in neighbours:
            if n not in self._nodes:
                self.create_node(n, [name])
            else:
                self._nodes[n].append(name)

    def connect(self, nodeA: str, nodeB: str):
        """
        Connects two nodes in the graph. If any of them is not already in the graph, it creates them first.
        :param nodeA: Name of the first node.
        :param nodeB: Name of second node.
        """
        if nodeB not in self._nodes:
            self.create_node(nodeB)
        if nodeA not in self._nodes:
            self.create_node(nodeA)
        if nodeA not in self._nodes[nodeB]:
            self._nodes[nodeB].append(nodeA)
        if nodeB not in self._nodes[nodeA]:
            self._nodes[nodeA].append(nodeB)

    def remove(self, n: str):
        """
        Removes the node *node* from the graph
        :param n: The node to be removed
        """
        neighbour_list = self._nodes.pop(n)
        for v in neighbour_list:
            self._nodes[v].remove(n)

    def get_nodes(self):
        return self._nodes

    def set_number_of_subgraphs(self, number: int):
        self._number_of_subgraphs = number

    def get_number_of_subgraphs(self) -> int:
        return self._number_of_subgraphs

    def distance(self, start: str):
        """
        Calculates distance from the node start to all other nodes in the graph.
        In the returned dictionary, start node gets a distance of zero,
        and nodes not connected to the start node gets math.inf.
        :param start: The node from which to calculate distances.
        :return: A dictionary like {'node': distance to start, ...}.
        """
        import queue
        import math
        infty = math.inf
        dist_so_far = 0
        dist_dict = {}
        for node in self._nodes:
            dist_dict[node] = infty
        q = queue.Queue()
        q.put(start)
        dist_dict[start] = dist_so_far
        while not q.empty():
            v = q.get()
            dist_so_far = dist_dict[v] + 1
            for u in self._nodes[v]:
                if dist_dict[u] == infty:
                    q.put(u)
                    dist_dict[u] = dist_so_far
        return dist_dict

    def save_to_file(self, directory: str):
        """
        Uses pickle to save nodes and arcs to a file.
        :param directory: Save directory.
        """
        import pickle
        fileObject = open(directory, 'wb')
        pickle.dump(self._nodes, fileObject)
        fileObject.close()

    def load_from_file(self, directory: str):
        """
        Uses pickle to load nodes and arcs from a file.
        :param directory: Load directory.
        """
        import pickle
        fileObject = open(directory, 'rb')
        self._nodes = pickle.load(fileObject)
        fileObject.close()

    def number_of_csg(self):
        """
        Calculates the number of different connected sub graphs is the graph.
        Also updates the attribute self.number_of_subgraphs.
        :return: a list containing one node from each connected sub graph.
        """
        import math
        backup = dict(self._nodes)
        c = 0
        distinct = []
        while len(self._nodes) > 0:
            for k in self._nodes:
                dist = self.distance(k)
                if not c % 100:
                    print(len(self._nodes), 'left to check.')
                for i in dist:
                    if dist[i] != math.inf and dist[i] != 0:
                        self._nodes.pop(i)
                distinct.append(k)
                self._nodes.pop(k)
                break
            c += 1
        self._nodes = backup
        self._number_of_subgraphs = len(distinct)
        return distinct

    # def sub_graph_numberer(self): # Gives all the nodes in each subgraph a number specific to the subgraph
    #     undiscovered = []
    #     for node in self.get_nodes():
    #         undiscovered.append(node)
    #     i = 0
    #     for node in self.get_nodes():
    #         if not node.get_graph_number():
    #             i += 1
    #             self.bfs_numberer(node, i, undiscovered)
    #     self.set_number_of_subgraphs(i)

    def sub_graph_numberer(self):  # Gives all the nodes in each subgraph a number specific to the subgraph
        # OLD
        undiscovered = []
        for node in self._nodes:
            undiscovered.append(node)
        i = 0
        for node in self._nodes:
            if not self.get_nodes()[node].get_graph_number():
                i += 1
                self.bfs_numberer(node, i, undiscovered)
                # print(i) # Remove!
        self.set_number_of_subgraphs(i)

    # def sub_graph_creater(self): # Takes a graph and returns a list of its connected subgraphs
    #     l = []
    #     for i in range(1, self.get_number_of_subgraphs + 1):
    #         l[i - 1] = Graph()
    #         for node in self.get_nodes():
    #             if node.get_graph_number() == i:
    #                 l[i - 1].create_node(node, node.get_length(), node.get_neighbours())
    #                 self.remove(node)
    #     return l

    def sub_graph_creater(self):  # Takes a graph and returns a list of its connected subgraphs
        # OLD
        l = []
        for i in range(1, self.get_number_of_subgraphs() + 1):
            # print(i) # Remove!
            graph = Graph()
            l.append(graph)
            for node in self.get_nodes().values():
                if node.get_graph_number() == i:
                    l[i - 1].create_node(node.get_name(), node.get_length(), node.get_neighbours())
                    # self.remove(node)
        return l

    # def bfs_numberer(self, start, number, undiscovered): # Numbers the nodes in a connected graph with number
    #     undiscovered.pop(start)
    #     start.set_graph_number(number)
    #     Q = fifoqueue(len(self.get_nodes()))
    #     Q.enqueue(start)
    #     while Q.len > 0:
    #         u = Q.dequeue()
    #         for v in u.get_neighbours():
    #             if v in undiscovered:
    #                 undiscovered.pop(v)
    #                 v.set_graph_number(number)
    #                 Q.enqueue(v)

    def bfs_numberer(self, start: str, number: int, undiscovered: list):
        # OLD
        # Numbers the nodes in a connected graph with number
        import queue as q
        undiscovered.remove(self.get_nodes()[start].get_name())
        self.get_nodes()[start].set_graph_number(number)
        Q = q.Queue(len(self.get_nodes()))
        Q.put(start)
        while not Q.empty() > 0:
            u = Q.get()
            for v in list(self.get_nodes()[u].get_neighbours().keys()):
                if v in undiscovered:
                    undiscovered.remove(v)
                    self.get_nodes()[v].set_graph_number(number)
                    Q.put(v)

    def social_node_remover(self, start, no_neighbours: int):
        # OLD
        # Removes nodes with number of neighbours equal to or more than no_neighbours
        import queue as q

        def social_node_lister(self: Graph, start, no_neighbours: int):
            # Lists nodes with number of neighbours equal to or more than no_neighbours
            social_nodes = []
            undiscovered = []
            for node in self.get_nodes():
                undiscovered.append(node)
            if len(start.get_neighbours()) >= no_neighbours:
                social_nodes.append(start)
            undiscovered.remove(start)
            Q = q.Queue(len(self.get_nodes()))
            Q.put(start)
            while not Q.empty() > 0:
                u = Q.get()
                for v in u.get_neighbours():
                    if v in undiscovered:
                        undiscovered.pop(v)
                        if len(v.get_neighbours()) >= no_neighbours:
                            social_nodes.append(v)
                        Q.put(v)
            return social_nodes

        social_nodes = social_node_lister(self, start, no_neighbours)
        for node in social_nodes:
            self.remove(node)


if __name__ == '__main__':

    from time import time

    start_1 = time()

    g = Graph.parse('Spruce_fingerprint_2017-03-10_16.48.olp.m4', 10**4)

    end_1 = time()

    print('Parsing took {} seconds'.format(end_1 - start_1))

    start_2 = time()

    g.sub_graph_numberer()

    end_2 = time()

    print('Numbering subgraphs took {} seconds'.format(end_2 - start_2))

    start_3 = time()

    l = g.sub_graph_creater()

    end_3 = time()

    print('Creating new subgraphs took {} seconds'.format(end_3 - start_3))
