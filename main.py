alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def encrypt():
    text=input("Enter your text: ")
    s_key=int(input("Enter the shift key value: "))
    new=list()
    for i in text:
        if i==" ":
            new.append(" ")
        else:
            x = alpha.index(i)
            res = (x + s_key) % 26
            new.append(alpha[res])
    return new
def decrypt():
    text = input("Enter your text: ")
    s_key = int(input("Enter the shift key value: "))
    new = list()
    for i in text:
        if i==" ":
            new.append(" ")
        else:
            x = alpha.index(i)
            res = (x - s_key) % 26
            new.append(alpha[res])
    return new

flag=True
while(flag==True):
    opt=input("Enter e for Encryption \t Enter d for Decryption : ")
    if opt=="e":
        a=encrypt()
        print(a)
    else:
        a=decrypt()
        print(a)

    i=input("Enter 'yes' to run the program again \n Enter 'no' to exit \n :")
    if i=='no':
        flag=False

