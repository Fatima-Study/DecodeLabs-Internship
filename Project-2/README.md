# DecodeLabs-Internship

# Project 2

# 🔐 Caesar Cipher Encryption & Decryption

> A Python-based Caesar Cipher program that encrypts and decrypts text using a user-defined shift key.

---

# 📑 Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Tools and Technologies](#tools-and-technologies)
- [Methods](#methods)
- [Project Structure](#project-structure)
- [Key Insights](#key-insights)
- [Output](#output)
- [How to Run This Project](#how-to-run-this-project)
- [Future Work](#future-work)
- [Final Recommendations](#final-recommendations)
- [Author & Contact](#author--contact)

---

# Overview

The **Caesar Cipher Encryption & Decryption** project was developed as part of the **DecodeLabs Cyber Security Internship** to demonstrate the fundamentals of classical cryptography using Python. The application accepts a text message and a shift key, encrypts the message by shifting alphabetic characters, and then decrypts it to recover the original text. This project provides practical experience with basic encryption techniques and Python programming.

---

# Problem Statement

Protecting sensitive information requires converting readable text into an unreadable format before transmission or storage. This project implements the **Caesar Cipher**, a simple substitution technique, to demonstrate the basic principles of encryption and decryption using a fixed shift key.

---

# Tools and Technologies

| Tool / Technology | Purpose |
|-------------------|---------|
| Python | Programming language used to implement the encryption and decryption logic |
| Python IDLE | Development and execution environment |
| Caesar Cipher | Basic substitution encryption technique |
| Windows | Development and testing environment |

---

# Methods

The program follows these steps:

1. Accept a text message from the user.
2. Accept a shift key (1–25).
3. Encrypt alphabetic characters using the Caesar Cipher.
4. Display the encrypted message.
5. Decrypt the encrypted message using the same shift key.
6. Display the decrypted message.
7. Verify that the decrypted text matches the original input.

---

# Project Structure

```text
Caesar-Cipher-Encryption-Decryption/
│
├── CODE-Encrypt_Decrypt.txt
│
├── OUTPUT.pdf/
│   ├── test-case-1.png
│   ├── test-case-2.png
│   └── test-case-3.png
│
├── docs/
│   └── Encryption and Decryption_Report.docx
│
├── README.md
├── LICENSE
├── .gitignore
```

---

# Key Insights

- Demonstrates the working principle of the Caesar Cipher.
- Uses a user-defined shift key for encryption and decryption.
- Preserves spaces, numbers, and special characters during processing.
- Successfully restores the original message after decryption.
- Provides a practical understanding of basic cryptographic concepts.

---

# Output

The program displays:

- Original Text
- Shift Key
- Encrypted Text
- Decrypted Text

### Sample Output

```text
==================================================
 BASIC ENCRYPTION & DECRYPTION
 CAESAR CIPHER
==================================================

Enter your text: Cyber Security
Enter shift key (1-25): 3

==================================================
 RESULTS
==================================================
Original Text  : Cyber Security
Shift Key      : 3
Encrypted Text : Fbehu Vhfxulwb
Decrypted Text : Cyber Security
==================================================
```

---

# How to Run This Project

### 1. Clone the repository

```bash
git clone https://github.com/Fatima-Study/DecodeLabs-Internship.git
```

### 2. Navigate to the project folder

```bash
cd DecodeLabs-Internship
```

### 3. Navigate to the source folder

```bash
cd src
```

### 4. Run the Python program

```bash
python caesar_cipher.py
```

### 5. Enter

- A text message
- A shift key (1–25)

The program will display the encrypted text and then decrypt it back to the original message.

---

# Future Work

- Support more advanced encryption algorithms such as the Vigenère Cipher.
- Add a graphical user interface (GUI).
- Enable encryption and decryption of text files.
- Improve input validation and error handling.
- Expand the project with additional cryptographic techniques.

---

# Final Recommendations

- Use the Caesar Cipher for educational and learning purposes only.
- Apply modern encryption algorithms for real-world applications.
- Validate user input before processing.
- Keep encryption keys secure.
- Continue learning advanced cryptographic techniques to strengthen cybersecurity skills.

---

# Author & Contact

**Author:** Fatima

**Project:** Caesar Cipher Encryption & Decryption

**Internship:** Cyber Security Internship

**LinkedIn:** linkedin.com/in/fatima-taufique-1313b633b
