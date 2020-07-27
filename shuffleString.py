# 1528 Shuffle String 


class Solution:

    def __init__( self ):
        self.self = self

    
    def restoreString( self, s, indices ):
        res = ''

        for i in range( len( indices ) ):

            res += s[ indices.index( i ) ]
        
        return res 

s = 'codeleet'
indices = [ 4, 5, 6, 7, 0, 2, 1, 3 ]

sol = Solution()
print( sol.restoreString( s, indices ))

