def extraCandies( candies, extraCandies ):
    output = [] 

    for i in range( len( candies ) ): 
        maxNum = candies[ i ] + extraCandies

        output.append( ( maxNum >= max( candies ) ) )

        maxNum = 0

    return output 
  

candies = [ 4, 2, 1, 1, 2 ]
extraC = 1

print( extraCandies( candies, extraC ))

