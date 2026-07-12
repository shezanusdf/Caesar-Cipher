alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def main():
    while True:
        try:
            print("Do you want to (e)ncrypt or (d)ecrypt?")
            choice = input("> ")
            print("Enter message to encrypt.")
            message = input("> ")
            key = int(input("Enter Key: "))
            if choice.upper() == "E":
                caesar(message, key)
            if choice.upper() == "D":
                caesar(message, -key)
        except KeyboardInterrupt:
            print("\nProgram Closing...")
            break
            

def caesar(message, key):
    result = []
    for char in message:
        if char in alphabets: 
            i = alphabets.index(char)
            result.append(alphabets[(i + key) % 26])
        elif char == " ":
            result.append(" ")
    print("".join(result))   

        



if __name__ == "__main__":
    main()
