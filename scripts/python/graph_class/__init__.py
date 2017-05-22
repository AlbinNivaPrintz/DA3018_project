class Graph:
    """
    Main graph object.
    """

    def __init__(self):
        self._nodes = {}
        self._number_of_subgraphs = None

    @classmethod
    def parse(cls, filename, n_lines=-1):
        """
        
        Creates a graph object from file
        :param filename: name of the file where the graph is
        :param n_lines: how many lines of the file do you want to read, optional
        :return: graph object
        """
        G = Graph()
        fileObject = open(filename, 'rb')
        n = 0
        for line in fileObject:
            if n == n_lines:
                break
            if not n % 1000000:
                print(n)
            n += 1
            l = line.split()
            nodeA = l[0]
            nodeB = l[1]
            similarity = l[3]
            matchA = (l[5], l[6])
            lengthA = l[7]
            matchB = (l[9], l[10])
            lengthB = l[11]
            G.connect(nodeA, matchA, lengthA,
                      nodeB, matchB, lengthB,
                      similarity)
        return G

    def create_m4(self):
        """
        Write the graph to a m4 file 
        """
        pass

    def create_node(self, name, length, neighbours = None):
        """
        Creates a node object, and puts it in the graph
        :param name: Name of the node
        :param length: Length of the string represented by the node
        :param neighbours: Optional neighbour set
        """
        self._nodes[name] = Node(name, length)
        if neighbours:
            self._nodes[name].set_neighbours(neighbours)

    def connect(self, nodeA: str, sectionA: tuple, lengthA: int,
                nodeB: str, sectionB: tuple, lengthB: int, similarity: str):
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
        arc = Arc(nodeA,sectionA,nodeB,sectionB,similarity)
        self._nodes[nodeB].insert(nodeA, arc)
        self._nodes[nodeA].insert(nodeB, arc)

    def remove(self, n):
        """
        Removes the node *node* from the graph
        :param n: The node to be removed
        """
        neighbour_list = list(self._nodes[n].get_neighbours().keys())
        self._nodes.pop(n)
        for v in neighbour_list:
            self._nodes[v].remove_a_neighbour(n)

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


class Arc:
    """
    An arc class.
    """

    def __init__(self,nameA: str, sectionA: tuple, nameB: str, sectionB: tuple, similarity: str):
        self.nodes = {nameA: sectionA, nameB: sectionB}
        self.similarity = float(similarity)


class Node:
    """
    Node class.
    """

    def __init__(self, name, length):
        self._name = name
        self._neighbours = {}
        self._length = length
        self._color = None
        self._graph_number = None

    def insert(self, name, arc):
        """
        Places a node in the neighbour set of this node.
        :param name: Name of the neighbour
        :param sectionSelf: Where in this node is the match occurring?
        :param sectionOther: Where in the neighbour is the match occurring?
        :param similarity: How strong is the match?
        """
        self._neighbours[name] = arc

    def get_name(self):
        return self._name

    def get_length(self):
        """
        Get the length of the node
        :return: length of node as float
        """
        return self._length

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

    def set_neighbours(self, neighbours: dict):
        """
        Manually creates a neighbour set for the node.
        
        Be certain the dict you're setting is on the right from.
        
        :param neighbours: the neighbour set
        """
        self._neighbours = neighbours

    def set_a_neighbour(self, name, arc):
        self._neighbours[name] = arc

    def remove_a_neighbour(self, name):
        self._neighbours.pop(name)
