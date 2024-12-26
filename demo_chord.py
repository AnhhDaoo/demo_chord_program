import bisect

class Chord:
    def __init__(self, m):
        self.m = m  # Số bit của ID
        self.max_id = 2 ** m
        self.nodes = []
    
    def add_node(self, node_id):
        if node_id < 0 or node_id >= self.max_id:
            raise ValueError(f"Node ID phải trong khoảng [0, {self.max_id -1}]")
        if node_id in self.nodes:
            raise ValueError(f"Node ID {node_id} đã tồn tại")
        bisect.insort(self.nodes, node_id)
        print(f"Thêm nút: {node_id}")
    
    def remove_node(self, node_id):
        index = bisect.bisect_left(self.nodes, node_id)
        if index < len(self.nodes) and self.nodes[index] == node_id:
            self.nodes.pop(index)
            print(f"Xóa nút: {node_id}")
        else:
            raise ValueError(f"Node ID {node_id} không tồn tại")
    
    def find_successor(self, key):
        if not self.nodes:
            return None
        index = bisect.bisect_right(self.nodes, key)
        if index == len(self.nodes):
            return self.nodes[0]  # Vòng quay
        return self.nodes[index]
    
    def display_ring(self):
        print("Vòng Chord hiện tại:", self.nodes)

# Hàm test các test case
def test_chord():
    print("=== Khởi tạo Chord với m=3 ===")
    chord = Chord(m=3)
    # Thêm các nút: 0,1,3,4,6
    chord.add_node(0)
    chord.add_node(1)
    chord.add_node(3)
    chord.add_node(4)
    chord.add_node(6)
    chord.display_ring()
    
    # Test Case 1: Tìm chủ sở hữu của key=2
    key = 2
    owner = chord.find_successor(key)
    print(f"Chủ sở hữu của key {key} là: N{owner}")
    
    # Test Case 2: Tìm chủ sở hữu của key=5
    key = 5
    owner = chord.find_successor(key)
    print(f"Chủ sở hữu của key {key} là: N{owner}")
    
    # Test Case 3: Tìm chủ sở hữu của key=7
    key = 7
    owner = chord.find_successor(key)
    print(f"Chủ sở hữu của key {key} là: N{owner}")

if __name__ == "__main__":
    test_chord()
