# Basic Encryption & Decryption using Caesar Cipher

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isupper():
            encrypted_text += chr(
                (ord(char) - ord('A') + shift) % 26 + ord('A')
            )
        elif char.islower():
            encrypted_text += chr(
                (ord(char) - ord('a') + shift) % 26 + ord('a')
            )
        else:
            encrypted_text += char
    return encrypted_text
def decrypt(text, shift):
    decrypted_text = ""

    for char in text:
        if char.isupper():
            decrypted_text += chr(
                (ord(char) - ord('A') - shift) % 26 + ord('A')
            )
        elif char.islower():
            decrypted_text += chr(
                (ord(char) - ord('a') - shift) % 26 + ord('a')
            )
        else:
            decrypted_text += char
    return decrypted_text
print("=" * 50)
print("     BASIC ENCRYPTION & DECRYPTION")
print("          CAESAR CIPHER")
print("=" * 50)
text = input("Enter your text: ")
shift = int(input("Enter shift key (1-25): "))
shift = shift % 26

encrypted_text = encrypt(text, shift)
decrypted_text = decrypt(encrypted_text, shift)

print("\n" + "=" * 50)
print("                 RESULTS")
print("=" * 50)
print("Original Text  :", text)
print("Shift Key      :", shift)
print("Encrypted Text :", encrypted_text)
print("Decrypted Text :", decrypted_text)
print("=" * 50)
