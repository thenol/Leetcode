'''
[medium]

For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

Output: [1]
Example 2 :

Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

Output: [3, 4]
Note:

According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-height-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# version 1: TLE
from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        size=n
        adj=defaultdict(list)
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        root=0
        res=[]
        for i in range(n):
            vis=[0]*n
            self.mn=0
            level=0
            self.dfs(adj,i,size,vis,level)
            res.append(self.mn)
        mini=min(res)
        ret=[]
        for k,v in enumerate(res):
            if v==mini:
                ret.append(k)
        return ret

    def dfs(self,adj,v,size,vis,level):
        vis[v]=1
        self.mn=max(self.mn,level)#  the altitude of tree, use max
        for n in adj[v]:
            if not vis[n]:
                self.dfs(adj,n,size,vis,level+1)

# version 2:
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        e = collections.defaultdict(set)        #字典初始化为集合
        for i, j in edges:
            e[i] |= {j}                         #把边哈希化，方便调用
            e[j] |= {i}
        q = {i for i in e if len(e[i]) == 1}    #建立初始宽搜队列，长度为1时代表只连接一个点
        while n > 2:
            t = set()                   #临时队列
            for i in q:
                j = e[i].pop()          #把连接点取出
                e[j] -= {i}             #连接是双向的，所以要删除关系
                if len(e[j]) == 1:      #更新后，如果长度为1时则加入下一个轮队列
                    t |= {j}   
                n -= 1                  #删除计数
            q = t
        return list(q)
# 很容易证明：每次从外往里递减一个层次，最后一个或者两个节点的高度必然相同
# 作者：tuotuoli
# 链接：https://leetcode-cn.com/problems/minimum-height-trees/solution/kuan-sou-bo-yang-cong-quan-ji-he-cao-zuo-by-tuotuo/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。