//落谷 p5788
//寻找数列中第 i 个元素之后第一个大于a[i]的元素的下标
//怎么做！面对这样的数据，不好下手。那么我们把她转化一下：有n个人，每个人向右看，求她看到的第一个人。
//https://www.luogu.com.cn/problemnew/solution/P5788
/*
input:

5
1 4 2 3 5

output:
2 5 4 5 0
*/


#include<cstdio>
#include<stack>
using namespace std;
int n,a[3000005],f[3000005];//a是需要判断的数组（即输入的数组），f是存储答案的数组
stack<int>s;//模拟用的栈
int main()
{
    scanf("%d",&n);
    for(int i=1;i<=n;i++) scanf("%d",&a[i]);
    for(int i=n;i>=1;i--)// for right to left
    {
        while(!s.empty()&&a[s.top()]<=a[i]) s.pop();//弹出栈顶比当前数小的(若栈顶在数组尾部，则单调递减)
        f[i]=s.empty()?0:s.top();//存储答案，由于没有比她大的要输出0，所以加了个三目运算,找到右边第一个比自己高的人,并且记下
        s.push(i);//压入当前元素
    }
    for(int i=1;i<=n;i++) printf("%d ",f[i]);//输出
    return 0;
}