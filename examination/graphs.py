from collections import deque

# Basically graph can be stored in two structures: adjacency list and adjacency matrix

# create some graph and fill its adjacency matrix and adjacency list
V, E = 10, 13

adjacency_matrix = [[0]*V for v in range(V)]
adjacency_matrix[0][1] = 1
adjacency_matrix[1][2] = 1
adjacency_matrix[2][3] = 1
adjacency_matrix[3][4] = 1
adjacency_matrix[4][5] = 1
adjacency_matrix[5][6] = 1
adjacency_matrix[6][7] = 1
adjacency_matrix[7][1] = 1
adjacency_matrix[0][8] = 1
adjacency_matrix[8][2] = 1
adjacency_matrix[8][6] = 1
adjacency_matrix[8][9] = 1
adjacency_matrix[9][5] = 1

adjacency_list = [[1, 8], [2], [3], [4], [5], [9, 6], [7], [0], [2, 9, 6], [5], [20, 21], [30, 35]] + [[]]*30


# Let's solve two basic graph search algorithms, DFS and BFS, using adjacency_list


def BFS(adjacency_list, start):
    """Just a simple BFS"""
    queue = deque()
    visited = set()
    queue.append(start)
    while queue:
        v = queue.popleft()
        visited.add(v)
        for vi in adjacency_list[v]:
            if vi not in visited:
                queue.append(vi)
    return visited


class DoDFS:
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start
        self.visited = set()

    def __call__(self, dfs_function):
        def wrapper():
            for v in range(len(self.graph)):
                if v not in self.visited:
                    dfs_function(self.graph, v, self.visited)
        return wrapper


def doDFS(dfs_function, graph, visited=set()):
    for v in range(len(graph)):
        if v not in visited:
            dfs_function(graph, v, visited)
    return visited


def DFS_recursive(graph, start, visited):
    visited.add(start)
    for v in graph[start]:
        if v not in visited:
            DFS_recursive(graph, v, visited)


def DFS_flat(graph, start, visited):
    stack = [start]
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            stack.extend(set(graph[current-1]) - visited)
    return visited

if __name__ == "__main__":
    print(BFS(adjacency_list, 0))
    print(doDFS(DFS_recursive, adjacency_list))
    print(doDFS(DFS_flat, adjacency_list))
