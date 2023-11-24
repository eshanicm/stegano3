import cv2
import os
import string
import sys

dictionary = {}
c = {}
for i in range(255):
    dictionary[chr(i)] = i
    c[i] = chr(i)


def Encrypt():
    key_length = 0
    length = len(message)
    n = 0
    m = 0
    z = 0

    for i in range(length):
        image[n, m, z] =dictionary[message[i]]^dictionary[password[key_length]]
        n = n + 1
        m = m + 1
        m = (m + 1) % 3
        key_length = (key_length + 1) % len(password)
    cv2.imwrite("Encrypted_image.jpg", image)
    os.startfile("Encrypted_image.jpg")
    print("Encryption Done \n")
    print("Thank You!")


def Decrypt(encrypted_image, password, length):
    key_length = 0
    n = 0
    m = 0
    z = 0
    decode = ""
    for i in range(length):
        decode += c[image[n, m, z] ^ dictionary[password[key_length]]]
        n = n + 1
        m = m + 1
        m = (m + 1) % 3
        key_length = (key_length + 1) % len(password)
    print("Decrypted text:", decode)
    print("Thank You!")


while True:
    print(" ----------- Menu ------------\n")
    print("Enter to Encrypt message\n to Decrypt message\n to Exit\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        image = cv2.imread("Image.jpg")
        pointer1 = image.shape[0]
        pointer2 = image.shape[1]
        password = input("Enter the Password to encrypt: ")
        message = input("Enter the message:")
        Encrypt()
    elif choice == 2:
        image_path = "Encrypted_new.jpg"
        encrypted_image = cv2.imread(image_path)
        password = input("Enter the password to decrypt: ")
        length = len(message)
        Decrypt(encrypted_image, password, length)
    elif choice == 3:
        sys.exit(0)