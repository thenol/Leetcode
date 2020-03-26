## The Notebook of Data Structure

#### 1. Introduction

#### 2. Vector

#### 3. List

#### 4. Stack and Queue

#### 5. Binary Tree
* Focus on the form of BT
```
                 |--------------[]--------------|
        |-------[]-------|              |-------[]-------|
    |---[]---|      |---[]---|      |---[]---|      |---[]---|
    []      []      []      []      []      []      []      []
```
* Focus on the forms of the Node
```
    |     O      O     O     O
    O      \    / \   /      
```

* Tranverse order
```
         |
         O
       // \\
       O   O
       |   |
```

* __Preorder Tranverse__:
```C++
    // 入右
    //从当前节点出发，沿左分支不断深入，直至没有左分支的节点；沿途节点遇到后访问 
    template <typename T, typename VST> //元素类型、操作器 
    static void visitAlongLeftBranch(BinNodePosi(T) x, VST& visit, Stack<BinNodePosi(T)>& S) { 
        while (x) { 
            visit(x->data); //访问当前节点 
            S.push(x->rChild); //右孩子入栈暂存（可优化：通过刞断，避免空癿右孩子入栈） 
            x = x->lChild;  //沿左分支深入一局 
        } 
    }

    template <typename T, typename VST> //元素类型、操作器 
    void travPre_I2(BinNodePosi(T) x, VST& visit) { //二叉树先序遍历算法（迭代版#2）
        Stack<BinNodePosi(T)> S; //辅助栈 
        while (true) { 
            visitAlongLeftBranch(x, visit, S); //从当前节点出収，逐批讵问 
            if (S.empty()) break; //直至栈空 
            x = S.pop(); //弹出下一批的起点 
        } 
    }

```

* __Inorder Tranverse__:
```C++
    // 入自己
    template <typename T, typename VST> //元素类型、操作器 
    void travIn_I2(BinNodePosi(T) x, VST& visit) { //二叉树中序遍历算法（迭代版#2）
        Stack<BinNodePosi(T)> S; //辅劣栈 
        while (true) 
            if (x) { 
                S.push(x); //根节点迕栈 
                x = x->lChild; //深入遍历左子树 
            } else if (!S.empty()) { 
                    x = S.pop(); //尚未讵问癿最低祖先节点退栈 
                    visit(x->data); //讵问诠祖先节点 
                    x = x->rChild; //遍历祖先癿右子树 
                    } 
                else
                    break; //遍历完成 
            } 

```

* __Inorder Succ__:
```C++
    template <typename T> BinNodePosi(T) BinNode<T>::succ() { //定位节点v癿直接后继 
        BinNodePosi(T) s = this; //记录后继癿临时发量 
        if (rChild) { //若有右孩子，则直接后继必在右子树中，具体地就是 
            s = rChild; //右子树中 5
            while (HasLChild(*s)) s = s->lChild; //最靠左（最小）癿节点 
        } else { //否则，直接后继应是“将弼前节点包含亍其左子树中癿最低祖先”，具体地就是 
            while (IsRChild(*s)) s = s->parent; //逆向地沿右向分支，丌断朝左上斱秱劢 
            s = s->parent; //最后再朝右上斱秱劢一步，即抵达直接后继（如枅存在） 
        } 
        return s; 
    }
```

* __Postorder__:
```C++
    // 记住走的路
    //于是从左侧水平向右看去，未被遮挡的最高叶节点v——称 作最高左侧可见叶节点（HLVFL）——即为后序遍历首先访问的节点
    template <typename T> //在以S栈顶节点为根癿子树中，找刡最高左侧可见叶节点 
    static void gotoHLVFL(Stack<BinNodePosi(T)>& S) { //沿递所遇节点依次入栈 
        while (BinNodePosi(T) x = S.top()) //自顶而下，反复检查当前节点（即栈顶） 
            if (HasLChild(*x)) { //尽可能向左 
                if (HasRChild(*x)) S.push(x->rChild); //若有右孩子，优先入栈 
                S.push(x->lChild); //然后才转至左孩子 
            } else //实丌得已 
                S.push(x->rChild); //才向右 
        S.pop(); //迒回乀前，弹出栈顶癿空节点 10 } 11 
    }

    template <typename T, typename VST> 
    void travPost_I(BinNodePosi(T) x, VST& visit) { //二叉树癿后序遍历（迭代版） 
       Stack<BinNodePosi(T)> S; //辅助栈
       if (x) S.push(x); //根节点入栈 
       while (!S.empty()) { 
           if (S.top() != x->parent) //若栈顶非当前节点之父（则必为其右兄），此时需 
                gotoHLVFL(S); //在以其右兄为根之子树中，找刡HLVFL（相当于递归深入其中） 
                x = S.pop(); visit(x->data); //弹出栈顶（即前一节点之后继），访问之
            } 
        } 
```
* __Level Order__:
```python
# iteration
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
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # go to next level
            level += 1
        
        return levels
'''
# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/er-cha-shu-de-ceng-ci-bian-li-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

'''

# recursive
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        
        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
            
        helper(root, 0)
        return levels
'''
作者：LeetCode
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/er-cha-shu-de-ceng-ci-bian-li-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
```
* Some notes:
    * Pay attention to the path to the leaves and judge the conditions of the leaves



#### 6. Graph

#### 7. Search Tree

#### 8. Advanced Search Tree

#### 9. Dictionary

#### 10. Priority Queue

#### 11. String

#### 12. Sort

#### Appendix


#### References:
> Data structure, C++ version, Junhui Deng