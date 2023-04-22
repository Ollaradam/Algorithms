def max_independent_set(nums):
    sum = 0
    
    cache=[0 for i in range(len(nums))]
    cache[0]=nums[0]
    cache[1]=nums[1]
    
    for i in range(2,len(nums)):
        cache[i]=max(nums[i],nums[i]+cache[i-2],cache[i-2],cache[i-1])  
    
    i=len(nums)-1
    lis=[]
    
    while(i>1):
        if cache[i]==cache[i-1]:
            i = i-1 
        elif cache[i]==nums[i]:
            lis.append(nums[i])
            lis.reverse()
            return lis
        elif cache[i]==cache[i-2]+nums[i]:
            lis.append(nums[i])
            i = i-2
        else:
            i = i-2
    
    if i==0:
        if(nums[i]>0 or len(lis)==0):
            lis.append(nums[i])
    else:
        t=max(nums[0],nums[1])
        if(t>0 or len(lis)==0):
            lis.append(t)
    lis.reverse()
    
    for i in lis:
        sum = sum+i
        if sum<0:
            lis = []
            return lis
        else:
            return lis

print(max_independent_set([-1, -1, 0]))
print(max_independent_set([-1, -1, -10, -34]))
print(max_independent_set([7,2,5,8,6]))