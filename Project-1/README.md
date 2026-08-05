# DecodeLabs-Internship

# Project 1

# 🔐 Password Strength Checker

> A Python-based Password Strength Checker that evaluates password security using rule-based validation and classifies passwords as Weak, Medium, or Strong.

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

The **Password Strength Checker** is a Python-based cybersecurity project developed as part of a Cyber Security Internship. The program evaluates a user-provided password using four essential security checks: password length, uppercase letters, numbers, and symbols. Based on the number of conditions satisfied, it classifies the password as **Weak**, **Medium**, or **Strong**.

---

# Problem Statement

Weak passwords remain one of the leading causes of unauthorized account access. Many users create passwords that lack the required complexity, making them vulnerable to brute-force and dictionary attacks.

This project provides a simple rule-based solution to evaluate password strength and encourage better password creation practices.

---

# Tools and Technologies

| Tool | Purpose |
|------|---------|
| Python 3.14.6 | Programming language |
| Python IDLE / Command Prompt | Code execution and testing |
| Windows | Development environment |

---

# Methods

The program follows these steps:

1. Accept user password.
2. Check password length (minimum 8 characters).
3. Check for uppercase letters.
4. Check for numbers.
5. Check for symbols.
6. Calculate security score.
7. Classify password as:
   - Weak
   - Medium
   - Strong
8. Display the result with PASS/FAIL status for each security check.

---

# Project Structure

```text
Password-Strength-Checker/
│
├── CODE-Password_Checker.txt
│
├── OUTPUT-Evaluation.pdf/
│   ├── weak-password.png
│   ├── medium-password.png
│   └── strong-password.png
│
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
```

---

# Key Insights

- Password length is a fundamental security requirement.
- Strong passwords should contain uppercase letters, numbers, and symbols.
- Combining multiple security requirements significantly improves password strength.
- Rule-based validation provides a simple and effective way to assess password complexity.

---

# Output

The application displays:

- Password Strength
- Length Check
- Uppercase Letter Check
- Number Check
- Symbol Check

### Sample Output

```text
======================================
 PASSWORD STRENGTH CHECKER
======================================

Enter your password: Password@123

========== RESULT ==========
Password Strength: STRONG

Security Checks:
Length (8+ characters): PASS
Uppercase Letter: PASS
Number: PASS
Symbol: PASS
============================
```

---

# How to Run This Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Password-Strength-Checker.git
```

### 2. Navigate to the project folder

```bash
cd Password-Strength-Checker
```

### 3. Run the Python program

```bash
python src/password_strength_checker.py
```

### 4. Enter a password

The program will evaluate the password and display whether it is **Weak**, **Medium**, or **Strong**.

---

# Future Work

- Detect commonly used or leaked passwords.
- Require lowercase letter validation.
- Provide suggestions for improving weak passwords.
- Add a graphical password strength indicator.
- Implement secure password hashing for real-world applications.

---

# Final Recommendations

- Use passwords with at least eight characters.
- Include uppercase letters, numbers, and symbols.
- Avoid simple or predictable passwords.
- Regularly update passwords for better security.
- Never store passwords in plain text in real-world applications.

---

# Author & Contact

**Author:** Fatima

**Project:** Password Strength Checker

**Internship:** Cyber Security Internship

**LinkedIn:** linkedin.com/in/fatima-taufique-1313b633b
