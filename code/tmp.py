# from numpy.random import choice
# samples = choice(['R','G','B'], size=100, p=[0.2,0.5,0.3])
# print(samples,len(samples))

# a=[[3,7,8],[9,11,13],[15,16,17]]

# print(a[0:3])

# a=[1,2,3]
# print(str(a))

# print(None or True or False or False)

a=[1,2,3,4,5]
for i in range(len(a)):
    if i==0 or i==1:
        a.pop()
    print(i)