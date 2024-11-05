"""
[hard]

给你一个 不含重复 单词的字符串数组 words ，请你找出并返回 words 中的所有 连接词 。

连接词 定义为：一个完全由给定数组中的至少两个较短单词（不一定是不同的两个单词）组成的字符串。

 

示例 1：

输入：words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
输出：["catsdogcats","dogcatsdog","ratcatdogcat"]
解释："catsdogcats" 由 "cats", "dog" 和 "cats" 组成; 
     "dogcatsdog" 由 "dog", "cats" 和 "dog" 组成; 
     "ratcatdogcat" 由 "rat", "cat", "dog" 和 "cat" 组成。
示例 2：

输入：words = ["cat","dog","catdog"]
输出：["catdog"]
 

提示：

1 <= words.length <= 104
1 <= words[i].length <= 30
words[i] 仅由小写英文字母组成。 
words 中的所有字符串都是 唯一 的。
1 <= sum(words[i].length) <= 105

https://leetcode.cn/problems/concatenated-words/description/?source=vscode
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd=True
    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.isEnd
    def starts_with(self,word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

class Solution:
    # method 1: Trie 树 + 动态规划
    # 核心优化：优化哈希匹配，降低哈希查找的时间，尤其当字符不存在的时候，hash必须计算整个hash值，而无法提前终止，会造成时间复杂度的增加，但是Trie前缀树，可以实现快速终止
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # insert words into Trie
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        def f(str):
            """检测str是否可以由s中更小单词组成"""
            nonlocal trie
            # state: d[i] 表示str[:i]是否由Trie中更小单词组成
            N = len(str)
            d = [False] * (N+1)
            
            # initialization
            d[0] = True

            # transition
            for i in range(N+1):
                for j in range(i): # 0<=j<i
                    if i-j==N:continue # 跳过整个word查询的情况
                    d[i] = d[i] or (trie.search(str[j:i]) and d[j])
                    if d[i]: break
            
            return d[N]
        
        ans = []
        for word in words:
            if f(word):
                ans.append(word)
        return ans
          
    # method 2: 分而治之 + 动态规划
    def findAllConcatenatedWordsInADict_2(self, words: List[str]) -> List[str]:
        @cache
        def f(str):
            """检测str是否可以由s中更小单词组成"""
            nonlocal s
            # state: f(str) 表示 是否能由s中更小单词组成
            N = len(str)
            for i in range(1, N): # 确保str[:i]非空且不是全集，否则可能会引发无穷递归
                if (str[:i] in s or f(str[:i])) and (str[i:] in s or f(str[i:])):
                    return True

            return False
        
        s = set(words)
        ans = []
        for word in words:
            if f(word): # 去掉自己
                ans.append(word)
        
        return ans 


    # TLE version 32/43
    def findAllConcatenatedWordsInADict_1(self, words: List[str]) -> List[str]:
        def f(str, s):
            """检测str是否可以由s中更小单词组成"""
            # state: d[i]表示str[:i]是否可以由s中更小单词组成
            # 0<=i<=len(str)
            N = len(str)
            d = [False] * (N+1)
            
            # initialization
            # 0<=i
            d[0] = True

            # transition
            # 0<=j<i
            for i in range(N+1):
                for j in range(i): # 1<=i-j<=N
                    d[i] = d[i] or (str[j:i] in s and d[j])
                    if d[i]: break
            return d[N]
        
        s = set(words)
        ans = []
        for word in words:
            if f(word, s-{word}): # 去掉自己
                ans.append(word)
        
        return ans   


"""
Trie树和哈希表（Hash）在匹配效率上各有优势，具体哪个更高效取决于使用场景和具体需求。以下是一些比较点：

前缀匹配效率：
Trie树在处理前缀匹配时非常高效，因为它的结构允许快速检索具有共同前缀的字符串。这是Trie树相较于哈希表的一个显著优势，因为哈希表不支持直接的前缀匹配
。

内存消耗：
Trie树可能比哈希表消耗更多的内存，因为每个节点都需要存储额外的指针信息。然而，如果有很多共享公共前缀的字符串，Trie树可以通过共享这些公共节点来节省空间
。

有序遍历：
Trie树支持有序遍历，这意味着可以按照字典顺序检索所有键。哈希表则不支持这种有序检索
。

查找速度：
哈希表在查找速度上通常更快，因为它的平均查找时间复杂度是O(1)。而Trie树的查找时间复杂度是O(n)，其中n是键的长度。但是，如果输入字符串不存在于Trie中，Trie可以提前终止搜索，而哈希表总是需要计算整个输入字符串的哈希值
。

数据局部性：
哈希表在数据局部性方面表现不佳，因为它们将相关元素存储在距离较远的位置，这意味着如果应用程序顺序查找共享前缀的元素，它将无法从缓存效应中受益。而搜索树在这方面表现更好
。

插入和删除操作：
Trie树在插入和删除操作上可能比哈希表慢，尤其是在处理大量数据时。Trie树需要额外的操作，可能涉及节点的创建或删除
。

应用场景：
如果需要全文查找，哈希表因其更快的查找速度而更优。但如果需要返回所有匹配前缀的单词，Trie是更好的解决方案
。

综上所述，Trie树在处理具有共同前缀的字符串集合、前缀匹配、有序检索等场景下比哈希表更高效。而哈希表在需要快速随机查找且不关心前缀匹配的场景下可能更胜一筹。因此，选择哪种数据结构取决于具体的应用需求和场景。
"""