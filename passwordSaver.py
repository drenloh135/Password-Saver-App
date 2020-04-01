import os 

def ShowPassword():
    print("Showing you a list of passwords saved ...\n")
    try:
        with open("PasswordSaver.txt", "r") as f:
            for x in f:
                print(x)
    except FileNotFoundError:
        print("No file created yet. Add password to automatically create file.\n")

def AddPassword():
    print("What is the domain?")
    domain = input()
    print("What is the user/email you're using?")
    user = input()
    print("What is the password?")
    pw = input()

    with open("PasswordSaver.txt", "a") as f:
        
        f.write("Domain: " + domain + '   ')
        f.write("User: " + user + '   ')
        f.write("Password: " + pw + "\n")
        
        print("Your infomation has been saved! \n")

def ClearFile():
    print("Are u sure? No going back after this!\n")
    print("1. Yes  2. No\n")
    ans = input()
    try:
        if int(ans) == 1:
            try: 
                os.remove("PasswordSaver.txt")
                print("\nPasswords deleted \n")
            except FileNotFoundError:
                print("File hasn't beeen created yet \n")
        else:
            print("Going back to main menu ... \n")
    except ValueError:
        print("Please type either 1 or 2. Returning you back to the main menu ...\n")
    

while (1):
    print("What would u like to do today?")
    print("1. See list of stored passwords")
    print("2. Add password")
    print("3. Clear passwords")
    print("4. Exit application\n")
    choice = int(input())
    try:
        if choice == 1:
            ShowPassword()
            
        elif choice == 2:
            AddPassword()
            
        elif choice == 3:
            ClearFile()
            
        elif choice == 4:
            break
        else:
            print("There was a error. Pls try again")
    except ValueError:
        print("Please enter either 1,2,3 or 4! \n")
        