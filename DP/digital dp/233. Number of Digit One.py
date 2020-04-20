'''
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example:

Input: 13
Output: 6 
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-digit-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
a=13
digits=[]
def convert(n):
    while n:
        digits.append(n%10)
        n=n//10
convert(a)
# note the order of the list

# version 0: tranverse all numbers satisfying the condition, which is the first step, counting is the second step

def dfs_0(pos,path,upbound):
    if pos<0: 
        print(path)
        return 
    up = digits[pos] if upbound else 9
    for i in range(up+1):
        dfs_0(pos-1,path[:]+[i],upbound and i==up) # If and only if the prefix is ​​an boundary and the current position is also a boundary


# version 1
# with path selection, output: time limit exceeded
def dfs_1(pos,path,prefix,upbound):
    if pos>=0:
        up=digits[pos] if upbound else 9
        count=0
        for i in range(up+1):
            if i==1:prefix+=1
            count+=dfs_1(pos-1,path[:]+[i],prefix,upbound and i==up)
        return count
    else:
        print(path,prefix)
        return prefix
        
# res=dfs_1(len(digits)-1,[],0,True)


# version 2: without path record, output: time limit exceeded!

def dfs_2(pos,prefix,upbound):
    if pos>=0:
        up=digits[pos] if upbound else 9
        count=0
        for i in range(up+1):
            if i==1:prefix+=1
            count+=dfs_2(pos-1,prefix,upbound and i==up)
        return count
    else:
        print(prefix)
        return prefix
        
# res=dfs_2(len(digits)-1,0,True)

# version 3: optimization using dynamic programming
'''
    Overlapping subproblems
    e.g.
    123
    prefix, last digit
        01       0-9 (overlapping)   state [pos=2][prefix=2] meanning total number of digit 1 in the suffix digits
        10       0-9 (overlapping)   state [pos=2][prefix=2]
        ...
    !!! When it is not boundary and is in the same position with the same prefix, it will overlap and comes out the same result
'''

d=[[-1 for _ in range(len(digits))] for _ in range(len(digits))]
def dfs(pos,prefix,upbound):
        if pos==-1:
            return prefix

        if not upbound:
            if d[pos][prefix]!=-1:return d[pos][prefix]

        up=digits[pos] if upbound else 9
        count=0
        for i in range(up+1):
            count+=dfs(pos-1,prefix+int(i==1),upbound and i==up)
        
        if not upbound: # Note: subsequent values will overwrite previous values, upper boundary value conflicts with non-boundary value
            d[pos][prefix]=count
        return count
res=dfs(len(digits)-1,0,True)
print(d,res)