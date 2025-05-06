* 前中后序遍历的递推通用方法：
    ```python
    # 中序遍历
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        对二叉树进行中序遍历（左-根-右），并返回遍历结果的列表。
        """
        WHITE, GRAY = 0, 1  # 定义两种颜色状态：白色表示节点尚未被访问，灰色表示节点已被访问但其子节点尚未完全处理
        res = []             # 初始化一个空列表，用于存储中序遍历的结果
        stack = [(WHITE, root)] # 初始化栈，将根节点标记为白色（未访问）并入栈

        # 循环直到栈为空，这意味着所有节点都已被处理
        while stack:
            color, node = stack.pop() # 从栈顶弹出一个元素，包含节点的颜色和节点本身

            # 如果弹出的节点为空，则跳过（表示遇到了叶子节点的子节点）
            if node is None:
                continue

            # 如果节点的颜色是白色，表示这是第一次访问该节点
            if color == WHITE:
                # 为了实现中序遍历（左-根-右），我们需要按照相反的顺序将相关节点压入栈中：
                # 1. 先压入右子节点（标记为白色），这样在处理完左子节点和当前节点后才会处理右子节点。
                stack.append((WHITE, node.right))
                # 2. 接着压入当前节点（标记为灰色），表示其左子树已经处理完毕，待其入栈后会被立即弹出并访问（将值加入结果列表）。
                stack.append((GRAY, node))
                # 3. 最后压入左子节点（标记为白色），这样会先处理左子树。
                stack.append((WHITE, node.left))
            # 如果节点的颜色是灰色，表示其左子树已经处理完毕，现在需要访问该节点（将其值加入结果列表）
            else:  # color == GRAY
                res.append(node.val) # 将当前节点的值添加到结果列表中

        return res # 返回最终的中序遍历结果列表

    # 前序遍历    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        对二叉树进行前序遍历（根-左-右），并返回遍历结果的列表。
        """
        WHITE, GRAY = 0, 1  # 定义两种颜色状态：白色表示节点尚未被访问，灰色表示节点已被访问但其子节点尚未完全处理
        res = []             # 初始化一个空列表，用于存储前序遍历的结果
        stack = [(WHITE, root)] # 初始化栈，将根节点标记为白色（未访问）并入栈

        # 循环直到栈为空，这意味着所有节点都已被处理
        while stack:
            color, node = stack.pop() # 从栈顶弹出一个元素，包含节点的颜色和节点本身

            # 如果弹出的节点为空，则跳过（表示遇到了叶子节点的子节点）
            if node is None:
                continue

            # 如果节点的颜色是白色，表示这是第一次访问该节点
            if color == WHITE:
                # 为了实现前序遍历（根-左-右），我们需要按照相反的顺序将相关节点压入栈中：
                # 1. 先压入右子节点（标记为白色），这样在处理完当前节点和左子节点后才会处理右子节点。
                stack.append((WHITE, node.right))
                # 2. 接着压入左子节点（标记为白色），这样会在处理完当前节点后立即处理左子节点。
                stack.append((WHITE, node.left))
                # 3. 最后压入当前节点（标记为灰色），表示该节点需要被访问（将值加入结果列表）。
                stack.append((GRAY, node))
            # 如果节点的颜色是灰色，表示该节点需要被访问（其子节点尚未入栈），现在将其值加入结果列表
            else:  # color == GRAY
                res.append(node.val) # 将当前节点的值添加到结果列表中

        return res # 返回最终的前序遍历结果列表

    # 后续遍历
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        对二叉树进行后序遍历（左-右-根），并返回遍历结果的列表。
        """
        WHITE, GRAY = 0, 1  # 定义两种颜色状态：白色表示节点尚未被访问，灰色表示节点已被访问但其子节点尚未完全处理
        res = []             # 初始化一个空列表，用于存储后序遍历的结果
        stack = [(WHITE, root)] # 初始化栈，将根节点标记为白色（未访问）并入栈

        # 循环直到栈为空，这意味着所有节点都已被处理
        while stack:
            color, node = stack.pop() # 从栈顶弹出一个元素，包含节点的颜色和节点本身

            # 如果弹出的节点为空，则跳过（表示遇到了叶子节点的子节点）
            if node is None:
                continue

            # 如果节点的颜色是白色，表示这是第一次访问该节点
            if color == WHITE:
                # 为了实现后序遍历（左-右-根），我们需要按照相反的顺序将相关节点压入栈中：
                # 1. 先压入当前节点（标记为灰色），表示其子节点需要先被处理，之后再处理自身。
                stack.append((GRAY, node))
                # 2. 接着压入右子节点（标记为白色），这样会在处理完左子节点后处理右子节点。
                stack.append((WHITE, node.right))
                # 3. 最后压入左子节点（标记为白色），这样会最先处理左子树。
                stack.append((WHITE, node.left))
            # 如果节点的颜色是灰色，表示其子节点已经处理完毕，现在需要访问该节点（将其值加入结果列表）
            else:  # color == GRAY
                res.append(node.val) # 将当前节点的值添加到结果列表中

        return res # 返回最终的后序遍历结果列表
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        核心思路：使用前序遍历的迭代方式，将 根->左->右，变换成 根->右->左
        然后逆序返回结果，极为 左->右->根，即后续遍历的迭代方式
        """
        ans = []
        if root is None:
            return ans
        
        stk = [root]
        while stk:
            node = stk.pop()
            if node:
                ans.append(node.val)
            if node.left:
                stk.append(node.left)
            if node.right:
                stk.append(node.right)
        
        return ans[::-1]

    ```
* 层次遍历
    ```python
        def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            if not root:
                return []
            q = [root]
            ans = []
            while q:
                w = len(q)
                lst = []
                for i in range(w):
                    node = q.pop(0)
                    lst.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                ans.append(lst)
            return ans
    ```