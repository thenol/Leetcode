### 字符串匹配中的 Next Table

在字符串匹配算法中，**Next Table** 是一种优化手段，特别是在 **KMP（Knuth-Morris-Pratt）算法** 中。它的作用是帮助提高匹配效率，避免在匹配过程中进行不必要的重复比较。`Next Table` 可以通过记录模式字符串中前缀与后缀的匹配信息，减少回溯的次数，从而提高整体匹配的效率。

#### 1. KMP 算法简介

KMP 算法是一种高效的字符串匹配算法，其核心思想是利用已经匹配的信息，在匹配失败时跳过一些字符，避免重复比较已匹配部分的字符。通过构建一个辅助的 **Next Table**，KMP 可以在失配时根据已匹配的部分决定模式字符串需要跳过多少个字符。

#### 2. Next Table 的定义

`Next Table` 是一个数组，记为 `next[]`，它记录了每个位置之前的前缀和后缀的最长匹配长度。`next[i]` 表示模式字符串 `P[0..i-1]` 的前缀和后缀的最长公共部分的长度。

- `next[i]` 表示在模式字符串 `P[0..i-1]` 这个子串中，最长的前缀后缀匹配的长度。
- `next[i]` 的值决定了失配时模式字符串指针应该跳转到的位置，从而避免重新比较已经匹配的部分。

#### 3. Next Table 的计算

构建 `Next Table` 的过程就是求模式字符串每个前缀和后缀的最长公共匹配长度。假设模式字符串为 `P = "ABABC"`，我们可以通过以下步骤计算出 `Next Table`：

1. **初始化：**
   - `next[0] = 0`，表示没有前缀和后缀，最长匹配长度为 0。
   - `i = 1`，从模式字符串的第二个字符开始计算。

2. **计算过程：**
   - 使用指针 `j` 来记录当前前缀和后缀的匹配长度。
   - 如果 `P[i] == P[j]`，则 `j` 增加，表示匹配长度增加。
   - 如果 `P[i] != P[j]`，则利用 `next[j-1]` 跳过不匹配的部分，直到找到一个匹配的位置或 `j` 为 0。

#### 示例：

假设模式字符串 `P = "ABABC"`，计算 `Next Table` 的过程如下：
```python
P = "ABABC"
next[0] = 0  # (没有前缀和后缀匹配)
next[1] = 0  # (子串 "A" 没有匹配的前缀和后缀)
next[2] = 1  # (子串 "AB" 的前缀和后缀 "A" 匹配)
next[3] = 2  # (子串 "ABA" 的前缀和后缀 "AB" 匹配)
next[4] = 3  # (子串 "ABAB" 的前缀和后缀 "ABA" 匹配)
```

最终得到的 `Next Table` 为：
```python
next = [0, 0, 1, 2, 3]
```


#### 4. Next Table 的作用

在 KMP 算法中，`Next Table` 可以用来指导模式字符串在发生失配时如何跳过已匹配的部分，而不需要从头开始比较。具体而言，当模式字符串和文本字符串发生失配时，`next[]` 数组指示了模式字符串指针应该跳跃到哪个位置，避免了不必要的重复比较。

#### 5. KMP 算法应用

在实际的字符串匹配中，KMP 算法会根据 `Next Table` 指示的跳跃位置继续匹配，确保算法的时间复杂度为 **O(n + m)**，其中 `n` 是文本的长度，`m` 是模式的长度，相比暴力匹配的 **O(n * m)** 具有更高的效率。

#### 6. 总结

- **Next Table** 是 KMP 算法中的关键部分，用于记录模式字符串的前缀和后缀的最长匹配长度。
- 它的作用是在匹配失败时，帮助算法跳过已匹配的部分，避免重复比较，从而提高匹配效率。
- `Next Table` 可以在 **O(m)** 时间内构建，其中 `m` 是模式字符串的长度。
- 最终，KMP 算法通过利用 `Next Table` 实现了 **O(n + m)** 的匹配时间复杂度，其中 `n` 是文本的长度，`m` 是模式字符串的长度。

### 示例代码（Python 实现 Next Table）

```python
"""next table"""
def get_next(pattern):
    # 初始化 next_table 数组，第一个元素设为 -1
    # next_table 数组用来记录模式串中每个位置的前缀和后缀的最长匹配长度
    # ❗️next_table[j]表示以j结尾的且在j处 不匹配的 最长公共前后缀长度，即 pattern[:j] 范围最长公共前后缀长度；即不含当前，前面字符串前后缀最大匹配长度（不能整体，含整体的时候，必相等，即abcd===abcd）
    # ❗️而当j处不匹配时，应当直接跳过 最长公共前后缀 的 overlap 部分，其重叠长度为next_table[j]，范围为 [0, next_table[j]-1]，因此下一个应当匹配的位置就是 next_table[j] 
    next_table = [-1]  
    
    # i 用来遍历模式字符串，j 用来指示❗️当前匹配的前缀❗️的末尾
    i = 0
    j = -1
    
    # 遍历模式字符串（从下标 0 开始直到倒数第二个字符）
    while i < len(pattern) - 1:
        
        # 如果 j == -1，表示当前没有前缀匹配（即从头开始匹配）
        # 或者 pattern[i] 与 pattern[j] 相等，表示可以扩展匹配
        if j == -1 or pattern[i] == pattern[j]:
            i += 1  # 移动 i，继续匹配下一个字符
            j += 1  # 扩展前缀的匹配长度
            next_table.append(j)  # 将当前匹配长度添加到 next_table 数组
            
        # 如果 pattern[i] 与 pattern[j] 不匹配，说明需要回溯
        # 根据已计算的 next_table 数组的信息，找到一个新的位置 j 进行匹配
        else:
            j = next_table[j]  # 回退 j 的位置，继续尝试匹配
    
    # 返回构建好的 next_table 数组
    return next_table

def KMP(text, pattern):
    """
    使用 KMP 算法进行字符串匹配
    """
    n = len(text)
    m = len(pattern)
    next = get_next(pattern)  # 获取模式串的 next 数组
    i = j = 0  # i 是文本串指针，j 是模式串指针

    while i < n and j < m:
        if text[i] == pattern[j]:  # 字符匹配
            i += 1
            j += 1
        elif j==0: # 不能在跳转了，说明当前没有匹配的地方，直接主串后移一位，从新开始查找
            i += 1  # 模式串从头开始重新匹配
        else: # 模式串部分匹配，跳到合适的位置
            j = next[j]

    return i-j if j==m else -1  # # 如果模式串完全匹配，返回匹配的起始位置；如果没有匹配，返回 -1

# 示例
print(get_next("ABABC")) # 输出: [-1, 0, 0, 1, 2]
print(KMP("BACABABCDEFS", "ABABC"))  # 输出: 3
```
> 动态规划角度理解：https://writings.sh/post/algorithm-string-searching-kmp

> 执行过程：https://www.cnblogs.com/fswly/p/17959786

> 总结：核心为求解 **`最长公共前后缀长度$f(j)$`**，即 $next$ 数组
