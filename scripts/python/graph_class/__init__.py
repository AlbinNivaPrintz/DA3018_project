class graph:
    """
    Main graph object.
    """
    def __init__(self):
        self.nodes = {}

    def __str__(self):
        return 'I exist!!'

    def create_node(self, name, length):
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
            self.create_node(nodeB, lengthB)
        if not nodeA in self.nodes:
            self.create_node(nodeA, lengthA)
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
        self.neighbours[name] = di_arc(sectionSelf, sectionOther, similarity)

    def set_color(self, color):
        self.color = color

    def set_graph_number(self, number):
        self.graph_number = number