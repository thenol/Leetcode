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
            # 弹出队列中的第一个元素；✅出队列的时候再访问；
            # ❗️❗️❗️有个问题，会导致同一个节点被反复加入到队列中❗️❗️❗️
            # 参见 934. 最短的桥.py
            node = queue.popleft()  
            if node not in visited:
                print(node, end=" ")  # 访问该节点
                visited.add(node)  # 标记为已访问
                for neighbor in graph[node]:
                    if neighbor not in visited: # ✅如果没有被访问过再增加，否则会导致重复增加
                        queue.append(neighbor)  # 将未访问的邻居节点加入队列，❗️❗️❗️ 但是并没有对是否已经存在队列中进行判断；邓俊晖版本中有discover状态和undiscover状态，解决了这个问题

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
                for neighbor in reversed(graph[node]): # 因为用的是栈，后入先出，所以要想先访问第一个，需要反过来入栈；每次来到一个新节点，反过来访问，先访问第一个节点；与树的迭代式深度优先一致
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
    * 无权重的图中，层次遍历，先遍历到的节点，一定是最短路径，例如到C，1）A->B->C；2）A->C，则 A->C 一定是最短路径
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
                
                for i in range(level_length): # 和bfs以及dfs最大的区别在于，每次访问一个level
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

## Dijkstra算法
Dijkstra算法是一种用于计算单源最短路径的经典算法，由荷兰计算机科学家 Edsger W. Dijkstra 在 1956 年提出。它适用于带权有向图或无向图（包括带环图），且权重必须为非负数。Dijkstra算法通过贪心策略逐步找到从起点到所有其他节点的最短路径。
```python
import heapq

def dijkstra(graph, start):
    """
    Dijkstra 算法实现：计算从起点到图中所有节点的最短路径。

    参数:
    - graph: 图的邻接表表示，格式为 {节点: {邻居节点: 权重}}。
    - start: 起点节点。

    返回:
    - dist: 字典，表示从起点到每个节点的最短距离。
    """
    # 初始化距离字典
    # 将所有节点的距离设置为无穷大（表示尚未访问）
    dist = {node: float('inf') for node in graph}
    # 起点到自身的距离为 0
    dist[start] = 0
    
    # 优先队列（最小堆），用于存储待处理的节点及其当前距离
    # 堆中的元素是元组 (当前距离, 节点)
    heap = [(0, start)]
    
    # 主循环：处理堆中的节点
    while heap:
        # 从堆中取出距离起点最近的节点
        current_dist, u = heapq.heappop(heap)
        
        # 如果当前节点的距离大于已知的最短距离，跳过
        # ❗️这是因为堆中可能存储了同一节点的多个不同距离
        if current_dist > dist[u]:
            continue
        
        # 遍历当前节点的所有邻居节点
        for v, weight in graph[u].items(): # u点只能看到从start到u以及到达其相邻节点的情况，其他路径到达其相邻节点的情况u看不到
            # 计算从起点经过当前节点 u 到邻居节点 v 的新距离
            new_dist = dist[u] + weight
            
            # 如果新距离比已知的距离更短，更新距离并将邻居节点加入堆
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v)) # 先将 u->v 即从u到v的这条可能的最短候选路径先缓存起来
    
    # 返回从起点到所有节点的最短距离
    return dist
```
