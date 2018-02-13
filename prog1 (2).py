print ("welcome to TIC-TAC-TOE ")
print ("this Game for 2 player ")
print ("the first player will be the odd number from 0 to 9 ")
print ("the second player will be the even number from 0 to 9 ")
print (" ")
print ("                  GOOD LUCK \O/               ")
print (" ")
arr=[['x1','x2','x3'],['x4','x5','x6'],['x7','x8','x9']]
for i in range (0,3):
    for y in range (0,1):
        print (arr[i][y],"\t",arr[i][y+1],"\t",arr[i][y+2])
arr1=[]
arr2=[]
pos1=[]
pos2=[]
w=9
while w>=1 :
    while True:
        player1=int(input("player 1 enter your number: "))
        if player1%2==0:
            print("enter odd number")
            player1=int(input("player 1 enter your number: "))
        if player1 in arr1:
                print ("you used this number before")
                player1=int(input("player 1 enter your number: "))
        if player1%2==0:
            continue
        if player1 in arr1:
            continue
        else:
            arr1.append(player1)
            break
    
    position1=int(input("Enter the position of number: "))
    while True:
        if (position1<0 or position1>9):
            print("Enter position from 1 to 9")
            position1=int(input("Enter the position of number: "))
        if position1 in pos1 or position1 in pos2:
            print("this position is busy")
            position1=int(input("Enter the position of number: "))
        if (position1<0 or position1>9):
            continue
        if position1 in pos1 or position1 in pos2:
            continue
        else:
            pos1.append(position1)
            break
        
    w-=1
    q=1
    for i in range(3):
        for x in range(3):
            if position1==q:
                arr[i][x]=player1
            q+=1
            
    for i in range (0,3):
        for y in range (0,1):
            print (arr[i][y],"\t",arr[i][y+1],"\t",arr[i][y+2])
    if  ((arr[0][0]!='x1')and(arr[0][1]!='x2')and(arr[0][2]!='x3')):
        if(arr[0][0]+arr[0][1]+arr[0][2]==15):
            print("player 1 is the winner !!!")
            break
    if ( (arr[1][0]!='x4')and(arr[1][1]!='x5')and(arr[1][2]!='x6')):
        if(arr[1][0]+arr[1][1]+arr[1][2]==15):
            print("player 1 is the winner !!!")
            break
    if ((arr[2][0]!='x7')and(arr[2][1]!='x8')and(arr[2][2]!='x9')):
        if (arr[2][0]+arr[2][1]+arr[2][2]==15):
            print("player 1 is the winner !!!")
            break
    if ((arr[0][0]!='x1')and(arr[1][0]!='x4')and(arr[2][0]!='x7')):
        if (arr[0][0]+arr[1][0]+arr[2][0]==15):
            print("player 1 is the winner !!!")
            break
    if ((arr[0][1]!='x2')and(arr[1][1]!='x5')and(arr[2][1]!='x8')):
        if (arr[0][1]+arr[1][1]+arr[2][1]==15):
            print("player 1 is the winner !!!")
            break
    if ((arr[0][2]!='x3')and(arr[1][2]!='x6')and(arr[2][2]!='x9')):
        if (arr[0][2]+arr[1][2]+arr[2][2]==15):
            print("player 1 is the winner !!!")
            break
    if ((arr[0][0]!='x1')and(arr[1][1]!='x5')and(arr[2][2]!='x9')):
        if (arr[0][0]+arr[1][1]+arr[2][2]==15):
            print("player 1 is the winner !!!")
            break
    if ((arr[0][2]!='x3')and(arr[1][1]!='x5')and(arr[2][0]!='x7')):
        if (arr[0][2]+arr[1][1]+arr[2][0]==15):
            print("player 1 is the winner !!!")
            break
    if w==0:
        break
    player2=int(input("player2 enter your number:"))

    while True:
        if (player2%2 !=0):
             print("Enter even number:")
             player2=int(input("player2 enter your number:"))
        if player2 in arr2:
                print("you used this number before")
                player2=int(input("player2 enter your number:"))
        if (player2%2 !=0):
            continue
        if player2 in arr2:
            continue
        else:
            arr2.append(player2)
            break
        
    position2=int(input("Enter the position of number: "))
    while True:
        if (position2 <0 or position2 >9):
            print ("Enter position from 1 to 9 ")
            position2=int(input("Enter the position of number: "))
        if position2 in pos1 or position2 in pos2:
                print("this position is busy")
                position2=int(input("Enter the position of number: "))
        if (position2 <0 or position2 >9):
            continue
        if position2 in pos1 or position2 in pos2:
            continue
        else:
            pos2.append(position2)
            break
    w-=1
    q=1
    for i in range(3):
        for x in range(3):
            if position2==q:
                arr[i][x]=player2
            q+=1
    for i in range (0,3):
            for y in range (0,1):
                print (arr[i][y],"\t",arr[i][y+1],"\t",arr[i][y+2])                
    if  ((arr[0][0]!='x1')and(arr[0][1]!='x2')and(arr[0][2]!='x3')):
        if(arr[0][0]+arr[0][1]+arr[0][2]==15):
            print("player 2 is the winner !!!")
            break
    if ( (arr[1][0]!='x4')and(arr[1][1]!='x5')and(arr[1][2]!='x6')):
        if(arr[1][0]+arr[1][1]+arr[1][2]==15):
            print("player 2 is the winner !!!")
            break
    if ((arr[2][0]!='x7')and(arr[2][1]!='x8')and(arr[2][2]!='x9')):
        if (arr[2][0]+arr[2][1]+arr[2][2]==15):
            print("player 2 is the winner !!!")
            break
    if ((arr[0][0]!='x1')and(arr[1][0]!='x4')and(arr[2][0]!='x7')):
        if (arr[0][0]+arr[1][0]+arr[2][0]==15):
            print("player 2 is the winner !!!")
            break
    if ((arr[0][1]!='x2')and(arr[1][1]!='x5')and(arr[2][1]!='x8')):
        if (arr[0][1]+arr[1][1]+arr[2][1]==15):
            print("player 2 is the winner !!!")
            break
    if ((arr[0][2]!='x3')and(arr[1][2]!='x6')and(arr[2][2]!='x9')):
        if (arr[0][2]+arr[1][2]+arr[2][2]==15):
            print("player 2 is the winner !!!")
            break
    if ((arr[0][0]!='x1')and(arr[1][1]!='x5')and(arr[2][2]!='x9')):
        if (arr[0][0]+arr[1][1]+arr[2][2]==15):
            print("player 2 is the winner !!!")
            break
    if ((arr[0][2]!='x3')and(arr[1][1]!='x5')and(arr[2][0]!='x7')):
        if (arr[0][2]+arr[1][1]+arr[2][0]==15):
            print("player 2 is the winner !!!")
            break
  
if (w==0):
    print("DRAW !!")



