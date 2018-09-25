#begine with python

print("Welcome to python")


#variable in python
"""In python variable declaration is not necessary"""

x=90   #here x is a int type
x="String"  #here x is a String type
print(x)

#concatination of string

x="Lucky "
y="Verma"

print(x+y)


#casting of a variable
"""we can cast a variable particularly in one data type
example """

x=int(1.58)
y=float(1)
z=str(123)
print(x,y,z)



#String in python

a="Welcome to python"
print("print alphabet at index 1 "+a[1]) #index of string start with 0
print("print substring from index 1 to 7 " +a[1:8]) #print substring

#String built in function in python
y="     hello"
print(y.strip()) #strip fuction remove whitespace from beginning and end
print("convert to upper case "+y.upper())
z="HELLO"
print("convert to lower case "+z.lower())
t="python"
l=len(t)
print(l)
print(t.replace('p','k'))
print(a.split())


#program to find factorial
x=6
factorial=1
while(x>0):
    factorial=factorial*x
    x=x-1
print(factorial)





#taking input from user
x=input("enter name")
print(x);