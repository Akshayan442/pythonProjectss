string = input("Enter 2 string separated by space : ")
string = string.split(' ')
print(string[0][0] + string[1][1] + string[0][2:] + " " + string[1][0] + string[0][1] + string[1][2:])
print(string[0][0] + string[1][1].upper() + string[0][2:] + " " + string[1][0] + string[0][1].upper() + string[1][2:])