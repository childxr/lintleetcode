"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
import Queue

class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        if not graph:
            return []
        
        mapper = {n.label: n for n in graph}
        degrees = {n.label: 0 for n in graph}
        
        for node in graph:
            for neighbor in node.neighbors:
                degrees[neighbor.label] += 1
        
        queue = Queue.Queue()
        
        for k, v in degrees.items():
            if v == 0:
                queue.put(k)
        
        ans = []
        
        while not queue.empty():
            cur = queue.get()
            ans.append(mapper[cur])
            for neighbor in mapper.get(cur).neighbors:
                degrees[neighbor.label] -= 1
                if degrees[neighbor.label] == 0:
                    queue.put(neighbor.label)
        
        return ans
            
