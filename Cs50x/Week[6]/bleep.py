from sys import argv

def rtuk(text):
    rtuk1=[]
    for i in range (len(text)):
        rtuk1.append("*")
    return "".join(rtuk1)    

def main():

    if len(argv)!=2:
        print("Usage: python bleep.py dictionary")
        exit(1)

    with open(argv[1],"r")as file:
        sor=input("What message would you like to censor:\n")
        text=sor.split()
        for i in range (len(text)):
            for j in file:
                if j.strip("\n")==text[i].lower():
                    text[i]=rtuk(text[i])
                    break
            file.seek(0)
        print(" ".join(text))
    exit(0)    

if __name__ == "__main__":
    main()
