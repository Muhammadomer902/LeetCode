class Solution:
    def maximumScore(self, nums, k):
        import heapq
        import numpy as np
        n=len(nums)
        def prime_factor_funct(x):
            res=[]

            for p in range(2,x):
                if p*p>x:
                    break
                if x%p!=0:
                    continue
                res.append(p)
                while x%p==0:
                    x=x//p
            if x>1:
                res.append(x)
            return len(res)
        
        
        prime_factor_list=[]
        
        max_count_list=[1]*n
        
        max_prime=np.inf
        cnt=1
        
        for i in range(n):
            cont_prime=prime_factor_funct(nums[i])
            prime_factor_list.append(cont_prime)
        
        
        nextGreaterElement = [n] * n
        s = []
        for i in reversed(range(n)):
            while s and prime_factor_list[i] >= prime_factor_list[s[-1]]:
                s.pop()

            nextGreaterElement[i] = s[-1] if s else n
            s.append(i)

        p_que=[]
        heapq.heapify(p_que)

        prevGreaterOrEqualElement = [-1] * n
        s = []
        for i in range(n):
            while s and prime_factor_list[i] > prime_factor_list[s[-1]]:
                s.pop()

            prevGreaterOrEqualElement[i] = s[-1] if s else -1
            
            heapq.heappush(p_que,(-nums[i],(i - prevGreaterOrEqualElement[i]) * (nextGreaterElement[i] - i)))
            s.append(i)


        
        mul=1

        while k>0:
            num,cnt=heapq.heappop(p_que)
            num=-num
            mul*=pow(num,min(k,cnt),10**9 + 7)
            k-=cnt
        
        return mul%(10**9 + 7)