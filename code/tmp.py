# from numpy.random import choice
# samples = choice(['R','G','B'], size=100, p=[0.2,0.5,0.3])
# print(samples,len(samples))

# a=[[3,7,8],[9,11,13],[15,16,17]]

# print(a[0:3])

# a=[1,2,3]
# print(str(a))

# print(None or True or False or False)



# print(math.floor(5/2))
import math
def check(s1):
    L=len(s1)
    return s1[:L//2]==s1[math.ceil(L/2):][::-1]
print(check('aba'))