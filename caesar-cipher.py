SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '

choice = input("do you want to (e)ncode or (d)ecode ? : ")

if choice == 'e': 
    message = input("Enter a message to encrypt : ")
    key = int(input("Enter key(0 to 26):"))
    encrypted_message = []
    
    
    for i in message:
        for y in range(len(SYMBOLS)):
            if i.upper() == SYMBOLS[y]:
                if (y + key) <= 26:
                    encrypted_message.append(SYMBOLS[y+key])
                
                elif (y + key) > 26:
                    x = (y + key - 26)
                    encrypted_message.append(SYMBOLS[x-1])
                        
    print("Encrypted result : ")
    print(''.join(encrypted_message))
    
elif choice == 'd':
    message = input("Enter a message to decrypt :")
    key = int(input("Enter key(0 to 26):"))
    
    decrypted_message = []
    for i in message:
        for y in range(len(SYMBOLS)):
            if i.upper() == SYMBOLS[y]:
                if (y - key) >= 0:
                    decrypted_message.append(SYMBOLS[y-key])
                
                elif (y - key) < 0:
                    x = (y - key)
                    decrypted_message.append(SYMBOLS[x])
    print("Decrypted result : ")
    print(''.join(decrypted_message))
        
    
    

                
