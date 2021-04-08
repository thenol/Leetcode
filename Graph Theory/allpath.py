def get_neighbor_available_sats(fr_sats, t=0):
    global delay
    border_sats=set()
    def add(x): 
        nonlocal border_sats
        res = (border_sats | {x}) if x not in fr_sats else border_sats
        border_sats|=(res)
        
    for sat in fr_sats:
        front, behind, left, right = jump(sat,0,1), jump(sat,0,-1), jump(sat,-1,0), jump(sat,1,0)
        add(front)
        add(behind)
        add(left)
        add(right)
    return border_sats

        
# 从候选集，生成源和目的地对
get_pairs = lambda border_sats: [(border_sats[i],border_sats[j]) for i in range(len(border_sats)) for j in range(i+1,len(border_sats))]

def get_real_NAP_planes(boundary_planes,fr_sats,direction='N'):
    '''
        获得真正高风险区域的四个最近可通行边界轨道
        参数: boundary_planes from (get_virtual_planes), fr_sats 高风险区域上空的卫星
        return NAPs
    '''
    NAPs={}
    NAPs[direction]=conv_ap(boundary_planes)[direction]
    tmp = get_horizontal_planes(fr_sats)['S' if direction=='N'else 'N']
    NAPs['H']={}
    NAPs['H']['b']=tmp['l']
    NAPs['H']['t']=tmp['r']
    return NAPs

def get_pathes(border_sats,fr_sats=set()):
    path_list=[]
    border_sats = list(border_sats)
    pairs = get_pairs(border_sats)
    i=0
    with tqdm(pairs) as t:
        for s,d in t:
            if s!=d:
                if i==0:
                    fix=False
                else:
                    fix=True
                if fr_sats:
                    RTT, path,cost = rtt(delay,s,d,byhop=True,avoid_set=fr_sats,fix_graph=fix)
                else:
                    RTT, path,cost = rtt(delay,s,d,byhop=True,avoid_set=set(),fix_graph=fix)
                path_list.append(path)
                i+=1
    return path_list
# get_pathes(border_sats)

# path_count = [0 for i in range(1584)]
def path_statistics(path_list):
    path_count = [0 for i in range(1584)]
    for path in path_list:
        for s in path:
            path_count[s]+=1
    return path_count
# path_statistics(path_list)

def path_to_pairs_dict(path):
    '''
    将路径列表转换为{s-d:path,...}
    '''
    dic={}
    for p in path:
        dic[str(p[0])+'-'+str(p[-1])]=p
    return dic

def same_pairs_path(path1,path2):
    '''
    筛选相同的源和目的地对的路径
    '''
    dic1=path_to_pairs_dict(path1)
    dic2=path_to_pairs_dict(path2)
    same_keys=set(dic1.keys())&set(dic2.keys())
    res1=[]
    res2=[]
    for k,v in dic1.items():
        if k in same_keys:
            res1.append(v)
    for k,v in dic2.items():
        if k in same_keys:
            res2.append(v)
    return res1,res2


def get_sat_count_from_path(without_fr,with_fr,opt='lt',raw=False,verbose=False,add_cond=False):
    '''
    对经过卫星的路径进行统计, 注意节点
    可选参数：
        opt[lt,le,gt,ge,False]:用来表示前面两个参数之间的关系，例如 lt 表示 path_count_with[i]<path_count_without[i]
            或者opt={'with':'=0','without':'>0'}
        raw:用来判断是否展示全集数据
        verbose:显示重新筛选后的数据
    
    return (with_list,without_list) # 即有风险区域的卫星路径树统计列表，没有风险区域的卫星路径数统计列表
    
    '''
    path_count_without = path_statistics(without_fr)
    path_count_with = path_statistics(with_fr)

    with_list=[]
    without_list=[]
        
    for i in range(len(path_count_with)):
        if type(opt)==dict:
            add_cond = eval('path_count_with[i]'+add_cond['with']+'and path_count_without[i]'+add_cond['without'])
        if opt=='lt':
            condition=path_count_with[i]<path_count_without[i]
        elif opt=='le':
            condition=path_count_with[i]<=path_count_without[i]
        elif opt=='gt':
            condition=path_count_with[i]>path_count_without[i]
        elif opt=='ge':
            condition=path_count_with[i]>=path_count_without[i]
        elif opt==False:
            condition = opt
        
        if not raw and (path_count_without[i]==0 and path_count_with[i]==0 or condition or add_cond):
            continue
        else:
            if verbose:
                print('卫星编号，有fr时路径数量，没有fr时路径数量：',i,path_count_with[i],path_count_without[i])
            with_list.append(path_count_with[i])
            without_list.append(path_count_without[i])
    return with_list,without_list

def link_info(src, dst, t=0, delta = 0, avoid_set=set(),fix_hop=True, verbose = False):
    '''
    计算从src到dst，距离为distance的所有路径，默认跳数
    '''
    global delay,GRAPH
    start, end = src,dst
    path_list = []
    latency_list = []
#     def backtrace(delay, v1, v2, path, hop, vis, time_delay):
#         nonlocal path_list
#         if hop<=0:
#             return
#         for node, lat in enumerate(delay[v1]):
#             if lat<0 or vis[node]:
#                 continue
#             else:
#                 if node==v2:
#                     path_list.append(path+[v2])
#                     latency_list.append(time_delay+delay[v1][v2])
#                 else:
#                     vis[node]=1
#                     backtrace(delay,node,v2,path+[node], hop-1, vis, time_delay+delay[v1][node])
#                     vis[node]=0
    def BFS(graph,start,end,distance=False, avoid_set =set(), fix_hop=True):
        temp_path = [start]
        q=[]
        q.append(temp_path)
        res=[]
        while q:
            tmp_path = q.pop(0)
            last_node = tmp_path[-1]
            #print tmp_path
            if last_node == end:
                if fix_hop:
                    if len(tmp_path)==distance:
                        res.append(tmp_path)
                else:
                    res.append(tmp_path)
            elif len(tmp_path)>=distance:
                continue
            for link_node in graph[last_node]:
                if link_node not in avoid_set and link_node not in tmp_path:
                    new_path = []
                    new_path = tmp_path + [link_node]
                    q.append(new_path)
        return res

    cost = rtt(delay,start,end, avoid_set = avoid_set, byhop=True,fix_graph=True)
    if verbose:
        print('min_cost:',cost)
    shortest_hop = cost[0]
    vis = [0]*1584
    vis[start]=1
#     backtrace(delay[t],start,end,[start],shortest_hop+delta, vis, 0)
    path_list=BFS(GRAPH,start,end,distance=shortest_hop+delta+1, avoid_set=avoid_set, fix_hop=fix_hop)
    for p in path_list:
        latency = 0
        for i in range(1,len(p)):
            latency+=delay[t][p[i-1]][p[i]]
        latency_list.append(latency)
    return path_list, latency_list, {'min_hop':shortest_hop+1,\
                                     'actual_hop:min_hop+delta:':shortest_hop+delta+1,\
                                    'min_delay:':cost[2],\
                                    'min_delay_path:':cost[1]}