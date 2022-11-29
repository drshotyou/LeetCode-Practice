class Solution:
    def isHappy(self, n: int) -> bool:
        numbers = []
        while not(1 in numbers):
            if n in numbers:
                return False
            numbers.append(n)
            total = 0
            while n != 0:
                rem = n % 10
                total+=rem*rem
                n = n//10
            n = total
        return True