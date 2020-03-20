def binSearch(a,target):
    left,right=0,len(a)-1
    while left<=right:
        mid=(left+right)//2
        if a[mid]>target:
            right=mid-1
        elif a[mid]<target:
            left=mid+1
        elif a[mid]==target:
            return mid
    return -1
_=binSearch([1,2,3,4,5],6)
print(_)


