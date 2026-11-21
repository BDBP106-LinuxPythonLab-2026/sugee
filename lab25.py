#Q1

class Car:

    showroom = "NewAge"

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200

    @classmethod
    def change_showroom(cls, name):
        cls.showroom = name

    def __str__(self):
        return f"{self.make} {self.model} {self.color} ({self.year})"

    @staticmethod
    def show_intro_message():
        print("This class represents cars.")


# (a) Create Toyota Camry
toyota_camry = Car("Toyota", "Camry", 2022, "Red")

print(toyota_camry.make)
print(toyota_camry.model)
print(toyota_camry.year)
print(toyota_camry.color)
print(toyota_camry.started)
print(toyota_camry.speed)
print(toyota_camry.max_speed)


# (b) Create Ford Mustang
ford_mustang = Car("Ford", "Mustang", 2022, "Black")

print(ford_mustang.__dict__)


# (c) Check class attribute
# print(Car.make) # AttributeError
print(toyota_camry.make)


# (d) Class dictionary
print(Car.__dict__)


# (e) Change showroom
Car.change_showroom("Premium Motors")
print(Car.showroom)
print(Car.__dict__)


# (f) Instance dictionary
print(toyota_camry.__dict__)


# (g) Magic method
print(str(toyota_camry))
print(str(ford_mustang))


# (h) Static method
Car.show_intro_message()


#Q2
# import re
#
# pattern = r"^(?:00[0-9]|0[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
#
# numbers = ["000", "099", "100", "255", "256", "12"]
#
# for n in numbers:
#
#     if re.fullmatch(pattern, n):
#         print(n, "Valid")
#     else:
#         print(n, "Invalid")


#Q4
# import re
#
# pattern = r"^(?:0|[1-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
#
# numbers = ["0", "5", "99", "100", "255", "256", "099"]
#
# for n in numbers:
#
#     if re.fullmatch(pattern, n):
#         print(n, "Valid")
#     else:
#         print(n, "Invalid")


#Q5
# import re
#
# text = input("Enter a string: ")
#
# pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
#
# if re.search(pattern, text):
#     print("Email found")
# else:
#     print("Email not found")


# import re
#
# line = input("Enter CSV line: ")
#
# fields = line.split(",")
#
# pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
#
# if len(fields) > 3 and re.fullmatch(pattern, fields[2].strip()):
#     print("Third field contains an email")
# else:
#     print("Third field does not contain an email")
#
#
#
# import re
#
# def mask_email(match):
#
#     email = match.group()
#
#     name, domain = email.split("@")
#
#     masked = name[0] + "*" * (len(name) - 2) + name[-1]
#
#     return masked + "@" + domain
#
#
# text = input("Enter text: ")
#
# pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
#
# result = re.sub(pattern, mask_email, text)
#
# print(result)
#
#
#
#
#
# import re
#
# dna = "ATCGCGAATTCAC"
#
# pattern = r"GAATTC"
#
# if re.search(pattern, dna):
#     print("EcoRI site found")
# else:
#     print("EcoRI site not found")
#
#
#
# import re
#
# dna = "ATCGCGAATTCAC"
#
# pattern = r"GGACC|GGTCC"
#
# if re.search(pattern, dna):
#     print("AvaII site found")
# else:
#     print("AvaII site not found")
#
#
#
# import re
#
# dna = "ATCGCGAATTCAC"
#
# pattern = r"GC[ATGC]GC"
#
# if re.search(pattern, dna):
#     print("BisI site found")
# else:
#     print("BisI site not found")
#
#
# import re
#
# dna = "ATCGCGYAATTCAC"
#
# pattern = r"[^ATGC]"
#
# ambiguous = re.findall(pattern, dna)
#
# if ambiguous:
#     print("Ambiguous bases:", ambiguous)
#
#     valid = re.findall(r"[ATGC]", dna)
#
#     print("Non-ambiguous bases:", "".join(valid))
#
# else:
#     print("No ambiguous bases")
#
#
#
#
#
# import re
#
# dna = "ACTNGCATRGCTACGTYACGATSCGAWTCG"
#
# pattern = r"[^ATGC]"
#
# result = re.split(pattern, dna)
#
# result = [i for i in result if i]
#
# print(result)



