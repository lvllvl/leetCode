class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        """
        for loop --> find haystack[n] == needle[0]
        if haystack[n] == needle[0]: 
            TEST A: haystack[ n + 1 ] == needle[ 0 + 1 ]?
            Yes --> repeat TEST A 
            No --> start search from beginning, e.g., haystack[n] == needle[0]?
            
        reach the end of needle? --> return a variable to track 
        reach end of haystack? --> return -1
        
        """
        needles_len = len( needle )
        haystack_len = len( haystack )
        
        for i in range( len( haystack ) ):
            
            if haystack[i] == needle[ 0 ]:
                
                temp_hay_idx = i + 1
                temp_needle_idx = 1
                
                ans = i # return this
                
                while temp_hay_idx < haystack_len and \
                temp_needle_idx < needles_len:
                    
                    if haystack[ temp_hay_idx ] == needle[ temp_needle_idx ]:
                        
                        temp_hay_idx += 1
                        temp_needle_idx += 1
                
                if temp_needle_idx == needles_len: 
                    return ans
        return -1
