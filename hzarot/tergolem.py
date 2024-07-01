# while True:
#     correct_name = "kewan"
#     correct_age = 28
#
#     answer_1 = input("Enter your name: ")
#     answer_1 = answer_1.lower()
#     answer_2 = int(input("enter your age : "))
#     if answer_1 == correct_name and answer_2 == correct_age:
#         print("Correct!")
#         break
#     else:
#         print(f"Incorrect!. the correct name is : {correct_name} and the correct age is : {correct_age}")
#         # print(f"your age should be {correct_age}")

#
# while True:
#     sky_color = "blue"
#     sun_color = "yellow"
#     sky_color_q = input("What is the color of the sky? ")
#     sun_color_q = input("What is the color of the sun? ")
#
#     if sky_color_q == sky_color and sun_color_q != sun_color:
#         print(f"Sky color is correct: {sky_color_q} but sun color is not, should be {sun_color}! Please try again.")
#     elif sky_color_q != sky_color and sun_color_q == sun_color:
#         print(f"Sky color is incorrect, should be {sky_color} but sun color is correct: {sun_color_q}! Please try again.")
#     elif sky_color_q == sky_color and sun_color_q == sun_color:
#         print("Both answers are correct!")
#         break
#     else:
#         print("Both answers are incorrect! Please try again.")
# while True:
#     sky_color = "blue"
#     sun_color = "yellow"
#     sky_color_q = input("What is the color of the sky? ")
#     sun_color_q = input("What is the color of the sun? ")
#
#     if sky_color_q == sky_color and sun_color_q != sun_color:
#         print("Sky color is correct but sun color is not! Please try again.")
#     elif sky_color_q != sky_color and sun_color_q == sun_color:
#         print("Sky color is incorrect but sun color is correct! Please try again.")
#     elif sky_color_q == sky_color and sun_color_q == sun_color:
#         print("Both answers are correct!")
#         break
#     else:
#         print("Both answers are incorrect! Please try again.")


# while True:
#     sky_color = "blue"
#     sun_color = "yellow"
#     sky_color_q = input("What is the color of the sky? ")
#     sun_color_q = input("What is the color of the sun? ")
#
#     if sky_color_q.lower() == sky_color and sun_color_q.lower() == sun_color:
#         print("Both answers are correct!")
#         break
#     elif sky_color_q == sky_color and sun_color_q != sun_color:
#         print("Sky color is correct but sun color is not! Please try again.")
#         while sun_color_q != sun_color:
#             sun_color_q = input("What is the color of the sun? ")
#             print("Sky color is correct but sun color is not! Please try again. ")
#         if sun_color_q == sun_color:
#             print("Your answer is correct. Stopping.")
#             break
#     elif sky_color_q != sky_color and sun_color_q == sun_color:
#         print("Sky color is incorrect but sun color is correct! Please try again.")
#         while sky_color_q != sky_color:
#             sky_color_q = input("What is the color of the sky? ")
#             print("Sky color is incorrect but sun color is correct! Please try again.")
#         if sky_color_q == sky_color:
#             print("Your answer is correct. Stopping.")
#             break
#     else:
#         print("Both answers are incorrect! Please try again.")

negative_found = False
while negative_found == False:
    user_input = input("Enter a list of integers separated by commas: ")
    numbers = [int(num.strip()) for num in user_input.split(',')]

    for number in numbers:
        if number < 0:
            print(f"the first Negative number is: {number}")
            negative_found = True
            break

        if not negative_found:
            print("No negative numbers found.")
            break
