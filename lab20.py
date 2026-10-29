#Q1

# n=int(input("enter a number: "))
# if n > 0:
#     print("the number is positive")
# elif n < 0:
#     print("the number is negative")
# elif n != 0:
#     if n % 2 == 0:
#         print("the number is even")
#     else:
#         print("the number is odd")
# elif n % 3 == 0 and n % 5 == 0:
#     print("fizzbuzz")
# else:
#     print("the number is zero")

#Q3
# N=10
# attempt=0
# while True:
#     guess=int(input("guess the number: "))
#     attempt=attempt+1
#     if guess==N:
#         print("you guessed the number")
#         print("the number is ",attempt)
#         break
#     elif guess > N:
#         print("the number is higher than the number")
#     elif guess < N:
#         print("the number is lower than the number")
#
#     if attempt == 7:
#         print(N)
#         break

#Q2
# text = input("Enter text: ")
#
# vowels = 0
# consonants = 0
# digits = 0
# spaces = 0
#
# for ch in text.lower():
#     if ch in "aeiou":
#         vowels += 1
#     elif ch.isalpha():
#         consonants += 1
#     elif ch.isdigit():
#         digits += 1
#     elif ch == " ":
#         spaces += 1
#
# print("Vowels:", vowels)
# print("Consonants:", consonants)
# print("Digits:", digits)
# print("Spaces:", spaces)


# #Q4
#
# n = int(input("Enter n: "))
#
# print(" ", end="")
#
# for j in range(1, n + 1):
#     print(str(j).rjust(4), end="")
# print()
#
# for i in range(1, n + 1):
#     print(str(i).rjust(3), end="")
#
#     for j in range(1, n + 1):
#         print(str(i * j).rjust(4), end="")
#
#     print()

#Q5
# items = []
#
# while True:
#     print("\n1. Add item")
#     print("2. Remove item")
#     print("3. View list")
#     print("4. Sort list")
#     print("5. Quit")
#
#     choice = input("Choose: ")
#
#     if choice == "1":
#         item = input("Enter item: ")
#
#         if item.lower() not in [x.lower() for x in items]:
#             items.append(item)
#             print("Item added")
#         else:
#             print("Duplicate item")
#
#     elif choice == "2":
#         item = input("Enter item to remove: ")
#         match = None
#
#         for x in items:
#             if x.lower() == item.lower():
#                 match = x
#                 break
#
#         if match is not None:
#             items.remove(match)
#             print("Item removed")
#         else:
#             print("Item not found")
#
#     elif choice == "3":
#         for i, item in enumerate(items, start=1):
#             print(i, item)
#
#     elif choice == "4":
#         items.sort(key=str.lower)
#         print("List sorted")
#
#     elif choice == "5":
#         break
#
#     else:
#         print("Invalid choice")


#Q6
# students = [
#     ("Asha", 88),
#     ("Ravi", 72),
#     ("Meera", 95),
#     ("Karan", 59),
#     ("Divya", 81)
# ]
#
# total = 0
# top_name, top_score = students[0]
# bottom_name, bottom_score = students[0]
#
# for name, score in students:
#     if score >= 90:
#         grade = "A"
#     elif score >= 80:
#         grade = "B"
#     elif score >= 70:
#         grade = "C"
#     elif score >= 60:
#         grade = "D"
#     else:
#         grade = "F"
#
#     print(name, score, grade)
#     total += score
#
#     if score > top_score:
#         top_name, top_score = name, score
#
#     if score < bottom_score:
#         bottom_name, bottom_score = name, score
#
# print("Average:", total / len(students))
# print("Top scorer:", top_name, top_score)
# print("Bottom scorer:", bottom_name, bottom_score)

#Q7
#
# text = input("Enter paragraph: ")
# counts = {}
#
# for word in text.lower().split():
#     word = word.strip(".,!?;:")
#
#     if word:
#         counts[word] = counts.get(word, 0) + 1
#
# for word in sorted(counts):
#     print(word, counts[word])
#
# if counts:
#     highest = max(counts.values())
#
#     for word in sorted(counts):
#         if counts[word] == highest:
#             print("Most frequent:", word, highest)


#Q8
# python_class = ["Anil", "Bina", "Chetan", "Deepa", "Anil", "Esha"]
# java_class = ["Chetan", "Farhan", "Deepa", "Gita", "Bina"]
#
# p = set(python_class)
# j = set(java_class)
#
# print("Both courses:", sorted(p & j))
# print("Only Python:", sorted(p - j))
# print("Exactly one course:", sorted(p ^ j))
# print("All students:", sorted(p | j))
#
# name = input("Enter student name: ")
#
# in_python = name in p
# in_java = name in j
#
# if in_python and in_java:
#     print("Enrolled in both courses")
# elif in_python:
#     print("Enrolled in Python")
# elif in_java:
#     print("Enrolled in Java")
# else:
#     print("Not enrolled in either course")


#Q9

#
# special = {"!", "@", "#", "$", "%", "&", "*"}
#
# while True:
#     password = input("Enter password: ")
#     errors = []
#
#     if len(password) < 8:
#         errors.append("At least 8 characters")
#
#     if not any(c.isupper() for c in password):
#         errors.append("At least one uppercase letter")
#
#     if not any(c.islower() for c in password):
#         errors.append("At least one lowercase letter")
#
#     if not any(c.isdigit() for c in password):
#         errors.append("At least one digit")
#
#     if not any(c in special for c in password):
#         errors.append("At least one special character")
#
#     if any(c.isspace() for c in password):
#         errors.append("No spaces allowed")
#
#     if "password" in password.lower():
#         errors.append("Cannot contain the word password")
#
#     if not errors:
#         print("Valid password")
#         break
#
#     print("Password invalid:")
#     for error in errors:
#         print("-", error)

