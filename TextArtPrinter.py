def print_leter_A():
    x = 0
    y = 7
    while True:
        y -= 1
        while True:
            if x == 16:
                print()
                x = 0
                break
            elif y == 6 and 6 <= x <= 9:
                print("*",end = " ")
                x += 1
            elif x == y or y == -x + 15:
                print("*",end = " ")
                x += 1
            elif y == 3 and 1 <= x <= 14:
                print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ")
                x += 1
        if y == 0:
            break
def print_leter_B():
    x = 0
    y = 9
    while True:
        y -= 1
        while True:
            if x == 6:
                print()
                x = 0
                break
            elif y == 8 and 0 <= x <= 4:
                print("*",end = " ")
                x += 1
            elif y == 4 and 0 <= x <= 4:
                print("*",end = " ")
                x += 1
            elif y == 0 and 0 <= x <= 4:
                print("*",end = " ")
                x += 1
            elif x == 0 or x == 5:
                if not y == 8 and not y == 4 and not y == 0:
                    print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ")
                x += 1
        if y == 0:
            break
def print_leter_C():
    y = 8
    x = 0
    while True:
        y -= 1
        while True:
            if x == 7:
                print()
                x = 0
                break
            elif y == 7 and 2 <= x <= 6:
                print("*",end = " ")
                x += 1
            elif y == 0 and 2 <= x <= 6:
                print("*",end = " ")
                x += 1
            elif x == 0 and 2 <= y <= 5:
                print("*",end = " ")
                x += 1
            elif (x == 1 and y == 6) or (x == 1 and y == 1):
                print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ") 
                x += 1
        if y == 0:
            break
def print_leter_D():
    y = 9
    x = 0
    while True:
        y -= 1
        while True:
            if x == 7:
                print()        
                x = 0
                break
            elif y == 8 and 0 <= x <= 5:
                print("*",end = " ")
                x += 1
            elif y == 0 and 0 <= x <= 5:
                print("*",end = " ")
                x += 1
            elif x == 0 or x == 6:
                if not y == 8 and not y == 0:
                    print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ")
                x += 1
        if y == 0:
            break
def print_leter_E():
    y = 9
    x = 0
    while True:
        y -= 1
        while True:
            if x == 5:
                print()
                x = 0
                break
            elif y == 8 and 0 <= x <= 4:
                print("*",end = " ")
                x += 1
            elif y == 4 and 0 <= x <= 4:
                print("*",end = " ")
                x += 1
            elif y == 0 and 0 <= x <= 4:
                print("*",end = " ")
                x += 1
            elif x == 0:
                print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ")
                x += 1
        if y == 0:
            break
def print_leter_S():
    y = 11
    x = 0
    while True:
        y -= 1
        while True:
            if x == 12:
                print()
                x = 0
                break
            elif y == x + 6 and 7 <= y <= 10:
                print("*",end = " ")
                x += 1
            elif y == 10 and 5 <= x <= 8:
                print("*",end = " ")
                x += 1
            elif (y == 6 and x == 1) or (y == 1 and x == 11):
                print("*",end = " ")
                x += 1
            elif y == 5 and 2 <= x <= 7:
                print("*",end = " ")
                x += 1
            elif y == -x + 13 and 2 <= y <= 5:
                print("*",end = " ")
                x += 1
            elif y == 0 and 0 <= x <= 10:
                print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ")
                x += 1
        if y == 0:
            break
def print_leter_O():
    y = 10
    x = 0
    while True:
        y -= 1
        while True:
            if x == 9:
                print()
                x = 0
                break
            elif y == 9 and 3 <= x <= 5:
                print("*",end = " ")
                x += 1
            elif (y == x + 7) or (y == -x + 15):
                print("*",end = " ")
                x += 1
            elif (x == 0 and 3 <= y <= 6) or (x == 8 and 3 <= y <= 6):
                print("*",end = " ")
                x += 1
            elif (y == -x + 2) or (y == x - 6):
                print("*",end = " ")
                x += 1
            elif y == 0 and 3 <= x <= 5:
                print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ")
                x += 1
        if y == 0:
            break
def print_leter_Q():
    x = 0
    y = 12
    while True:
        y -= 1
        while True:
            if x == 8:
                print()
                x = 0
                break
            elif y == 11 and 1 <= x <= 5:
                print("*",end = " ")
                x += 1
            elif (x == 0 and 3 <= y <= 10) or (x == 6 and 3 <= y <= 10):
                print("*", end = " ")
                x += 1
            elif y == 2 and 1 <= x <= 5:
                print("*",end = " ")
                x += 1
            elif y == - x + 6 and 0 <= y <= 3:
                print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ")
                x += 1
        if y == 0:
            break
def print_leter_Y():
    y = 11
    x = 0
    while True:
        y -= 1
        while True:
            if x == 11:
                print()
                x = 0
                break
            elif y == 10 and not (4 <= x <= 6):
                print("*",end = " ")
                x += 1
            elif (y == -x + 11 and 7 <= y <= 9) or (y == x + 1 and 7 <= y <= 9):
                print("*",end = " ")
                x += 1
            elif (x == 5 and 1 <= y <= 6) or (x == 2 and 0 <= y <= 2):
                print("*",end = " ")
                x += 1
            elif y == 1 and 2 <= x <= 5:
                print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ")
                x += 1
        if y == 0:
            break
def print_leter_G():
    y = 12
    x = 0
    while True:
        y -= 1
        while True:
            if x == 10:
                print()
                x = 0
                break
            elif x == 9 and not (5 <= y <= 8 or 0 <= y <= 1):
                print("*",end = " ")
                x += 1
            elif y == 10 and 3 <= x <= 8:
                print("*",end = " ")
                x += 1
            elif y == 4 and 5 <= x <= 8:
                print("*",end = " ")
                x += 1
            elif y == x + 8 and 8 <= y <= 10:
                print("*",end = " ")        
                x += 1
            elif x == 0 and 3 <= y <= 7:
                print("*",end = " ")
                x += 1
            elif x == 4 and 2 <= y <= 6:
                print("*",end = " ")
                x += 1
            elif (y == -x + 2 and 0 <= y <= 2) or (y == x - 7 and 0 <= y <= 2):
                print("*",end = " ")
                x += 1
            elif y == 0 and 3 <= x <= 6:
                print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ")
                x += 1
        if y == 0:
            break
def print_leter_W():
    y = 7
    x = 0
    while True:
        y -= 1
        while True:
            if x == 17:
                print()
                x = 0
                break
            elif y == 6 and not(3 <= x <= 13):
                print("*",end = " ")
                x += 1
            elif y == -x + 6 or (y == -x + 10 and 0 <= y <= 3) or (y == x - 6 and 0 <= y <= 3) or y == x - 10:
                print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ")
                x += 1
        if y == 0:
            break
def print_leter_M():
    y = 10
    x = 0
    while True:
        y -= 1
        while True:
            if x == 17:
                print()
                x = 0
                break
            elif y == 2 * x - 1:
                print("*",end = " ")
                x += 1
            elif y == -2 * x + 31:
                print("*",end = " ")
                x += 1
            elif y == -2 * x + 20 and 4 <= y <= 8:
                print("*",end = " ")
                x += 1
            elif y == 2 * x - 12 and 6 <= y <= 8:
                print("*",end = " ")
                x += 1
            elif y == 0 and not (3 <= x <= 13):
                print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ")
                x += 1
        if y == 0:
            break
def print_leter_V():
    y = 11
    x = 0
    while True:
        y -= 1
        while True:
            if x == 13:
                print()
                x = 0
                break
            elif y == 10 and not (3 <= x <= 9):
                print("*",end = " ")
                x += 1
            elif y == -2 * x + 11 or y == 2 * x - 13:
                print("*",end = " ")
                x += 1
            elif y == 0 and x == 6:
                print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ")
                x += 1
        if y == 0:
            break
def print_leter_X():
    y = 11
    x = 0
    while True:
        y -= 1
        while True:
            if x == 13:
                print()
                x = 0
                break
            elif y == 10 and not (3 <= x <= 9):
                print("*",end = " ")
                x += 1
            elif y == - x + 11 or y == x - 1:
                print("*",end = " ")
                x += 1
            elif y == 0 and not (3 <= x <= 9):
                print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ")
                x += 1
        if y == 0:
            break
def print_leter_Z():
    y = 10
    x = 0
    while True:
        y -= 1
        while True:
            if x == 9:
                print()
                x = 0
                break
            elif (x == 0 and 7 <= y <= 8) or (x == 8 and 0 <= y <= 1):
                print("*",end = " ") 
                x += 1
            elif y == 8 or y == 0:
                print("*",end = " ")
                x += 1
            elif y == x:
                print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ")
                x += 1
        if y == 0:
            break
def print_leter_N():
    y = 10
    x = 0
    while True:
        y -= 1
        while True:
            if x == 12:
                print()
                x = 0
                break
            elif y == 9 and 9 <= x <= 11:
                print("*",end = " ")
                x += 1
            elif x == 1 or x == 10:
                print("*",end = " ")
                x += 1
            elif y == -x + 10:
                print("*",end = " ")
                x += 1
            elif y == 0 and 0 <= x <= 2:
                print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ")
                x += 1
        if y == 0:
            break
def print_leter_K():
    y = 13
    x = 0
    while True:
        y -= 1
        while True:
            if x == 9:
                print()
                x = 0
                break
            elif y == 12 and not (3 <= x <= 5):
                print("*",end = " ")
                x += 1
            elif x == 1:
                print("*",end = " ")
                x += 1
            elif (y == x + 5 and 2 <= x <= 6) or (y == -x + 7 and 2 <= x <= 6):
                print("*",end = " ")
                x += 1
            elif y == 0 and not (3 <= x <= 5):
                print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ")
                x += 1
        if y == 0:
            break
def print_leter_R():
    y = 13
    x = 0
    while True:
        y -= 1
        while True:
            if x == 10:
                print()
                x = 0
                break
            elif y == 12 and 2 <= x <= 6:
                print("*",end = " ")
                x += 1
            elif y == 6 and 2 <= x <= 6:
                print("*",end = " ")
                x += 1
            elif x == 1 or (x == 7 and 7 <= y <= 11):
                print("*",end = " ")
                x += 1
            elif y == - x + 8 and 3 <= x <= 7:
                print("*",end = " ")
                x += 1
            elif y == 0 and not (3 <= x <= 6):
                print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ")
                x += 1
        if y == 0:
            break
def print_leter_P():
    y = 11
    x = 0
    while True:
        y -= 1
        while True:
            if x == 8:
                print()
                x = 0
                break
            elif (y == 10 and 0 <= x <= 6) or (y == 5 and 1 <= x <= 6) or (y == 0 and 0 <= x <= 2):
                print("*",end = " ")
                x += 1
            elif x == 1 or (x == 7 and 6 <= y <= 9):
                print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ")
                x += 1
        if  y == 0:
            break
def print_leter_H():
    y = 11
    x = 0
    while True:
        y -= 1
        while True:
            if x == 9:
                print()
                x = 0
                break
            elif (y == 10 and not 3 <= x <= 5) or (y == 0 and not 3 <= x <= 5):
                print("*",end = " ")
                x += 1
            elif x == 1 or x == 7:
                print("*",end = " ")
                x += 1
            elif y == 5 and 2 <= x <= 7:
                print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ")
                x += 1
        if y == 0:
            break
def print_leter_L():
    y = 11
    x = 0
    while True:
        y -= 1
        while True:
            if x == 8:
                print()
                x = 0
                break
            elif (y == 10 and 0 <= x <= 2) or y == 0:
                print("*",end = " ")
                x += 1
            elif x == 1 or (x == 7 and 0 <= y <= 2):
                print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ")
                x += 1
        if y == 0:
            break
def print_leter_I():
    y = 9
    x = 0
    while True:
        y -= 1
        while True:
            if x == 3:
                print()
                x = 0
                break
            elif y == 8 or x == 1 or y == 0:
                print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ")
                x += 1
        if y == 0:
            break
def print_leter_T():
    y = 10
    x = 0
    while True:
        y -= 1
        while True:
            if x == 11:
                print()
                x = 0
                break
            elif y == 9 or (y == 8 and (x == 0 or x == 10)):
                print("*",end = " ")
                x += 1
            elif x == 5 or (y == 0 and 4 <= x <= 6):
                print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ")
                x += 1
        if y == 0:
            break
def print_leter_J():
    y = 8
    x = 0
    while True:
        y -= 1
        while True:
            if x == 8:
                print()
                x = 0
                break
            elif (y == 7 and 3 <= x <= 7) or (y == 2 and 0 <= x <= 2) or (y == 0 and 2 <= x <= 4):
                print("*",end = " ")
                x += 1
            elif (x == 1 and y == 1) or (x == 5 and not y == 0):
                print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ")
                x += 1
        if y == 0:
            break
def print_leter_U():
    y = 8
    x = 0
    while True:
        y -= 1
        while True:
            if x == 9:
                print()
                x = 0
                break
            elif y == 7 and not (3 <= x <= 5) or (y == 0 and 2 <= x <= 6):
                print("*",end = " ")
                x += 1
            elif (x == 1 or x == 7) and (not y == 0):
                print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ")
                x += 1
        if y == 0:
            break
def print_leter_F():
    y = 10
    x = 0
    while True:
        y -= 1
        while True:
            if x == 7:
                print()
                x = 0
                break
            elif y == 9 or (y == 5 and 1 <= x <= 5) or (y == 0 and 0 <= x <= 2):
                print("*",end = " ")
                x += 1
            elif x == 1 or (x == 5 and 4 <= y <= 6) or (x == 6 and y == 8):
                print("*",end = " ")
                x += 1
            else:
                print(" ",end = " ")
                x += 1
        if y == 0:
            break

if __name__ == "__main__":
    a = 0
    numbers_list = ""
    charcters_list = "~`!@#$%^&*()_-+=[:;'<,>.?/|\/]"
    charcters_list1 = ""
    while True:
        string = input("you can turn word or sentence to ascii art printer: ")
        if string == "q":
            break
        while True:
            try:
                sayi = int(string[a])
                numbers_list += str(sayi)
            except ValueError:
                if string[a] in charcters_list:
                    charcters_list1 += string[a]
            a += 1
            if a == len(string):
                a = 0
                break
        if bool(numbers_list):
            print("we can not write numbers with ascii symbol")
        if bool(charcters_list1):
            print("we can not write specific symbols with ascii symbol")
        while True:
            if bool(numbers_list) or bool(charcters_list1):
                next = input("if you want to continue 'y' or 'n': ")
                if next == "y":
                    break
                elif next == "n":
                    break
                else:
                    print("what do you wan to do 'yes' or 'no'")
                    continue
            elif not numbers_list and not charcters_list1:
                break
        if (next == "y") or (not numbers_list and not charcters_list1):
            while True:
                character = string[a]
                if character == "a" or character == "A":
                    print_leter_A()
                elif character == "b" or character == "B":
                    print_leter_B()
                elif character == "c" or character == "C":
                    print_leter_C()
                elif character == "d" or character == "D":
                    print_leter_D()
                elif character == "e" or character == "E":
                    print_leter_E()
                elif character == "f" or character == "F":
                    print_leter_F()
                elif character == "g" or character == "G":
                    print_leter_G()
                elif character == "h" or character == "H":
                    print_leter_H()
                elif character == "i" or character == "I":
                    print_leter_I()
                elif character == "j" or character == "J":
                    print_leter_J()
                elif character == "k" or character == "K":
                    print_leter_K()
                elif character == "l" or character == "L":
                    print_leter_L()
                elif character == "m" or character == "M":
                    print_leter_M()
                elif character == "n" or character == "N":
                    print_leter_N()
                elif character == "o" or character == "O":
                    print_leter_O()
                elif character == "p" or character == "P":
                    print_leter_P()
                elif character == "q" or character == "Q":
                    print_leter_Q()
                elif character == "r" or character == "R":
                    print_leter_R()
                elif character == "s" or character == "S":
                    print_leter_S()
                elif character == "t" or character == "T":
                    print_leter_T()
                elif character == "u" or character == "U":
                    print_leter_U()
                elif character == "v" or character == "V":
                    print_leter_V()
                elif character == "w" or character == "W":
                    print_leter_W()
                elif character == "x" or character == "X":
                    print_leter_X()
                elif character == "y" or character == "Y":
                    print_leter_Y()
                elif character == "z" or character == "Z":
                    print_leter_Z()
                elif character == " ":
                    print()
                    print()
                a += 1
                if a == len(string):
                    a = 0
                    break
        charcters_list1 = ""
        numbers_list = ""       