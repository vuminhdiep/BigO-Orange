# import heapq
#
#
#
# def kahn(adj, in_degree):
#     zero_in_degree = min_heap()
#     topo = []
#
#     for i in range(1,n):
#         if in_degree[i] == 0:
#             zero_in_degree.push(i)
#
#     while not zero_in_degree.empty():
#         u = zero_in_degree.top()
#         zero_in_degree.pop()
#         topo.append(u)
#
#         for v in adj[u]:
#             in_degree[v] -= 1
#             if in_degree[v] == 0:
#                 zero_in_degree.push(v)
#
#     return topo
#
# def main():
#     n, m = map(int, input().split())
#
#     adj = [[], [], [], ...]
#     in_degree = [0, 0, ...]
#
#     for i = 0 -> m - 1:
#         read(u, v)
#         adj[u].append(v)
#         in_degree[v] + +
#
#     topo = kahn(adj, in_degree)
#
#     if topo.size < n:
#         print("sandro fails.")
#     else:
#     for e in topo:
#         print(e)