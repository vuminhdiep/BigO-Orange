import queue


def topologicalSort(graph, result):
    indegree = [0] * V
    zero_indegree = queue.Queue()
    for u in range(V):
        for v in graph[u]:
            indegree[v] += 1

    for i in range(V):
        if indegree[i] == 0:
            zero_indegree.put(i)

    while not zero_indegree.empty():
        u = zero_indegree.get()
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                zero_indegree.put(v)

    for i in range(V):
        if indegree[i] != 0:
            return False

    return True


if __name__ == "__main__":
    V, E = map(int, input().split())
    graph = [[] for i in range(V)]
    result = []
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)

    if topologicalSort(graph, result):
        print('Topological Sort of graph:')
        for i in range(V):
            print(result[i], end=' ')

    else:
        print("No result")
