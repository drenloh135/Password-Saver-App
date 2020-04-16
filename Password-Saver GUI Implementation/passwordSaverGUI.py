import os 
import os.path
from os import path
import cryptography
from cryptography.fernet import Fernet #Symmetric encrpytion is done here
import tkinter as tk
from tkinter import messagebox as mb

OutputFile = 'test.encrypted' #For encryption purposes
TargetFile = "PasswordSaver.txt" #Target file to be used
#File = "PasswordSaverReal.txt"
init = 0 #flow control


def GenerateKey(): #Ensures key is created/ready when app is launched
    if path.exists('Filekey.key'): #Checks if key alr exists, so as not to replace existing key
        mb.showinfo('Key is ready!')
        print("Key is ready\n")
    else:
        CrpytKey = Fernet.generate_key()
        file = open('FileKey.key', 'wb')
        file.write(CrpytKey)
        file.close()
        print("Key has been generated\n")
    file = open('FileKey.key', 'rb')
    Key = file.read()
    file.close()
    return Key    #Key is returned in bytes

        

def ShowPassword(): #Shows a list of passwords stored
    #mb.showinfo('Showing you a list of passwords saved ...')
    text = ''
    try:
        pwWindow = tk.Toplevel()
        pwWindow.title("Stored passwords")
        labelExample = tk.Label(pwWindow, text = "New Window")
        with open(TargetFile, "r") as f:
            for x in f:
                text += str(x)
        Text = tk.Text(pwWindow)
        Text.pack()
        Text.insert(tk.END, text)

                
    except FileNotFoundError:
        mb.showerror("No file created yet. Add password to automatically create file.")

def AddPassword(): #Allows user to add info about domain,user and PW. Creates file if it does not exist
    # print("What is the domain?")
    # domain = input()
    # print("What is the user/email you're using?")
    # user = input()
    # print("What is the password?")
    # pw = input()
    addpw = tk.Toplevel()
    addpw.title("Add password")
    addpw.geometry("200x200")

    # def makeEntry(parent,caption):
    #     lab = tk.Label(parent,caption)
    #     lab.pack()
    #     value = tk.Entry(parent)
    #     value.pack()
    #     # value.delete(0,tk.END)
    #     # value.insert(0,caption)
    #     return value.get()
    
    def makeEntry(parent, caption):
        
        tk.Label(parent, caption).pack()
        entry = tk.Entry(parent).pack()
        return entry.get()

    
    domain = makeEntry(addpw,"Domain: ")

    # user = makeEntry(addpw, 'User: ')
    # pw = makeEntry(addpw, 'Password: ')

    with open(TargetFile, "a") as f:
        
        f.write("Domain: " + domain + '   ')
        # f.write("User: " + user + '   ')
        # f.write("Password: " + pw + "\n")
        
        print("Your infomation has been saved! \n")

def ClearFile(): #Completely deletes target file
    print("Are u sure? No going back after this!\n")
    print("1. Yes  2. No\n")
    ans = input()
    try:
        if int(ans) == 1:
            try: 
                os.remove(TargetFile)
                print("\nPasswords deleted \n")
            except FileNotFoundError:
                print("File hasn't beeen created yet \n")
        else:
            print("Going back to main menu ... \n")
    except ValueError:
        print("Please type either 1 or 2. Returning you back to the main menu ...\n")

def EncryptFile(): #Encrypts file and saves it as test.encrypted
    global TargetFile
    global OutputFile
    global Key

    with open(TargetFile, 'rb') as f:
        data = f.read()
    fernet = Fernet(Key)
    encrypted = fernet.encrypt(data)
    open(OutputFile, 'x')
    with open(OutputFile,'wb') as f:
        f.write(encrypted)

def DecryptFile(): #Decrypts test.encrypted and outputs in decrypted.txt
    global TargetFile
    global OutputFile
    global Key
    
    with open(OutputFile, 'rb') as f:
        data = f.read()
    fernet = Fernet(Key)
    decrypted = fernet.decrypt(data)
    with open('decrypted.txt', 'wb') as f:
        f.write(decrypted)
    
# while (1):
#     if init == 0:
#         Key = GenerateKey()
#         init = 1
    
#     print("What would u like to do today?")
#     print("1. See list of stored passwords")
#     print("2. Add password")
#     print("3. Clear passwords")
#     print("4. Encrpyt file")
#     print("5. Decrypt file")
#     print("6. Exit application\n")
#     choice = int(input())
#     try:
#         if choice == 1:
#             ShowPassword()
            
#         elif choice == 2:
#             AddPassword()
            
#         elif choice == 3:
#             ClearFile()
            
#         elif choice == 4:
#             EncryptFile()
        
#         elif choice == 5:
#             DecryptFile()

#         elif choice == 6:
#             break
#         else:
#             print("There was a error. Pls try again")
#     except ValueError:
#         print("Please enter either 1,2,3 or 4! \n")
        