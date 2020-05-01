//acwing
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
// 0<N≤1000
// 0<V≤2000
// 0<vi,wi,si≤2000
// 提示：
// 本题考查多重背包的二进制优化方法。

// 输入样例
// 4 5
// 1 2 3
// 2 4 1
// 3 4 3
// 4 5 2
// 输出样例：
// 10

# include<bits/stdc++.h>
using namespace std;
const int SIZE=15000;//打包个数 新的物品总数=每个物品size * 物品总数 =log(2000)*N = 12000 【0-1背包的扩展】
int f[SIZE], v[SIZE],w[SIZE];    
int main(){
    int N,V;
    cin>>N>>V;
    // package
    int idx=1;
    for(int i=1;i<=N;i++){
        int a,b,s;
        cin>>a>>b>>s;

        // 打包
        for(int k=1;k<=s;k<<=1){
            v[idx]=k*a;
            w[idx++]=k*b;
            s-=k;
        }
        if(s>0){
            v[idx]=s*a;
            w[idx++]=s*b; //必须自增，因为还有下一个物品
        }
    }

    //0-1背包
    for(int i=1;i<=idx;i++)
        for(int j=V;j>=v[i];j--){
            f[j]=max(f[j],f[j-v[i]]+w[i]);
        }
    cout<<f[V]<<endl;
    return 0;
}

/*
The essence is that the number of i can be decomposed into a combination of many binary numbers.
e.g.
s=7
0 0
1 1
2 2
3 1+2
4 4
5 1+4
6 2+4
7 1+2+4

打包策略:
包大小为:1 2 4

s=4
包队列为:1 2 1

s=10
包大小列表: 1 2 4 (3)
*/