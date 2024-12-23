#### <center>STL</center>

* C++ 标准模板库的核心包括以下三个组件：
    |组件|描述|
    |-|-|
    |容器（Containers）|	容器是用来管理某一类对象的集合。C++ 提供了各种不同类|型|的容器，比如| deque、list、vector、map 等。|
    |算法（Algorithms）|	算法作用于容器。它们提供了执行各种操作的方式，包括对|容|器内容执行初始化、排序、搜索和转换等操作。|
    |迭代器（iterators）|	迭代器用于遍历对象集合的元素。这些集合可能是容器，也可能是容器的子集。|
* <a href='http://www.cplusplus.com/reference/'>容器模板类:</a>
    * 序列容器
        |头文件|说明|
        |-|-|
        |<a href='http://www.cplusplus.com/reference/array/array/'>array</a>| (c++11 only)	数组类 （模板类）|
        |<a href='http://www.cplusplus.com/reference/vector/vector/'>vector</a>|	动态数组 （模板类）|
        |<a href='http://www.cplusplus.com/reference/deque/deque/'>deque</a>|	双端队列 （模板类）|
        |<a href='http://www.cplusplus.com/reference/forward_list/forward_list/'>forward_list</a>|	单链表 （模板类）|
        |<a href='http://www.cplusplus.com/reference/list/list/'>list (c++11 only)</a>	链表| （模板类）|

        * 成员变量：size, 
        * 方法：
            * 访问：front, back, at, [], 
            * 修改：push_back, pop_back, push_front(deque), pop_front(deque)
    * 容器适配器
        |头文件|说明|
        |-|-|
        |<a href='http://www.cplusplus.com/reference/stack/stack/'>stack</a>|	先入后出栈 （模板类）|
        |<a href='http://www.cplusplus.com/reference/queue/queue/'>queue</a>|	先入先出队列 （模板类）|
        |<a href='http://www.cplusplus.com/reference/queue/priority_queue/'>priority_queue</a>|	优先队列 （模板类）|
    * 关联容器
        |头文件|说明|
        |-|-|
        |<a href='http://www.cplusplus.com/reference/set/set/'>set</a>|	集合 （模板类）|
        |<a href='http://www.cplusplus.com/reference/set/multiset/'>multiset</a>|	多重集合 （模板类）|
        |<a href='http://www.cplusplus.com/reference/map/map/'>map</a>|	映射 （模板类）|
        |<a href='http://www.cplusplus.com/reference/map/multimap/'>multimap</a>|	多重影射 （模板类）|
    * 无序关联容器
        |头文件|说明|
        |-|-|
        |<a href='http://www.cplusplus.com/reference/unordered_set/unordered_set/'>unordered_set</a>|	无序集合 （模板类）|
        |<a href='http://www.cplusplus.com/reference/unordered_set/unordered_multiset/'>unordered_multiset</a>|	无序多重集合 （模板类）|
        |<a href='http://www.cplusplus.com/reference/unordered_map/unordered_map/'>unordered_map</a>|	无序映射 （模板类）|
        |<a href='http://www.cplusplus.com/reference/unordered_map/unordered_multimap/'>unordered_multimap</a>|	无序多重映射 （模板类）|
    
        