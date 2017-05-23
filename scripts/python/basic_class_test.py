import unittest
import graph_class as gc


class TestGraphMethods(unittest.TestCase):
    """
    Test basic graph functionality.
    """
    def setUp(self):
        self.test_graph = gc.Graph()
        self.test_graph.connect('A', (0, 1), 2, 'B', (1, 2), 2, '0.98')
        self.test_graph.connect('B', (0, 1), 2, 'C', (1, 2), 2, '0.98')
        self.test_graph.connect('D', (0, 1), 2, 'F', (1, 2), 2, '0.98')

    def test_type_test(self):
        """
        Makes sure all the types, and the graph structure is in order.
        """
        self.assertIsInstance(self.test_graph.get_nodes(), dict)
        self.assertEqual(set(self.test_graph.get_nodes().keys()), {'A', 'B', 'C', 'D', 'F'})
        for name in self.test_graph.get_nodes():
            self.assertIsInstance(self.test_graph.get_nodes()[name], gc.Node)
        node = self.test_graph.get_nodes()['A']
        self.assertIsInstance(node.get_name(), str)
        self.assertIsInstance(node.get_length(), int)
        neigh_dict = node.get_neighbours()
        self.assertIsInstance(neigh_dict, dict)
        self.assertIn('B', neigh_dict)
        self.assertIsInstance(neigh_dict['B'], gc.Arc)
        arc = neigh_dict['B']
        self.assertIn('B', arc.nodes)
        self.assertIn('A', arc.nodes)
        self.assertEqual((0, 1), arc.nodes['A'])
        self.assertIsInstance(arc.similarity, float)
        self.assertTrue((arc.similarity <= 1) and (arc.similarity > 0))

    def test_create_test(self):
        """
        Makes sure it is possible to create a node in the graph.
        """
        self.test_graph.create_node('E', 3)
        self.assertIn('E', self.test_graph.get_nodes())

    def test_connect_nodes(self):
        """
        Makes sure it is possible to create a node via connect.
        """
        self.test_graph.connect('NEW', (0, 1), 2, 'A', (1, 2), 2, '0.98')
        self.assertIn('NEW', self.test_graph.get_nodes())
        node_a = self.test_graph.get_nodes()['A']
        self.assertIn('NEW', node_a.get_neighbours())

    def test_remove(self):
        """
        Makes sure gc.remove() works properly.
        """
        self.test_graph.remove('A')
        self.assertNotIn('A', self.test_graph.get_nodes())
        neighbours_of_B = self.test_graph.get_nodes()['B'].get_neighbours()
        self.assertNotIn('A', neighbours_of_B)

    def test_distance(self):
        import math
        dist = self.test_graph.distance('A')
        self.assertEqual(dist['A'], 0)
        self.assertEqual(dist['C'], 2)
        self.assertEqual(dist['D'], math.inf)


if __name__ == '__main__':
    unittest.main()
