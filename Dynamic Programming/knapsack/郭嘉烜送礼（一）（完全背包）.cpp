// 链接：https://ac.nowcoder.com/acm/problem/25745
// 来源：牛客网

// 题目描述 
// 郭嘉烜现在在给女朋友挑礼物，以提升女朋友对他的好感度。商店里有n种礼物，他们的库存都是无限的。第i种礼物能够提升女朋友对他的好感度v[i]，第i种礼物的价格为w[i]，现在郭嘉烜只有c元，问他应该挑选哪些礼物来使得女朋友对他的好感度提升最多。
// 输入描述:
// 第一行包括两个整数n、c。

// 接下来n行，每行2个数，表示表示第i种礼物能够提升女朋友对他的好感度v[i]与第i种礼物的价格w[i]。
// 输出描述:
// 一行。一个整数，表示最多能提升的好感度。
// 示例1
// 输入
// 复制
// 2 2
// 1 1
// 2 1
// 输出
// 复制
// 4
// 备注:
// 1<=n,c<=1000,1<=v[i],w[i]<=100


// total knapsack
#include<bits/stdc++.h>
using namespace std;
const int N=105;
int v[N],w[N];
int f[1010];
int main(){
    int n,c;
    cin>>n>>c;
    for(int i=1;i<=n;i++){
        int v,w;
        cin>>v>>w;
        for(int j=w;j<=c;j++){
            f[j]=max(f[j],f[j-w]+v);
        }
    }
    cout<<f[c]<<endl;
    
}