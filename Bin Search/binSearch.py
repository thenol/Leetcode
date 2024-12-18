# 二分查找总体方法见邓俊辉版本《数据结构》第三版本48页开始

# 减而治之

# 二分查找（版本A）—— 三分支
"""
核心思想：
    以任意元素 S[mi] = x 为界，都可将区间分为三部分，且根据此时的有序性必有：
        S[lo, mi) <= S[mi] <= S(mi, hi)
算法流程：
    于是，只需将目标元素e与x做一比较，即可视比较结果分三种情况做进一步处理：
        1）若e < x，则目标元素如果存在，必属于左侧子区间S[lo, mi)，故可深入其中继续查找；
        2）若x < e，则目标元素如果存在，必属于右侧子区间S(mi, hi)，故也可深入其中继续查找；
        3）若e = x，则意味着已经在此处命中，故查找随即终止。
不足：
    尽管二分查找算法（版本A）即便在最坏情况下也可保证O(logn)的渐进时间复杂度，但就其常系数1.5而言仍有改进余地。以成功查找为例，即便是迭代次数相同的情况，对应的查找长度也不尽相等。究其根源在于，在每一步迭代中为确定左、右分支方向，分别需要做1次或2次元素比较，从而造成不同情况所对应查找长度的不均衡。尽管该版本从表面上看完全均衡，但我们通过以上细致的分析已经看出，最短和最长分支所对应的查找长度相差约两倍。
"""
# 有多个命中元素时，不能保证返回秩最大者；
# 查找失败时，简单地返回-1，而不能指示失败的位置
def binSearch(A, e):
    """
    每次数组被拆分成三个分支
    S[lo, mi) S[mi] 和 S[mi, hi)
    """
    lo, hi = 0, len(A) # ❗️❗️❗️左闭右开❗️❗️❗️
    while lo < hi: # 每步迭代可能要做两次比较判断，有三个分支
        mi = (lo + hi) >> 1 # 以中点为轴点
        if e < A[mi]:
            hi = mi # 深入前半段[lo, mi)继续查找；因为左闭右开，自然hi=mi意味着mi已经被排除
        elif A[mi] < e : # 体会都写小于号的精辟之处
            lo = mi + 1 # 深入后半段(mi, hi)继续查找；因为左闭右开，自然而A[mi]<e，自然mi需要被排除，所以lo=mi+1
        else:
            return mi # 在mi处命中，成功查找可以提前终止
    return -1 # 查找失败，没找到，返回-1


# 二分查找（版本B）—— 从三分支到两分支
"""
核心思想：
    二分查找算法版本A的不均衡性体现为复杂度递推式中(2^(k-1)-1)和2x(2^(k-1)-1)两项的不均衡。为此，Fibonacci查找算法已通过采用黄金分割点，在一定程度上降低了时间复杂度的常系数。实际上还有另一更为直接的方法，即令以上两项的常系数同时等于1。也就是说，无论朝哪个方向深入，都只需做1次元素的大小比较。相应地，算法在每步迭代中（或递归层次上）都只有两个分支方向，而不再是三个。

算法流程：
    与二分查找算法的版本A基本类似。不同之处是，在每个切分点A[mi]处，仅做一次元素比较。
    1) 具体地，若目标元素小于A[mi]，则深入前端子向量A[lo, mi)继续查找；
    2) 否则，深入后端子向量A[mi, hi)继续查找。

进一步的要求：
    在更多细微之处，此前实现的二分查找算法（版本A和B）及Fibonacci查找算法仍有改进的余地。比如，当目标元素在向量中重复出现时，它们只能“随机”地报告其一，具体选取何者取决于算法的分支策略以及当时向量的组成。而在很多场合中，重复元素之间往往会隐含地定义有某种优先级次序，而且算法调用者的确可能希望得到其中优先级最高者。比如按照表2.1的定义，在有多个命中元素时，向量的search()接口应以它们的秩为优先级，并返回其中最靠后者。
    
    这种进一步的要求并非多余。以有序向量的插入操作为例，若通过查找操作不仅能够确定可行的插入位置，而且能够在同时存在多个可行位置时保证返回其中的秩最大者，则不仅可以尽可能低减少需移动的后继元素，更可保证重复的元素按其插入的相对次序排列。对于向量的插入排序等算法（习题[3-8]）的稳定性而言，这一性质更是至关重要。
    
    另外，对失败查找的处理方式也可以改进。查找失败时，以上算法都是简单地统一返回一个标识“-1”。同样地，若在插入新元素e之前通过查找确定适当的插入位置，则希望在查找失败时返回不大（小）于e的最后（前）一个元素，以便将e作为其后继（前驱）插入向量。同样地，此类约定也使得插入排序等算法的实现更为便捷和自然。
""" 
# 有多个命中元素时，不能保证返回秩最大者；
# 查找失败时，简单地返回-1，而不能指示失败的位置
def binSearch(A, e):
    """
    每次数组被拆分成两个分支
    S[lo, mi) 和 S[mi, hi)
    
    算法执行：
        1) 具体地，若目标元素小于A[mi]，则深入前端子向量A[lo, mi)继续查找；
        2) 否则，深入后端子向量A[mi, hi)继续查找。
    
    条件终结：
        左闭右开，hi=lo+1，区间只剩一个元素
    """
    lo, hi = 0, len(A)
    while 1 < hi - lo: # 每步迭代仅需做一次比较判断，有两个分支；成功查找不能提前终止
        mi = (lo + hi) >> 1
        if e < A[mi]: # 经比较后确定深入[lo, mi)或者[mi, hi)
            hi = mi
        else: # A[mi] <= e 情况
            lo = mi # 不是mi+1的原因是，此时 A[mi] <= e，会导致丢失一个元素
        
        # 出口时hi = lo + 1，查找区间仅含一个元素A[lo]
    
    return lo if e == A[lo] else -1 # 查找成功时返回对应的秩；否则统一返回-1；判断原因：A[mi] <= e 情况，即可能A[lo]<e


#  二分查找（版本C）—— 
"""
核心思想：

算法流程：
"""
# 有多个命中元素时，总能保证返回秩最大者；
# 查找失败时，能够返回失败的位置
# 易错点❌：
#   注意不一定是-1，是失败的位置！！！
def binSearch(A, e):
    """
    每次数组被拆分成两个分支
    S[lo, mi) 和 S(mi, hi)
    图像说明：
        0         lo mi hi       n
        [...<=e...   X  ...e<...]
        ✅✅✅相对位置完美记忆：升序，相对e来就行了，e的右边都大于e，e的左边自然小于等于e
    算法执行：
        1) 具体地，若目标元素小于A[mi]，则深入前端子向量A[lo, mi)继续查找；
        2) 否则，深入后端子向量A(mi, hi)继续查找，注意此种写法，跳过了 A[mi]，而 e <= A[mi]，即如果A中存在e，会被跳过一个，如果不存在e，也就是查找失败的时候，会跳到一个比e大的最小值，此时由于A[lo]>e，因此区间[lo, hi)开始收缩
    
    条件终结：
        左闭右开，lo = hi，区间不剩元素，lo最终指向大于e的元素的最小秩，因此lo - 1即不大于e的元素的最大秩
    """
    lo, hi = 0, len(A)
    while lo < hi: # 每步迭代仅需做一次比较判断，有两个分支；成功查找不能提前终止
        mi = (lo + hi) >> 1 # 以中点为轴点
        if e < A[mi]: # 经比较后确定深入[lo, mi)或(mi, hi)
            hi = mi
        else: # A[mi] <= e 的情况
            lo = mi + 1
        
        # 循环结束时，lo为大于e的元素的最小秩，故lo - 1即不大于e的元素的最大秩，即 lo - 1 指向的是小于或者等于e的元素的最大秩

    return lo - 1


# 小的点:
"""
1. hi = mi 而不是 hi = mi-1 解释？
因为，e < A[mi]只意味着A[mi]可以不用考虑了，但是必须，hi = mi - 1可能会导致漏掉一个元素，例如 (1+3)//2=2，但是(1+2)//2 = 1, 因此漏掉一个元素

2. 如何理解上述代码：
    1）易错点❌千万注意：左闭右开 区间
    2）减而治之，区间规模不断缩小
"""

# 扩展，python 二分查找封装函数

#https://blog.csdn.net/YMWM_/article/details/122378152
#bisect.bisect和bisect.bisect_right返回大于x的第一个下标(相当于C++中的upper_bound)，bisect.bisect_left返回大于等于x的第一个下标(相当于C++中的lower_bound)。简记为   [ e <= bisect.bisect_left < bisect.bisect_right )
import bisect
ls = [1,5,9,13,17]
index1 = bisect.bisect(ls,9)
index2 = bisect.bisect_left(ls,9)
index3 = bisect.bisect_right(ls,9)
print("index1 = {}, index2 = {}, index3 = {}".format(index1, index2, index3))
#index1 = 3, index2 = 2, index3 = 3

bisect.bisect_left(ls,0) # 此时，bisect_left = bisect_right 返回 0
bisect.bisect_left(ls,18) # 此时，bisect_left = bisect_right 返回 N = len(ls) = 5

"""
The insort function from the bisect module is specifically designed to insert an element into a sorted list while maintaining the order. It has two variants:

* bisect.insort(arr, cur) is used to insert an element (cur) into a sorted list (arr) while maintaining the list's sorted order
* bisect.insort_left(list, item): Inserts the item into the list while maintaining the sorted order. If the item is already in the list, it inserts it to the left of any existing occurrences.
* bisect.insort_right(list, item): Similar to insort_left, but if the item is already in the list, it inserts it to the right of any existing occurrences.
"""

# 可以使用的模型  ... [ e ] +∞
# 三种可能的位置： ..e1.. [ e2 ] ..e3.. ; e1位置查找失败返回0，e2位置超找成功返回e2，e3位置查找失败返回N
# 因此：
#   1. 查找失败，一共有 两种 情况，返回 0 or N，此时 bisect_left和bisect_right相同
#   2. 查找成功，一共有 一种 情况，返回正常下标，此时bisect_left和bisect_right返回值一定不同
# 

# ❗️❗️❗️总结❗️❗️❗️：
"""
binSearch——C版本中标定一个点 lo及其右侧均大于e, 即 lo为大于e的元素的最小秩

bisect.bisect_left 和 bisect.bisect_right 标定了一个区间[bisect.bisect_left, bisect.bisect_right)，即 e <= bisect.bisect_left < bisect.bisect_right，即：
    1. bisect.bisect_left 为大于等于（不小于）e的元素的最小秩
    2. bisect.bisect_right 为大于e的元素的最小秩（与lo等效）
    3. 0<=bisect.bisect_left<=bisect.bisect_right<=len(arr)
"""


# ❌❌❌❌❌❌❌❌❌❌❌ 错误版本 start ❌❌❌❌❌❌❌❌❌❌
# 思考错误在哪
def binSearch(nums, e):
    """
    返回小于e的最大下标
    核心想法如下图：
        0       lo mi hi        n
        [...<e...  X  ...e<=...]
    """
    lo, hi = 0, len(nums)
    while lo < hi: # 查找tail中比i小的最大值
        mi = (lo + hi) >> 1
        if nums[mi] < e:
            lo = mi
        else:
            hi = mi - 1
        print(lo , hi)
    return lo + 1
# 错误case:
"""
执行binSearch([2, 3, 5, 7, 9, 10, 18, 101], 120)
会陷入死循环，此时lo=7, hi=8
"""
# 根本原因：
"""
死循环必要条件：lo=7, hi=8时
    mi = (lo + hi) >> 1 #  mi=7
    lo = mi # lo = 7
因此造成了死循环
"""
# ❌❌❌❌❌❌❌❌❌❌❌ 错误版本 end ❌❌❌❌❌❌❌❌❌❌

# 总结向下整除的常见错误点❌
"""
1. 相邻数对：(1+2)//2=1, (2+3)//2=2 为左
2. 隔1数对：(1+3)//2=2, (2+4)//2=3  为中
3. 隔2数对：(1+4)//2=2, (2+4)//2=3  为中左
也就是说，(lo+hi)//2一定是[lo, hi]中间偏lo一侧的数值，换句话说
    
    千万注意易错点❌❌❌：只要lo < hi，则一定有lo <= (lo+hi)//2 < hi
                      当 lo == hi，则自然 lo==(lo+hi)//2==hi

证明：
    假设 lo < hi，则 (lo+lo)/2=lo < (lo+hi)/2 < (hi+hi)//2=hi
    但是对于计算机中的向下取整 lo<= (lo+hi)//2 < (hi+hi)//2=hi
    因此只要 lo < hi，则 lo <= (lo+hi)//2 < hi，就一定在 hi 点是开区间，即规模缩减，也从侧面解释了为啥是左闭右开

因此 hi=mi 不会错误，能够正常缩减规模，但是 lo=mi可能引起死循环

而在版本B中
hi - lo >1 即 hi - lo >=2，也就是 hi>=lo+2，因此 (hi+lo)//2>=(2lo+2)//2=lo+1>=1，因此每次赋值时，mi=(lo+hi)>>1 不可能 等于 lo
"""