scr = input("enter a string")
newscr = scr[-1:] + scr[1:-1] + scr[:1]
print(newscr)