class SegmentTree():
    ...
# 示例
arr = [1, 3, 5, 7, 9, 11]
segment_tree = SegmentTree(arr)  # 构建线段树

# 查询区间 [1, 3] 的和
print(segment_tree.query(0, 0, len(arr) - 1, 1, 3))  # 输出 15

# 更新数组第 2 个元素为 10
segment_tree.update(0, 0, len(arr) - 1, 2, 10)

# 查询区间 [1, 3] 的和（更新后）
print(segment_tree.query(0, 0, len(arr) - 1, 1, 3))  # 输出 20
