def runningSum( nums ) -> List[ int ]:

    res = [ nums[ 0 ] ]

    for i in range( 1, len( nums ) ):
        res.append( sum( nums[ : i + 1 ] ) )

    return res 

nums = [ 1, 2, 3, 4 ] 

print( runningSum( nums ) )

# Expecting [ 1, 3, 6, 10 ]
