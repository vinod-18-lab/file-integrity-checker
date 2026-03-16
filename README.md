# FILE-INTEGRITY-CHECKER

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: VINOD KUMAR

*INTERN ID*: CTIS6525

*DOMAIN*: CYBER SECURITYY & ETHICAL HACKING

*DURATION*: 4 WEEKS

*MEENTOR*: NELLA SANTHOSH




---

#File Integrity Checker#

Project Overview

The File Integrity Checker is a Python-based security tool that monitors files and detects any unauthorized modifications. It works by generating a unique hash value for a file and comparing it with a previously stored hash value. If the file content changes, the hash value also changes, which helps identify whether the file has been altered.

This project demonstrates how cryptographic hashing techniques can be used to verify file integrity and ensure that important files remain unchanged.


---

Objectives

To detect changes or tampering in files.

To ensure the integrity and authenticity of stored data.

To demonstrate the use of cryptographic hashing in cybersecurity.

To build a simple command-line security tool using Python.



---

Features

Generates a unique hash value for a selected file.

Stores the generated hash value for future verification.

Compares current file hash with stored hash.

Detects if a file has been modified or tampered with.

Simple command-line interface for easy use.

Fast and efficient integrity checking.

Helps maintain file security and reliability.



---

Technologies Used

Programming Language: Python

Hashing Library: hashlib

Hash Algorithm: SHA-256

Development Environment: Visual Studio Code

Version Control: GitHub



---

Project Files

The project contains the following files:

file_integrity_checker.py
Main Python script that generates and checks hash values.

hash_store.txt
Stores the original hash value of files.

sample.txt
A sample file used for testing file integrity.

README.md
Documentation explaining the project.



---

Working Process

Step 1: Generate Hash

The user selects the option to generate a hash.

The program reads the selected file.

A hash value is generated using SHA-256.

The hash value is stored in hash_store.txt.


Step 2: Verify File Integrity

The user selects the integrity check option.

The program generates a new hash value for the file.

The new hash is compared with the stored hash.


Step 3: Display Result

If both hash values match → File is unchanged.

If hash values differ → File has been modified.



---

Advantages

Detects unauthorized file modifications.

Ensures file integrity and reliability.

Simple and lightweight implementation.

Demonstrates practical cybersecurity concepts.

Easy to run in any Python environment.



---

Conclusion

The File Integrity Checker is a simple yet effective security tool that verifies whether files have been modified. By using cryptographic hash functions, the program ensures that any change in file content can be quickly detected. This project provides a basic understanding of file integrity monitoring and demonstrates how hashing techniques are used in cybersecurity applications.

#OUTPUT#
<img width="962" height="620" alt="Image" src="https://github.com/user-attachments/assets/1fdcd36f-75a7-4836-a9d5-5fd0038410fe" />
