def filt(y, n):
    new_Y = [0 for i in range(n)]
    for i in range(n):
        j = i
        iter = 0
        while j > 0 and i - j < 8:
            new_Y[i] += y[j]
            j -= 1 
            iter += 1
        if iter != 0:
            new_Y[i] = new_Y[i]/iter   
    return(new_Y)

