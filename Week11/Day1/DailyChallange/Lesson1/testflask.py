
def fibonachi():

    fibo_code = [(0,0),(1,1)]
    for i in range(2, 15):
        fibo_tuple = (i,fibo_code[i-1][1]+fibo_code[i-2][1])
        fibo_code.append(fibo_tuple)
    return fibo_code
