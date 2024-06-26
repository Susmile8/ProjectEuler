from math import sqrt, pi
def f(x,n):
    return min(x/n,1-sqrt(1-(x-1)*(x-1)))
def g(n):
    step=1/10000
    A=0
    for i in range(10000):
        u=step*i
        v=step*(i+1)
        area=step*(f(u,n)+f(v,n))/2
        A+=area
    return A
def Q587_v1():
    Lsec=1-pi/4
    lo=1
    hi=100000
    while lo<hi:
        mid=(lo+hi)//2
        ratio=g(mid)/Lsec*100
        if ratio<0.1:
            hi=mid
        else:
            lo=mid+1
    print(lo,g(lo)/Lsec,hi)
if __name__=="__main__":
    Q587_v1()
    