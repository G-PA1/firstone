r=[]
v = [98,0,2,4,75,7,5,3]
u = [99,'a',72,'b',True,(1,3),{'a','b'}]
l = [13,4,5,2,2,3,78,8,3,1,3,2,4,9,0,8,1]


def freq(n,l):
    f=0
    for a in l:
        if a == n:
            f=f+1
    return f


def max_freq(l):
    mf=freq(l[0],l)
    for a in l:
        if freq(a,l)>mf:
            mf=freq(a,l)

    m=[]
    for a in l:
        if freq(a,l)==mf:
            if a not in m:
                m.append(a)

    return (mf,m)


def min_freq(l):
    m=[]
    for a in l:
        if freq(a,l)==1:
            m.append(a)
    return m


def duplicate(l):
    d=[]
    for i in l:
        d=l
    return d


def find_index(i,l,a,b):
    pass


def max_of_list(l):
    m=l[0]
    for a in l:
        if a>m:
            m=a
    return m


def min_of_list(l):
    m=l[0]
    for a in l:
        if a<m:
          m=a

    return m


