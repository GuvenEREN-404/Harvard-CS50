from cs50 import get_int


yukseklik=get_int("Height:")
while yukseklik<1 or yukseklik>8:
    yukseklik=get_int("Height:")
        

for i in range(0,yukseklik):
    for k in range(0,yukseklik-i-1):
        print(" ",end = "")
    for j in range(0,i+1):
        print("#", end = "" )
        
    print("  ", end = "")   
    for j in range(0,i+1):
        print("#", end = "" )
    print("")
