// 链接：https://ac.nowcoder.com/acm/problem/19990
// 来源：牛客网

// [HAOI2012]音量调节
// 题目描述 
// 一个吉他手准备参加一场演出。他不喜欢在演出时始终使用同一个音量，所以他决定每一首歌之前他都要改变一次音量。在演出开始之前，他已经做好了一个列表，里面写着在每首歌开始之前他想要改变的音量是多少。每一次改变音量，他可以选择调高也可以调低。
// 音量用一个整数描述。输入文件中给定整数beginLevel，代表吉他刚开始的音量，以及整数maxLevel，代表吉他的最大音量。音量不能小于0也不能大于maxLevel。输入文件中还给定了n个整数c1,c2,c3…..cn，表示在第i首歌开始之前吉他手想要改变的音量是多少。
// 吉他手想以最大的音量演奏最后一首歌，你的任务是找到这个最大音量是多少。
// 输入描述:
// 第一行依次为三个整数：n, beginLevel, maxlevel。
// 第二行依次为n个整数：c1,c2,c3…..cn。
// 输出描述:
// 输出演奏最后一首歌的最大音量。如果吉他手无法避免音量低于0或者高于maxLevel，输出-1。
// 示例1
// 输入
// 复制
// 3 5 10               
// 5 3 7
// 输出
// 复制
// 10

#include<bits/stdc++.h>
using namespace std;
int main(){
    int n,b,m;
    cin>>n>>b>>m;
    int v[n];
    bool d[n][m+1];
    memset(d,false,sizeof(d));
    for(int i=0;i<n;i++)cin>>v[i];
    if(b-v[0]>=0)d[0][b-v[0]]=true;
    if(b+v[0]<=m)d[0][b+v[0]]=true;
    for( int i=0;i<n-1;i++){
        for(int j=0;j<=m;j++){
            if(d[i][j]){
                b=j;
                if(b-v[i+1]>=0)d[i+1][b-v[i+1]]=true;
                if(b+v[i+1]<=m)d[i+1][b+v[i+1]]=true;
            }
        }
    }
    int ans=-1;
    for(int j=m;j>=0;j--){
         if (d[n-1][j]){
             ans=j;
             break;
         }
    }
    cout<<ans;
    
}