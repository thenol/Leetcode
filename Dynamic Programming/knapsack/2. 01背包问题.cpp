// from ACWING
// 有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。

// 第 i 件物品的体积是 vi，价值是 wi。

// 求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
// 输出最大价值。

// 输入格式
// 第一行两个整数，N，V，用空格隔开，分别表示物品数量和背包容积。

// 接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 件物品的体积和价值。

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
// 8

#include<bits/stdc++.h>
using namespace std;
int main(){
    int N,V;
    cin>>N>>V;
    int dp[N+1][V+1]; //
    int v[N+1],w[N+1];
    for(int i=1;i<=N;i++){
        cin>>v[i]>>w[i];
    }
    memset(dp,0,sizeof(dp));
    for(int i=1;i<=N;i++)//[0,:],[:,0] as the boundary
        for(int j=1;j<=V;j++){
           dp[i][j]=dp[i-1][j];//放不下，价值不变
           if(j>=v[i])//如果放得下，更新价值
                dp[i][j]=max(
                    dp[i-1][j], // 不选
                    dp[i-1][j-v[i]]+w[i]); // 只能 选择 1 个，
                    // 注意 d[i][j]，代表前 i 个物品中，背包容量为 j 时候的最大价值，也就意味着背包里面 包含了所有的可能性，可能放了无数个 i 
                    // 而题意中，每样物品只能选择 1 次，因此为了确保 只选了 1 次，因此必须是从前 i-1 个物品中（因此一定没有i），背包为 j-v[i] 的时候，选择一个 i ，即 +w[i]
                    // 一定要注意状态的精准把握和理解 d[i][j] 代表了前 i 个物品中，背包容量为 j 时候的所有可能的最大价值
        }
    cout<<dp[N][V]<<endl; //note dp[N][V],dp[N][V-1]... are all optimal value
}


//Carefully consider the comparison with the enumeration method

#include<bits/stdc++.h>
using namespace std;
int main(){
    int N,V;
    cin>>N>>V;
    int dp[V+1];
    int v[N+1],w[N+1];
    for(int i=1;i<=N;i++){
        cin>>v[i]>>w[i];
    }
    memset(dp,0,sizeof(dp));
    for(int i=1;i<=N;i++)//[0,:],[:,0] as the boundary
        for(int j=V;j>=v[i];j--){
            dp[j]=max(dp[j],dp[j-v[i]]+w[i]);
        }
    cout<<dp[V]<<endl;
}