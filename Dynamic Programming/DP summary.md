### Dynamic programming
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
* __Probability dp__
* __Tree dp__