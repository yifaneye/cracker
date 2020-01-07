from dictionary_attack import crack


hash_input = input("\nEnter md5 hash: ")
plaintext = crack(hash_input)
if plaintext:
    print("\nPlaintext is found: " + plaintext + "\n")
else:
    print("\nPlaintext is NOT found\n")
