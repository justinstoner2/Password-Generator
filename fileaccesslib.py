from cryptography.fernet import Fernet
import random
import subprocess, sys

character_dictionary = {0: "`", 1: "!", 2: "@", 3: "#", 4: "$", 5: "%", 6: "^", 7: "&", 8: "*", 9: "(", 10: "-",
                        11: "_",
                        12: "=", 13: "+", 14: "{", 15: "[", 16: "}", 17: "]", 18: "q", 19: "w", 20: "e", 21: 'r',
                        22: "t", 23: 'y', 24: 'u',
                        25: 'i', 26: 'o', 27: 'p', 28: 'a', 29: 's', 30: 'd', 31: 'f', 32: 'g', 33: 'h', 34: 'j',
                        35: 'k', 36: 'l', 37: 'z',
                        38: 'x', 39: 'c', 40: 'v', 41: 'b', 42: 'n', 43: 'm', 44: 'Q', 45: 'W', 46: 'E', 47: 'R',
                        48: 'T', 49: 'Y', 50: 'U',
                        51: 'I', 52: 'O', 53: 'P', 54: 'A', 55: 'S', 56: 'D', 57: 'F', 58: 'G', 59: 'H', 60: 'J',
                        61: 'K', 62: 'L', 63: 'Z',
                        64: 'X', 65: 'C', 66: 'V', 67: 'B', 68: 'N', 69: 'M', 70: '0', 71: '1', 72: '2', 73: '3',
                        74: '4', 75: '5', 76: '6',
                        77: '7', 78: '8', 79: '9'}



def encrypt_file(str):
    key = Fernet.generate_key()
    with open("filekey.key", 'wb') as filekey:
        key = filekey.write(key)
    with open('filekey.key','rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open(str,'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(str, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)



def decrypt_file(str):
    with open("filekey.key", 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open(str,"rb") as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(str,'wb') as dec_file:
        dec_file.write(decrypted)

def print_passwords():
    try:
        decrypt_file("mypasswords.txt")
    except:
        print("no passwords set")
    current_passwords = {}
    with open("mypasswords.txt", 'r') as file:
        for line in file:
            stripped_line = line.strip('\n')
            key, value = stripped_line.split("\t")
            current_passwords[key] = value
    print(current_passwords)
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, "/Users/justinstoner/PycharmProjects/Password generator/mypasswords.txt"])
    input()
    encrypt_file("mypasswords.txt")

def newPassword():
    try:
        decrypt_file("mypasswords.txt")
    except:
        pass

    current_passwords = {}
    with open("mypasswords.txt",'r') as file:
        for line in file:
            stripped_line = line.strip('\n')
            key, value = stripped_line.split("\t")
            current_passwords[key] = value
    create_new_password(current_passwords)
    with open("mypasswords.txt", "w") as file:
        for key, value in current_passwords.items():
            file.write(key + "\t" + value + "\n")
    encrypt_file("mypasswords.txt")



def create_new_password(password_dict):
    password_key = input("what is this password for?: ")
    new_password_array = [0] * 20
    new_password = []
    for i in new_password_array:
        i = random.randint(0, 79)
        new_password.append(character_dictionary[i])
    password_dict[password_key] = "".join(new_password)

def get_passwords():
    try:
        decrypt_file("mypasswords.txt")
    except:
        pass
    current_passwords = {}
    with open("mypasswords.txt",'r') as file:
        for line in file:
            stripped_line = line.strip('\n')
            key, value = stripped_line.split("\t")
            current_passwords[key] = value
    return current_passwords

def change_password():
    print_passwords()
    password_dict = get_passwords()
    inKey=True
    while inKey==True:
        key = input("Enter the key you want the password changed for")
        if key in password_dict:
            inKey=False
        else:
            print("key not in database")
    new_password_array = [0] * 20
    new_password = []
    for i in new_password_array:
        i = random.randint(0, 79)
        new_password.append(character_dictionary[i])

    password_dict[key] = "".join(new_password)
    with open("mypasswords.txt", "w") as file:
        for key, value in password_dict.items():
            file.write(key + "\t" + value + "\n")
    encrypt_file("mypasswords.txt")
def delete_password():
    print_passwords()
    password_dict = get_passwords()
    inKey = True
    while inKey == True:
        key = input("Enter the key you want the password deleted for")
        if key in password_dict:
            inKey = False
        else:
            print("key not in database")
    del password_dict[key]
    with open("mypasswords.txt", "w") as file:
        for key, value in password_dict.items():
            file.write(key + "\t" + value + "\n")
    encrypt_file("mypasswords.txt")