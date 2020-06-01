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
        with open(TargetFile, "r") as f:
            for x in f:
                text += str(x)
    except FileNotFoundError:
        mb.showerror("File not found","No file created yet. Click 'Add password' to automatically create file.")
    else:
        pwWindow = tk.Toplevel()
        pwWindow.title("Stored passwords")
        labelExample = tk.Label(pwWindow, text = "New Window")
        
        Text = tk.Text(pwWindow)
        Text.pack()
        Text.insert(tk.END, text)

                
    

def AddPassword(): #Allows user to add info about domain,user and PW. Creates file if it does not exist

    addpw = tk.Toplevel()
    addpw.title("Add password")
    addpw.geometry("250x150")

    def submitData():
        xget = str(x.get())
        yget = str(y.get())
        zget = str(z.get())
        f = open(TargetFile, "a")
        f.write("Domain: " + xget + '   ')
        f.write("User: " + yget + '   ')
        f.write("Password: " + zget + "\n")
        addpw.destroy()

    def close():
       addpw.destroy()
    

    tk.Label(addpw, text = "Domain: ").grid(row = 1, column = 0)
    x = tk.Entry(addpw)
    x.grid(row = 1, column = 2)
    
    tk.Label(addpw, text = "User: ").grid(row = 2, column = 0)
    y = tk.Entry(addpw)
    y.grid(row = 2, column = 2)

    tk.Label(addpw, text = "Password: ").grid(row = 3, column = 0)
    z = tk.Entry(addpw)
    z.grid(row = 3, column = 2)
    
    submit = tk.Button(addpw, text = "Submit", fg="red", command = submitData)
    submit.grid(row = 4, column = 0)
    close = tk.Button(addpw, text = "Close", fg="red", command = close)
    close.grid(row = 4, column = 2)

def ClearFile(): #Completely deletes target file

    msgAnswer = mb.askquestion('Clear file?', 'Are you sure you want to clear file?')
    if msgAnswer == 'yes':
        try: 
            os.remove(TargetFile)
            mb.showinfo("","Passwords deleted!")
        except FileNotFoundError:
            mb.showinfo("File not found","No file created yet. Click 'Add password' to automatically create file.")
        
    else:
        mb.showinfo("","Going back to main menu ... ")
    

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

root = tk.Tk()
root.title("Password Saver App")
root.geometry("250x150") #Width x Height

frame = tk.Frame(root)
frame.place(relx = 0.1, rely = 0.1, relheight = 0.8, relwidth = 0.8)


opt1 = tk.Button(frame, 
                   text="1. See list of stored passwords", 
                   fg="red",
                   command = ShowPassword)
opt2 = tk.Button(frame,
                   text="2. Add password", 
                   fg="red",
                   command = AddPassword)
opt3 = tk.Button(frame, 
                   text="3. Clear passwords", 
                   fg="red",
                   command = ClearFile)
# opt4= tk.Button(frame, 
#                    text="4. Encrpyt file", 
#                    fg="red",
#                    command = EncryptFile)
# opt5 = tk.Button(frame, 
#                    text="5. Decrypt file", 
#                    fg="red",
#                    command = DecryptFile)
opt6 = tk.Button(frame, 
                   text="Quit ", 
                   fg="red",
                   command = root.quit)

opt1.pack(fill=tk.X, padx = 10)
opt2.pack(fill=tk.X, padx = 10)
opt3.pack(fill=tk.X, padx = 10)
# opt4.pack(fill=tk.X, padx = 10)s
# opt5.pack(fill=tk.X, padx = 10)
opt6.pack(fill=tk.X, padx = 10)

root.mainloop()
          