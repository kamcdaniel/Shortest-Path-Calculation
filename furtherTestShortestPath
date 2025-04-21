import unittest
from project4 import HashMap, MinHeap, dijkstra, insert_edge, get_neighbors, enqueue, dequeue
class StudentTestHashMapInsert(unittest.TestCase):
    def test_insert_into_already_existing(self):
        graph = HashMap(capacity=4)
        graph = insert_edge(graph, "A", "B", 4)
        graph = insert_edge(graph, "A", "C", 2)
        expected = [(' ', []), ("A", [("B", 4), ("C", 2)]), (' ', []), (' ', [])]
        self.assertEqual(graph.data, expected)
    
    def test_insert_into_unexpected_pos(self):
        graph = HashMap(capacity=4)
        graph = insert_edge(graph, "A", "B", 4)
        graph = insert_edge(graph, "E", "A", 2)
        graph = insert_edge(graph, "E", "C", 3)
        expected = [(' ', []), ("A", [("B", 4)]), ("E", [("A", 2), ("C", 3)]), (' ', [])]
        self.assertEqual(graph.data, expected)

class StudentTestGetNeighbors(unittest.TestCase):
    def test_get_single_neighbor(self):
        graph = HashMap(capacity=4)
        graph = insert_edge(graph, "A", "B", 4)
        graph = insert_edge(graph, "E", "A", 2)
        graph = insert_edge(graph, "E", "C", 3)
        expected = [("B", 4)]
        self.assertEqual(get_neighbors(graph,"A"), expected)
    
    def test_get_multiple_neighbors(self):
        graph = HashMap(capacity=4)
        graph = insert_edge(graph, "A", "B", 4)
        graph = insert_edge(graph, "A", "C", 2)
        graph = insert_edge(graph, "E", "C", 3)
        expected = [("B", 4), ("C", 2)]
        self.assertEqual(get_neighbors(graph,"A"), expected)

    def test_get_multiple_neighbors_linear_probed(self):
        graph = HashMap(capacity=4)
        graph = insert_edge(graph, "A", "B", 4)
        graph = insert_edge(graph, "E", "A", 2)
        graph = insert_edge(graph, "E", "C", 3)
        expected = [("A", 2), ("C", 3)]
        self.assertEqual(get_neighbors(graph,"E"), expected)

    def test_get_no_neighbors_bc_doesnt_exist(self):
        graph = HashMap(capacity=4)
        graph = insert_edge(graph, "A", "B", 4)
        graph = insert_edge(graph, "E", "A", 2)
        graph = insert_edge(graph, "E", "C", 3)
        expected = []
        self.assertEqual(get_neighbors(graph,"C"), expected)

class StudentTestHeapInsert(unittest.TestCase):
    def test_insert_same_value(self):
        heap = MinHeap()
        heap = enqueue(heap, ("A", 3))
        heap = enqueue(heap, ("B", 1))
        heap = enqueue(heap, ("B", 2))
        self.assertEqual(heap.data, [("B", 1), ("A", 3), ("B", 2)]) 

class StudentTestExtractMin(unittest.TestCase):
    def test_extract_min_same_char(self):
        heap = MinHeap()
        heap = enqueue(heap, ("A", 1))
        heap = enqueue(heap, ("B", 1))
        heap = enqueue(heap, ("B", 2))
        heap, min_element = dequeue(heap)
        self.assertEqual(min_element, ("A", 1))
        self.assertEqual(heap.data, [("B", 1), ("B", 2)]) 

if __name__ == "__main__":
    unittest.main()
