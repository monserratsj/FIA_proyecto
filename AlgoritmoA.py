import numpy as np
from scipy.spatial import KDTree

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

def heuristic(node1, node2, mean_dist, mean_angle):
    dist = np.linalg.norm(np.array(node1) - np.array(node2))
    angle = np.arctan2(node2[1] - node1[1], node2[0] - node1[0])
    normalized_dist = dist / mean_dist
    normalized_angle = angle / mean_angle
    return normalized_dist + normalized_angle

def a_star(start, end, nodes):
    open_list = []
    closed_list = set()
    kd_tree = KDTree(nodes)

    start_node = Node(start)
    end_node = Node(end)
    
    open_list.append(start_node)
    
    mean_dist = np.mean([np.linalg.norm(np.array(n) - np.array(end)) for n in nodes])
    mean_angle = np.mean([np.arctan2(end[1] - n[1], end[0] - n[0]) for n in nodes])
    
    while open_list:
        open_list.sort(key=lambda x: x.f)
        current_node = open_list.pop(0)
        closed_list.add(tuple(current_node.position))
        
        if np.array_equal(current_node.position, end_node.position):
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        neighbors = kd_tree.query_ball_point(current_node.position, mean_dist * 1.5)
        for i in neighbors:
            neighbor = nodes[i]
            if tuple(neighbor) in closed_list:
                continue
            
            neighbor_node = Node(neighbor, current_node)
            neighbor_node.g = current_node.g + np.linalg.norm(np.array(current_node.position) - np.array(neighbor))
            neighbor_node.h = heuristic(neighbor, end, mean_dist, mean_angle)
            neighbor_node.f = neighbor_node.g + neighbor_node.h
            
            if any(open_node.position == neighbor_node.position and open_node.g < neighbor_node.g for open_node in open_list):
                continue
            
            open_list.append(neighbor_node)
    
    return None

# Ejemplo de uso:
nodes = [(0,0), (1,1), (2,2), (3,3), (4,4), (5,5)]
start = (0, 0)
end = (5, 5)
path = a_star(start, end, nodes)
print("Ruta encontrada:", path)
