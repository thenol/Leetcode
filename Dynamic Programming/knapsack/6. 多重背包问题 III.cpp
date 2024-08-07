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


/*
思路：直接看左神b站视频
*/

// use monotonic queue to optimize

/**
 * Analysis:
 * https://www.acwing.com/solution/acwing/content/4237/
 * 解析：
 *  看完全背包转移方程：f[i][j]=max(f[i-1][j],f[i-1][j-v]+w,f[i-1][j-2v]+2w,...,f[i-1][j-sv]+sw)，即找不放i,放1个，放2个，...，放完s个的最大值，
 *  而每个相差都是v，也说明，对于f(i,j)只受和他相差v的倍数的影响，或者只依赖他们，也就是每次必然只能放整数个i,体积为v, 
 *  从而可以换一种遍历方式，按照模余来遍历, 仔细看上面的转移方程，容量的转移本身就是相差v个
 * 故直接就按照模余来遍历：
 *  遍历余数：[0,v-1]:
 *      f[i, j ] = f[i-1, j-v]+w, f[i-1, j-2v]+2w, f[i-1, j-3v] +3w,  f[i-1, j-4v]+4w,  ... f[i-1,j-sv]+sw
        f[i, j-v] =               f[i-1, j-2v]+w,  f[i-1，j-3v] +2w,  f[i-1, j-4v]+3w, ... f[i-1, j-(s+1)v] + sw
        f[i, j-2v] =                               f[i-1, j-3v] +w ,  f[i-1, j-4v]+2w, ...f[i-1, j-(s+2)v] + sw


 *      ...
 *      技巧：如果不用技巧，每次去计算加几个价值的时候比较麻烦，因此可以在入单调队列的时候，先把用变换映射关系减去的这个最大值入队，最后加上就行了，如下
 *      设m % v = d 变换下上面式子可以得出，
 *      f[i, d]    = f[i-1][d]
        f[i, d+v]  = max(f[i-1, d] +w,  f[i-1, d+v])                                    = max(f[i-1, d],  f[i-1, d+v]-w)                                    + w
        f[i, d+2v] = max(f[i-1, d] +2w, f[i-1, d+v] +w,  f[i-1, d+2v])                  = max(f[i-1, d],  f[i-1, d+v]-w, f[i-1, d+2v]-2w)                   + 2w
        f[i, d+3v] = max(f[i-1, d] +3w, f[i-1, d+v] +2w, f[i-1, d+2v]+w,  f[i-1, d+3v]) = max(f[i-1, d],  f[i-1, d+v]-w, f[i-1, d+2v]-2w,  f[i-1, d+3v]-3w) + 3w
        f[i, d+4v] = max(f[i-1, d] +4w, f[i-1, d+v] +3w, f[i-1, d+2v]+2w, f[i-1, d+3v]+w, f[i, d+4v])

        注意：f(i,j) = max(f(i-1,j),f(i-1,j-v)+w,...,f(i-1,j-sv)+sw),也就是f(i-1,j)可以取到，意思是不选或者不放v

        我们发现对于体积 j，j % v = d的话，j的状态仅由体积 % v 也等于d的状态转移而来， 比如d+3v, 仅由体积为d+v, d+2v, d这些状态转移， 这些体积 % v都等于d，我们将之前的状态
        放入单调队列即可， 放入时，有个技巧，放入 f[i-1, d+ jv] - jw  而不是 f[i-1, d+ jv] ，看看上面的式子就知道为啥了，是为了利用之前的结果。 我们减去再加回来就能保证当前状态最后的答案正确了。

        第0次 f[i, d] = f[i-1, d] 入队
        第1次 f[i-1, d+v]-w 进队列与队列之前的数字比较
        第2次 f[i-1, d+2v]-2w 进队列与队列之前的数字比较
        第j次 f[i-1, d+jv]-jw 进队列与之前队列中的数字比较

 *      
 * 1. 关于>s那个判断：注意
 *  f[i, j ] = f[i-1, j-v]+w, f[i-1, j-2v]+2w, f[i-1, j-3v] +3w,  f[i-1, j-4v]+4w,  ... f[i-1,j-sv]+sw 
 *  只跟前S个有关系，因为假设当前体积为j，那么用当前物品i最多为s个，最多只能用s个，所以窗口大小为s，即维护窗口为s的单调队列，记录最大值，即j最多能减s*v，即j-sv
 * 2. 注意技巧：先减j*w，后加j*w
 */

#include<bits/stdc++.h>
using namespace std;
int f[1010][20020];
int q[20020],idx[20020];
int main(){
    int N,V;
    cin>>N>>V;
    for(int i=1;i<=N;i++){
        int v,w,s;
        cin>>v>>w>>s;
        for(int d=0;d<v;d++){
            int head=0,tail=-1; // note: the queue for each mode
            for(int j=0;j<=(V-d)/v;j++){
                int cur=f[i-1][j*v+d]-j*w;

                // save the max
                while(head<=tail&&cur>=q[head])tail--;
                q[++tail]=cur;
                idx[tail]=j;
                if(j-idx[head]>s)head++;
                
                f[i][j*v+d]=q[head]+j*w;
            }
        }
    }
    cout<<f[N][V]<<endl;
}

//如果用deque, 会超时，简单的数据结构，还是自己写比较省时，而且简单，对于记录两个数组指针的情况，很明显，用相同的head,tail来控制两个队列入队出队更简单