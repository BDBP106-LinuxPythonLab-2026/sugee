#Q1
# def celsius_fahrenheit(c):
#     return (c * 9 / 5 ) + 32
# temp = [120,30,45,90]
# result=list(map(celsius_fahrenheit,temp))
# print(result)



#Q2
# temp=[120,30,45,90]
# result = list(map(lambda c: (c * 9/5) + 32, temp))
# print(result)

#Q3
# import math
# angles=(25,35,45,55,65,75,85,95,100)
# def f(angle):
#     x=math.sin(math.radians(angle))
#     y=math.cos(math.radians(angle))
#     return x,y
# result=list(map(f,angles))
# print(result)

# Q3 using a lambda function
# import math
# angles=(25,34,40,90)
# def f(angle):
#     x=math.sin(math.radians(angle))
#     y=math.cos(math.radians(angle))
#     return x,y
# result=list(map(lambda x: f(x),angles))
# print(result)

#Q4
# n=int(input("enter a number: "))
# fib=[]
# a=0
# b=1
# for i in range(n):
#     fib.append(b)
#     odd=list(map(filter(lambda x:x%2 !=0,fib)))
# print("Fibonacci series", fib)
# print("odd elements are",odd)

#Q5
# from functools import reduce
# n=[2,4,6,8,10]
# sum= reduce(lambda x,y:x+y,n)
# print(sum)

#Q7
# def analyse_dna(seq):
#     seq = seq.upper()
#     def gc_content():
#         g_count=seq.count('G')
#         c_count=seq.count('C')
#         return [g_count+c_count/len(seq)*100]
# gc_pct = gc_content()
# at_pct = 100-gc_pct
# print(f" gc_content: {gc_pct:.2f}%, at_pct: {at_pct:.2f}%")
# if gc_pct > at_pct:
#     print("seq is gc rich")
# else:
#     print("seq is at rich")
#
# analyse_dna('ATGCGCGC')

#Q6
# def cell_metabolism(glucose, oxygen):
#     def energy_output():
#         complete = min(glucose, oxygen // 6)
#         return complete * 38
#
#     return energy_output()
#
# print(cell_metabolism(10, 60))

#Q8
# def protein_energy_temp():
#     def calculate_free_energy(enthalpy, entropy, temperature):
#         return enthalpy - temperature * entropy
#
#     enthalpy = float(input("Enter enthalpy: "))
#     entropy = float(input("Enter entropy: "))
#     temperature = float(input("Enter temperature in Kelvin: "))
#
#     dg = calculate_free_energy(enthalpy, entropy, temperature)
#     print("Delta G:", dg)
#
#     if dg < 0:
#         return "Stable"
#     return "Unstable"
#
#
# print(protein_energy_temp())

#Q9
# import math
#
# def population_growth(initial, rate, time):
#     def exponential_growth():
#         return initial + math.exp(rate * time)
#
#     result = exponential_growth()
#     print(round(result))
# population_growth(100, 0.2, 5)

#Q11
# from functools import reduce
#
# words = ["Python", "is", "fun"]
#
# sentence = reduce(lambda a, b: a + " " + b, words)
# print(sentence)

#Q10
# text = input("Enter a string: ")
# vowels = [c for c in text if c.lower() in "aeiou"]
# print(vowels)
