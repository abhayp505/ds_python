
class Graph:

    def __init__(self):
        # self.edges = edges
        self.graph_dir={}
        # for start, end in edges:
        #     if start == end:
        #         return
        #     print("is present ::", start in self.graph_dir)
        #     if start in self.graph_dir:
        #         self.graph_dir[start].append(end)
        #     else:
        #         self.graph_dir[start] = [end]
        # print("graph_nodes ::", self.graph_dir)


    def add(self, edges):
        for start, end in edges:
            if start == end:
                return
            if start in self.graph_dir:
                self.graph_dir[start].append(end)
            else:
                self.graph_dir[start] = [end]
        return self.graph_dir



    def routes(self, start, end, path=[]):
        path = path + [start]
        if start not in self.graph_dir:
            return []
        if start == end:
            # path.append(start)
            return [path]
        else:
            paths = []
            for node in self.graph_dir[start]:
                if node not in path:
                    new_path = self.routes(node, end, path)
                    for p in new_path:
                        paths.append(p)
        return paths


    def routeWithLoop(self):
        return 0

if __name__ =='__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "New York"),
        ("Paris", "Dubai"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
        ]

graph=Graph()
graph_nodes =graph.add(routes)
path = graph.routes("Mumbai", "New York")
print("graph_nodes ::", graph_nodes)
print("path ::", path)

