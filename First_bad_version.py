#You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your
#product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
#Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
#You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

import time #Comparing time spent between two different classes
def isBadVersion(i):
    if i < 1702766719:
        return False
    else:
        return True

#The main idea is how to calculate the mean between high and low numbers in a dynamic way
class Solution:
    def firstBadVersion(self, n: int) -> int:
        low,high = 1, n
        while low<=high:
            mid=(low+high)//2       #// gives the smallest integer divisor
            print(f'class1 mid = {mid}')
            isBad = isBadVersion(mid)
            if(isBad):
                high = mid-1
            else:
                low = mid+1
        return low

#validation
n = 2126753390

c = Solution()
c3 = Solution3()

start = time.time()
print(c.firstBadVersion(n))
end = time.time()
print(f'Class 1 running time = {end - start}')

start = time.time()
print(c3.firstBadVersion3(n))
end = time.time()
print(f'Class 2 running time = {end - start}')
