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




# optimized Dijkstra algorithm using heap data structure
def dijkstra(G,start):     ###dijkstra算法    
    INF = 999999999
 
    dis = dict((key,INF) for key in G)    # start到每个点的距离
    dis[start] = 0
    vis = dict((key,False) for key in G)    #是否访问过，1位访问过，0为未访问
    ###堆优化
    pq = []    #存放排序后的值
    heapq.heappush(pq,[dis[start],start])
 
    t3 = time.time()
    path = dict((key,[start]) for key in G)    #记录到每个点的路径
    while len(pq)>0:
        v_dis,v = heapq.heappop(pq)    #未访问点中距离最小的点和对应的距离
        if vis[v] == True:
            continue
        vis[v] = True
        p = path[v].copy()    #到v的最短路径
        for node in G[v]:    #与v直接相连的点
            new_dis = dis[v] + float(G[v][node])
            if new_dis < dis[node] and (not vis[node]):    #如果与v直接相连的node通过v到src的距离小于dis中对应的node的值,则用小的值替换
                dis[node] = new_dis    #更新点的距离
              #  dis_un[node][0] = new_dis    #更新未访问的点到start的距离
                heapq.heappush(pq,[dis[node],node])
                temp = p.copy()
                temp.append(node)    #更新node的路径
                path[node] = temp    #将新路径赋值给temp
 
    t4 = time.time()
    print('Dijkstra算法所用时间:',t4-t3)
    return dis,path