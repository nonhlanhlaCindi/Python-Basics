# # print('HELLO NONNY') 

# #Variables
# name = str(input('What is your name? '))
# age = int(input('How old are you? '))

# print('Hey '+ name + ' Sweetheart!')
# print('You are ' + str(age))


# # print(f"{name}")


# #Loops
# #FLOOR CONTROL



# #The code id = bool(input('Do you have an IDENTITY DOCUMENT (True/False?) ')) 
# # is not behaving as expected because the input() function always returns a string, 
# # even if the user enters "True" or "False." When you convert this string to a boolean using bool(),
# # any non-empty string, including "True" or "False," will be evaluated as True.
# # Therefore, regardless of the input, the result will always be True. This is what's causing the unexpected behavior in this code.

# id = input('Do you have an IDENTITY DOCUMENT (True/False?) ')
# age = int(input('How old are you? '))

# bool(id)


# if id == True and age >= 21: 
#         print('You are welcome to CAVO BY SKHOTHENI')
        
# elif id == True and age < 21:
#     print('Go home and do your homework, you are still a child')
    
# else:
#     print('Provide proof')





# x = 2

# if x > 2:
#     print('you have gotten 23')
    
# elif x == 5:
#     print('goten just 2')
    
# else: x
# print('Such a low score')

fruits = ['apple','banana','pineapple','watermelon']
for fruit in fruits:
        print(fruit)
