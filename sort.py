def selectionSort(x):
    for i in range(len(x)-1,0,-1):
        n=0
        for l in range(1,i+1):
            if x[l]>x[n]:
                n=l
        t=x[i]
        x[i]=x[n]
        x[n]=t
    return x

def bubbleSort(x):
    n=0
    for j in range(len(x)-1):
        for i in range(len(x)-1-j):
            if x[i+1]<x[i]:
                n=x[i]
                x[i]=x[i+1]
                x[i+1]=n
    return x


def insertionSort(x):
    for i in range(1,len(x)):
        n=x[i]
        m=i
        while m>0 and x[m-1]>n:
            x[m]=x[m-1]
            m-=1
        x[m]=n
    return x


    
def binarySearch(x,y):
    fir=0
    lst=len(x)-1
    m=(fir+lst)/2+(fir+lst)%2
    while True:
        if x[m]==y:
            return m
        elif x[m]>y:
            lst=m
            m=(fir+lst)/2+(fir+lst)%2
        elif x[m]<y:
            fir=m
            m=(fir+lst)/2+(fir+lst)%2
        else:
            return -1
        
