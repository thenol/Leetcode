// 给你一个n种面值的货币系统，求组成面值为m的货币有多少种方案。

// 输入格式
// 第一行，包含两个整数n和m。

// 接下来n行，每行包含一个整数，表示一种货币的面值。

// 输出格式
// 共一行，包含一个整数，表示方案数。

// 数据范围
// n≤15,m≤3000

// 输入样例：
// 3 10
// 1
// 2
// 5
// 输出样例：
// 10
// ————————————————
// 版权声明：本文为CSDN博主「njuptACMcxk」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
// 原文链接：https://blog.csdn.net/njuptACMcxk/java/article/details/105523079

// 分析：
// n种货币<=>n种物品
// 组成面值为m的货币<=>装满容量为m的背包。!!!!!!!!!!!

// 问题即从n种物品中选择，求能够装满背包的方案总数，转化为完全背包问题。问题即从n种物品中选择，
// 求能够装满背包的方案总数，转化为完全背包问题。问题即从n种物品中选择，求能够装满背包的方案总数，转化为完全背包问题。



/**
 * the capacity of the package is just V
 * state: d[i][j] means the number of combination using items selected from the previous i items to fill the volume j.
 * Note the total volume equals j
 * state transition: d[i][j]=d[i-1][j]+d[i][j-v[i]]
 * simplify: f[j]=f[j]+f[j-v[i]]
 */

#include<iostream>
#include<algorithm>

using namespace std;

const int N=3010;

int n,m;
long long f[N];

int main()
{
    cin>>n>>m;
    
    f[0]=1;
    for(int i=1;i<=n;i++)
    {
        int v;
        cin>>v;
        for(int j=v;j<=m;j++)
            f[j]+=f[j-v];
    }
    
    cout<<f[m]<<endl;
    
    return 0;
}