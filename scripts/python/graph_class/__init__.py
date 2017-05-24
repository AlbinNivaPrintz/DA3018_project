class Graph:
    def __init__(self):
        self._nodes = {}
        self._number_of_subgraphs = None

    def __str__(self):
        out = str(len(self)) + "\t"
        for node in self._nodes:
            out += node + "\t"
        return out

    def __len__(self):
        return len(list(self._nodes.values()))

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

    def create_node(self, name: str, neighbours=None):
        """
        Creates a node object, and puts it in the graph
        :param name: Name of the node
        :param neighbours: Optional list of the neighbours
        """
        if not neighbours:
            neighbours = []
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
            self._nodes[nodeB] = [nodeA]
        if nodeA not in self._nodes:
            self._nodes[nodeA] = [nodeB]
        if nodeA not in self._nodes[nodeB]:
            self._nodes[nodeB].append(nodeA)
        if nodeB not in self._nodes[nodeA]:
            self._nodes[nodeA].append(nodeB)

    def remove(self, n: str):
        """
        Removes the node *node* from the graph
        :param n: The node to be removed
        """
        if n in self._nodes:
            neighbour_list = self._nodes.pop(n)
            for v in neighbour_list:
                if v in self._nodes:
                    if n in self._nodes[v]:
                        self._nodes[v].remove(n)

    def get_nodes(self) -> dict:
        return self._nodes

    def get_neighbours(self, node: str) -> list:
        return self._nodes[node]

    def set_number_of_subgraphs(self, number: int):
        self._number_of_subgraphs = number

    def get_number_of_subgraphs(self) -> int:
        return self._number_of_subgraphs

    def get_sub_graph(self, start: str, disc_dict):
        """
        Returns the connected subgraph of self, which contains the node start.
        :param start: The node from which to calculate distances.
        :return: The connected subgraph in self containing start.
        """
        import queue
        new_G = Graph()
        q = queue.Queue()
        q.put(start)
        disc_dict[start] = 1
        new_G.create_node(start, neighbours=self._nodes[start])
        while not q.empty():
            v = q.get()
            for u in self._nodes[v]:
                if disc_dict[u]:
                    q.put(u)
                    disc_dict.pop(u)
                    new_G.create_node(u, neighbours=self._nodes[u])
        return new_G, disc_dict


    def csg_ify(self):
        """
        This method will destroy the graph.
        Calculates the number of different connected sub graphs is the graph.
        Also updates the attribute self.number_of_subgraphs.
        :return: A list with all the connected subgrahs of self.
        """
        csg = []
        c = 0
        disc_dict = {}
        for node in self._nodes:
            disc_dict[node] = 1
        while len(self._nodes) > 0:
            for k in self._nodes:
                new_G, disc_dict = self.get_sub_graph(k, disc_dict)
                if not c % 100000:
                    print(len(self._nodes), 'left to check.')
                for i in new_G.get_nodes():
                    self.remove(i)
                self.remove(k)
                break
            csg.append(new_G)
            c += 1
        return csg

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

    import sys

    from time import time

    start_1 = time()

    print('Initializing parsing...')

    g = Graph.parse(sys.argv[1])

    end_1 = time()

    print('Parsing complete and took {} seconds'.format(end_1 - start_1))

    print('Creating subgraphs...')

    start_3 = time()

    l = g.csg_ify()

    end_3 = time()

    print('Subgraphs created. It took {} seconds'.format(end_3 - start_3))

    print('Creating resultfile...')

    start_4 = time()

    res=open('../../../results/Result.txt','w+')
    for graph in l:
        res.write(str(graph))
    res.close()


    end_4 = time()

    print('Creating the result file took {} seconds'.format(end_4 - start_4))

    print('Finished.')
