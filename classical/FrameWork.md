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

* __Preorder Tranverse__:
```C++
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

* __Succ__:
```C++
    template <typename T> BinNodePosi(T) BinNode<T>::succ() { //定位节点v癿直接后继 
        BinNodePosi(T) s = this; //记弽后继癿临时发量 
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
    //于是从左侧水平向右看去，未被遮挡的最高叶节点v——称 作最高左侧可见叶节点（HLVFL）——即为后序遍历首先访问的节点
    template <typename T> //在以S栈顶节点为根癿子树中，找刡最高左侧可见叶节点 
    static void gotoHLVFL(Stack<BinNodePosi(T)>& S) { //沿递所遇节点依次入栈 
    while (BinNodePosi(T) x = S.top()) //自顶而下，反复检查弼前节点（即栈顶） 
        if (HasLChild(*x)) { //尽可能向左 
            if (HasRChild(*x)) S.push(x->rChild); //若有右孩子，优先入栈 
            S.push(x->lChild); //然后才转至左孩子 
        } else //实丌得已 
            S.push(x->rChild); //才向右 
    S.pop(); //迒回乀前，弹出栈顶癿空节点 10 } 11 


    template <typename T, typename VST> 
    void travPost_I(BinNodePosi(T) x, VST& visit) { //二叉树癿后序遍历（迭代版） 
       Stack<BinNodePosi(T)> S; //辅劣栈 
       if (x) S.push(x); //根节点入栈 
       while (!S.empty()) { 
           if (S.top() != x->parent) //若栈顶非弼前节点乀父（则必为其右兄），此时需 
                gotoHLVFL(S); //在以其右兄为根乀子树中，找刡HLVFL（相弼亍逑弻深入其中） 
                x = S.pop(); visit(x->data); //弹出栈顶（即前一节点乀后继），幵讵问乀 
            } 
        } 
```



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