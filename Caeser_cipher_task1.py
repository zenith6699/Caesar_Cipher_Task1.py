def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():  # process only alphabetic characters
            base = ord('A') if char.isupper() else ord('a')
            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == "decrypt":
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char  # keep spaces, punctuation, numbers unchanged
    return result


def main():
    print("=== Caesar Cipher ===")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g. 3): "))
    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()

    if choice == 'e':
        encrypted = caesar_cipher(message, shift, "encrypt")
        print("Encrypted message:", encrypted)
    elif choice == 'd':
        decrypted = caesar_cipher(message, shift, "decrypt")
        print("Decrypted message:", decrypted)
    else:
        print("Invalid choice. Please select 'e' or 'd'.")


if __name__ == "__main__":
    main()
