# 树状数组
树状数组（Fenwick Tree 或 Binary Indexed Tree，简称 BIT）是一种用于高效处理前缀和问题的数据结构。它可以**在 O(logn) 时间内实现查询和更新操作**，相较于传统的线性扫描方法要高效得多。

* 树状数组的原理

    树状数组的核心思想是将数组拆分成多个区间，维护每个区间的和。每个节点的值代表了一个区间的和，通过低位与运算来高效地更新和查询前缀和。

    对于一个大小为 **n** 的数组，树状数组的大小通常是 **n + 1**，其中第一个元素（索引为0）是空的，其他位置存储着不同区间的和。

* 主要操作：
    * 更新操作：修改某个位置的值并更新所有受此影响的区间和。
    * 查询操作：查询数组中前 i 个元素的和。

* Python实现树状数组
    * 原理：
        <img src='../Z_Summary/resources/FIT.png'>
        * **每个节点覆盖范围**由所有的下标对应的 **`最低位1`** 形成的数决定即`lowbit(x)`=`(index&-index)`来计算得到
        * 任何一个节点的父节点计算`parent(x)=x+(index&-index)`，注意此图中，父节点是最后一个节点，如果反过来，公式即为`parent(x)=x-(index&-index)`
    * 下面是树状数组的 Python 代码实现，并且在代码中加入了详细的注释。
    ```python
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
            ❗️注意区间为 [1, index]，即左闭右闭
            """
            result = 0
            while index > 0:
                result += self.tree[index]  # 累加当前节点的值
                index -= index & -index  # 移动到下一个父节点（父节点是 index - (index & -index)）；这里注意每一个index覆盖的范围或者区间长度为lowbit(index)，因此当前index覆盖的区间累加完之后，其下一个应该跳转的index为 index - lowbit(index)，即index减去当前覆盖区间长度，来到下一个覆盖的区间长度 
            return result

        def range_query(self, left, right):
            """
            范围查询：返回从 left 到 right 的区间和。
            通过两次查询来计算：sum(1, right) - sum(1, left - 1)
            ❗️注意左闭右闭
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

    ```
# 树状数组中的父节点计算方式

在树状数组（Fenwick Tree，或 Binary Indexed Tree，BIT）中，每个节点代表了数组中某个区间的和。树状数组本质上是一种 **隐式的二叉树** 结构，通过低位运算来实现父子节点之间的关系。

## 父节点计算公式
对于树状数组中的任意一个节点 `index`，其 **父节点** 的位置可以通过以下公式计算：
> parent(index) = index - (index & -index)


### 解释：

1. **`index & -index`**：
   - 这个操作计算的是 `index` 的 **最低有效 1 位**，即 `index` 的二进制表示中最低的 `1` 所在的位置。
   - 例如，假设 `index = 6`（二进制为 `110`），则 `index & -index` 计算结果为 `2`（即 `10`，提取出 `6` 的最低有效 1 位）。
   - **负数的补码求法**：
        - 方式1: 原码取反加1，例如-6，原码110，取反001，+1=010
        - 方式2: 以最后一位1为分界点，前面和原码相反，后面和原码相同

2. **`index - (index & -index)`**：
   - 通过从 `index` 中减去 `index & -index`，得到的是 **父节点** 的索引。
   - 这一计算方式是模拟了树状数组中父子节点之间的层级关系。每个节点的父节点索引和当前节点的索引之间的差值由 `index & -index` 决定。

### 示例：
```
树状数组结构：
Index:   1   2   3   4   5   6   7   8
区间:  [1] [2] [3] [4] [5] [6] [7] [8]       (每个节点对应一个元素)

树状数组的二叉树结构示意：
          1
       /     \
      2       4
    /   \     /   \
   3     5   6     8

```

假设我们有一个大小为 `8` 的树状数组，索引从 `1` 到 `8`，我们来计算 `index = 6` 的父节点。

1. **`index = 6`**，二进制表示为：`110`
2. 计算 `index & -index`：  
   - `6` 的二进制是 `110`，`-6` 的二进制是 `010`（取反加一）。  
   - `6 & (-6)` 计算结果为 `2`（即 `010`），表示最低有效 1 位所在的位置。
3. 根据公式计算父节点：  
   - `parent(6) = 6 - 2 = 4`
   
所以，`index = 6` 的父节点是 `index = 4`。


# 树状数组 vs 线段树

## 1. 结构差异
- **树状数组**：
  - 基于 **一维数组** 实现，用于维护前缀和或简单的统计信息。
  - 通过低位与运算（`index & -index`）来更新和查询。

- **线段树**：
  - 基于 **二叉树** 实现，节点表示数组的某一部分区间，支持更复杂的查询和更新。
  - 每个节点可以存储区间的和、最值、最小值等信息。

## 2. 时间复杂度
- **树状数组**：
  - **更新操作**：`O(log n)`
  - **查询操作**：`O(log n)`
  - **区间查询**：通过两次查询，`O(log n)`

- **线段树**：
  - **更新操作**：`O(log n)`
  - **查询操作**：`O(log n)`
  - **区间查询**：`O(log n)`

## 3. 空间复杂度
- **树状数组**：`O(n)`  
  只需一个大小为 `n+1` 的一维数组。

- **线段树**：`O(n)`  
  需要构建一棵完整的二叉树，通常最多为 `4n` 个节点。

## 4. 支持的操作
- **树状数组**：
  - 主要支持 **前缀和** 和 **区间和**。
  - 对于复杂操作（如区间最值、区间更新等），树状数组不适用或效率较低。

- **线段树**：
  - 支持 **区间和、区间最值、区间更新** 等多种复杂操作。
  - 通过 **懒标记** 优化区间更新，支持 **区间修改**。

## 5. 实现复杂度
- **树状数组**：
  - 实现简单，支持基本的前缀和和区间和查询操作，适用于简单场景。
  
- **线段树**：
  - 实现复杂，支持更广泛的操作，如区间最值、区间修改等。

## 6. 动态更新的支持
- **树状数组**：
  - `只支持单点更新，不支持区间更新`。
  
- **线段树**：
  - 支持 **`区间更新`**，例如对区间内的每个元素加常数或执行其他操作。

## 7. 应用场景
- **树状数组**：
  - 适合处理 **`动态前缀和`** 或 **`区间和`** 问题。
  - 如果问题中没有复杂的区间更新操作，树状数组是一个更轻量、效率高的选择。

- **线段树**：
  - 适合更复杂的 **`区间查询和区间更新`** 问题，支持多种查询和更新操作，如求区间和、最值、区间修改等。

## 8. 总结

| 特性                | 树状数组                         | 线段树                             |
|-------------------|--------------------------------|-----------------------------------|
| **结构**            | 一维数组，树形结构（隐式）       | 完整二叉树，显式树形结构            |
| **更新复杂度**       | `O(log n)`                      | `O(log n)`                         |
| **查询复杂度**       | `O(log n)`                      | `O(log n)`                         |
| **空间复杂度**       | `O(n)`                          | `O(n)`                             |
| **支持操作**         | 前缀和、区间和                   | 区间和、区间最值、区间更新等        |
| **实现复杂度**       | 较简单                           | 较复杂                             |
| **适用场景**         | 前缀和和简单的区间查询          | 复杂的区间查询和区间更新            |
| **支持区间更新**     | 不支持（仅支持单点更新）         | 支持区间更新（通过懒标记优化）       |

## 总结：
- **树状数组** 适合处理简单的前缀和查询，且实现非常简单，适用于频繁进行单点更新和前缀查询的场景。
- **线段树** 则更为灵活，能够支持复杂的区间查询和区间更新，尤其适用于需要动态维护区间数据（如区间和、区间最值、区间修改等）的场景。

