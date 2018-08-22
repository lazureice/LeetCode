def spiralMatrixIII(R, C, r0, c0):
    """
    :type R: int
    :type C: int
    :type r0: int
    :type c0: int
    :rtype: List[List[int]]
    """

    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    d=0
    steps=1
    res=[(r0,c0)]
    squares=1

    while squares<R*C:
        # steps=int(squares**0.5) # 太麻烦
        for i in range(steps):
            r0,c0=r0+directions[d][0],c0+directions[d][1]
            if 0<=r0<R and 0<=c0<C:
                squares+=1
                res.append((r0,c0))
        d=(d+1)%4
        steps+=((d+1)%2)
    return res
    
R = 5; C = 6; r0 = 1; c0 = 4
print(spiralMatrixIII(R, C, r0, c0))
