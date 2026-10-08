##-----two pointer----------------------
class Solution(object):
    def isHappy(self, n):

        def get_next(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1
    

##--------------Hash set----------------
class Solution(object):
    def isHappy(self, n):
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10

            n = total

        return True