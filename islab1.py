def encrypt():
    str_input = input("\t\tInput String: ")
    encrypted_str = ''.join([chr(ord(char) + 3) for char in str_input])
    print(f"\n\t\tEncrypted String: {encrypted_str}")

def decrypt():
    str_input = input("\t\tInput String: ")
    decrypted_str = ''.join([chr(ord(char) - 3) for char in str_input])
    print(f"\n\t\tDecrypted String: {decrypted_str}")

def main():
    print("\t\tConfidentiality")
    while True:
        print("\t\tChoose operation\n\t\t1. Encryption\n\t\t2. Decryption\n\t\t3. Exit\n\t\t")
        choice = int(input("\t\t"))
        
        if choice == 1:
            encrypt()
        elif choice == 2:
            decrypt()
        elif choice == 3:
            break
        else:
            print("\t\tInvalid choice!")
        
        ch = input("\n\t\tDo you want to continue (Y/N): ")
        if ch.lower() != 'y':
            break

if __name__ == "__main__":
    main()