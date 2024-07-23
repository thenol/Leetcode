### Dynamic programming
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
    * 破环成链
        * 多边形
    * 先遍历区间
* __Probability dp__
* __Tree dp__