// 单点修改，区间查询

#include<iostream>
using namespace std;
int n,m,i,num[100001],t[100001],l,r;//num:原数组；t：树状数组 
void update(int x,int p)//将第x个数加p 
{
    for(;x<=n;x+=x&-x) t[x]+=p; //更新父节点
}
int sum(int x)//前k个数的和 ，前缀和
{
    int ans=0;
    for(;x>1;x-=x&-x) ans+=t[x]; //寻找
    return ans;
}
int ask(int l,int r)//求l-r区间和 即：[l,r] 左闭右闭
{
    return sum(r)-sum(l-1); 
}


int main()
{
    cin>>n>>m;
    for(i=1;i<=n;i++) // 下标从1开始
    {
        cin>>num[i];
        update(i,num[i]);
    }
    for(i=1;i<=m;i++)
    {
        cin>>l>>r;
        cout<<ask(l,r)<<endl;
    }
    return 0;
}