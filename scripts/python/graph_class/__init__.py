class graph:
    """
    Main graph object.
    """
    def __init__(self):
        self._arcs = {}

    def connect(self, nodeA: str, sectionA: tuple, nodeB: str, sectionB: tuple, similarity: str):
        """
        Connects two nodes.
        :param nodeA: name of first node
        :param sectionA: match location in A 
        :param nodeB: name of second node
        :param sectionB: match location in B
        :param similarity: match strength
        """
        if not nodeA in self._arcs:
            self._arcs[nodeB] = {}
        if not nodeA in self._arcs:
            self._arcs[nodeA] = {}
        self._arcs[nodeB][nodeA] = di_arc(nodeA, sectionB, sectionA, similarity)
        self._arcs[nodeA][nodeB] = di_arc(nodeB, sectionA, sectionB, similarity)

class di_arc:
    """
    A directional arc object.
    """
    def __init__(self, name, sectionSelf: tuple, sectionOther: tuple, similarity: str):
        self.target = name
        self.ownLocation = sectionSelf
        self.otherLocation = sectionOther
        self.similarity = similarity
