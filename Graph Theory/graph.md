## 图论

### 图的遍历算法

* BFS（广度优先搜索）
    ```python

    from collections import deque

    # 定义BFS函数，参数包括图、起始顶点和目标顶点
    def bfs(graph, start, goal):
        visited = set()  # 创建一个集合来记录访问过的顶点
        queue = deque([start])  # 创建一个队列，并将起始顶点加入队列

        # 当队列不为空时，继续遍历
        while queue:
            vertex = queue.popleft()  # 从队列中取出一个顶点
            if vertex == goal:  # 如果当前顶点是目标顶点，则返回True
                return True
            if vertex not in visited:  # 如果当前顶点未被访问过
                visited.add(vertex)  # 将当前顶点标记为已访问
                # 遍历当前顶点的所有邻居，并将未访问过的邻居加入队列
                for neighbor in graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return False  # 如果遍历完所有顶点仍未找到目标顶点，返回False

    # 示例图，使用字典表示图的邻接表
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    # 使用BFS检查从A到F是否存在路径
    print(bfs(graph, 'A', 'F'))  # 输出：True
    ```

* DFS（深度优先搜索）代码示例（非递归）
    ```python
    from collections import deque

    # 定义DFS函数，参数包括图、起始顶点、目标顶点和已访问集合
    def dfs(graph, start, goal):
        visited = set()  # 创建一个集合来记录访问过的顶点
        stack = deque([start])  # 创建一个栈，并将起始顶点加入栈

        # 当栈不为空时，继续遍历
        while stack:
            vertex = stack.pop()  # 从栈中取出一个顶点
            if vertex == goal:  # 如果当前顶点是目标顶点，则返回True
                return True
            if vertex not in visited:  # 如果当前顶点未被访问过
                visited.add(vertex)  # 将当前顶点标记为已访问
                # 遍历当前顶点的所有邻居，并将未访问过的邻居加入栈
                for neighbor in reversed(graph[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return False  # 如果遍历完所有顶点仍未找到目标顶点，返回False

    # 示例图，使用字典表示图的邻接表
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    # 使用DFS检查从A到F是否存在路径
    print(dfs(graph, 'A', 'F'))  # 输出：True
    ```
* DFS（深度优先搜索）代码示例（递归）
    ```python
    # 定义DFS函数，参数包括图、起始顶点、目标顶点和已访问集合
    def dfs(graph, start, goal, visited=None):
        if visited is None:  # 如果未提供已访问集合，则创建一个新的集合
            visited = set()
        visited.add(start)  # 将当前顶点标记为已访问
        if start == goal:  # 如果当前顶点是目标顶点，则返回True
            return True
        # 遍历当前顶点的所有邻居
        for neighbor in graph[start]:
            if neighbor not in visited:  # 如果邻居未被访问过
                if dfs(graph, neighbor, goal, visited):  # 递归调用DFS
                    return True
        return False  # 如果遍历完所有顶点仍未找到目标顶点，返回False

    # 示例图，使用字典表示图的邻接表
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    # 使用DFS检查从A到F是否存在路径
    print(dfs(graph, 'A', 'F'))  # 输出：True
    ```
