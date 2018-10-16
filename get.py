from getch import getch, pause

"""
上 27 91 65
下 27 91 66
右 27 91 67
左 27 91 68
"""

while True:
    key = ord(getch())
    if key == 13: #enter
        print("Enter")
        break
    else:
        #print("You pressed: %s (%d)" % (chr(key), key))

        #Macの上下左右キー入力検知
        if(key == 27):
            getch(); key = getch()
            if(key=="A"):
                print("up")
            elif(key=="B"):
                print("down")
            elif(key=="C"):
                print("right")
            elif(key=="D"):
                print("left")


pause()
