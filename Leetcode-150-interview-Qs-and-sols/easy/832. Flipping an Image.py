class Solution(object):
    def flipAndInvertImage(self, image):
        
        result = []
        
        for row in image:
            new_row = []
            
            for num in row[::-1]:
                new_row.append(1 - num)
            
            result.append(new_row)
                
        return result