'''
Given a tree (i.e. a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. The root of the tree is the node 0, and each node of the tree has a label which is a lower-case character given in the string labels (i.e. The node with the number i has the label labels[i]).

The edges array is given on the form edges[i] = [ai, bi], which means there is an edge between nodes ai and bi in the tree.

Return an array of size n where ans[i] is the number of nodes in the subtree of the ith node which have the same label as node i.

A subtree of a tree T is the tree consisting of a node in T and all of its descendant nodes.

 

Example 1:


Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"
Output: [2,1,1,1,1,1,1]
Explanation: Node 0 has label 'a' and its sub-tree has node 2 with label 'a' as well, thus the answer is 2. Notice that any node is part of its sub-tree.
Node 1 has a label 'b'. The sub-tree of node 1 contains nodes 1,4 and 5, as nodes 4 and 5 have different labels than node 1, the answer is just 1 (the node itself).
Example 2:


Input: n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"
Output: [4,2,1,1]
Explanation: The sub-tree of node 2 contains only node 2, so the answer is 1.
The sub-tree of node 3 contains only node 3, so the answer is 1.
The sub-tree of node 1 contains nodes 1 and 2, both have label 'b', thus the answer is 2.
The sub-tree of node 0 contains nodes 0, 1, 2 and 3, all with label 'b', thus the answer is 4.
Example 3:


Input: n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"
Output: [3,2,1,1,1]
Example 4:

Input: n = 6, edges = [[0,1],[0,2],[1,3],[3,4],[4,5]], labels = "cbabaa"
Output: [1,2,1,1,2,1]
Example 5:

Input: n = 7, edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]], labels = "aaabaaa"
Output: [6,5,4,1,3,2,1]
 

Constraints:

1 <= n <= 10^5
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
labels.length == n
labels is consisting of only of lower-case English letters.
'''

# version 1: find out, then statistics : TLE
from collections import defaultdict,Counter
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree=defaultdict(list)
        nodes=set()
        nodes.add(0)
        for e in edges:
            if e[0] in nodes:
                tree[e[0]].append(e[1])
                nodes.add(e[1])
            else:
                tree[e[1]].append(e[0])
        # print(tree)
        for i in range(n):
            if i not in tree:
                tree[i].append(None)
        self.lab=[0]*n
        res=self.post_order(tree,0,labels)
        self.lab[0]=res
        ret=[]
        print(self.lab)
        for i in range(n):
            if self.lab[i]:
                c=Counter(self.lab[i])
                # print(i,c)
                ret.append(c[labels[i]])
            else:
                ret.append(1)
        return ret
        
    def post_order(self,tree,v,labels):
        if len(tree[v])==1 and tree[v][0]==None:
            return [labels[v]]
        else:
            res=[]
            for node in tree[v]:
                if node:
                    res+=self.post_order(tree,node,labels)
            res+=[labels[v]]
        self.lab[v]=res
        return res
    
        

# version 2: Statistics for each node
from collections import defaultdict,Counter
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree=defaultdict(list)
        nodes=set()
        nodes.add(0)
        for e in edges:
            if e[0] in nodes:
                tree[e[0]].append(e[1])
                nodes.add(e[1])
            else:
                tree[e[1]].append(e[0])
        # print(tree)
        for i in range(n):
            if i not in tree:
                tree[i].append(None)
        self.lab=[0]*n
        res=self.post_order(tree,0,labels)
        self.lab[0]=res
        ret=[]
        self.lab[0]=self.lab[0][labels[0]]
        return self.lab
        
    def post_order(self,tree,v,labels):
        if len(tree[v])==1 and tree[v][0]==None:
            self.lab[v]=1
            return {labels[v]:1}
        else:
            res=defaultdict(int)
            for node in tree[v]:
                if node:
                    dic=self.post_order(tree,node,labels)
                    for i,j in dic.items():
                        res[i]+=j
            res[labels[v]]+=1
        self.lab[v]=res[labels[v]]
        return res
        
            
        
        
            
        
        