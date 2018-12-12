class fact:
    def __init__(self,n):
        self.n=n
        self.f=1
    
    def cal(self):
        for i in range(1,self.n+1):
              self.f=self.f*i
        print("value is:",self.f)
class add(fact):
    def __init__(self,n,m):
        super(). __init__(n)
        self.m=m
    def cal(self):
        super().cal()
        print("sum is:",self.m+self.n)

class fib(fact):
    def __init__(self,n,a,b):
        super(). __init__(n)
        self.a=a
        self.b=b
    def cal(self):
        for i in range(2,self.n+1):
            self.c=self.a+self.b
            self.a=self.b
            self.b=self.c
            print('fib series:',self.c)
    
        
        

a1=add(4,5)
a1.cal()              
f1=fib(4,0,1)
f1.cal()
        
        
