# @Author: Farhad Yusifov
# @Email: farhadyusifov@protonmail.com
# @Date: 2025-08-30

# @Description: Try and Except blocks are used to handle exceptions in Python.

while True:
    try:
        age = int(input("Enter your age: "))
        print(f"You entered: {age}")
        break
    except ValueError:
        print("Invalid input. Please enter a valid age.")