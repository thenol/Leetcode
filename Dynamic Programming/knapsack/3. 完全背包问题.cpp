//ACWING
// 有 N 种物品和一个容量是 V 的背包，每种物品都有无限件可用。

// 第 i 种物品的体积是 vi，价值是 wi。

// 求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
// 输出最大价值。

// 输入格式
// 第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。

// 接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 种物品的体积和价值。

// 输出格式
// 输出一个整数，表示最大价值。

// 数据范围
// 0<N,V≤1000
// 0<vi,wi≤1000
// 输入样例
// 4 5
// 1 2
// 2 4
// 3 4
// 4 5
// 输出样例：
// 10

// version 2:optimization
#include<bits/stdc++.h>
using namespace std;
int main(){
    int N,V;
    cin>>N>>V;
    int dp[N+1][V+1];
    int v[N+1],w[N+1];
    for(int i=1;i<=N;i++){
        cin>>v[i]>>w[i];
    }
    memset(dp,0,sizeof(dp));
    for(int i=1;i<=N;i++){
        for(int j=1;j<=V;j++){
            dp[i][j]=dp[i-1][j];//放不下v[i]，价值不变
            if(j>=v[i])//放得下v[i]，更新价值
                dp[i][j]=max(dp[i][j],dp[i][j-v[i]]+w[i]);//每种无数，所以选完还可以继续接着选
                /*
                ！！！状态理解Congnition！！！
                dp[i][j] 代表只能放前i个物品的情况下，背包容量为j的时候，所有情况下的最大价值，包括可能选择了无数个 i（从 0->∞ ） 商品
                dp[i][j] = max(
                    dp[i-1][j], // 选择0个i
                    dp[i-1][j-v[i]] + w[i] //选择1个i
                    dp[i-1][j-v[i] * 2] + w[i] * 2 //选择2个i
                    ...
                    dp[i-1][j-v[i] * k] + w[i] * k //选择k个i, 即在只能选择前 i-1 个物品，背包容量为 j-v[i] * k 的时候，决定选择 k 个 i，从而增加了 w[i] * k 的价值

                ) = max(
                    dp[i-1][j], // 不选i物品（选择0个i）：只能放前 i-1 个物品的情况下（因此肯定没有 i 物品），背包容量为 j 的时候，不选择放 i 物品
                    dp[i][j - v[i]] + w[i] // 前i个物品中至少选择 1 个i物品：选择了 i 物品，可能选择 1,2,..., ∞ 个
                    // 理解：
                    //      dp[i][j - v[i]] 表示，只能放前i个物品的情况下，背包容量为 j-v[i] 的时候，所有情况下的最大价值，包括可能选择了无数个 i（从 0->∞ ） 商品, 
                    //      + w[i] 表示，最后选择 1 个 i, 
                    //      因此总体上代表的是，只能放前i个物品的情况下，背包容量为 j-v[i] 的时候，至少选择了 1 个 i 的时候的最大价值，
                    //      也就是至少选择 1 个i物品的最大价值
                )
                */
        }
    }
    cout<<dp[N][V]<<endl;//note dp[N][V],dp[N][V-1]... are all optimal value
    
}
// The only difference from 0-1 knapsack is 
// very easy to understand
//dp[i][j]=max(dp[i][j],dp[i][j-v[i]]+w[i]) // total knapsack, because of the infinite number of the products
//dp[i][j]=max(dp[i][j],dp[i-1][j-v[i]]+w[i]) // 0-1 knapsack



#include<bits/stdc++.h>
using namespace std;
int main(){
    int N,V;
    cin>>N>>V;
    int f[1010];
    int v[1010],w[1010];
    for(int i=1;i<=N;i++){
        cin>>v[i]>>w[i];
    }
    memset(f,0,sizeof(f));
    for(int i=1;i<=N;i++){
        for(int j=v[i];j<=V;j++){ 
            f[j]=max(f[j],f[j-v[i]]+w[i]);
        }
    }
    cout<<f[V]<<endl;
    
}
// Note the calculation order
// for(int j=v[i];j<=V;j++) // total knapsack, because of the infinite number of the products
// for(int j=V;j<=v[i];j--) // 0-1 knapsack


// version 2
#include<bits/stdc++.h>
using namespace std;
int f[1005];
int N,V;
int v,w;
int main(){
    cin>>N>>V;
    memset(f,0,sizeof(f));
    for(int i=1;i<=N;i++){
        cin>>v>>w;
        for(int j=v;j<=V;j++){
            f[j]=max(f[j],f[j-v]+w);
        }
    }
    cout<<f[V]<<endl;
}