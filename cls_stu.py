class Student:
    st=60
    nt=180

    def __init__(self,id,name,p,c,m):
        self.id = id
        self.p=p
        self.c=c
        self.m=m
        self.name=name

    def __str__(self):
        return f'''Test result of {self.name}:
    physics={self.p}
    chemistry={self.c}
    mathematics={self.m}'''


    def total(self):
        return self.p+self.c+self.m

    def sub_percent(self):
        return tuple(((self.p/self.st)*100,(self.c/self.st)*100,(self.m/self.st)*100))

    def net_percent(self):
        return (self.total()/self.nt)*100

    def weak_sub(self):
        m=min(self.p,self.c,self.m)
        if m==self.p:
            print('physics')
        if m==self.c:
            print('chemistry')
        if m==self.m:
            print('mathematics')

    def strong_sub(self):
        m = max(self.p, self.c, self.m)
        if m == self.p:
            print('physics')
        if m == self.c:
            print('chemistry')
        if m == self.m:
            print('mathematics')



s1=Student(1,'ari',74,34,34)

print(s1)
print(s1.weak_sub())