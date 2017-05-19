class Graph:
    """
    Main graph object.
    """

    def __init__(self):
        self._nodes = {}
        self._number_of_subgraphs = None

    def create_node(self, name, length):
        """
        Creates a node object, and puts it in the graph
        :param name: Name of the node
        :param length: Length of the string represented by the node
        """
        self._nodes[name] = Node(name, length)

    def connect(self, nodeA: str, sectionA: tuple, nodeB: str, sectionB: tuple,
                similarity: str, lengthA: int, lengthB: int):
        """
        Connects two nodes in the graph. If any of them is not already in the graph, it creates them first.
        :param nodeA: Name of the first node.
        :param sectionA: Location of match in nodeA
        :param nodeB: Name of second node.
        :param sectionB: Location of match in nodeB
        :param similarity: Strength of match
        :param lengthA: Length of nodeA
        :param lengthB: Length of nodeB
        """
        if nodeB not in self._nodes:
            self.create_node(nodeB, lengthB)
        if nodeA not in self._nodes:
            self.create_node(nodeA, lengthA)
        self._nodes[nodeB].insert(nodeA, sectionB, sectionA, similarity)
        self._nodes[nodeA].insert(nodeB, sectionA, sectionB, similarity)

    def remove(self, n):
        """
        Removes the node *node* from the graph
        :param n: The node to be removed
        """
        neighbours = list(self._nodes[n].neighbours.keys())
        self._nodes.pop(n)
        for v in neighbours:
            self._nodes[v].neighbours.pop(n)

    def get_nodes(self):
        return self._nodes

    def set_number_of_subgraphs(self, number):
        self._number_of_subgraphs = number

    def get_number_of_subgraphs(self):
        return self._number_of_subgraphs

    def distance(self, start):
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

    def save_to_file(self, directory):
        """
        Uses pickle to save nodes and arcs to a file.
        :param directory: Save directory.
        """
        import pickle
        fileObject = open(directory, 'wb')
        pickle.dump(self._nodes, fileObject)
        fileObject.close()

    def load_from_file(self, directory):
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


class DiArc:
    """
    A directional arc class.
    """

    def __init__(self, sectionSelf: tuple, sectionOther: tuple, similarity: str):
        self.ownLocation = sectionSelf
        self.otherLocation = sectionOther
        self.similarity = similarity


class Node:
    """
    Node class.
    """

    def __init__(self, name, length):
        self._name = name
        self._neighbours = {}
        self.length = length
        self._color = None
        self._graph_number = None

    def insert(self, name, sectionSelf, sectionOther, similarity):
        """
        Places a node in the neighbour set of this node.
        :param name: Name of the neighbour
        :param sectionSelf: Where in this node is the match occurring?
        :param sectionOther: Where in the neighbour is the match occurring?
        :param similarity: How strong is the match?
        """
        self._neighbours[name] = DiArc(sectionSelf, sectionOther, similarity)

    def get_name(self):
        return self._name

    def set_color(self, color):
        """
        Set the color of the node.
        :param color: Color
        """
        self._color = color

    def get_color(self):
        """
        Get the color of the node.
        :return: Color of the node as string.
        """
        return self._color

    def set_graph_number(self, number):
        """
        Specify which internal graph the node belongs to.
        :param number: Internal graph number
        """
        self._graph_number = number

    def get_graph_number(self):
        """
        Number of which the node belongs to.
        :return: The number of the graph the node belongs to.
        """
        return self._graph_number

    def get_neighbours(self):
        """
        Get the neighbour set of the node.
        :return: The neighbour set as a dictionary.
        """
        return self._neighbours
