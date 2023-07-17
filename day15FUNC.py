import random
import string
 


# def main(n):
#     if n % 2 == 0:
#         if n == 0:
        

#             return n
#     return n + 1

# print(main(0))
# def bool_to_word(bollean):
#     if bollean == True:
#         return "Yes"
#     else:
#         return "No"
    
# def area_of_perimetr(a,b):
#     if a == 0 or b == 0:
#         return 0
#     else:
#         return a*b  def no_boring_zeros(n)



# def remove_trailing_zeros(number):
    # if number == 0:
    #     return 0

    # num_str = str(number)
    # num_str = num_str.rstrip('0')

    # if num_str[-1] == '-':
    #     num_str = '-' + num_str[:-1]

    # return int(num_str)

# def reverse_list(lst):
#     return lst[::-1]

# print(reverse_list([1,2,3,4,5,6,7,8,9,10]))


# def str_count(string,letter):
#     count = 0
#     for i in string:
#         if i == letter:
#             count += 1
#     return count
# print(str_count("kanagattandyrylmagantyryndan","y"))


# def positive_sum(arr):
# #     sum = 0
# #     for i in arr:
# #         if i > 0:
# #             sum += i
# #     return sum

# # print(positive_sum([1,2,3,-4,5]))


# def no_space(x):
#     x = x.replace(" ","")
#     return x

# print(no_space("I live in almaty IM from kazakhstan and i love my country"))


# def no_space(x):"))

#problem 1
# def add(a,b):
#     return a + b

# def substract(a,b):
#     return a - b

# def multiply(a,b):
#     return a * b

# def divide(a,b):
#     if b == 0:
#         return b
#     return a / b


# print(divide(2,4))

#problem2
# def letter(x):
#     count = 0
#     for _ in x:
#         count += 1
#     return count

# print(letter('bekzhan'))


#problem3
def dictionary(dict1,dict2):
    dict1.update(dict2)
    return dict1

print(dictionary('astana','capital'),('github'))