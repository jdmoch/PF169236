def fibonacci(n : int) -> int:
    if n<0:
        raise ValueError("musi byc wieksze od 0")
    elif n==0:
        return 0
    elif n==1:
        return 1
    a,b =0,1
    for _ in range(2,n+1):
        a,b = b, a + b
    return b