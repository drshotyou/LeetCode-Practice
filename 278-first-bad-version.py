# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        result = n
        
        while low <= high:
            mid = low + (high -low) // 2
            if(isBadVersion(mid)):
                result = mid
                high = mid -1
            else:
                low = mid + 1
        return result

# other version this one is slower
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        return binSearch(0,n)
    
def binSearch(left,right):
    mid = left + (right - left) // 2
    if(isBadVersion(mid)):
        if(not isBadVersion(mid-1)):
            return mid
        else:
            return binSearch(left,mid-1)
    else:
        return binSearch(mid+1,right)

#v3 Better than 97% optimize for extreme cases
class Solution:
    def firstBadVersion(self, n: int) -> int:
        if(isBadVersion(1)):
            return 1
        elif(isBadVersion(n) and not isBadVersion(n-1)):
            return n
        return binSearch(1,n)

def binSearch(left,right):
    mid = left + (right - left) // 2
    if(isBadVersion(mid)):
        if(not isBadVersion(mid-1)):
            return mid
        else:
            return binSearch(left,mid-1)
    else:
        return binSearch(mid+1,right)