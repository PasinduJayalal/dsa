class Graph:
    def __init__(self, nodes=None):
        self.nodes = nodes 
        self.path = {}
        
        for start , end in self.nodes:
            if start in self.path:
                self.path[start].append(end)
            else:
                self.path[start] = [end]
        print("Graph:", self.path)
        
    def get_paths(self , start, end , path = []):
        path = path + [start]
        
        if start not in self.path:
            return None
        
        if start == end:
            return path
        paths = []
        for node in self.path[start]:
            if node not in path:
                new_path = self.get_paths(node, end, path)
                for p in new_path:
                    paths.append(p)
                    
        return paths
                
    def shortest_path(self , start, end, path = []):
        path = path + [start]
        
        
        if start not in self.path:
            return None
        
        if start == end:
            return path
        
        
        shortest_path = []
        
        for node in self.path[start]:
            if node not in path:
                sp = self.shortest_path(node, end, path)
                if sp:
                    # if shortest_path is None or len(sp) < len(shortest_path):
                    #     shortest_path = sp
                    if len(shortest_path) == 0:
                        shortest_path = sp
                    if len(sp) < len(shortest_path):
                        shortest_path = sp
                    
        return shortest_path
    

if __name__ == "__main__":
    
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    
    
    graph = Graph(routes)
    
    # print(graph.get_paths("Mumbai", "New York"))
    print(graph.shortest_path("Mumbai", "New York"))
  
    
    
    
    