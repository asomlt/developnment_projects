

def add(a,b):
    c=a+b
    print("addition",c)

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    

for  i in range(10):
    print(i,end=",")
    add(i,i+1)
    a=fibo(i)
    print("Fibonacci series upto",i,"is: ",a)


class clos:
    def __init__(self,a ,b):
        self.a = a
        self.b = b
        self.c=self.a+self.b
    def __repr__(self):
        return "Addition of {} and {} is {}"
    def display():
        print("ram ram ji ")
    def representation():
        for i in "Heloo":
            print(i)

ab={"key":"value","leu":"oo"}
a=clos
print(a(3,4))
a.display()
a.representation()
print(ab["key"])

