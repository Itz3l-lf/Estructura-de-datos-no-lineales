class AdjNode(object):
    def __init__(self, data):
        self.vertex = data
        self.next = None

class AdjList(object):

    def __init__(self, vertices):
        self.v = vertices
        self.graph = [None] * self.v

    def addedge(self, source, destination):
        node = AdjNode(destination)
        node.next = self.graph[source]
        self.graph[source] = node
 
    def addvertex(self, vk, source, destination):
        self.addedge(source, vk)
        self.addedge(vk, destination)

    def print_graph(self):
        for i in range(self.v):
            print(i, end=" ")
            temp = self.graph[i]
            while temp:
                print("->", temp.vertex, end=" ")
                temp = temp.next
            print("\n")

    def delVertex(self, k):
        for i in range(self.v):
            curr = self.graph[i]
            prev = None

            if i == k:
                self.graph[i] = None
            else:
                while curr is not None:
                    if curr.vertex == k:
                        if prev is None:
                 
                            self.graph[i] = curr.next
                        else:
                            prev.next = curr.next
                        break
                    prev = curr
                    curr = curr.next

if __name__ == "__main__":

    V = 6
    graph = AdjList(V)
    graph.addedge(0, 1)
    graph.addedge(0, 3)
    graph.addedge(0, 4)
    graph.addedge(1, 2)
    graph.addedge(3, 2)
    graph.addedge(4, 3)

    print("Initial adjacency list")
    graph.print_graph()

    graph.addvertex(5, 3, 2)
    print("Adjacency list after adding vertex")
    graph.print_graph()

    graph.delVertex(4)
    print("Adjacency list after deleting vertex")
    graph.print_graph()