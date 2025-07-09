#things to add anyone who runs the command A() should be noticedimport time
import getpass
import socket
import time
import hashlib

# Load users from file

###

###     
def load_users():
    users = {}
    try:
        with open("users.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) ==2:
                    username, password= parts
                    
                #username, password = line.strip().split(",")
                    users[username] = password
                else:
                    print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        pass
    return users
###

users = load_users()

# Get IP
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

pc_user = getpass.getuser()
hostname = socket.gethostname()
ip = get_local_ip()

# Login function

def E():
    tries = 0
    #password = getpass.getpass("Password: ")#!
    while tries < 3:
        username = input("Username")
        time.sleep(1)
        password = getpass.getpass("Password: ")
        hashed_input = hashlib.sha256(password.encode()).hexdigest()

        if username in users and users[username] == hashed_input:
            print("Access allowed")
            time.sleep(1)
            with open("login_log.txt", "a") as file:
                file.write(f"{username} logged in at {time.ctime()}\n"
                           f"From PC user: {pc_user}, Host: {hostname}, IP: {ip}\n\n")
            B(username)
            return
        else:
            print("Check if username or password is correct")
            tries += 1

    print("Access denied ")

    

# Welcome screen
def B(username):
    print(f"Welcome {username}")
    C()
#add a manger password for view_user
# Menu 2
def C():
    time.sleep(2)
    print("What would you like?")
    time.sleep(1)
    print("1 view secret, 2 users, 3 exit")
    time.sleep(1)

    x = input("Choice 1 2 or 3 ")
    if x == "1":
        print("nothing")
        time.sleep(6)
        C()
        #speaicle
        
        
    elif x == "2":
        """
        g = getpass.getpass("password")
        if hashed_g == MANAGER_HASH:
        """
        # Manager password hash (for "AAAA")
        manager_password = "AAAA"
        MANAGER_HASH = hashlib.sha256(manager_password.encode()).hexdigest()
        g = getpass.getpass("Manager password: ")
        hashed_g = hashlib.sha256(g.encode()).hexdigest()
        if hashed_g == MANAGER_HASH:
          
         
          time.sleep(1)
          print("Correct password")
          time.sleep(1)
          print("Welcome Manger")
          time.sleep(1)
          print(users)
          time.sleep(6)
          C()
        else:
          
          time.sleep(1)
          print("Wrong Password")
          time.sleep(1)
          C()
    elif x == "3":
        print("exited")
        time.sleep(1)
    else:
        time.sleep(1)
        print("Invalid")
        time.sleep(3)
        C()

# Main function
def A():
    global users  
#this part should save who ever make the code run but to know who is not possible
    with open("enabled the command.txt", "a") as file:
        file.write(f"someone started this command {time.ctime()}\n"
                   f"From PC user: {pc_user}, Host: {hostname}, IP: {ip}\n\n")
    
        time.sleep(1)
        print("Would you like to register or log in")
        time.sleep(2)
        y = input("1 Log-in, 2= Register, 3= Exit ")

    if y == "1":
         E()
       #register part
    elif y == "2":
         
         new_user = input("Username ")
         #new_pass = getpass.getpass("Password: ")#!
         
         #---
         if new_user in users:
             print("this username exist try agin")  
             A()
             return
         
             #_
         new_pass = getpass.getpass("Password: ")#!
         hashed_pass = hashlib.sha256(new_pass.encode()).hexdigest()
         with open("users.txt", "a") as file:
                 file.write(f"{new_user},{hashed_pass}\n") 
             #_
         users = load_users()  # reload users from file
         print("Registered.")
         A()

    elif y == "3":  
         print("exited")
         
    else:
         print("Your choices are 1, 2 or 3")
         A()

users = load_users()
A()

