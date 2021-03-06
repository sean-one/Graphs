"""
Simple graph implementation
"""

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# covert this to a link list later
class Queue():
    def __init__(self):
        self.queue = []
    def nq(self, value):
        self.queue.append(value)
    def dq(self):
        if self.size() > 0:
            return self.queue.pop()
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        pass  # TODO

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, edge_one, edge_two):
        if edge_one in self.vertices and edge_two in self.vertices:
            self.vertices[edge_one].add(edge_two)
            self.vertices[edge_two].add(edge_one)
        else:
            raise IndexError("That vertex does not exist")
        pass
    
    def bft(self, start):
        # create que
        q = Queue()
        # create visited
        visited = set()
        # que the start
        q.nq(start)
        # # while que not empty
        while q.size() > 0:
            # remove item from que
            node = q.dq()
            if node not in visited:
                # mark as visited / add to visited
                print(node)
                visited.add(node) 
                # add children to que
                for next_node in self.vertices[node]:
                    q.nq(next_node)
        pass
    
    def dft(self, start):
        # create a stack
        s = Stack()
        visited  = set()
        # push start
        s.push(start)
        # while stack is not empty
        while s.size() > 0:
            # pop a node from the stack
            node = s.pop()
            # if the node is not in visited
            if node not in visited:
                # mark it as visited
                print(node)
                visited.add(node)
                # push all children that have not been visited
                for next_node in self.vertices[node]:
                    s.push(next_node)
    
    def dft_r(self, start, visited=None):
        # python gotcha because of set method doesnt like to be passes as a default argument
        if visited is None:
            visited = set()
        # mark as visited
        visited.add(start)
        print(start)
        # recursively check the children
        for child in self.vertices[start]:
            if child not in visited:
                self.dft_r(child, visited)

    def bfs(self, start, target):
        # create que
        q = Queue()
        # create visited
        visited = set()
        # que the start
        q.nq(start)
        # # while que not empty
        while q.size() > 0:
            # remove item from que
            node = q.dq()
            if node not in visited:
                # mark as visited / add to visited
                if node == target:
                    return True
                visited.add(node)
                # add children to que
                for next_node in self.vertices[node]:
                    q.nq(next_node)
        return False
    
    def bfs_path(self, start, target):
        # create que
        q = []
        # create visited
        visited = set()
        # que the start
        path = [start]
        q.append(path)
        # while que not empty
        while len(q) > 0:
            # remove item from que
            current_path = q.pop(0)
            check = current_path[-1]
            if check not in visited:
                # mark as visited / add to visited
                if check == target:
                    return current_path
                visited.add(check)
                # add children to que
                for child in self.vertices[check]:
                    duplicate_cp = list(current_path)
                    duplicate_cp.append(child)
                    q.append(duplicate_cp)
        return False

    def dfs(self, start, target):
        # create a stack
        s = Stack()
        visited = set()
        # push start
        s.push(start)
        # while stack is not empty
        while s.size() > 0:
            # pop a node from the stack
            node = s.pop()
            # if the node is not in visited
            if node not in visited:
                if node == target:
                    return True
                # mark it as visited
                print(node)
                visited.add(node)
                # push all children that have not been visited
                for next_node in self.vertices[node]:
                    s.push(next_node)
        return False

    def dfs_path(self, start, target):
        # create a stack
        s = Stack()
        visited = set()
        # create a path
        path = [start]
        # push start
        s.push(path)
        # while stack is not empty
        while s.size() > 0:
            # pop a node from the stack
            current_path = s.pop()
            check = current_path[-1]
            # if the node is not in visited
            if check not in visited:
                if check == target:
                    return current_path
                # mark it as visited
                visited.add(check)
                # push all children that have not been visited
                for child in self.vertices[check]:
                    duplicate_cp = list(current_path)
                    duplicate_cp.append(child)
                    s.push(duplicate_cp)
        return False


# tester = Graph()
# tester.add_vertex('1')
# tester.add_vertex('2')
# tester.add_vertex('3')
# tester.add_vertex('4')
# tester.add_vertex('5')
# tester.add_vertex('6')
# tester.add_vertex('7')
# tester.add_vertex('8')
# tester.add_edge('1', '2')
# tester.add_edge('1', '3')
# tester.add_edge('1', '4')
# tester.add_edge('2', '4')
# tester.add_edge('2', '5')
# tester.add_edge('3', '6')
# tester.add_edge('4', '6')
# tester.add_edge('4', '7')
# tester.add_edge('5', '8')
# tester.add_edge('6', '7')
# tester.add_edge('7', '8')
# # print(tester.vertices)
# print(tester.dfs_path('1', '9'))
