from collections import deque


class Graph:
    def __init__(self):
        self._nodes = {}

    def __len__(self):
        """
        :return: The number of nodes in the graph.
        """
        return len(self._nodes.values())

    @classmethod
    def parse(cls, filename: str, n_lines=-1):
        """
        Creates a graph object from file
        :param filename: name of the file where the graph is
        :param n_lines: how many lines of the file do you want to read, optional
        :return: graph object
        """
        G = Graph()
        with open(filename, 'r') as fileObject:
            n = 0
            for line in fileObject:
                if n == n_lines:
                    # If the optional argument n_lines is passed,
                    # this makes sure the script stops reading at
                    # the appropriate place.
                    break
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
                self._nodes[v].remove(n)

    def get_nodes(self) -> dict:
        return self._nodes

    def get_neighbours(self, node: str) -> list:
        return self._nodes[node]

    def get_sub_graph(self, start: str, disc_dict) -> tuple:
        """
        Returns the connected subgraph of self, which contains the node start.
        :param start: The node from which to calculate distances.
        :param disc_dict: A dictionary with all the nodes not already discovered in the tree.
        :return: The connected subgraph in self containing start.
        """
        new_deq = deque()
        q = deque()
        q.append(start)
        new_deq.append(start)
        while len(q) > 0:
            v = q.popleft()
            for u in self._nodes[v]:
                if u in disc_dict:
                    q.append(u)
                    disc_dict.pop(u)
                    new_deq.append(u)
        return new_deq, disc_dict

    def csg_ify(self):
        """
        This method will destroy the graph.
        Calculates the number of different connected sub graphs is the graph.
        Also updates the attribute self.number_of_subgraphs.
        :return: A list with the string representations of the subgraphs in self.
        """
        csg = deque()
        disc_dict = {}
        for node in self._nodes:
            disc_dict[node] = 1
        while len(self._nodes) > 0:
            nodename, x = disc_dict.popitem()
            new_deq, disc_dict = self.get_sub_graph(nodename, disc_dict)
            new_str = ""
            while new_deq:
                node = new_deq.popleft()
                new_str += "\t" + node
                self.remove(node)
            csg.append(new_str.strip())
        return csg


if __name__ == '__main__':

    import sys

    from time import time

    start_1 = time()

    print('Initializing parsing...')

    g = Graph.parse("resources/unsocial_contigs_over_{}.txt".format(sys.argv[1]))

    end_1 = time()

    print('Parsing complete and took {} seconds'.format(end_1 - start_1))

    print('Creating subgraphs...')

    start_3 = time()

    l = g.csg_ify()

    end_3 = time()

    print('Subgraphs created. It took {} seconds'.format(end_3 - start_3))

    print('Creating resultfile...')

    start_4 = time()

    with open('/results/Result_'+sys.argv[1]+'.txt','w+') as res:
        while l:
            res.write(l.popleft()+'\n')


    end_4 = time()

    print('Creating the result file took {} seconds'.format(end_4 - start_4))

    print('Finished.')
