# 线段树
线段树（Segment Tree） 是一种高级数据结构，常用于处理**区间查询**和**区间更新**问题。它能够在 O(log n) 的时间复杂度内进行区间求和、区间最值等查询操作，并支持在 O(log n) 的时间内对区间内元素进行修改。线段树广泛应用于需要快速进行区间操作的场景，如求**区间和、区间最小值、区间最大值**等。

* 线段树的基本结构
线段树通常用于处理一维数组上的区间查询问题。其基本思路是将数组划分成多个区间，并通过二叉树的结构表示这些区间。每个节点存储一个区间的值（如区间和、区间最小值等）。

* 线段树的特点：
    * 构建时间复杂度： O(n)
    * 查询时间复杂度： O(log n)
    * 更新时间复杂度： O(log n)
* 线段树的构建: 假设我们有一个长度为 n 的数组，并希望实现如下操作：
    * 区间查询：求区间 [l, r] 的某种结果（如求和、最小值、最大值等）。
    * 区间更新：修改区间中的某些值。
为了实现这些操作，线段树需要将数组划分为多个区间，每个区间可以进一步递归划分为更小的子区间，直到每个区间只包含一个元素。

* 线段树的基本操作：
    * 构建树： 根据原数组构建线段树，树的叶子节点表示数组的元素，内部节点表示区间的某种结果（如区间和、区间最小值等）。
    * 查询操作： 根据查询的区间，使用线段树来合并节点的结果，从而快速得到区间的结果。
    * 更新操作： 更新某个元素或区间的值，并相应地调整线段树。

* 代码模板: 线段树的实现（以区间和为例）
以下是一个简单的线段树实现，支持区间求和查询和单点更新：
```python
    class SegmentTree:
        def __init__(self, arr):
            """
            初始化线段树
            :param arr: 输入的数组，用于构建线段树
            """
            self.n = len(arr)  # 数组的大小
            self.tree = [0] * (4 * self.n)  # 线段树数组，大小为 4n（防止树过深）
            self.build(arr, 0, 0, self.n - 1)  # 从根节点开始构建线段树，根节点在0，构建区间为[0, n-1]；[左闭右闭]区间

        def build(self, arr, node, start, end):
            """
            构建线段树
            :param arr: 输入的数组
            :param node: 当前节点的索引
            :param start: 当前节点对应区间的起始索引
            :param end: 当前节点对应区间的结束索引
            """
            if start == end:
                # 如果当前节点对应的区间只有一个元素（即叶子节点）
                self.tree[node] = arr[start]  # 将数组中的元素存入叶子节点
            else:
                # 计算中间索引，将区间分成左右两个子区间
                mid = (start + end) // 2
                left_child = 2 * node + 1  # 左子节点的索引
                right_child = 2 * node + 2  # 右子节点的索引

                # 递归地构建左右子树
                self.build(arr, left_child, start, mid)
                self.build(arr, right_child, mid + 1, end)

                # 更新当前节点的值，表示当前区间的总和
                self.tree[node] = self.tree[left_child] + self.tree[right_child]

        def query(self, node, start, end, L, R):
            """
            区间查询：返回区间 [L, R] 的和
            :param node: 当前节点的索引
            :param start: 当前节点对应区间的起始索引
            :param end: 当前节点对应区间的结束索引
            :param L: 查询区间的左端点
            :param R: 查询区间的右端点
            :return: 区间 [L, R] 的和
            """
            # 如果查询区间完全不在当前节点的区间内
            if R < start or end < L: # 即：[start, end] < [L, R] 或者 [L, R] < [start, end]
                return 0  # 返回 0，表示不贡献任何值

            # 如果查询区间完全在当前节点的区间内；
            # 这种方式不重不漏【充要条件】：
            #   只有符合区间完全被查询范围覆盖才会返回
            #   另外只要有重叠或者相交，就会继续细分查询，因此一定所有满足的小区间都会被选中并且返回
            if L <= start and end <= R: # 即 [L, ..., start, ..., end, ..., R]
                return self.tree[node]  # 返回当前节点存储的值

            # 如果查询区间与当前节点的区间部分重叠
            mid = (start + end) // 2
            left_child = 2 * node + 1  # 左子节点的索引
            right_child = 2 * node + 2  # 右子节点的索引

            # 分别查询左右子树
            left_sum = self.query(left_child, start, mid, L, R)
            right_sum = self.query(right_child, mid + 1, end, L, R)

            # 返回左右子树查询结果的合并
            return left_sum + right_sum

        def update(self, node, start, end, pos, new_val):
            """
            单点更新：将数组中的元素 arr[pos] 更新为 new_val
            :param node: 当前节点的索引
            :param start: 当前节点对应区间的起始索引
            :param end: 当前节点对应区间的结束索引
            :param pos: 要更新的位置
            :param new_val: 新的值
            """
            if start == end:
                # 到达叶子节点，更新该位置的值
                self.tree[node] = new_val
            else:
                mid = (start + end) // 2
                left_child = 2 * node + 1  # 左子节点的索引
                right_child = 2 * node + 2  # 右子节点的索引

                if start <= pos <= mid:
                    # 如果 pos 位于左子树
                    self.update(left_child, start, mid, pos, new_val)
                else:
                    # 如果 pos 位于右子树
                    self.update(right_child, mid + 1, end, pos, new_val)

                # 更新当前节点的值，重新计算该区间的和
                self.tree[node] = self.tree[left_child] + self.tree[right_child]

    # 示例
    arr = [1, 3, 5, 7, 9, 11]
    segment_tree = SegmentTree(arr)  # 构建线段树

    # 查询区间 [1, 3] 的和
    print(segment_tree.query(0, 0, len(arr) - 1, 1, 3))  # 输出 15

    # 更新数组第 2 个元素为 10
    segment_tree.update(0, 0, len(arr) - 1, 2, 10)

    # 查询区间 [1, 3] 的和（更新后）
    print(segment_tree.query(0, 0, len(arr) - 1, 1, 3))  # 输出 20

    """
                                   [36] (sum of [1, 3, 5, 7, 9, 11])
                             /                          \
                     [9] (sum of [1, 3, 5])           [27] (sum of [7, 9, 11])
                    /          \                      /              \
              [4] (sum of [1, 3])  [5] (sum of [5]) [16] (sum of [7, 9]) [11] (sum of [11])
             /      \                                               /
        [1] (arr[0]) [3] (arr[1])                                  [7] (arr[3])
                                                               /         \
                                                      [9] (arr[4]) [11] (arr[5])

    """

```
* 懒操作

    在处理线段树时，常常会遇到“区间更新”的问题，即需要对某个区间内的所有元素执行某种操作（例如加法、赋值等）。在这种情况下，如果每次都更新区间内的每个元素，线段树的效率会大幅下降。为了解决这个问题，我们引入了 懒操作（Lazy Propagation）。

    懒操作的基本思路是：**延迟更新**，即只在必要时才进行更新。具体来说，当我们对某个区间进行更新时，我们不会立即更新所有相关的节点，而是将更新的信息保存在一个额外的懒标记数组中，只有当查询或更新这些区间时，才会实际进行更新。

    1. 懒操作线段树的思路
        * 懒标记：对于每个节点，我们维护一个懒标记数组，表示该节点的子树是否需要更新。当某个节点的子树需要更新时，我们将更新信息推迟到子节点，并通过懒标记延迟传播。
        * 懒更新：如果当前节点的懒标记不为零，我们需要将其值更新到该节点的左右子树，之后再清空该节点的懒标记。

    2. 懒操作线段树的基本操作：
        * 区间更新（Lazy Propagation）：将一个区间的更新推迟到子节点。
        * 查询：查询时需要先进行懒更新，确保查询时的数据是最新的。
        * 更新：如果更新的是区间中的某一部分，先标记懒标记，延迟更新，直到需要用到该区间时再更新。
        
    3. Python实现带懒操作的线段树
        
        下面是一个实现了懒操作的线段树，支持 区间加法更新 和 区间求和查询：
        ```python
        class LazySegmentTree:
            def __init__(self, arr):
                """
                初始化懒操作线段树
                :param arr: 输入的数组，用于构建线段树
                """
                self.n = len(arr)
                self.tree = [0] * (4 * self.n)  # 线段树数组
                self.lazy = [0] * (4 * self.n)  # 懒标记数组
                self.build(arr, 0, 0, self.n - 1)  # 从根节点开始构建线段树

            def build(self, arr, node, start, end):
                """
                构建线段树
                :param arr: 输入的数组
                :param node: 当前节点的索引
                :param start: 当前节点对应区间的起始索引
                :param end: 当前节点对应区间的结束索引
                """
                if start == end:
                    # 如果当前节点对应的区间只有一个元素（即叶子节点）
                    self.tree[node] = arr[start]
                else:
                    mid = (start + end) // 2
                    left_child = 2 * node + 1  # 左子节点的索引
                    right_child = 2 * node + 2  # 右子节点的索引

                    # 递归地构建左右子树
                    self.build(arr, left_child, start, mid)
                    self.build(arr, right_child, mid + 1, end)

                    # 更新当前节点的值（区间的和）
                    self.tree[node] = self.tree[left_child] + self.tree[right_child]

            def update_range(self, node, start, end, L, R, val):
                """
                区间更新：对区间 [L, R] 进行加法更新，将区间内的每个元素加上 val
                :param node: 当前节点的索引
                :param start: 当前节点对应区间的起始索引
                :param end: 当前节点对应区间的结束索引
                :param L: 更新区间的左端点
                :param R: 更新区间的右端点
                :param val: 要加的值
                """
                if self.lazy[node] != 0:
                    # 如果当前节点有懒标记，先处理懒标记
                    self.tree[node] += (end - start + 1) * self.lazy[node]  # 更新当前节点的值
                    if start != end:
                        # 如果不是叶子节点，将懒标记传递给左右子节点
                        self.lazy[2 * node + 1] += self.lazy[node]
                        self.lazy[2 * node + 2] += self.lazy[node]
                    # 清除当前节点的懒标记
                    self.lazy[node] = 0

                if start > end or start > R or end < L:
                    # 当前区间不在更新范围内，直接返回
                    return

                if start >= L and end <= R:
                    # 当前区间完全在更新范围内，直接更新
                    self.tree[node] += (end - start + 1) * val
                    if start != end:
                        # 将懒标记传递给左右子节点
                        self.lazy[2 * node + 1] += val
                        self.lazy[2 * node + 2] += val
                    return

                # 如果当前区间部分在更新范围内，递归更新左右子树
                mid = (start + end) // 2
                self.update_range(2 * node + 1, start, mid, L, R, val)
                self.update_range(2 * node + 2, mid + 1, end, L, R, val)

                # 更新当前节点的值
                self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

            def query_range(self, node, start, end, L, R):
                """
                区间查询：查询区间 [L, R] 的和
                :param node: 当前节点的索引
                :param start: 当前节点对应区间的起始索引
                :param end: 当前节点对应区间的结束索引
                :param L: 查询区间的左端点
                :param R: 查询区间的右端点
                :return: 区间 [L, R] 的和
                """
                if self.lazy[node] != 0:
                    # 如果当前节点有懒标记，先处理懒标记
                    self.tree[node] += (end - start + 1) * self.lazy[node]
                    if start != end:
                        # 如果不是叶子节点，将懒标记传递给左右子节点
                        self.lazy[2 * node + 1] += self.lazy[node]
                        self.lazy[2 * node + 2] += self.lazy[node]
                    # 清除当前节点的懒标记
                    self.lazy[node] = 0

                if start > end or start > R or end < L:
                    # 当前区间不在查询范围内，返回 0
                    return 0

                if start >= L and end <= R:
                    # 当前区间完全在查询范围内，直接返回
                    return self.tree[node]

                # 如果当前区间部分在查询范围内，递归查询左右子树
                mid = (start + end) // 2
                left_sum = self.query_range(2 * node + 1, start, mid, L, R)
                right_sum = self.query_range(2 * node + 2, mid + 1, end, L, R)
                return left_sum + right_sum

        # 示例
        arr = [1, 3, 5, 7, 9, 11]
        seg_tree = LazySegmentTree(arr)

        # 查询区间 [1, 3] 的和
        print(seg_tree.query_range(0, 0, len(arr) - 1, 1, 3))  # 输出 15

        # 对区间 [1, 3] 加 10
        seg_tree.update_range(0, 0, len(arr) - 1, 1, 3, 10)

        # 查询区间 [1, 3] 的和（更新后）
        print(seg_tree.query_range(0, 0, len(arr) - 1, 1, 3))  # 输出 45

        # 查询整个区间的和
        print(seg_tree.query_range(0, 0, len(arr) - 1, 0, 5))  # 输出 66
        ```