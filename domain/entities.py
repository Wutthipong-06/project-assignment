class Node:
    # ฟังก์ชั่นสร้าง Node 
    def __init__ (self, name: str):
        self.name = name

class Edge:
    # ฟังก์ชั่นสร้าง Edge 
    def __init__ (self, source: str, target: str, weight: int):
        self.source = source
        self.target = target
        self.weight = weight

class Graph:
    # ฟังก์ชั่นสร้าง Graph 
    def __init__ (self):
        self.nodes = []
        self.edges = []
