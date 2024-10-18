#Multiplication over Addition
a=int(input("Enter a "))
b=int(input("Enter b "))
c=int(input("Enter c "))
def Distributive_Law(a,b,c):
    LHS=a*(b+c)
    RHS=(a*b)+(a*c)
    print(f"Left Side=(a*(b*c)):{a}*({b}+{c})={LHS}")
    print(f"Right Side=((a*b)+(a*c)):({a}*{b})+({a}*{c})={RHS}")
    if(LHS==RHS):
        print("X=",LHS,"Y=",RHS,"\n","It Follows Distributive Law")
    else:
         print("X=",LHS,"Y=",RHS,"\n","It DO Not Follows Distributive Law")
Distributive_Law(a,b,c)

#Multiplication over Subtraction
a=int(input("Enter a "))
b=int(input("Enter b "))
c=int(input("Enter c "))
def Distributive_Law(a,b,c):
    LHS=a*(b+c)
    RHS=(a*b)+(a*c)
    print(f"Left Side=(a*(b-c)):{a}*({b}-{c})={LHS}")
    print(f"Right Side=((a*b)-(a*c)):({a}*{b})-({a}*{c})={RHS}")
    if(LHS==RHS):
        print("X=",LHS,"Y=",RHS,"\n","It Follows Distributive Law")
    else:
         print("X=",LHS,"Y=",RHS,"\n","It Do Not Follows Distributive Law")
Distributive_Law(a,b,c)
