"""
1. find all of fibo numbers
2. check m value divisible - it just looping n time
"""
def fun(n,m):
    fibo = [0,1]
    count = 0
    # print(fibo[1],"index")
    
    while True:
        fibo.append(fibo[-1]+fibo[-2])
        # print(fibo,count)
        if fibo[-1] % m == 0:
            count += 1
            if count == n:
                return fibo[-1]
    
        
print(fun(4, 3))

