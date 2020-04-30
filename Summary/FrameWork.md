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

```python
# python version #144 leetcode
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack=[]
        vis=[]
        node=root
        while True:
            if node:
                vis.append(node.val)
                if node.right:
                    stack.append(node.right)
                node=node.left
            else:
                if stack:
                    node=stack.pop()
                else:
                    break
        return vis
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
            } else
                if (!S.empty()) { 
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
// C++ version

    // 记住走的路
    //于是从左侧水平向右看去，未被遮挡的最高叶节点v——称 作最高左侧可见叶节点（HLVFL）——即为后序遍历首先访问的节点
    template <typename T> //在以S栈顶节点为根的子树中，找刡最高左侧可见叶节点 
    static void gotoHLVFL(Stack<BinNodePosi(T)>& S) { //沿递所遇节点依次入栈 
        while (BinNodePosi(T) x = S.top()) //自顶而下，反复检查当前节点（即栈顶） 
            if (HasLChild(*x)) { //尽可能向左 
                if (HasRChild(*x)) S.push(x->rChild); //若有右孩子，优先入栈 
                S.push(x->lChild); //然后才转至左孩子 
            } else //实不得已 
                S.push(x->rChild); //才向右 
        S.pop(); //返回之前，弹出栈顶的空节点 
    }

    template <typename T, typename VST> 
    void travPost_I(BinNodePosi(T) x, VST& visit) { //二叉树的后序遍历（迭代版） 
       Stack<BinNodePosi(T)> S; //辅助栈
       if (x) S.push(x); //根节点入栈 
       while (!S.empty()) { 
           if (S.top() != x->parent) //若栈顶非当前节点之父（则必为其右兄【因为入栈顺序】，【加判断原因：若不判断，就会反复再次深入，反复入栈，就会出错】），此时需 
                gotoHLVFL(S); //在以其右兄为根之子树中，找刡HLVFL（相当于递归深入其中） 
            x = S.pop(); visit(x->data); //弹出栈顶（即前一节点之后继），访问之
        }
    }
```
```python
# python version

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        def is_child(father,child):
            return father.left==child or father.right==child

        vis=[] # 访问
        stack=[] #栈
        stack.append(root) #入栈
        cur=root
        while stack: #栈不为空执行
            if not is_child(stack[-1],cur): # 如果当前栈顶节点不为当前节点父节点，则必为其有兄弟，此时再次深入，相当于递归操作
                while stack[-1]: # 当栈顶不为空时
                    node = stack[-1]
                    if node.left: # 按照递归的路劲入栈
                        if node.right:
                            stack.append(node.right)
                        stack.append(node.left)
                    else:
                        stack.append(node.right) # 如果不是叶节点，继续深入，否则，会入栈一个空节点，返回
                stack.pop() # 弹出上面叶节点入栈的一个空节点
            cur=stack.pop() # 弹出当前最左边的叶节点
            vis.append(cur.val) # 访问，并且进行下次循环
        return vis

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
* BFS (Page 160):
```C++
template <typename Tv, typename Te> //广度优先搜索BFS算法（单个连通域） 
void Graph<Tv, Te>::BFS(int v, int& clock) { //assert: 0 <= v < n 
    Queue<int> Q; //引入辅劣队列

    status(v) = DISCOVERED; Q.enqueue(v); //刜始化起点
    while (!Q.empty()) { //在Q发空之前，丌断
        int v = Q.dequeue(); dTime(v) = ++clock; //叏出队首顶点v
        for (int u = firstNbr(v); -1 < u; u = nextNbr(v, u)) //构丼v癿所有邻屁u
            if (UNDISCOVERED == status(u)) { //若u尚未被収现，则 
                status(u) = DISCOVERED; Q.enqueue(u); //収现诠顶点 status(v, u) = TREE; parent(u) = v; //引入树边拓展支撑树
            } else { //若u已被収现，戒者甚至已讵问完毕，则 
                status(v, u) = CROSS; //将(v, u)弻类亍跨边
            } 
        } 
        status(v) = VISITED; //至此，弼前顶点讵问完毕 
}
```
* DFS:
```C++
template <typename Tv, typename Te> //深度优先搜索DFS算法（单个连通域） 
void Graph<Tv, Te>::DFS(int v, int& clock) { //assert: 0 <= v < n 12 13 14
    dTime(v) = ++clock; status(v) = DISCOVERED; //収现弼前顶点v
    for (int u = firstNbr(v); -1 < u; u = nextNbr(v, u)) //构丼v癿所有邻屁u 
        switch (status(u)) { //幵规其状态分删处理
            case UNDISCOVERED: //u尚未収现，意味着支撑树可在此拓展
                status(v, u) = TREE; parent(u) = v; DFS(u, clock); 
                break; 
            case DISCOVERED: //u已被収现但尚未讵问完毕，应属被后代指向癿祖先
                status(v, u) = BACKWARD; 
                break;
            default: //u已讵问完毕（VISITED，有向图），则规承袭兲系分为前向边戒跨边 
                status(v, u) = (dTime(v) < dTime(u)) ? FORWARD : CROSS; 
                break;
        } 
    status(v) = VISITED; fTime(v) = ++clock; //至此，弼前顶点v斱告讵问完毕 
}
```
* __Topology Sort__:
```c++
//C++ version

template <typename Tv, typename Te> //基亍DFS癿拓扑排序算法 
Stack<Tv>* Graph<Tv, Te>::tSort(int s) { //assert: 0 <= s < n 
    reset(); int clock = 0; int v = s; 
    Stack<Tv>* S = new Stack<Tv>; //用栈记弽排序顶点 
    do { 
    if (UNDISCOVERED == status(v)) 
        if (!TSort(v, clock, S)) { //clock幵非必需 
            while (!S->empty()) //仸一连通域（亦即整图）非DAG 
                S->pop(); break; //则丌必继续计算，故直接迒回 
        } 
    } while (s != (v = (++v % n))); 
    return S; //若输入为DAG，则S内各顶点自顶向底排序；否则（丌存在拓扑排序），S空 
} 

template <typename Tv, typename Te> //基亍DFS癿拓扑排序算法（单趟） 
bool Graph<Tv, Te>::TSort(int v, int& clock, Stack<Tv>* S) { //assert: 0 <= v < n 
    dTime(v) = ++clock; status(v) = DISCOVERED; //収现顶点v 
    for (int u = firstNbr(v); -1 < u; u = nextNbr(v, u)) //构丼v癿所有邻屁u 
    switch (status(u)) { //幵规u癿状态分删处理 
        case UNDISCOVERED: 
            parent(u) = v; status(v, u) = TREE; 
            if (!TSort(u, clock, S)) //从顶点u处出収深入搜索 
                return false; //若u及其后代丌能拓扑排序（则全图亦必如此），故迒回幵报告 
            break; 
        case DISCOVERED: 
            status(v, u) = BACKWARD; //一旦収现后向边（非DAG），则 
            return false; //丌必深入，故迒回幵报告 
        default: //VISITED (digraphs only) 
            status(v, u) = (dTime(v) < dTime(u)) ? FORWARD : CROSS; 
            break; 
    } 
    status(v) = VISITED; S->push(vertex(v)); //顶点被标记为VISITED时，随即入栈 
    return true; //v及其后代可以拓扑排序 
```

```python
# python version

from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency={_:[] for _ in range(numCourses)}
        indegree={_:0 for _ in range(numCourses)}
        for it in prerequisites:
            if it[1] in adjacency:
                adjacency[it[1]].append(it[0])
            else:
                adjacency[it[1]]=[it[0]]
            indegree[it[0]]+=1
        queue=deque([])
        ans=[]
        for k,v in indegree.items():
            if v==0:
                queue.append(k)
                ans.append(k)
        while queue:
            course=queue.popleft()
            for c in adjacency[course]:
                indegree[c]-=1
                if indegree[c]==0:
                    queue.append(c)
                    ans.append(c)
            
        return ans if len(ans)==numCourses else []
```

#### 7. Search Tree

#### 8. Advanced Search Tree

#### 9. Dictionary

#### 10. Priority Queue

#### 11. String
* __KMP__（P314）:
```C++
int match(char* P, char* T){//KMP算法
    int* next = buildNext(P); //构造next表
    int n = (int) strlen(T), j = 0; //文本串指针
    int m = (int) strlen(P), j=0; //模式串指针
    while ( j < m && i < n ) //自左向右逐个比对字符
        if ( 0 > j || T[i] == P[j]) //若匹配，或者P已移出最左侧（两个判断的次序不可交换）
        { i++; j++;}
        else //否则
            j = next[j]; //模式串右移（注意：文本串不用回退）
    delete [] next; //释放next表
    return i-j

}

int* buildNext(char* P){ //构造模式串P的next表
    size_t m = strlen(P), j = 0;//主串指针
    int* N = new int[m]; //next表
    int t = N[0] = -1;
    while ( j < m-1){
        if ( 0>t || P[j] == P[t] ){//匹配
            j++; t++;
            N[j] = t;//此句可改进...看书
        }else{ //失配
            t = N[t];
        }
    }
    return N;
}
```



#### 12. Sort
* <a href='https://sort.hust.cc/'>十大经典排序算法</a>
    <a href='https://cloud.tencent.com/developer/article/1108770'><img src='./resources/sort.png'></a>
* __堆排序__
```python
# 1. Build a heap
# 2. Adjust the sub heap from bottom to top
# 3. Sorting process: every time recursively swap the top element of the heap and the last element of the heap

# 大根堆（从小打大排列）
def heapSort(nums):
    # 调整堆 (自上而下)
    def adjustHeap(nums, i, size):
        # 非叶子结点的左右两个孩子
        lchild = 2 * i + 1
        rchild = 2 * i + 2
        # 在当前结点、左孩子、右孩子中找到最大元素的索引
        largest = i 
        if lchild < size and nums[lchild] > nums[largest]: 
            largest = lchild 
        if rchild < size and nums[rchild] > nums[largest]: 
            largest = rchild 
        # 如果最大元素的索引不是当前结点，把大的结点交换到上面，继续调整堆
        if largest != i: 
            nums[largest], nums[i] = nums[i], nums[largest] 
            # 第 2 个参数传入 largest 的索引是交换前大数字对应的索引
            # 交换后该索引对应的是小数字，应该把该小数字向下调整
            adjustHeap(nums, largest, size)
    # 建立堆 (自下而上)
    def builtHeap(nums, size):
        for i in range(len(nums)//2)[::-1]: # 从倒数第一个非叶子结点开始建立大根堆
            adjustHeap(nums, i, size) # 对所有非叶子结点进行堆的调整（即调整子堆，从而使每个子堆有序，大部分节点都在底层，所以时间复杂度小）
        # print(nums)  # 第一次建立好的大根堆
    # 堆排序 
    size = len(nums)
    builtHeap(nums, size) 
    for i in range(len(nums))[::-1]: 
        # 每次根结点都是最大的数，最大数放到后面
        nums[0], nums[i] = nums[i], nums[0] 
        # 交换完后还需要继续调整堆，只需调整根节点，此时数组的 size 不包括已经排序好的数
        adjustHeap(nums, 0, i) 
    return nums  # 由于每次大的都会放到后面，因此最后的 nums 是从小到大排列
```

#### Appendix


#### References:
> Data structure, C++ version, Junhui Deng
