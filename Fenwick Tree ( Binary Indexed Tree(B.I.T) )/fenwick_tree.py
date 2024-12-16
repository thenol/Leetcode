class FenwickTree:
    def __init__(self, n):
        """
        初始化一个大小为 n 的树状数组（Fenwick Tree），
        由于树状数组的下标从 1 开始，所以需要分配 n+1 的空间，
        其中索引 0 留空不用。
        """
        self.n = n
        self.tree = [0] * (n + 1)  # 初始化一个大小为 n+1 的数组

    def update(self, index, delta):
        """
        更新操作：将数组 index 位置的值增加 delta，
        时间复杂度为 O(log n)
        """
        while index <= self.n:
            self.tree[index] += delta  # 更新树状数组中对应的位置
            index += index & -index  # 更新父节点（父节点是 index + (index & -index)）

    def query(self, index):
        """
        查询操作：返回从 1 到 index 的前缀和，
        时间复杂度为 O(log n)
        """
        result = 0
        while index > 0:
            result += self.tree[index]  # 累加当前节点的值
            index -= index & -index  # 移动到父节点（父节点是 index - (index & -index)）
        return result

    def range_query(self, left, right):
        """
        范围查询：返回从 left 到 right 的区间和。
        通过两次查询来计算：sum(1, right) - sum(1, left - 1)
        """
        return self.query(right) - self.query(left - 1)
    

# 示例使用
if __name__ == "__main__":
    # 假设我们有一个大小为 10 的数组，初始化时所有元素都为 0
    fenwick_tree = FenwickTree(10)

    # 向位置 3 增加 5
    fenwick_tree.update(3, 5)
    print(fenwick_tree.query(3))  # 输出从 1 到 3 的前缀和，应该是 5

    # 向位置 5 增加 3
    fenwick_tree.update(5, 3)
    print(fenwick_tree.query(5))  # 输出从 1 到 5 的前缀和，应该是 8

    # 查询范围 3 到 5 的区间和
    print(fenwick_tree.range_query(3, 5))  # 输出 8
    print(fenwick_tree.range_query(4, 5))  # 输出 3
