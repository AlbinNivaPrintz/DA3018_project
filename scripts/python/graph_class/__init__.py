class graph:
    """
    Main graph object.
    """
    def __init__(self):
        self.nodes = {}

    def __create_node(self, name, length):
        """
        Creates a node object, and puts it in the graph
        :param name: Name of the node
        :param length: Length of the string represented by the node
        """
        self.nodes[name] = node(name, length)

    def connect(self, nodeA: str, sectionA: tuple, nodeB: str, sectionB: tuple, similarity: str, lengthA: int, lengthB: int):
        """
        Connects two nodes.
        :param nodeA: name of first node
        :param sectionA: match location in A 
        :param nodeB: name of second node
        :param sectionB: match location in B
        :param similarity: match strength
        """
        if not nodeB in self.nodes:
            self.__create_node(nodeB, lengthB)
        if not nodeA in self.nodes:
            self.__create_node(nodeA, lengthA)
        self.nodes[nodeB].insert(nodeA, sectionB, sectionA, similarity)
        self.nodes[nodeA].insert(nodeB, sectionA, sectionB, similarity)


class di_arc:
    """
    A directional arc class.
    """
    def __init__(self, sectionSelf: tuple, sectionOther: tuple, similarity: str):
        self.ownLocation = sectionSelf
        self.otherLocation = sectionOther
        self.similarity = similarity

class node:
    """
    Node class.
    """
    def __init__(self, name, length):
        self.name = name
        self.neighbours = {}
        self.length = length
        self.color = None
        self.graph_number = None

    def insert(self, name, sectionSelf, sectionOther, similarity):
        """
        Places a node in the neighbour set of this node.
        :param name: Name of the neighbour
        :param sectionSelf: Where in this node is the match occurring?
        :param sectionOther: Where in the neighbour is the match occurring?
        :param similarity: How strong is the match?
        """
        self.neighbours[name] = di_arc(sectionSelf, sectionOther, similarity)

    def set_color(self, color):
        """
        Set the color of the node.
        :param color: Color
        """
        self.color = color

    def set_graph_number(self, number):
        """
        Specify which internal graph the node belongs to.
        :param number: Internal graph number
        """
        self.graph_number = number