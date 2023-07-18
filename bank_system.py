class bank:
    
    total_deposits = 0
    total_withdraws = 0
       
    def __init__(self, name, password, age, gender,balance):
        self.name = name
        self.password = password
        self.age = age
        self.gender = gender
        self.balance = balance
    
    def account_info(self):
        print("------------------------------------------")
        print("Personal Details: " )
        print("")
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Gender: {}".format(self.gender))
        print("account balance : ${}".format(self.balance))
        print("------------------------------------------")
          
    def deposit(self):
        print("------------------------------------------")
        while True:
            try:    
                db = float(input(f"{self.name}, please enter how much you want to deposit: "))
                if db < 0:
                    print("please enter a positive value")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")
        self.balance = float(self.balance)
        self.balance += db
        self.total_deposits += 1
        print("------------------------------------------")
        print("thank you for depositing...")
        print(f"Account balance has been updated to : ${self.balance}")
        print("------------------------------------------")
    
    def withdraw(self):
        print("------------------------------------------")
        while True:
            self.balance = float(self.balance)
            try:    
                wd = float(input(f"{self.name}, please enter how much you want to withdraw: "))
                if wd < 0:
                    print("please enter a positive value")
                elif self.balance < wd:
                    print("you can\'t withdraw that amount") 
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")
        self.balance = self.balance - wd 
        self.total_withdraws += 1        
        print("------------------------------------------")                   
        print("thank you for withdrawing...")    
        print(f"Account balance has been updated to : ${self.balance}")
        print("------------------------------------------")
    
    def T_deposits(self):
        return self.total_deposits
        
    def T_withdraws(self):
        return self.total_withdraws

    def data(self):
        
        with open('database.txt', 'r') as file:
            records = file.readlines()
            
            for i, record in enumerate(records):
                if record.startswith(self.name):
                    records[i] = f"{self.name}, {self.password}, {int(self.age)}, {self.gender}, {float(self.balance)}\n"

        with open('database.txt', 'w') as file:
            file.writelines(records)
            file.close()
    def transfer(self):
        with open('database.txt', 'r') as file:
            users = {}
            for line in file:
                name, password, age, gender, balance = line.strip().split(", ")
                users[name] = bank(name, password, age, gender, balance)
            
            receiver_name = input("Please enter the username of the person you want to send to: ")
            if receiver_name in users:
                receiver = users[receiver_name]
                receiver.balance = float(receiver.balance)
                self.balance = float(self.balance)
                while True:
                    try:
                        amount = float(input(f"{self.name}, please enter the amount you want to send: "))
                        if amount < 0:
                            print("please enter a positive value")
                        elif amount > self.balance:
                            print("You don't have enough balance to send this amount.")
                        else:
                            break
                    except ValueError:
                        print("Please enter a valid number.")
                self.balance -= amount
                receiver.balance += amount
                users[receiver_name].data()
                print("------------------------------------------")
                print(f"${amount} has been sent to {receiver.name}")
                print(f"{self.name}'s account balance has been updated to: ${self.balance}")
                print("------------------------------------------")
            else:
                print("Username incorrect or does not exist.")
                self.transfer()
        file.close()

def option(user):
    options = {
        1: user.account_info,
        2: user.withdraw,
        3: user.deposit,
        4: lambda: print(f"------------------------------------------\nThere have been {user.T_withdraws()} withdraws\n------------------------------------------"),
        5: lambda: print(f"------------------------------------------\nThere have been {user.T_deposits()} deposits\n------------------------------------------"),
        6: user.transfer,
        7: lambda: print("------------------------------------------\nThank you for using our bank\n------------------------------------------") and False
    }
    print("------------------------------------------")
    print("thank you for creating your bank account\nHere are a list of options, please choose the number you want")
    print("------------------------------------------")
    while True:
        try:
            choice = int(input("please choose a number:\n1) account balance\n2) withdraw\n3) deposit\n4) total_withdraws\n5) total_deposits\n6) transfert\n7) Quit\n:"))
            if choice not in options:
                print("------------------------------------------") 
                print("please choose a number from 1-7")
                print("------------------------------------------") 
                continue
            options[choice]()
            if choice == 2 or choice == 3 or choice == 6:
                user.data()
            if choice == 7:
                break
        except ValueError:
            print("------------------------------------------")
            print("Invalid input. Please enter an integer.")
            print("------------------------------------------")    
         
# register in
def register():
    database = open("database.txt", "r")
    username = input("create username: ")
    password = input("create password: ")
    cpassword = input("confirm password: ")

    for line in database:
        if username in line :
            print("username exists")
            register()
        else:
            if " " in username:
                print("you can't use space in your name")
                register()
            else:    
                break

        
    if password != cpassword:
        print ("password don't match, restart")
        register()
                
    elif len(password) <= 6 :
        print("password too short,restart")
        register()

    else:
                
        while True:
            try:
                age = int(input("Please enter your age: "))
                break
            except ValueError:
                continue
        while True:        
            try:
                gender = str(input("please enter your gender (M: for Male or F: for Female ):  "))
                if gender == 'M' or gender == 'm' or gender == 'F' or gender == 'f':
                    gender = gender.upper()
                    break
                else:
                    continue        
            except ValueError:
                continue
                        
        while True:           
            try:
                balance = float(input("please enter your balance: "))
                break
            except ValueError:
                continue
                    
        database = open("database.txt","a")
        database.write(username +", "+password+", "+str(age)+", "+str(gender)+", "+str(balance)+"\n")
        print("------------------------------------------") 
        print("success!")
        print("------------------------------------------")
        database.close()
        access() 
        
      
     
def access():
    with open('database.txt', 'r') as file:
        users = {}
        P_list = {}
        for line in file:
            name, password, age, gender, balance = line.strip().split(", ")
            P_list.update({name : password})     
            users[name] = bank(name, password, age, gender, balance)
    while True:
        username = input("enter username: ")
        password = input("enter password: ")
        if len(username) < 1 or len(password) < 1:
            print("username or password cannot be empty")
        else:
            if username in P_list:
                if password == P_list[username]:
                        print("Login success")
                        print("Hi! ",username)
                        user_0 = users[username]
                        file.close()
                        option(user_0)
                        break
                else: 
                    print("password incorrect")    
            else:
                print("username incorrect or does not exist")


def home(option = None):
    option = input("login | signup:")
    if option == "login" :
        access()
    elif option == "signup":
        register()  
    else:
        print("please choose an option ")
        home()

home()
