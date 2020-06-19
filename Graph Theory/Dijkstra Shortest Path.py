# 5
# 7
# 1 2 10
# 1 4 30
# 1 5 100
# 2 3 50
# 3 5 10
# 4 3 20
# 4 5 60

n=int(input())
e=int(input())
INF=float('inf')
g=[[INF for _ in range(n+1)] for _ in range(n+1)]
for k in range(e):
    num=input().split(' ')
    i,j,v=int(num[0]),int(num[1]),float(num[2])
    g[i][j]=g[j][i]=v

def dijkstra(graph,n,start):
    INF=float('inf')

    # initialization
    path=[i for i in range(n+1)]
    vis=[0 for i in range(n+1)]
    dist=[INF for i in range(n+1)]
    for i in range(n+1):
        if graph[start][i]<INF:
            path[i]=start
            dist[i]=graph[start][i]

    dist[start]=0
    path[start]=-1
    vis[start]=1

    # n-1 
    for i in range(n-1):
        # select
        mn=INF
        idx=-1
        for d in range(n+1):
            if not vis[d] and dist[d]<mn:
                mn=dist[d]
                idx=d
        vis[idx]=1
        # update
        for k in range(n+1):
            if not vis[k] and dist[idx]+graph[idx][k]<dist[k]:
                dist[k]=dist[idx]+graph[idx][k]
                path[k]=idx

    return dist,path
def pth(arr,n):
    path=[]
    while arr[n]!=-1:
        path.append(n)
        n=arr[n]
    path.append(n)
    return path[::-1]

dist,path=dijkstra(g,n,0)
print(dist)
print(pth(path,6))

