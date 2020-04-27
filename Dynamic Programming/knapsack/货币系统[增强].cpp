// 链接：https://ac.nowcoder.com/acm/problem/21467
// 来源：牛客网

// 题目描述 
// 在网友的国度中共有n种不同面额的货币，第i种货币的面额为a[i]，你可以假设每一种货币都有无穷多张。为了方便，我们把货币种数为n、面额数组为a[1..n]的货币系统记作(n,a)。
// 在一个完善的货币系统中，每一个非负整数的金额x 都应该可以被表示出，即对每一个非负整数x，都存在n个非负整数t[i] 满足a[i] x t[i] 的和为x。然而，在网友的国度中，货币系统可能是不完善的，即可能存在金额x不能被该货币系统表示出。例如在货币系统n=3, a=[2,5,9]中，金额1,3就无法被表示出来。
// 两个货币系统(n,a)和(m,b)是等价的，当且仅当对于任意非负整数x，它要么均可以被两个货币系统表出，要么不能被其中任何一个表出。
// 现在网友们打算简化一下货币系统。他们希望找到一个货币系统(m,b)，满足(m,b) 与原来的货币系统(n,a)等价，且m尽可能的小。他们希望你来协助完成这个艰巨的任务：找到最小的m。
// 输入描述:
// 输入的第一行包含一个整数T,表示数据组数。接下来按照如下格式分别给出T组数据。
// 每组数据的第一行包含一个正整数n。接下来一行包含n个由空格隔开的正整数a[i]。
// 输出描述:
// 输出文件共T行, 对于每组数据, 输出一行一个正整数, 表示所有与(n, a)等价的货币系统(m, b)中, 最小的m。
// 示例1
// 输入
// 复制
// 2
// 4
// 3 19 10 6
// 5
// 11 29 13 19 17
// 输出
// 复制
// 2
// 5
// 说明
// 在第一组数据中，货币系统(2, [3,10])和给出的货币系统(n, a)等价，并可以验证不存在m < 2的等价的货币系统，因此答案为2。
// 在第二组数据中，可以验证不存在m < n的等价的货币系统，因此答案为5。
// 备注:
// 1 <= T <= 20, 1 <= n <= 100, 1 <= a[i] <= 25000

// 分析参见：https://blog.csdn.net/njuptACMcxk/article/details/105523079?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1

// It can be regarded as total knapsack, for each volume a[i]
// As a matter of fact, while calculatint the total knapsack <N,V>
// all volumes less than V have been calculated in the state transition, which comes from state transition
// if(j>=v[i])d[i][j]=max(d[i-1][j],d[i-1][j-v[i]]) // i.e. the volume of j-v[i] has been calculated


// total knapsack
# include<bits/stdc++.h>
using namespace std;
const int M=25000;
int main(){
    int T;
    cin>>T;
    while(T--){
        int n;
        cin>>n;
        int a[n+1];
        int f[M+1];
        int ans=n;
        memset(f,0,sizeof(f));
        f[0]=1;
        for(int i=1;i<=n;i++)cin>>a[i];
        sort(a+1,a+n+1);
        for(int i=1;i<=n;i++){
            if(f[a[i]]){ // total knapsack, volume equals a[i], i.e. calculating the total knapsack whose volume equals a[i]
                ans--;
                continue;
            }
            for(int j=a[i];j<=a[n];j++){// calculate knapsack whose volume equals a[i],a[i]+1,...,a[n] using previous i items
                f[j]= f[j]||f[j-a[i]];//f[i][j]=f[i-1][j]||f[i][j-a[i]] for two dimenssion
            }
            
        }
        cout<<ans<<endl;
    }
    
}