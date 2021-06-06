#include<bits/stdc++.h>
# define INF 0x3f3f3f3f
using namespace std;
int w[100][100];
int dijkstra(int w[][100],int n,int path[],int dis[],int vis[])
{
    //初始化v[0]到v[i]的距离
    for(int i=1;i<=n;i++){
        dis[i] = w[0][i];      
        path[i]= w[0][i]==INF?i:0;                                 
    }
    vis[0]=1;//标记v[0]点
    path[0]=-1;
    for(int i = 1; i <= n-1; i++) // total n-1 times
    {
        //查找最近点
        int min = INF,k = 0;
        for(int j = 0; j <= n; j++)
            if(!vis[j] && dis[j] < min)
                min = dis[j],k = j;
        vis[k] = 1;//标记查找到的最近点
        //判断是直接v[0]连接v[j]短，还是经过v[k]连接v[j]更短
        for(int j = 1; j <= n; j++)
            if(!vis[j] && min+w[k][j] < dis[j]){
                dis[j] = min+w[k][j];
                path[j]=k;
            }
    }
    return dis[n];
}
int main(){
    int n,edge;
    cin>>n>>edge;
    memset(w,INF,sizeof(w));
    int path[n+1],vis[n+1]={0},dis[n+1]={INF};
    for(int k=1;k<=edge;k++){
        int i,j,val;
        cin>>i>>j>>val;
        w[i][j]=w[j][i]=val;
    }
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            cout<<(w[i][j]>100?-1:w[i][j])<<' ';
        }
        cout<<endl;
    }
    cout<<dijkstra(w,5,path,dis,vis)<<endl;
}


