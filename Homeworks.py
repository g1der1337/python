
# match (int(input())):
#     case(1):
#         print("super 1")
#     case(2):
#         print("super 2")
#     case(3):
#         print("super 3")
#     case(4):
#         print("super 4")
#     case(5):
#         print("super 5")

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# match (num2):
#     case('+'):
#         print(num1 + num2)
#     case('-'):
#         print(num1 - num2)
#     case(':'):
#         print(num1 / num2)
#     case('*'):
#         print(num1 * num2)
# 

# import json

# users = {}

# def create_user():
#     username = input()
#     password = input()

#     if username in users:
#         print('your name had added')
#     else:
#         users[username] = password
#         print(f"User {username} had added.")

# def delete_user():
#     username = input()
#     if username in users:
#         del users[username]

# def display_users():
#     for user in users:
#         print("-", user)

# while 0 == 0:
#     command = input()

#     if command == "new":
#         create_user()
#     elif command == "del":
#         delete_user()
#     elif command.lower() == "exit":
#         break
#     else:
#         display_users()

# with open('users.txt', 'w') as file:
#     json.dump(users, file)
