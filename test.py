# 1. Calculate the Year of Birt given a user's age

# from random import randint
# from math import pi

# def circumference(radius):
#     return 2 * pi * radius

# print(circumference(randint(1,10)))

# def year_of_birth(age):
#     current_year = 2022
#     year_of_birth = 2022 - age
#     difference_to_eighty = 80 - age
#     year_of_eighty = current_year + difference_to_eighty
#     return {
#         year_of_birth:year_of_birth,
#         year_of_eighty:year_of_eighty
#     }
    
# print(year_of_birth(int(input())))

# 2. Calculate the Tip a Customer pays depending on Service received

# def tip_calculator():
#     print("What's Your Total?")
#     cost_price = int(input())
#     print("How was the Service")
#     service = input()
#     tip = 0
#     if(service.lower() == 'good'):
#         tip = 0.15 * cost_price
#     elif(service.lower() == 'great'):
#         tip = 0.20 * cost_price
#     else:
#         tip = 0 * cost_price    

#     total = cost_price + tip
#     return total

# print(tip_calculator())


# 3. Determine the number of times a Phone Keypad is pressed to type a given string

# Phone Keypad
# def count_pressed():
#     print('What is your Name')
#     name = input()
#     keypad = {
#         'first_button': ['A', 'B', 'C'], 
#         'second_button': ['D', 'E', 'F'],
#         'third_button': ['G', 'H', 'I'],
#         'fourth_button': ['J', 'K', 'L'],
#         'fifth_button': ['M', 'N', 'O'],
#         'six_button': ['P', 'Q', 'R', 'S'],
#         'seventh_button': ['T', 'U', 'V'],
#         'eighth_button': ['W', 'X', 'Y', 'Z']
#     }

#     total = 0

#     for letter in name:
#         letter = letter.upper()
#         if letter in keypad['first_button']:
#             total = total + keypad['first_button'].index(letter) + 1
#         elif letter in keypad['second_button']:
#             total = total + keypad['second_button'].index(letter) + 1
#         elif letter in keypad['third_button']:
#             total = total + keypad['third_button'].index(letter) + 1
#         elif letter in keypad['fourth_button']:
#             total = total + keypad['fourth_button'].index(letter) + 1
#         elif letter in keypad['fifth_button']:
#             total = total + keypad['fifth_button'].index(letter) + 1
#         elif letter in keypad['six_button']:
#             total = total + keypad['six_button'].index(letter) + 1
#         elif letter in keypad['seventh_button']:
#             total = total + keypad['seventh_button'].index(letter) + 1
#         else:
#             total = total + keypad['eighth_button'].index(letter) + 1

#     return 'Your name ' + name + ' would require ' + str(total) + ' clicks if you were using a phone keypad'

# print(count_pressed())


# 3. Fizz Buzz Challenge

# def fizz_buzz():
#     for number in range(1, 101):
#         if(number % 3 == 0 and number % 5 == 0):
#             print('FizzBuzz')
#         elif(number % 5 == 0):
#             print('Buzz')
#         elif(number % 3 == 0):
#             print('Fizz')
#         else:
#             print(str(number))

# fizz_buzz()

# 4. Check is string is a palindrome - Reads the same forwards and Backwards

# def palindrome(str):
#     reversed_str = str[::-1]
#     return str == reversed_str

# print(palindrome('abba'))

# 4. Convert a String with underscore and/or hypen to camel case
# Codewars challenge : https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python

# def to_camel_case(text):
#     #your code here
#     text_array = text.replace('_', " ").replace('-', " ").split(" ")
#     for word in text_array:
#         index = text_array.index(word)
#         if word == text_array[0]:
#             continue
#         text_array[index] = word.title()
#     return "".join(text_array)

# to_camel_case('the_stealth_warrior')