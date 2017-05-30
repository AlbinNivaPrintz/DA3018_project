from collections import deque


class Graph:
    """
    A simple graph class, designed for dividing a 
    graph class into its connected sub graphs and printing the output.
    """
    def __init__(self):
        self._nodes = {}

    def __len__(self):
        """
        :return: The number of nodes in the graph.
        """
        return len(self._nodes)

    @classmethod
    def parse(cls, filename: str, n_lines=-1):
        """
        Creates a graph object from file.
        Each line in the file should contain a node pair,
        representing an arc in the graph. Example:
        
        node1   node2
        node3   node4
        ...
        
        :param filename: path to the input file.
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

    def connect(self, nodeA: str, nodeB: str):
        """
        Connects two nodes in the graph. If any of them is not already in the graph, it creates them first.
        :param nodeA: Name of the first node.
        :param nodeB: Name of second node.
        """
        if nodeB not in self._nodes:
            self._nodes[nodeB] = {nodeA: 1}
        else:
            if nodeA not in self._nodes[nodeB]:
                self._nodes[nodeB][nodeA] = 1
        if nodeA not in self._nodes:
            self._nodes[nodeA] = {nodeB: 1}
        else:
            if nodeB not in self._nodes[nodeA]:
                self._nodes[nodeA][nodeB] = 1

    def remove(self, n: str):
        """
        Removes the node n from the graph (and the neighbour sets of all its neighbours).
        :param n: The node to be removed
        """
        if n in self._nodes:
            neighbour_list = self._nodes.pop(n)
            for v in neighbour_list:
                self._nodes[v].pop(n)

    def get_nodes(self) -> dict:
        """
        Get a dictionary of all the nodes in the graph and their neighbours.
        {'node name': [neighbours], ...}
        :return: The node dictionary of the graph.
        """
        return self._nodes

    def get_neighbours(self, node: str) -> list:
        """
        Get the neighbour set of a given node.
        :param node: The name of the node which neighbour set you desire.
        :return: A list of the neighbours of node name.
        """
        return self._nodes[node]

    def get_sub_graph(self, start: str, disc_dict) -> tuple:
        """
        Returns the connected sub graph of self, which contains the node start.
        :param start: The node from which to calculate distances.
        :param disc_dict: A dictionary with all the nodes not already discovered in the tree.
        :return: The connected sub graph in self containing start.
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
        :return: A list with the string representations of the sub graphs in self.
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
