def encrypt_decrypt(message,shift,mode):
    if mode == "encrypt":
        direction = 1
    elif mode == "decrypt":
        direction = -1
    else:
        return "Invalid mode"
    
    new_message = ""
    for letter in message:
        if letter.isupper():
            position = ord(letter) - ord("A")
            new_position = (position + direction*shift) % 26
            new_letter = chr(new_position + ord("A"))
            new_message += new_letter
        elif letter.islower():
            position = ord(letter) - ord("a")
            new_position = (position + direction*shift) % 26
            new_letter = chr(new_position + ord("a"))
            new_message += new_letter
        else:
            new_message += letter
    return new_message

print("===== Ceaser Cipher =====")
print("1. encrypt")
print("2. decrypt")
print(" ")
option = input("Choose an option: ")
if option == "1":
    mode = "encrypt"
    message = input("Enter your message: ")
    shift = int(input("Enter shift amount: "))
    print(" ")
    result = encrypt_decrypt(message,shift,mode)
    print(f"Result: {result}")
elif option == "2":
    mode = "decrypt"
    message = input("Enter your message: ")
    shift = int(input("Enter shift amount: "))
    print(" ")
    result = encrypt_decrypt(message,shift,mode)
    print(f"Result: {result}")
else:
    print("Invalid mode")