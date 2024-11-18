# #1
open_file = open("i_file.txt" , "w")
print(open_file)
open_file.write(input())

# #2
n = 'Тут надо писать'
open_file_1 = open("i_file.txt" , 'a')
open_file_1.write(n)

#3
n = 0
while n != 'ex':
    n = input()
    if n == 'new':
        name = input()
        password = input()
        if (name not in open_file_2) and (password not in open_file_2): 
            open_file_2 = open("file_1.txt", 'a')
            open_file_2.write(name, password)
    elif n == 'del':
        name = input()
        password = input()
        open_file_2.name = ''
        open_file_2.password = ''
