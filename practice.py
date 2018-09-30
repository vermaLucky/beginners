#taking input from user
#x=input("please enter your name\n")
#print("your name is \t"+ x)

#loops in python

#patterns

"""n=int(input("enter no of rows"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=" ")
    print()


input=5

output=

*
* *
* * *
* * * *
* * * * *  """

"""n=int(input("enter no of rows"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print('*',end=" ")
    print()


input=5

output

* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * *

n=int(input("enter no of rows"))
for i in range(1,n+1):
    for j in range(n+1,1):
        print('*',end=" ")
        n=n-1
    print()


y=int(input("ENTER THE NO OF ROWS"))
for i in range(y,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")

    print()

input=5

output=
ENTER THE NO OF ROWS5
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 


a=str(input("ENTER THE STRING"))
l=len(a)
for i in a:
    if(i==a[l-1]):
        l=l-1
        continue
    else:
        print('no')
        exit()
print('yes')


x=int(input())
for i in range(1,x+1):
    for i in range(1,x):
        if(i%3!=0):
            print("*\t*")
        else:
            print("*****")
            break
print("*   *")
print("*   *")

input 5

output:

*	*
*	*
*****
*	*
*	*
*****
*	*
*	*
*****
*	*
*	*
*****
*	*
*	*
*****
*   *
*   *


#Alphabetical order
x=str(input("enter the string"))
y=sorted(x)
for i in y:
    print(i,end=" ")

#class concept in python
class myclass:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def myfunction(self):
        print("hello myself " + self.fname + self.lname )

p=myclass("lucky","verma")

p.myfunction()

#frequency of character in a string
def frequency(string):
    d={}
    for i in string:
        key=d.keys()
        if i in key:
            d[i]+=1
        else:
            d[i]=1

    return d

frequency(input("enter the string"))
#fibonacci series

#METHOD 1

def fib(n):
    if(n==1 or n==2):
        return  1
    return (fib(n-1)+fib(n-2))
for i  in range(1,11):
    print(fib(i))

#fibonacci series

#METHOD 2


def fib(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b
    return a

for i in range(1,11):
    print(fib(i))



#sorting a string
a,b=input().split(" ")
if sorted(a)==sorted(b):
    print("YES")
else:
    print("NO")


#LCM AND HCF OF A NUMBER

a,b = input("enter the numbers").split(" ")
a= int(a);
b = int(b);
t1 = a
t2 = b
while t2 != 0:
    temp = t2;
    t2 = t1%t2;
    t1 = temp;
hcf = t1;
lcm = (a*b)/hcf;
print("HCF =",hcf);
print("LCM =",lcm);
"""
#cipher text

a=str(input("enter string"))
k=int(input("enter the key"))
l=len(a)
r=" "
for i in range(l):
    if(a[i].isupper()):
        print(chr((ord(a[i])+k-65)%26 +65),end=" ")
    elif(a[i].islower()):
        print(chr((ord(a[i])+k-97)%26 +97),end=" ")
    elif(a[i].isdigit()):
        print(chr((ord(a[i])+k-49)%10 +48),end=" ")
    else:
        continue



