MAX = 100
def printColoring():
    for i in range(V):
        print("Vertex {} --> Color {}".format(i, result[i]))

def greedyColoring():
    for u in range(V):
        for neighbor in graph[u]:
            if result[neighbor] != -1:
                colors[result[neighbor]] = True

        for cr in range(V):
            if colors[cr] == False:
                result[u] = cr
                break

        for neighbor in graph[u]:
            if result[neighbor] != -1:
                colors[result[neighbor]] = False

if __name__ == '__main__':
    V, E = map(int, input().split())
    result = [-1 for i in range(V)]
    colors = [False for i in range(V)]
    graph = [[] for i in range(V)]
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    greedyColoring()
    printColoring()