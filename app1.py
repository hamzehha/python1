'''
Q1) Write a simple program that will read the input r which indicate redies of the circle and calculate the area and the circumference of that circle ?

Area = pi * r ^2

Cir = Pi * 2 * r


r = int(input("plz enter redies of the circle "))
py = 3.14
area = py * r**2
Cir = py * 2 * r
print("the area of circle is = ",area ,"the  circumference  of circle is =",Cir)
---------------
Q2) write a program to calculate summation of the numbers from n to m for example the summation of when n=3 and m=9 is  3+4+5+6+....9 = 42 ?

Note: n should be always less than m


n = int(input("plz enter number"))
m = int(input("plz enter number"))
sum = 0
x = 0
for x in range (n,m+1):
    print(x)
    sum +=x

print("the sum ",sum)
#-------------
Q3) write a program to calculate fibonacci sequence at index n fibonacci sequence is  0, 1, 1, 2, 3, 5, 8 where each number should  equal the previous two numbers

arr = [0,1]

arr.append(arr[0] + arr[1])
arr.append(arr[1] + arr[2])
arr.append(arr[2] +arr[3])
arr.append(arr[3] +arr[4])
arr.append(arr[4] +arr[5])
print(arr)

input=int(input("plz enter the num "))
A = [0,1]
for i in range(2,input):
    A.append(A[i-1]+A[i-2])
print(A)

-----------
Q4) given two arrays as constant for example A=[1,2,4,6] B=[2,3,6] you should be able to merge them so the output will be C=[1,2,2,3,4,6,6]
'''

A = [1, 4, 9, 10]
B = [2, 6,7, 9]
c = []
a = 0
b = 0
for i in range(len(A) + len(B)):  # 7
    if a == len(A) :
        c.append(B[b:])
        break
    if b== len(B):
        c.append(A[a:])
        break
    if A[a] < B[b]:
        c.append(A[a])
        a = a + 1
    else:
        c.append(B[b])
        b += 1

print(c)
