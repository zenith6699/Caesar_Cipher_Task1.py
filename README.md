# Caesar Cipher Encryption/Decryption

This is a simple Python program that implements the **Caesar Cipher** algorithm.  
It allows users to **encrypt** and **decrypt** text using a shift value.

---

## 📜 How It Works
- The Caesar Cipher shifts each letter in the text by a given number (`shift value`).
- Non-alphabetic characters (spaces, numbers, punctuation) remain unchanged.
- The same shift value must be used to decrypt the message.

---

## 🚀 Usage

1. Clone or download the script.
2. Run the Python file:

   ```bash
   python caesar_cipher.py
   ```

3. Enter:
   - A message to encrypt or decrypt
   - A shift value (integer)
   - Choose `e` for encryption or `d` for decryption

---

## 📝 Example

```
=== Caesar Cipher ===
Enter your message: hello world
Enter shift value (e.g. 3): 3
Do you want to encrypt or decrypt? (e/d): e
Encrypted message: khoor zruog
```

```
=== Caesar Cipher ===
Enter your message: khoor zruog
Enter shift value (e.g. 3): 3
Do you want to encrypt or decrypt? (e/d): d
Decrypted message: hello world
```

---

## ⚙️ Requirements
- Python 3.x

No extra libraries are required.

---

## 📂 File Structure
```
caesar_cipher.py   # Main program
README.md          # Documentation
```

---

## ✨ Features
- Supports both encryption and decryption
- Works with uppercase and lowercase letters
- Preserves spaces, numbers, and symbols
