import tkinter as tk
import passwordSaverGUI as pws


root = tk.Tk()
root.title("Password Saver App")
root.geometry("250x200") #Width x Height

frame = tk.Frame(root)
frame.place(relx = 0.1, rely = 0.1, relheight = 0.8, relwidth = 0.8)


opt1 = tk.Button(frame, 
                   text="1. See list of stored passwords", 
                   fg="red",
                   command=pws.ShowPassword)
opt2 = tk.Button(frame,
                   text="2. Add password", 
                   fg="red",
                   command=pws.AddPassword)
opt3 = tk.Button(frame, 
                   text="3. Clear passwords", 
                   fg="red",
                   command=pws.ClearFile)
opt4= tk.Button(frame, 
                   text="4. Encrpyt file", 
                   fg="red",
                   command=pws.EncryptFile)
opt5 = tk.Button(frame, 
                   text="5. Decrypt file", 
                   fg="red",
                   command=pws.DecryptFile)
opt6 = tk.Button(frame, 
                   text="Quit ", 
                   fg="red",
                   command = root.quit)

opt1.pack(fill=tk.X, padx = 10)
opt2.pack(fill=tk.X, padx = 10)
opt3.pack(fill=tk.X, padx = 10)
opt4.pack(fill=tk.X, padx = 10)
opt5.pack(fill=tk.X, padx = 10)
opt6.pack(fill=tk.X, padx = 10)

root.mainloop()
          