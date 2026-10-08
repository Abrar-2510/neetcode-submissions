class Solution:
    def moveZeroes(self, arr):
        j = 0   # مكان أول صفر
        
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        
        return arr

