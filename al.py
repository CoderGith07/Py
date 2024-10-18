#addition
a=input("Enter Equation in a+(b+c) This Form : ")
b=input("Enter Equation in (a+b)+c This Form : ")
def associative_Law(a,b):
    x=eval(a)
    y=eval(b)
    if(x==y):
        print("X=",x,"Y=",y,"\n","It Follows Associative Law")
    else:
        print("X=",x,"Y=",y,"\n","It Does Not Follow Associative Law")
associative_Law(a,b)

#multiplication
a=input("Enter Equation in a*(b*c) This Form ")
b=input("Enter Equation in (a*b)*c This Form ")
def associative_Law(a,b):
    x=eval(a)
    y=eval(b)
    if(x==y):
        print("X=",x,"Y=",y,"\n","It Follows Associative Law")
    else:
        print("X=",x,"Y=",y,"\n","It Does Not Follow Associative Law")
associative_Law(a,b)
