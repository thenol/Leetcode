// 简单的烦恼
// 链接：https://ac.nowcoder.com/acm/problem/25184
// 来源：牛客网

// 题目描述 
// 网易云音乐推出了定时关闭播放的功能，假设到了定时关闭播放的时间，当前这首歌还没有播放完，那就把它播放完关闭；如果到了定时关闭的时间，当前歌恰好播放完，那就立即关闭。xrc 在知道网易云这个算法后，想知道如果自己定时 t 时间后关闭播放，那最多能听多长时间的歌，已知 xrc 歌单中一共有 n 首歌，并且知道每首歌的播放时间分别是 a[i]。

// 输入描述:
// 第一行一个整数T(T <=
// 23)，表示数据组数。

// 在每组输入数据中，第一行有两个正整数，n(n
// <= 200), t(t <= 80000)，分别表示歌单中歌曲的数目，和题目描述中的t。

// 第二行中有n个正整数a[i](a[i] <= 400),表示每首歌曲的时间长度。
// 输出描述:
// 对于每组数据，输出一个ans，表示最多能听多长时间的歌曲。
// 示例1
// 输入
// 复制
// 1
// 3 7
// 4 3 2
// 输出
// 复制
// 9
// 说明
// 先听第2首歌和第3首歌，最后播放第1首歌，在7单位时间后，第3首歌还没有播放完，所以要等第1首歌播放完，共能听9单位时间的歌。

#include<bits/stdc++.h>
using namespace std;
int main(){
    int T;
    cin>>T;
    int n,t;
    while(T--){
        cin>>n>>t;
        int a[n+1];
        int dp[n+1][t+1];
        memset(a,0,sizeof(a));
        memset(dp,0,sizeof(dp));
        for(int i=1;i<=n;i++)cin>>a[i];
        sort(a+1,a+n+1);
        for(int i=1;i<=n-1;i++){//有i无i的dfs,无i是对整个集合进行dfs,有i只需按照这种决策顺序，进行dfs
            for(int j=1;j<=t-1;j++){
                dp[i][j]=dp[i-1][j];
                if(j>=a[i]){
                    dp[i][j]=max(dp[i][j],dp[i-1][j-a[i]]+a[i]);//选i的条件
                }
            }
        }
        cout<<dp[n-1][t-1]+a[n]<<endl;
    }
    return 0;
}

// 0-1 backpack problem:
// If the last song is deleted, it can be converted to a 0-1 backpack problem with a volume of t-1. 
// The goal is to solve for the maximum volume of any combined subsequence.

//!!!!!!! Pay attention to line breaks in new code.


// Wrong code !!!
// for(int i=1;i<=n-1;i++){//有i无i的dfs,无i是对整个集合进行dfs,有i只需按照这种决策顺序，进行dfs
//     for(int j=1;j<=t-1;j++){
//         dp[i][j]=(i==1?a[i]:dp[i-1][j]); //note the d[i][1]=0 !!! because it is now the 0-1 knapsack problem now !!!!!
//         if(j>=a[i]){
//             dp[i][j]=max(dp[i][j],dp[i-1][j-a[i]]+a[i]);//选i的条件
//         }
//     }
// }
