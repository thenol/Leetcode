// acwing
// 有 N 种物品和一个容量是 V 的背包。

// 第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。

// 求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
// 输出最大价值。

// 输入格式
// 第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。

// 接下来有 N 行，每行三个整数 vi,wi,si，用空格隔开，分别表示第 i 种物品的体积、价值和数量。

// 输出格式
// 输出一个整数，表示最大价值。

// 数据范围
// 0<N,V≤100
// 0<vi,wi,si≤100
// 输入样例
// 4 5
// 1 2 3
// 2 4 1
// 3 4 3
// 4 5 2
// 输出样例：
// 10

// 思路：朴素做法

// version 1:
# include<bits/stdc++.h>
using namespace std;
int main(){
    int N,V;
    cin>>N>>V;
    int v[N+1],w[N+1],s[N+1];
    int dp[N+1][V+1];
    memset(dp,0,sizeof(dp));
    for(int i=1;i<=N;i++)cin>>v[i]>>w[i]>>s[i];
    for(int i=1;i<=N;i++){
        for(int j=1;j<=V;j++){
            for(int k=0;k<=s[i] && k*v[i]<=V;k++){
                if(j>=k*v[i])//?
                dp[i][j]=max(dp[i][j],dp[i-1][j-k*v[i]]+k*w[i]); // Note k=0:d[i-1][j-k*v[i]]=d[i-1][j] !!! note the calculation order，0-1 knapsack extention
            }
        }
    }
    cout<<dp[N][V]<<endl;
    
}


//version 2: convert to 0-1 knapsack


// 