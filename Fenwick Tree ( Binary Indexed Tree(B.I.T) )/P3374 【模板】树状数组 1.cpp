/*
【落谷】
题目描述
如题，已知一个数列，你需要进行下面两种操作：

将某一个数加上 xx

求出某区间每一个数的和

输入格式
第一行包含两个正整数 n,mn,m，分别表示该数列数字的个数和操作的总个数。

第二行包含 nn 个用空格分隔的整数，其中第 ii 个数字表示数列第 ii 项的初始值。

接下来 mm 行每行包含 33 个整数，表示一个操作，具体如下：

1 x k 含义：将第 xx 个数加上 kk

2 x y 含义：输出区间 [x,y][x,y] 内每个数的和

输出格式
输出包含若干行整数，即为所有操作 22 的结果。

输入输出样例
输入 #1复制
5 5
1 5 4 2 3
1 1 3
2 2 5
1 3 -1
1 4 2
2 1 4
输出 #1复制
14
16
说明/提示
【数据范围】

对于 30\%30% 的数据，1 \le n \le 81≤n≤8，1\le m \le 101≤m≤10；
对于 70\%70% 的数据，1\le n,m \le 10^41≤n,m≤10 
4
 ；
对于 100\%100% 的数据，1\le n,m \le 5\times 10^51≤n,m≤5×10 
5
 。

样例说明：



故输出结果14、16
*/

// 单点修改，区间查询

#include<bits/stdc++.h>
using namespace std;
int n,m,num[500000+5],t[500000*2+5];
int update(int x,int v){
    for(;x<=n;x+=x&-x)t[x]+=v;
}
int sum(int x){
    int sum=0;
    for(;x>=1;x-=x&-x)sum+=t[x];
    return sum;
}
int ask(int l,int r){
    return sum(r)-sum(l-1);
}
int main(){
    int a,b,c;
    cin>>n>>m;
    for(int i=1;i<=n;i++){cin>>num[i];update(i,num[i]);}
    for(int i=1;i<=m;i++){
        cin>>a>>b>>c;
        if(a==1)update(b,c);
        else
            cout<<ask(b,c)<<endl;
    }
    return 0;
}