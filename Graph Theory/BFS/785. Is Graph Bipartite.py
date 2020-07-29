'''
[medium] the graph base theory

Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.
 

Note:

graph will have length in range [1, 100].
graph[i] will contain integers in range [0, graph.length - 1].
graph[i] will not contain i or duplicate values.
The graph is undirected: if any element j is in graph[i], then i will be in graph[j].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/is-graph-bipartite
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# version 1: BFS
from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        return self.bfs(graph,len(graph))
    def bfs(self,graph,n):
        vis=set()
        for v in range(n):
            if v not in vis and graph[v]:
                q=deque([v])
                s1=set()
                s2=set()
                s1.add(v)
                no=1
                dic={1:s1,2:s2}
                while q:
                    size=len(q)
                    no=2 if no==1 else (1 if no==2 else 2)
                    for i in range(size):
                        node=q.popleft()
                        for val in graph[node]:
                            if val not in vis:
                                q.append(val)
                                dic[no].add(val)
                                vis.add(val)
                            elif val not in dic[no]:
                                return False
                # print("s1:",s1,"\ns2:",s2)
        return True


# version 2:bfs color
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2
        color = [UNCOLORED] * n
        
        for i in range(n):
            if color[i] == UNCOLORED:
                q = collections.deque([i])
                color[i] = RED
                while q:
                    node = q.popleft()
                    cNei = (GREEN if color[node] == RED else RED)
                    for neighbor in graph[node]:
                        if color[neighbor] == UNCOLORED:
                            q.append(neighbor)
                            color[neighbor] = cNei
                        elif color[neighbor] != cNei:
                            return False

        return True

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/is-graph-bipartite/solution/pan-duan-er-fen-tu-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



        
    
