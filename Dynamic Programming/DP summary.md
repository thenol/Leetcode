### Dynamic programming
* **问题特征**
    * 最优子结构(子集有解且唯一)
    * 重叠子问题(也是与减治法的区别)，同时也是所有的子问题或者所有的可能性(与暴力法的区别，子问题之间有相互关系，通过相互关联可以相互推导得出解，避免了大量的重复计算)
* **解的性质**：
    * 每个问题必然有解(不用恐惧，冷静思考)
    * 必然存在唯一的最优解(仔细展开分类讨论所有可能性)
    * **```本质```**：**最优解一定考虑且涵盖了所有的可能性(最优解的充要条件)**，也就是暴力情况下的可能性，它一定是所有情况下的最优解(一定可以通过可能性展开，从而找到相互之间关系，避免重复计算，即空间换时间)
* **方法论(思路)**：本质是有向无环图(也就是无后效性)
    > **注意顺序：** 状态确定 -> 状态转移方程 -> **确定方程中的变量之间的依赖关系也就是 ```d[i]``` 依赖于哪些前置状态条件例如 ```d[i-1]、d[i-2]``` -> 得到下标变量范围 ```2<=i``` -> 初始化哪些(```d[0],d[1]```)下标边界以及从哪里(```i=2```)开始计算**
    
    > **技巧：对于拿不准的下标边界，最简单最不容易出错的方式就是，编码的时候直接写出范围，特例举出**

    1. 确定状态 -> 聚焦 **```单个元素```** （**研究最优策略的最后一步**），同时关注数据规模，规模也是提示，可以决定状态中所含变量个数，状态的内涵或者必要条件，必须能够正确表示题目里面的所有关系（参见**87. 扰乱字符串.py**）。
    2. 状态转移方程 -> 考虑 **```状态决策的充要条件```** **核心目的减少问题规模，关键在于拆，按照可能性展开拆分成子问题，枚举子问题并求解**，然后构建子问题和父问题点之间的关系，即根据题意的所有可能决策路径
    3. 初始化条件和边界条件(**技巧:哨兵**) -> 开始建表(类似数独，准备刷图)
    4. 计算顺序 -> 填表顺序(根据已知依据状态转移方程推未知，**尤其注意状态计算依赖，以及最开始递归或者迭代所依赖的边界范围条件的初始化，可以参考《32. 最长有效括号.py》和《87. 扰乱字符串.py》**)
    

* **两种写法**：记忆化搜索dfs(注意可以**挂或者传入缓存表，如果需要预处理就必须传入预处理之后的缓存表**)、刷表法dp
    * 记忆化搜索方法dfs
        * 好处：思路直接，不需要考虑显示考虑表格填写顺序
        * 坏处：但是需要注意缓冲，否则容易超时或者溢出
    * 刷表法dp
        * 好处：迭代处理，显示思路比较直接
        * 坏处：需要严格以来表格之间位置关系，因此需要显示考虑表格填写顺序，需要处理细节
        * 填表法技巧：一定要用特列法，先画一个简单的表格，摸清表格之间以来关系，再去写遍历

* **注意点**
    * 后效性的消除
        1. 无后效性情况不用处理：当d[i][j]不依赖外部信息时，基本上不会存在后效性
        2. 有后效性情况需要转换成无有效性，例如d[t][i][j]，也就是不同的时刻下 d[i][j]的值是不一样的，例如典型题目 **戳气球**，如果考虑状态表示的是最后打爆，则没有后效性，否则如果考虑状态为首先打爆气球的状态，则就会存在后效性。
    * 返回值处理
        1. 注意，如果各个子问题需要返回的数值不同，那么为了处理方便，必须返回所有信息，然后在使用的时候，在不同的子问题处理的时候，可以跳选着处理返回信息的不同部分，例题：**布尔运算**， 即d[i][j]=[F, T]，分别为False和True对应的数量，也就是d[i][j][0]代表False的数量。
* **特殊值验证**
    * 可以带入特殊值，验证状态转移之间的计算是否正确，以及如果错误，问题出在哪

* 注意边界初始化以及填表顺序的技巧
```python
# 方式一：对角线方式，往右上方刷表
# 场景：处理回文字符串相关
# 例题见，interval dp -> 5.longestPalindrome.py
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N=len(s)
        d=[[-1 for _ in range(N)] for _ in range(N)]
        mx=0
        start=end=0
        for le in range(1,N+1): # 控制遍历次数，执行N次
            for i in range(N-le+1): # 控制遍历行，次序为[0,N), [0,N-1), [0,N-2),..., [0,1), 同样是 N 次
                j=i+le-1 # 控制遍历列，每次遍历，列都会右移一个，第le次遍历，自然右移le，但是 j 得从i位置开始，因此自然得初始为 i+le-1 (否则j就从i右边第一个下标开始了)
                d[i][j]=s[i]==s[j] and ( le < 3  or d[i+1][j-1])
                if d[i][j] and j-i>mx:
                    start,end=i,j
        return s[start:end+1]

# 方式二：从左到右或者从右到左，从上到下，或者从下到上，见以下背包问题
```

* __knapsack dp__
    * __0-1 背包问题: 【$P_{272}$】__
        * Questions: 
            * 有$n$种物品，每种只有一个。第$i$种物品的体积为$V_{i}$, 重量为$W_i$。选一些物品撞到一个容量为$C$的背包，使得背包物品在总体积不超过$C$的前提下重量尽可能大。$1\le{n}\le{100},\;1\le{V_i}\le{C}\le10000,\;1\le{W_i}\le{10^6}$。
        * State transition equation: 
            * $d[i][j]$从前$i$种物品中选一些装到容量为$j$的背包中的最大总重量
            * $f(i,j)=max\{f(i-1,j),f(i-1,j-V_i)+W_i\}$
        * Calculation:
            * 边界：$i=0时为0$，$j\lt{0}$时为负无穷，最终答案为$f(n,C)$

        ```C++
        // 填表法，从下至上
        // version 1
        for(int i=1;i<=n;i++)
            for (int j=0;j<=c;j++){
                //感受这样写的代码精简之处
                //i=1时,f[i-1][j]=f[0][j]=0,也相当于不记录，直接初始化
                //就相当于f[1][j]=f[0][j]=0
                //V[i]体积太大，放不下
                f[i][j] = (i==1 ? 0:f[i-1][j]); 
                //当前背包容量可以放下V[i],求没选i和选i的时候的最大重量
                if(j>=V[i]) f[i][j] = max(f[i][j],f[i-1][j-V[i]]+W[i]);
            }

        // version 2, when the array has been initialized, like 'memset()'
        // the way of less computation, because the maximum is f(n,C)
        /*for(int i=1;i<=n;i++)
            for (int j=V[i];j<=c;j++){
                f[i][j] = max(f[i-1][j],f[i-1][j-V[i]]+W[i]);
            }*/

        
        
        //这种状态转移方程或者规划方向，可以边读入编计算
        for(int i=1;i<=n;i++){
            cin>>V>>W;
            for(int j=0;j<=C;j++){
                f[i][j]=(i==1?0:f[i-1][j]);
                if(j>=V) f[i][j]=max(f[i][j],f[i][j-V]+W);
            }
        }
        

        //滚动数组简化
        memset(f,0,sizeof(f));
        for(int i=1;i<=n;i++){
            cin>>V>>W;
            for (int j=C;j>=0;j--){
                if(j>=V) f[j]=max(f[j],f[j-V]+W);
            }
        }
        //再次合并条件简化
        memset(f,0,sizeof(f));
        for(int i=1;i<=n;i++){
            cin>>V>>W;
            for (int j=C;j>=V;j--){
                f[j]=max(f[j],f[j-V]+W);
            }
        }
        ```
    * __Conclusion__:
        * The essence is to solve the optimal value problem of any combination of subsequences.

* __Digital dp__
* __Interval dp__
    * 大范围的问题拆解成若干小范围的问题来求解
    * 可能性展开的常见方式：
        1. 基于两侧端点讨论的可能性展开(即讨论对象是端点)，更具体一点状态转移方程 dp[i][j] 一般只依赖于 i,j
        2. 基于范围上划分点的可能性展开(即讨论对象是范围内的点)，更具体一点状态转移方程 dp[i][j] 除了依赖于 i,j，还依赖于 m ，其中 i < m < j
    * 例题
        *  括号区间匹配（牛客）：
        ```python
        """
        给定一个由'[', ']', '(', ')'组成的字符串，请问最少插入多少个括号就能使这个字符串的所有括号左右配对
        """
        # 思路：
        ## 状态定义：d[i][j]表示s[i:j+1]，上最少需要插入多少个括号就能使得这个字符串的所有括号左右配对
        ## 这里只讨论当 s[i]和s[j] 不配对 的时候状态转移方程，按照中间点展开，即 i<=m<j, d[i][j] = min(d[i][m] + d[m+1][j])，对所有的m。
        ## 啥意思，为啥能这么分解，再注意一千遍状态表示：d[i][j]表示s[i:j+1]，上最少需要插入多少个括号就能使得这个字符串的所有括号左右配对。
        ## 也就是说，当 s[i]和s[j] 不配对 的时候，必然有某一个，或者需要插入一个 s[m]，来和 s[i] 或者 s[j] 配对，因此必须遍历所有这种配对的可能性
        ```
* __Probability dp__
* __Tree dp__
    * **定义**：树形dp在树上做动态规划
    * **套路**：
        * 分析父树得到答案**需要子树的哪些信息**
        * 把子树信息的全集定义成递归返回值(不区分左右子树，左右子树merge到一起)
        * 通过递归让子树返回全集信息(用什么父节点决定)
        * 整合子树的全集信息得到父树的全集信息并返回(父节点再次整合自己需要的信息并返回)
    * **注意点：**
        * 也可能是子节点需要父节点信息，灵活处理
    * **空节点处理(边界初始化)**：本质是树的初始化和边界处理，也就是哨兵
* __状态压缩dp__
    * **套路：**
        * 设计一个整型可变参数status，利用status的位信息，来表示某个样本是否还能使用，然后利用这个信息进行尝试。
        * 写出尝试的递归函数->记忆化搜索->严格位置以来的动态规划->空间压缩等优化
        * 如果有k个样本，那么表示这些样本的状态，数量是$2^k$，所以可变参数status的范围:$0\sim(2^k-1)$
    * **注意点：**
        * 样本每增加一个，状态的数量是指数级增长的，所以状压dp能解决的问题往往样本数据量都不大一般样本数量在**20**以内$(10^6)$，如果超过这个数量，计算量（指令条数）会超过 $10^7\sim 10^8$。经典例题：我能赢吗
        * 利用status来表示选择的对象，注意上述的样本数量的范围限制，**需要选择合适的对象来作为status表示的被选择的对象**
    * **典型代码**
        ```python
        # 数能不能选择；选择该数
        if ((status & (1 << i))) !=0 and !f(n, (status ^ (1 << i)), rest - i, dp)
        ```