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
