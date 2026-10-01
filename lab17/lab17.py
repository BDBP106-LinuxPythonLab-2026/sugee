#Q1
# B=int(input("enter a binary number: "))
# decimal=0
# power=0
# for digit in B[::-1]:
#     decimal=decimal*10+int(digit)**power
#     power=power+1
# print("decimal= " ,decimal)
from operator import truediv
from os import MFD_ALLOW_SEALING

from orca.messages import character_count
from twisted import names

#Q10
# lists=[1,2,12,13,17,34,26,47,52,60]
# for i in lists:
#     if i%2==0:
#         print(i)
#         continue

#Q2
# base=int(input("enter a base: "))
# n=int(input("enter a power: "))
# result=1
# for i in range(n):
#     result=result*base
# print("result=" , result)

#Q3
# n=int(input("enter a number: "))
# if n < 2:
#     print("Not a prime number")
# else:
#     isPrime = True
#     for i in range(2,n):
#         if n % i == 0:
#             isPrime = False
#     if isPrime:
#         print("Prime number")
#     else:
#         print("Not a prime number")

#Q4
# N=int(input( "enter a number: "))
# while N > 0 :
#     digit=N%10
#     print(digit)
#     N=N//10

#Q5
# s=input("enter a string: ")
# mid=len(s)//2
# print("First half= ",s[0:mid])

# #Q6
# s=input("enter a string: ")
# alternate=s[::2]
# print(alternate)


#Q9
# s1=input("enter first string: ")
# s2=input("enter second string: ")
# if sorted(s1) == sorted(s2):
#     print("anagrams")
# else:
#     print("are not anagrams")

#Q7
# S=input("enter a string: ")
# print("after removing leading whitespaces:", S.lstrip())

#Q8
# s=input("enter a sentence: ")
# w=input("enter a word: ")
# words=s.split()
# count=0
# for word in words:
#     if word==w:
#         count=count+1
#         print()
#         break


#Q12

# m1=[[1,2],
#     [3,4]]
# m2=[[5,6],
#     [7,8]]
#
# result= []
# for i in range(2):
#     row=[]
#     for j in range(2):
#         row.append(m1[i][j]-m2[i][j])
#         result.append(row)
# print("result: ")
# for row in result:
#     print(row)


#Q13

# l=list  (map(int. input("enter list elements: ")))

#Q11
# A=[1,2,1,3,1,2,4,5,4]
# l=len(A)
# print(l)
#
# for i in range(0,l-1):
#     for j in range(i+1,l):
#         if A[i]==A[j]:
#            print(A[j])



