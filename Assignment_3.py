# 1. Write a Python function to sum all the numbers in a list.


def sum_of_list(lst):
  lsum = 0
  for val in lst:
    lsum = lsum + val
  return lsum

my_list = []
size = int(input("Enter the size of the list: "))
for i in range(size):
    elements = int(input(f"Enter element {i+1} :"))
    my_list.append(elements)
print(my_list)
print("The sum of my_list is", sum_of_list(my_list))


# 2. Write a Python program to reverse a string.


def reverse_list(data):
    output = data[::-1]
    return output

user_input = str(input("Enter a string: "))
print("Original string: ",user_input)
print("Reversed string: ",reverse_list(user_input))


# 3.  Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def up_low(data):
    sum_up = 0
    sum_low = 0
    for i in data:
        if i.isupper():
            sum_up += 1
        elif i.islower():
            sum_low += 1
        else:
            pass
    print("String: ",data)
    print("Number of upper case letters = ",sum_up)
    print("Number of lower case letters = ",sum_low)

user_input = str(input("Enter a string: "))
up_low(user_input)