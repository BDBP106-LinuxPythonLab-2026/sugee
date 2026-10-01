#Q1
# D=dict([('rain','blue') , ('rainbow','colorful')])
# for k,v in D.items():
#     print(k,v)


#Q2
# D={'a': 100, 'b': 200, 'c': 300}
# res=0
# for val in D.values():
#     res+=val
# print(res)

#Q3
# d={'a':1,'b':2,'c':3}
# max=0
# min=0
# for k in d:
#     if d[k]>max:
#         max=d[k]
#     if d[k]<min:
#         min=d[k]
# print(max,min)

#Q4
# test_dict= {"Gfg" : [5,7,7,7,7], "is" :[6,7,7,7], "best" : [9,9,6,5,5]}

#Q5
# sentence=input("enter a sentence: ")
# words = sentence.split()
# unique_words=set(words)
# for word in unique_words:
#    if word not in unique_words:
#        print(word)


#Q6
# import math
# def area_triangle(a,b,c):
#     s=(a+b+c)/2
#     area=math.sqrt(s*(s-a)*(s-b)*(s-c))
#     return area
# a=3
# b=4
# c=5
# print(area_triangle(a,b,c))

#Q7
# def triangle_type(a,b,c):
#     if a == b and b == c:
#         return "equilateral"
#     elif a == b or b == c or a == c:
#         return "isosceles"
#     else:
#         return "scalene"
# a=int(input("enter first number: "))
# b=int(input("enter second number: "))
# c=int(input("enter third number: "))
#
# print(triangle_type(a,b,c))

#Q8
# lst=[23,32,33,44,'BDBH101', 'hello', 'python', '15,1e-10','true', 'hit']
# for i in range (0,len(lst)-1,2):
#     lst[i]=lst[i+1]=lst[i+1],lst[i]
#     print(lst[i])

#Q9
#first position
DNA="AGTCTTA"











