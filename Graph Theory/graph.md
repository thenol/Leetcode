# 图论

## 图的遍历算法【结合：邓俊辉版本《数据结构》】

* BFS（广度优先搜索）
    ```python

    # 定义BFS函数，参数包括图、起始顶点和目标顶点
    from collections import deque

    def bfs(graph, start):
        visited = set()  # 用于记录已访问的节点
        queue = deque([start])  # 队列初始化，开始节点入队

        while queue:
            node = queue.popleft()  # 弹出队列中的第一个元素
            if node not in visited:
                print(node, end=" ")  # 访问该节点
                visited.add(node)  # 标记为已访问
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)  # 将未访问的邻居节点加入队列

    # 示例图，使用字典表示图的邻接表
         A
        / \
       B   C
      / \   \
     D   E   F

    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B'],
        'F': ['C']
    }

    bfs(graph, 'A') # 输出： A B C D E F
    ```

* DFS（深度优先搜索）代码示例（非递归）
    ```python
    # 定义DFS函数，参数包括图、起始顶点、目标顶点和已访问集合
    def dfs_stack(graph, start):
        visited = set()  # 用于记录已访问的节点
        stack = [start]  # 初始化栈，起始节点入栈；后进先出

        while stack:
            node = stack.pop()  # 弹出栈顶元素
            if node not in visited:
                print(node, end=" ")  # 访问该节点
                visited.add(node)  # 标记为已访问
                for neighbor in reversed(graph[node]): # 每次来到一个新节点，反过来访问，先访问第一个节点；与树的迭代式深度优先一致
                    if neighbor not in visited:
                        stack.append(neighbor)  # 将未访问的邻居节点入栈
        
    """
    执行过程：
    
    A ['B', 'C']
    C ['B', 'F']
    F ['B']
    B ['D', 'E']
    E ['D']
    D []
    """
    ```
* DFS（深度优先搜索）代码示例（递归）
    ```python
    def dfs(graph, node, visited=None):
        if visited is None:
            visited = set()  # 初始化访问集合

        visited.add(node)  # 访问当前节点
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(graph, neighbor, visited)  # 递归访问邻居节点
    
    ```
* 总结：
    * BFS 适用于按层遍历图，通常用于找最短路径、层次遍历等问题，使用队列实现。
    * DFS 适用于深度遍历图，通常用于路径查找、拓扑排序、图的连通性检查等问题，可以通过递归或栈实现。

* 层次遍历【本质和树的层次遍历完全相同】
    ```python
    from collections import deque
    class Solution:
        def levelOrder(self, root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
            levels = []
            if not root:
                return levels
            
            level = 0
            queue = deque([root,]) #deque:双端队列
            while queue:
                # start the current level
                levels.append([])
                # number of elements in the current level 
                level_length = len(queue)
                
                for i in range(level_length):
                    node = queue.popleft()
                    # fulfill the current level
                    levels[level].append(node.val)
                    
                    # add child nodes of the current level
                    # in the queue for the next level
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            queue.append(neighbor)  # 将未访问的邻居节点加入队列
                
                # go to next level
                level += 1
            
            return levels
    ```
