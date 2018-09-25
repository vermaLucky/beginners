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
* * * * *"""

n=int(input("enter no of rows"))
for i in range(1,n+1):
    for j in range(n+1,1):
        print('*',end=" ")
        n=n-1
    print()








