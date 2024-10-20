'''Write a python program which finds the maximum number from num1 to num2 (num2 inclusive) based on the following rules.

1. Always num1 should be less than num2
2. Consider each number from num1 to num2 (num2 inclusive). Populate the number into a list, if the below conditions are satisfied

      a. Sum of the digits of the number is a multiple of 3
      b. Number has only two digits
      c. Number is a multiple of 5
3. Display the maximum element from the list
In case of any invalid data or if the list is empty, display -1.'''

def find_max_number(num1, num2):
    if num1 >= num2:
        return -1

    max_list = []
    for num in range(num1, num2 + 1):
        if len(str(num)) == 2 and num % 5 == 0:
            digit_sum = sum(int(digit) for digit in str(num))
            if digit_sum % 3 == 0:
                max_list.append(num)

    if not max_list:
        return -1
    else:
        return max(max_list)

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

print(find_max_number(num1, num2))