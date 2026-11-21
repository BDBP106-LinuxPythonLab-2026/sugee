#Q1
# def greet_decorator(func):
#      def wrapper():
#        print("Greeting started")
#      func()
#      return wrapper
# @greet_decorator
# def message():
#     print("Hello")
# message()

#Q2
# def before_after(func):
#      def wrapper():
#        print("Function is starting....")
#      func()
#      print("Function has finished!")
#      return wrapper
# @before_after
# def calculate():
#    print("Calculating...")
# calculate()

#Q3
# def count_calls(func):
#     count = 0
#     def wrapper():
#        nonlocal count
#        count += 1
#        func()
#     print("Call count:", count)
#     return wrapper
# @count_calls
# def say_hi():
#     print("Hi!")
# say_hi()
# say_hi()
# say_hi()

#Q4
# def check_positive(func):
#     def wrapper(n):
#         if n > 0:
#           return func(n)
#     print("Number must be positive")
#     return wrapper
# @check_positive
# def show_number(n):
#    print("Number: ", n)
# show_number(5)
# show_number(-2)

#Q5
# import time
# def measure_time(func):
#     def wrapper(*args, **kwargs):
#      start = time.perf_counter()
#      result = func(*args, **kwargs)
#      print("Execution time:", time.perf_counter() -start ,"seconds")
#      return result
#     return wrapper
# @measure_time
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#      result *= i
#     return result
# print(factorial(12))

#Q6
# import math
# def population_growth(initial, rate, time):
#    def exponential_growth():
#      return initial + math.exp(rate * time)
#    print(round(exponential_growth()))
# population_growth(100, 0.2, 5)

#Q7
import time
# @measure_time
# def population_growth_loop():
#    total = 0
#    for i in range(1000000):
#      total += i
#    return total
# print(population_growth_loop())

#Q8
# def analyse_dna(sequence):
#     def gc_content():
#      seq = sequence.upper()
#      if not seq:
#          return 0
#      return (seq.count("G") + seq.count("C")) / len(seq) * 100
#
#     percentage = gc_content()
#     print("GC content: {percentage:.2f}")
#     if percentage > 50:
#         print("GC rich sequence")
#     else:
#          print("AT rich sequence")
# analyse_dna("ATGCGC")

#Q9
# def log_function_call(func):
#     def wrapper(*args, **kwargs):
#         print("Running DNA analysis....")
#         result = func(*args, **kwargs)
#         print("Analysis complete!")
#         return result
#     return wrapper
#
# @log_function_call
# def gc_content(sequence):
#     sequence = sequence.upper()
#
#     if not sequence:
#         return 0
#
#     gc = sequence.count("G") + sequence.count("C")
#     return gc / len(sequence) * 100
#
# print(gc_content("ATGCGC"))