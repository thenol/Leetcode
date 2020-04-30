// 链接：https://ac.nowcoder.com/acm/problem/24382
// 来源：牛客网

// 题目描述 
//     W学长有很多零花钱，其中包括1元，5元，10元三种面值的纸币。现在他想出去买巧克力用掉这些零钱，但是他又不想带太多钱，而且他不想找零，因为他觉得找零意味着又产生了新的零钱。请你帮忙计算W学长最少需要带几张纸币才能刚好买到巧克力。

// 输入描述:
// 第一行一个T（1≤T≤1000），表示测试数据组数。

// 第二行4个数m（1≤m≤100）,a,b,c,分别表示巧克力售价，W学长拥有的1元纸币、5元纸币、10元纸币的数量。（0≤a,b,c≤10）。
// 输出描述:
// 一个数，表示最少要带的纸币数量，如果拿已有的钱无法刚好买到巧克力则输出-1。
// 示例1
// 输入
// 复制
// 3
// 16 4 3 1
// 10 2 1 2
// 8 2 1 3
// 输出
// 复制
// 3
// 1
// -1

// two dimension array d[i][j]: items among first i, volume is j

#include<bits/stdc++.h>
using namespace std;
# define INF 0x3f
int f[4][101];
int main(){
    int T;
    cin>>T;
    while(T--){
        int v[4]={0,1,5,10};
        int s[4],m;
        cin>>m;
        memset(f,INF,sizeof(f));
        //!!!!! the most important initialization, which is actually the base of recursion or the ending condition of the recursion
        /*
            if(j==0) f[i][0]=0 :means 0 money
            if(i==0&&j>0) f[0][j]=INF : unavailable, get to understand the benefit of the operation
        */
        for(int i=0;i<=3;i++)f[i][0]=0; 
        for(int i=1;i<=3;i++)cin>>s[i];
        for(int i=1;i<=3;i++){
            for(int j=1;j<=m;j++){
                for(int k=0;k<=s[i]&&k*v[i]<=m;k++){
                    if(j>=k*v[i])f[i][j]=min(f[i][j],f[i-1][j-k*v[i]]+k);
                }
            }
        }
        if(f[3][m]==INF)cout<<-1<<endl;
        cout<<f[3][m]<<endl;
    }
}


// version 2: one dimenssion array
#include<bits/stdc++.h>
using namespace std;
const int N=110;
int main()
{
    int T; cin >> T;
    while (T --) {
        int m, a[4], b[4] = {0, 1, 5, 10};
        cin >> m >> a[1] >> a[2] >> a[3];
        vector<int> dp(m+1, m+1);
        dp[0] = 0;
        int i, j, k;
        for (i = 1; i <= 3; i ++) {
            for (j = m; j >= b[i]; j --) {
                for (k = 1; k <= a[i]; k ++) {
                    if (j-k*b[i] < 0) break;
                    dp[j] = min(dp[j], dp[j-k*b[i]]+k);
                }
            }
        }
        if (dp[m] == m+1) cout << -1 << endl;
        else cout << dp[m] << endl;
    }
 
    return 0;
}
