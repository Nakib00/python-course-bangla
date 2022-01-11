def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1) # 5*4*3*2*1

f = fact(5)

print("Factorial:" + str(f))