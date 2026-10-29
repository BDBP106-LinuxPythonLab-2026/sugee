# # #Q1
# # a=[i for i in range(1,50)]
# # print(a[1:5])
# # print(a[3:20:2])
# # print(a[::2])
# # print(a[::-1])
# # print(a[::2])
# # print(a[10::2])
# # print(a[1:1:1])
# # print(a[:0:])
# # print(a[-7::1])
# # print(a[-6:])
# # print(a[-10:-4])
# #
# # print(a[::-1])
# # print(a[::-3])
# # print(a[:1:-2])
# # print(a[-1:-1:-1])
# # print(a[:-5:-1])
# # print(a[:0:-1])
# # print(a[:-1:-1])
# # print(a[0:-5:-1])
# # print(a[-1:5:-1])
# # print(a[2:2:-1])
# # print(a[2:1:-1])
# # print(a[0:-5])
#
#
# #Q1-4
# # a = [i for i in range(1, 50)]
# # even=a[1::2]
# # print(even)
# # print(a[:10])
# # print(a[35::2])
# # new_list=a[:10] + a[35::2]
# # print(new_list)
#
# #Q2
# #1.
#
# # a=[i for i in range(1,51)]
# # total=0
# # for i in a:
# #     total+=i
# # print(total)   //using a for loop
#
# # total_sum=sum(num for num in a)
# # print(total_sum)  //using a list comprehension
#
# #2.
#
# # b=[n for n in range (2,51) if all (n % i != 0 for i in range(2,n))]
# # print(b)
#
# #3
# # c=[]
# # for i in a:
# #     if i in b:
# #         c.append(i)
# # print(c)
#
# #Q3-1
# # result=",".join([str(i) for i in a])
# # print(result)  //using a comma
#
# # result=".".join([str(i) for i in a])
# # print(result)  //using a period
#
# # result="_".join([str(i) for i in a])
# # print(result) //using a "_"
#
# #Q3-4
# # C=[i*i for i in a]
# # result="\n".join([f"{i} {i*i}"for i in a])
# # print(result)
#
# #Q3-2
#
# d=["sugee ghoderao","nandini nandwana","chitra godiwala","divya boobana","jeeba leela","jayasri su","nandan soni","keshav vyas","ashmika labhade","sushant suryawanshi"]
# # upper_case=[name.upper() for name in d]
# # print(upper_case) // uppercase
# # last_name=[name.split()[1]+" " + name.split()[0] for name in d]
# # print(last_name) //last name

# #Q3-3
# sentence = "She sells sea shells that she collects from the sea floor"
# words = sentence.split()
#
# longest = max(words, key=len)
# print(longest) # collects
#
#
# #Q3-4
# sentence = "She sells sea shells that she collects from the sea floor"
# words = sentence.lower().split()
#
# repeated = [
#     word for word in dict.fromkeys(words)
#     if words.count(word) > 1
# ]
#
# print(repeated) # ['she', 'sea']