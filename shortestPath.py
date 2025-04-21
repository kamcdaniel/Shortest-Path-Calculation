from dataclasses import dataclass, field

def hash_function(key: str, capacity: int) -> int:
        # Simple hash function based on the ASCII value of the first character
        return ord(key) % capacity

@dataclass(frozen=True)
class HashMap:
    capacity: int
    data: list[tuple[str, list[tuple[str, int]]]] = field(default_factory=list)

    def __post_init__(self):
        if len(self.data) > self.capacity:
            raise ValueError("Data exceeds capacity")
        object.__setattr__(self, 'data', self.data + [(' ', [])] * (self.capacity - len(self.data)))

def insert_edge(hash_map: HashMap, node: str, neighbor: str, weight: int) -> HashMap:

    map = HashMap(hash_map.capacity, hash_map.data)

    i = hash_function(node, map.capacity)
    
    if map.data[i][0] == node:
        map.data[i][1].append((neighbor, weight))
    elif map.data[i] != node:
        check_for_full_loop = i
        found = False
        if map.data[i][0] == node:
            found = True
            map.data[i][1].append((neighbor, weight))
        i = (i+1) % map.capacity
        while i != check_for_full_loop and found == False:
            if map.data[i][0] == node:
                found = True
                map.data[i][1].append((neighbor, weight))
                break
            i = (i+1) % map.capacity

        check_for_full = i
        #print(map.data[i][0])
        if map.data[i][0] == " ":
            found = True
            map.data[i] = (node, [(neighbor, weight)])
        i = (i+1) % map.capacity
        while i != check_for_full and found == False:
            if map.data[i][0] == " ":
                found = True
                map.data[i] = (node, [(neighbor, weight)])
                break
            i = (i+1) % map.capacity

    return map


def get_neighbors(hash_map: HashMap, node: str) -> list[tuple[str, int]]:

    neighbors = []
    i = hash_function(node, hash_map.capacity)
    if hash_map.data[i][0] == node:
        for neighbor in hash_map.data[i][1]:
            neighbors.append(neighbor)
    else:
        check_for_full_loop = i
        found = False
        if hash_map.data[i][0] == node:
            found = True
            for neighbor in hash_map.data[i][1]:
                neighbors.append(neighbor)
        i = (i+1) % hash_map.capacity
        while i != check_for_full_loop and found == False:
            if hash_map.data[i][0] == node:
                found = True
                for neighbor in hash_map.data[i][1]:
                    neighbors.append(neighbor)
                break
            i = (i+1) % hash_map.capacity

    return neighbors



from dataclasses import dataclass, field

@dataclass(frozen=True) 

class MinHeap:
    data: list[tuple[str, int]] = field(default_factory=list)

def heapify_up(heap: MinHeap, index: int) -> MinHeap:
    if index == 0:
        return heap
    parent_index = (index - 1) // 2
    heap_data = heap.data
    if heap_data[index][1] < heap_data[parent_index][1]:
        new_heap_data = heap_data[:]
        new_heap_data[index], new_heap_data[parent_index] = new_heap_data[parent_index], new_heap_data[index]
        return heapify_up(MinHeap(new_heap_data), parent_index)
    else:
        return heap

def insert(heap: MinHeap, element: tuple[str, int]) -> MinHeap:
    new_heap_data = heap.data[:] + [element]
    last_index = len(new_heap_data) - 1
    new_heap = heapify_up(MinHeap(new_heap_data), last_index)
    return new_heap

def heapify_down(heap: MinHeap, index: int) -> MinHeap:
    heap_data = heap.data
    current_size = len(heap_data)
    smallest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < current_size and heap_data[left][1] < heap_data[smallest][1]:
        smallest = left

    if right < current_size and heap_data[right][1] < heap_data[smallest][1]:
        smallest = right

    if smallest != index:
        new_heap_data = heap_data[:]
        new_heap_data[index], new_heap_data[smallest] = new_heap_data[smallest], new_heap_data[index]
        return heapify_down(MinHeap(new_heap_data), smallest)
    else:
        return heap

def extract_min(heap: MinHeap) -> tuple[MinHeap, tuple[str, int]]:
    if not heap.data:
        raise ValueError("Heap is empty")

    min_element = heap.data[0]
    new_heap_data = heap.data[:]
    last_index = len(new_heap_data) - 1
    new_heap_data[0] = new_heap_data[last_index]
    new_heap_data = new_heap_data[:last_index]
    new_heap = heapify_down(MinHeap(new_heap_data), 0)
    return new_heap, min_element

def enqueue(heap: MinHeap, element: tuple[str, int]) -> MinHeap:
    return insert(heap, element)

def dequeue(heap: MinHeap) -> tuple[MinHeap, tuple[str, int]]:
    return extract_min(heap)


def dijkstra(graph: HashMap, start: str) -> tuple[dict[str, float], dict[str, str]]:
    distances = {n: float('infinity') for n, _ in graph.data if n != ' '}
    distances[start] = 0
    parents = {n: None for n, _ in graph.data if n != ' '}
    parents[start] = start
    pq = MinHeap()
    pq = enqueue(pq, (start, 0))

    while pq.data:
        print(pq)
        pq, (current_vertex, current_distance) = dequeue(pq)
        neighbors = get_neighbors(graph, current_vertex)

        for neighbor, weight in neighbors:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_vertex
                pq = enqueue(pq, (neighbor, distance))

    return distances, parents

# Example usage:
"""
graph = HashMap(capacity=4)
graph = insert_edge(graph, "A", "B", 4)
graph = insert_edge(graph, "A", "C", 1)
graph = insert_edge(graph, "B", "D", 1)
graph = insert_edge(graph, "C", "B", 2)
graph = insert_edge(graph, "C", "D", 5)
graph = insert_edge(graph, "D", "C", 1)
print(graph)
distances, parents = dijkstra(graph, "A")
print(distances)  # Output: {'A': 0, 'B': 3, 'C': 1, 'D': 4}
print(parents)    # Output: {'A': 'A', 'B': 'C', 'C': 'A', 'D': 'B'}
"""
