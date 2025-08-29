# @Author: Farhad Yusifov
# @Email: farhadyusifov@protonmail.com
# @Date: 2025-08-28

# @Description: General use of functions.


def happy_birthday_song(age):
    x = 1
    print("Happy birthday to you!~")
    print("Happy birthday to you!~")
    print("How old are you now?~")
    print("How old are you now?~")
    while x <= age:
        print("Are you", x, "?~")
        if x == age:
            print("Hurray! You are", x, "years old!")
        x += 1
    return print("Congratulations!")


age = int(input("Age: "))
happy_birthday_song(age)