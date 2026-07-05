alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
encrypted_msg = []
decrypted_msg = []

def main():
    while True:
        try:
            print("Do you want to (e)ncrypt or (d)ecrypt?")
            choice = input("> ")
            if choice.upper() == "E":
                encrypt()
            if choice.upper() == "D":
                decrypt()
        except KeyboardInterrupt:
            print("\nProgram Closing...")
            break
            

def encrypt():
    encrypted_msg.clear()
    print("Enter message to encrypt.")
    message = input("> ")
    key = int(input("Enter Key: "))
    for x in message:
        for i in range(len(alphabets)):
            if alphabets[i] == x:
                if (i + key) >= (len(alphabets)):
                    encrypted_msg.append(alphabets[(i + key) % (len(alphabets))])
                else:
                    encrypted_msg.append(alphabets[i + key])
            elif alphabets[i].upper() == x:
                if (i + key) >= (len(alphabets)):
                    encrypted_msg.append(alphabets[(i + key) % (len(alphabets))].upper())
                else:
                    encrypted_msg.append(alphabets[i + key].upper())

        if x == " ":
            encrypted_msg.append(" ")
    
    print("".join(encrypted_msg))


def decrypt():
    decrypted_msg.clear()
    print("Enter message to decrypt.")
    message = input("> ")
    key = int(input("Enter Key: "))
    for x in message:
        for i in range(len(alphabets)):
            if alphabets[i] == x:
                    if (i - key) < -26:
                        decrypted_msg.append(alphabets[(i - key) % -26])
                    else:
                        decrypted_msg.append(alphabets[i - key])
            elif alphabets[i].upper() == x:
                if (i - key) < -26:
                    decrypted_msg.append(alphabets[(i - key) % -26].upper())
                else:
                    decrypted_msg.append(alphabets[i - key].upper())            

        
        if x == " ":
            decrypted_msg.append(" ")

    print("".join(decrypted_msg))



if __name__ == "__main__":
    main()
