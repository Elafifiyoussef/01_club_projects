from tkinter import *
from tkinter import ttk
import tkinter.font as tkfont
#from PIL import Image,ImageTk

class bank:
    
    total_deposits = 0
    total_withdraws = 0
       
    def __init__(self, name, password, age, gender,balance):
        self.name = name
        self.password = password
        self.age = age
        self.gender = gender
        self.balance = balance
        
       
    #-------------------------bank_menu------------------------------
    global bank_menu
    def bank_menu(self):
        menu_window = Toplevel(main)
        menu_window.title("bank menu")
        menu_window.geometry('900x600+150+20')
        menu_window.configure(bg="#EFF3FC")
        menu_window.resizable(False, False)
        frame = Frame(master=menu_window,width=500,height=600,bg="#EFF3FC")
        frame.pack()

        Menu_name = Label(frame,text= "Menu",font=('Louis George Cafe',72),padx=20,pady=10,bg="#EFF3FC")
        Menu_name.pack()

        account_info_frame = Frame(master=frame,width=500,height=50,bg="#EFF3FC")
        account_info_frame.pack()
        
        transfer_frame = Frame(master=frame,width=500,height=50,bg="#EFF3FC")
        transfer_frame.pack()
        
        deposit_frame = Frame(master=frame,width=500,height=50,bg="#EFF3FC")
        deposit_frame.pack()
        
        withdraw_frame = Frame(master=frame,width=500,height=50,bg="#EFF3FC")
        withdraw_frame.pack()
        
        log_out_frame = Frame(master=frame,width=500,height=50,bg="#EFF3FC")
        log_out_frame.pack()
        
        account_info_button = button(transfer_frame,"user info",'Louis George Cafe',20,17,"#F4F7FF","#325BFF",self.account_info,3,5,'top')
        
        transfer_button = button(transfer_frame,"transfer",'Louis George Cafe',20,17,"#F4F7FF","#325BFF",self.transfer,3,5,'top')
        
        deposit_button = button(deposit_frame,"deposit",'Louis George Cafe',20,17,"#F4F7FF","#325BFF",self.deposit,3,5,'top')
        
        withdraw_button = button(withdraw_frame,"withdraw",'Louis George Cafe',20,17,"#F4F7FF","#325BFF",self.withdraw,3,5,'top')
        
        log_out_button = button(log_out_frame,"log out",'Louis George Cafe',20,17,"#E74C3C","#EFF3FC",menu_window.destroy,0,30,'bottom')


    #-------------------------account_info------------------------------ 
    def account_info(self):
        info_window = Toplevel(main)
        info_window.title("account info")
        info_window.geometry('900x600+150+20')
        info_window.configure(bg="#EFF3FC")
        info_window.resizable(False, False)

        frame = Frame(master=info_window,width=300,height=600,bg="#EFF3FC")
        frame.pack()

        login_title = Label(frame,text= "account info",font=('Louis George Cafe',30),padx=20,pady=30,bg="#EFF3FC")
        login_title.pack()
        
        frame2 = Frame(master=frame,width=300,height=400,background="#EFF3FC") 
        frame2.pack()
        
        username_frame = LabelFrame(master=frame2,text="Username",font=('Louis George Cafe',12),width=250,height=50,bg="#EFF3FC")
        age_frame = LabelFrame(master=frame2,text="age",font=('Louis George Cafe',12),width=250,height=50,bg="#EFF3FC")
        gender_frame = LabelFrame(master=frame2,text="gender",font=('Louis George Cafe',12),width=250,height=50,bg="#EFF3FC")
        balance_frame = LabelFrame(master=frame2,text="balance",font=('Louis George Cafe',12),width=250,height=50,bg="#EFF3FC")
        
        username_frame.pack(padx=20,pady=5)
        age_frame.pack(padx=20,pady=5)
        gender_frame.pack(padx=20,pady=5)
        balance_frame.pack(padx=20,pady=5)

        
        username = Label(username_frame,text=self.name,font=('Louis George Cafe',12),width=50)
        age = Label(age_frame,text=self.age,font=('Louis George Cafe',12),width=50)
        male_button = Label(gender_frame,text=self.gender,font=('Louis George Cafe',12),width=50)
        balance = Label(balance_frame,text=f"{self.balance} DH",font=('Louis George Cafe',12),width=50)
    
        

        username.pack(padx=5,pady=5)
        age.pack(padx=5,pady=5)
        male_button.pack(padx=5,pady=2)
        balance.pack(padx=5,pady=5)
        back_button = button(frame,"Back",'Louis George Cafe',12,10,"#E74C3C","#EFF3FC",info_window.destroy,50,30,"bottom")


    #-------------------------data_saver------------------------------
    
    def data_saver(self):
        
        with open('database.txt', 'r') as file:
            records = file.readlines()
            
            for i, record in enumerate(records):
                if record.startswith(self.name):
                    records[i] = f"{self.name}, {self.password}, {int(self.age)}, {self.gender}, {float(self.balance)}\n"

        with open('database.txt', 'w') as file:
            file.writelines(records)
            file.close()
    
    #-------------------------transfer------------------------------
    def transfer(self):
        def check_transfer(check_recever_name,
                            check_amount,
                            error_name,
                            error_amount):
            
            with open('database.txt', 'r') as file:
                v1 = 0
                v2 = 0
                users = {}
                for line in file:
                    name, password, age, gender, balance = line.strip().split(", ")
                    users[name] = bank(name, password, age, gender, balance)
    
                if check_recever_name in users:
                    if check_recever_name == self.name:  
                        error_name.config(text="you are not enable to send to this user",font=('Louis George Cafe',12))
                        receiver_name.delete(0,END)
                        
                    else:
                        error_name.config(text="",font=('Louis George Cafe',12))
                        receiver = users[check_recever_name]
                        receiver.balance = float(receiver.balance)
                        self.balance = float(self.balance)
                        v1 = 1
                else:
                    error_name.config(text= "username doesn\'t exist",font=('Louis George Cafe',12))
                    receiver_name.delete(0,END)
            
                try:
                    check_amount = float(check_amount)
                            
                    if check_amount < 0:
                        error_amount.config(text= "please enter a positive value",font=('Louis George Cafe',12))
                        amount.delete(0,END)
                    
                    elif check_amount > self.balance:
                        error_amount.config(text= "You don't have enough balance to send this amount",font=('Louis George Cafe',12))
                        amount.delete(0,END)
                        
                    else:
                        error_amount.config(text= "",font=('Louis George Cafe',12))
                        v2 = 1
                        
                except ValueError:
                    error_amount.config(text= "Please enter a valid number",font=('Louis George Cafe',12))

                if v1 == 1 and v2 == 1 :
                    self.balance -= check_amount
                    receiver.balance += check_amount
                    users[check_recever_name].data_saver()
                    self.data_saver()
                    message.config(text=f"{check_amount} DH has been sent to {check_recever_name}",font=('Louis George Cafe',12) )
                    balance_message.config(text=f"{self.name}'s account balance has been updated to: {self.balance} DH",font=('Louis George Cafe',12))
                    file.close()
                    
            
        transfer_window = Toplevel(main)
        transfer_window.title("transfer")
        transfer_window.geometry('900x600+150+20')
        transfer_window.configure(bg="#EFF3FC")
        transfer_window.resizable(False, False)

        frame = Frame(master=transfer_window,width=400,height=600,bg="#EFF3FC")
        frame.pack()
        
        transfer_title = Label(frame,text= "transfer",font=('Louis George Cafe',40),bg="#EFF3FC",justify="center")
        transfer_title.pack(pady=15)
        
        text = Label(frame,text= "Enter the recever_name and the amount you want to send",font=('Louis George Cafe',12),bg="#EFF3FC",justify="center")
        text.pack(pady=10)
        
        error_name = Label(frame,text= "",font=('Louis George Cafe',12),bg="#EFF3FC",fg="red",justify="center")
        error_name.pack()
        
        receiver_name_frame = LabelFrame(master=frame,width=250,height=50,text="receiver_name",font=('Louis George Cafe',12),bg="#EFF3FC")
        receiver_name_frame.pack(padx=20,pady=10)
        
        receiver_name = Entry(receiver_name_frame,width=50)
        receiver_name.pack(padx=5,pady=5)
        
        error_amount = Label(frame,text= "",font=('Louis George Cafe',12),bg="#EFF3FC",fg="red",justify="center")
        error_amount.pack()
        
        amount_frame = LabelFrame(master=frame,width=250,height=50,text="amount",font=('Louis George Cafe',12),bg="#EFF3FC")
        amount_frame.pack(padx=20,pady=10)
        
        amount = Entry(amount_frame,width=50)
        amount.pack(padx=5,pady=5)
        
        balance_frame = Frame(master=frame,width=250,height=50,bg="#EFF3FC")
        balance_frame.pack(padx=20,pady=30)
        
        message = Label(balance_frame,width=250,text= "",bg="#EFF3FC",font=('Louis George Cafe',12),justify="center")
        message.pack(padx=5,pady=5)
        
        balance_message = Label(balance_frame,width=250,text="",font=('Louis George Cafe',12),bg="#EFF3FC")
        balance_message.pack(padx=5,pady=5)
        
        button_frame = Frame(master=frame,width=400,height=50,bg="#EFF3FC")
        button_frame.pack(padx=5,pady=5)
        
        transfer_button = button(button_frame,"confirm",'Louis George Cafe',12,10,"#F4F7FF","#325BFF",lambda:check_transfer(receiver_name.get(),amount.get(),error_name,error_amount),40,10,"right")
        
        back_button = button(button_frame,"Back",'Louis George Cafe',12,10,"#E74C3C","#EFF3FC",transfer_window.destroy,40,10,"left")

        

    #-------------------------deposit------------------------------
    def deposit(self):
        def check_deposit(check_deposit,error_deposit):
            
            if check_deposit == "" :
                error_deposit.config(text="please enter a value",font=('Louis George Cafe',12))
            else:
                try:
                    check_deposit = float(check_deposit)
                    
                    if check_deposit < 0:
                        error_deposit.config(text="please enter a positive value",font=('Louis George Cafe',12))
                        deposit.delete(0,END)
                    else:
                        error_deposit.config(text="",font=('Louis George Cafe',12))
                        deposit.delete(0,END)
                        self.balance = float(self.balance)
                        self.balance += check_deposit
                        self.total_deposits += 1
                        balance.config(text = f"thank you for depositing...\n{self.name} Account balance has been updated to : {self.balance} DH",font=('Louis George Cafe',12))
                        self.data_saver()
                        
                except ValueError:    
                    error_deposit.config(text="please enter a number",font=('Louis George Cafe',12))
                    deposit.delete(0,END)
                

        
        deposit_window = Toplevel(main)
        deposit_window.title("deposit")
        deposit_window.geometry('900x600+150+20')
        deposit_window.configure(bg="#EFF3FC")
        deposit_window.resizable(False, False)

        frame = Frame(master=deposit_window,width=400,height=600,bg="#EFF3FC")
        frame.pack()
        
        empty_frame = Frame(master=frame,width=300,height=20,bg="#EFF3FC")
        empty_frame.pack()
        
        deposit_title = Label(frame,text= "Deposit",font=('Louis George Cafe',40),bg="#EFF3FC",justify="center")
        deposit_title.pack(pady=15)
        
        text = Label(frame,text= "please enter how much you want to deposit",font=('Louis George Cafe',12),bg="#EFF3FC",justify="center")
        text.pack(pady=15)
        
        error_deposit = Label(frame,text= "",font=('Louis George Cafe',12),bg="#EFF3FC",fg="red",justify="center")
        error_deposit.pack()
        
        deposit_frame = LabelFrame(master=frame,width=250,height=50,text="amount",font=('Louis George Cafe',12),bg="#EFF3FC")
        deposit_frame.pack(padx=20,pady=10)
        
        deposit = Entry(deposit_frame,width=50)
        deposit.pack(padx=5,pady=5)
        
        balance_frame = LabelFrame(master=frame,width=250,height=40,bg="#EFF3FC",border=0)
        balance_frame.pack(padx=20,pady=15)
        
        balance = Label(balance_frame,width=250,height=4,text="",font=('Louis George Cafe',12),bg="#EFF3FC")
        balance.pack(padx=5)
        
        button_frame = Frame(frame,width=300,height=100,bg="#EFF3FC")
        button_frame.pack(padx=5,pady=5)
    
        deposit_button = button(button_frame,"confirm",'Louis George Cafe',14,10,"#F4F7FF","#325BFF",lambda: check_deposit(deposit.get(),error_deposit),21,10,"right")
        
        back_button = button(button_frame,"Back",'Louis George Cafe',14,10,"#E74C3C","#EFF3FC",deposit_window.destroy,21,15,"left")

    #-------------------------withdraw------------------------------
    def withdraw(self):
        def check_withdraw(check_withdraw,error_withdraw):
            
            if check_withdraw == "" :
                error_withdraw.config(text="please enter a value",font=('Louis George Cafe',12))
            else:
                try:
                    check_withdraw = float(check_withdraw)
                    
                    if check_withdraw < 0:
                        error_withdraw.config(text="please enter a positive value",font=('Louis George Cafe',12))
                        withdraw.delete(0,END)
                    else:
                        error_withdraw.config(text="",font=('Louis George Cafe',12))
                        withdraw.delete(0,END)
                        self.balance = float(self.balance)
                        self.balance -= check_withdraw
                        self.total_withdraws += 1
                        balance.config(text = f"thank you for withdrawing...\n{self.name} Account balance has been updated to : {self.balance} DH",font=('Louis George Cafe',12))
                        self.data_saver()
                        
                except ValueError:    
                    error_withdraw.config(text="please enter a number",font=('Louis George Cafe',12))
                    withdraw.delete(0,END)
                    
        withdraw_window = Toplevel(main)
        withdraw_window.title("withdraw")
        withdraw_window.geometry('900x600+150+20')
        withdraw_window.configure(bg="#EFF3FC")
        withdraw_window.resizable(False, False)

        frame = Frame(master=withdraw_window,width=400,height=600,bg="#EFF3FC")
        frame.pack()
        
        empty_frame = Frame(master=frame,width=300,height=20,bg="#EFF3FC")
        empty_frame.pack()
        
        deposit_title = Label(frame,text= "withdraw",font=('Louis George Cafe',40),bg="#EFF3FC",justify="center")
        deposit_title.pack(pady=15)
        
        text = Label(frame,text= "please enter how much you want to withdraw :",font=('Louis George Cafe',12),bg="#EFF3FC",justify="center")
        text.pack(pady=15)
        
        error_withdraw = Label(frame,text= "",font=('Louis George Cafe',12),bg="#EFF3FC",fg="red",justify="center")
        error_withdraw.pack()
        
        withdraw_frame = LabelFrame(master=frame,width=250,height=50,text="amount",font=('Louis George Cafe',12),bg="#EFF3FC")
        withdraw_frame.pack(padx=20,pady=10)
        
        withdraw = Entry(withdraw_frame,width=50)
        withdraw.pack(padx=5,pady=5)
        
        balance_frame = LabelFrame(master=frame,width=250,height=40,bg="#EFF3FC",border=0)
        balance_frame.pack(padx=20,pady=15)
        
        balance = Label(balance_frame,width=250,height=4,text="",font=('Louis George Cafe',12),bg="#EFF3FC")
        balance.pack(padx=5)
        
        button_frame = Frame(frame,width=300,height=100,bg="#EFF3FC")
        button_frame.pack(padx=5,pady=5)
    
        transfer_button = button(button_frame,"confirm",'Louis George Cafe',14,10,"#F4F7FF","#325BFF",lambda: check_withdraw(withdraw.get(),error_withdraw),21,10,"right")
        
        back_button = button(button_frame,"Back",'Louis George Cafe',14,10,"#E74C3C","#EFF3FC",withdraw_window.destroy,21,15,"left")
        

#--------------------------login-----------------------------
def open_login_window():
    with open('database.txt', 'r') as file:
        users = {}
        P_list = {}
        for line in file:
            name_, password_, age_, gender_, balance_ = line.strip().split(", ")
            P_list.update({name_ : password_})     
            users[name_] = bank(name_, password_, age_, gender_, balance_)
      
    def check_login(check_username, check_password, error_name, error_password):

        if len(check_username) < 1 :
            error_name.config(text="please enter your username",font=('Louis George Cafe',12))
        elif check_username not in P_list:
            username.delete(0,END)
            error_name.config(text="username doesn\'t exist",font=('Louis George Cafe',12))   
        else:
            error_name.config(text="",font=('Louis George Cafe',12))
            if len(check_password) < 1 :
                error_password.config(text="please enter your password",font=('Louis George Cafe',12)) 
            elif check_password == P_list[check_username]:
                error_password.config(text="",font=('Louis George Cafe',12)) 
                username.delete(0,END)
                password.delete(0,END)
                user_0 = users[check_username]
                bank_menu(user_0)
                file.close()
                login_window.destroy()
            else: 
                password.delete(0,END)
                error_password.config(text="password incorrect",font=('Louis George Cafe',12)) 
                
    
    login_window = Toplevel(main)
    login_window.title("Login")
    login_window.geometry('900x600+150+20')
    login_window.configure(bg="#EFF3FC")
    login_window.resizable(False, False)

    frame = Frame(master=login_window,width=300,height=600,bg="#EFF3FC")
    frame.pack()
    login_title = Label(frame,text= "Login",font=('Louis George Cafe',40),padx=20,pady=15,bg="#EFF3FC")
    login_title.pack()
    
    frame2 = Frame(master=frame,width=300,height=50,bg="#EFF3FC")
    frame2.pack()
    
    
    error_name = Label(frame,text= "",font=('Louis George Cafe',12),bg="#EFF3FC",fg="red",justify="center")
    error_password = Label(frame,text= "",font=('Louis George Cafe',12),bg="#EFF3FC",fg="red",justify="center")
        
    username_frame = LabelFrame(master=frame,text="Username",font=('Louis George Cafe',12),width=250,height=50,bg="#EFF3FC")
    password_frame = LabelFrame(master=frame,text="Password",font=('Louis George Cafe',12),width=250,height=100,bg="#EFF3FC")
        
    error_name.pack(padx=20,pady=5)    
    username_frame.pack(padx=20,pady=5)
    error_password.pack(padx=20,pady=5)    
    password_frame.pack(padx=20,pady=5)
    
    username = Entry(username_frame,width=50)
    password = Entry(password_frame,width=50,show='•')
    back_button = button(frame,"back",'Louis George Cafe',14,10,"#E74C3C","#EFF3FC",login_window.destroy,20,30,"left")
    login_button = button(frame,"login",'Louis George Cafe',14,10,"#F4F7FF","#325BFF",lambda:check_login(username.get(),password.get(),error_name,error_password),20,30,"right",)
    
    username.pack(padx=5,pady=5)
    password.pack(padx=5,pady=5)

    
    login_window.mainloop()
        
#--------------------------sign_up-----------------------------



def open_sign_up_window():
    
         
    
    def check_sign_up(check_username,
                      check_password,
                      check_copy_password,
                      check_age,
                      check_gender,
                      check_balance):
            
            
        v1 = 0
        v2 = 0
        v3 = 0
        v4 = 0
        
        file = open('database.txt', 'r')     
                   
        if len(check_username) < 1:
            error_name.config(text="please create a username",font=('Louis George Cafe',12))  
            
        elif " " in check_username:
            error_name.config(text="you can't use space in your name",font=('Louis George Cafe',12))
            username.delete(0,END)  
            
        else:
            for line in file:
                if check_username in line :
                    error_name.config(text="username exists",font=('Louis George Cafe',12))
                    username.delete(0,END)
                    break
            else:
                error_name.config(text="",font=('Louis George Cafe',12))
                v1 = 1  
        
        
            
        if len(check_password) <= 6 :
            error_password.config(text="password too short,restart",font=('Louis George Cafe',12))
            password.delete(0,END)
            copy_password.delete(0,END)
                    
        elif check_password != check_copy_password  :
            error_password.config(text="password don't match, restart",font=('Louis George Cafe',12))
            password.delete(0,END)
            copy_password.delete(0,END)
            
        else:
            error_password.config(text="",font=('Louis George Cafe',12))
            v2 = 1
        
        if check_gender == "":
                error_gender.config(text="please choose an option",font=('Louis George Cafe',12))
        else:
            error_gender.config(text="",font=('Louis George Cafe',12))
            v3 = 1 
                     
        if check_balance == "" :
            error_balance.config(text="please enter a value",font=('Louis George Cafe',12))
        else:
            try:
                check_balance = float(check_balance)
                if check_balance < 0:
                    error_balance.config(text="please enter a positive value",font=('Louis George Cafe',12))
                    balance.delete(0,END)
                else:
                    error_balance.config(text="",font=('Louis George Cafe',12))
                    v4 = 1
            except:    
                error_balance.config(text="please enter a number",font=('Louis George Cafe',12))
                balance.delete(0,END)
            
        
        if v1 == 1 and v2 == 1 and v3 == 1 and v4 == 1 :
            file = open("database.txt","a")
            file.write(check_username +", "+check_password+", "+str(check_age)+", "+check_gender+", "+str(check_balance)+"\n")
            file.close()
            
            sign_in_success_window = Tk()
            sign_in_success_window.title()
            sign_in_success_window.geometry('400x150+400+300')
            sign_in_success_window.configure(bg="#EFF3FC")
            sign_in_success_window.resizable(False, False)
            frame = Frame(sign_in_success_window,width=150,height=200,bg="#EFF3FC")
            frame.pack()
            sign_in_message = Label(frame,text= "account created successfully",font=('Louis George Cafe',20),padx=20,pady=15,bg="#EFF3FC")
            sign_in_message.pack()
            login_button = button(sign_in_success_window,"close",'Louis George Cafe',24,10,"#F4F7FF","#325BFF",sign_in_success_window.destroy,20,30,"bottom")
            sign_up_window.destroy()
            sign_in_success_window.mainloop()

    sign_up_window = Toplevel(main)
    sign_up_window.title("sign up")
    sign_up_window.geometry('900x600+150+20')
    sign_up_window.configure(bg="#EFF3FC")
    sign_up_window.resizable(False, False)


    frame = Frame(master=sign_up_window,width=300,height=600,bg="#EFF3FC")
    
    login_title = Label(frame,text= "sign up",font=('Louis George Cafe',40),padx=20,pady=10,bg="#EFF3FC")
    
    error_name = Label(frame,text= "",font=('Louis George Cafe',12),bg="#EFF3FC",fg="red",justify="center")
    error_password = Label(frame,text= "",font=('Louis George Cafe',12),bg="#EFF3FC",fg="red",justify="center")
    error_gender = Label(frame,text= "",font=('Louis George Cafe',12),bg="#EFF3FC",fg="red",justify="center")
    error_balance = Label(frame,text= "",font=('Louis George Cafe',12),bg="#EFF3FC",fg="red",justify="center")
    username_frame = LabelFrame(master=frame,text="Username",font=('Louis George Cafe',12),width=250,height=50,bg="#EFF3FC")
    password_frame = LabelFrame(master=frame,text="Password",font=('Louis George Cafe',12),width=250,height=50,bg="#EFF3FC")
    copy_password_frame = LabelFrame(master=frame,text="confirm password",font=('Louis George Cafe',12),width=250,height=50,bg="#EFF3FC")
    age_frame = LabelFrame(master=frame,text="age",font=('Louis George Cafe',12),width=250,height=50,bg="#EFF3FC")
    gender_frame = LabelFrame(master=frame,text="gender",font=('Louis George Cafe',12),width=250,height=50,bg="#EFF3FC")
    balance_frame = LabelFrame(master=frame,text="balance",font=('Louis George Cafe',12),width=250,height=50,bg="#EFF3FC")
    
    username = Entry(username_frame,width=50)
    password = Entry(password_frame,width=50,show='•')
    copy_password = Entry(copy_password_frame,width=50,show='•')
    age = Spinbox(age_frame,from_=18,to=70,width=48,state='readonly')
    gender_button = ttk.Combobox(gender_frame,value=('Male','Female'),state='readonly',width=47)
    #male_button = Radiobutton(gender_frame,text="male",variable=gender_varm,value="Male",bg="#EFF3FC")
    #female_button = Radiobutton(gender_frame,text="female",variable=gender_varf,value="Female",bg="#EFF3FC")   
    balance = Entry(balance_frame,width=50)
    
        

    username.pack(padx=5,pady=5)
    password.pack(padx=5,pady=5)
    copy_password.pack(padx=5,pady=5)
    age.pack(padx=5,pady=5)
    gender_button.pack(padx=5,pady=5)
    #male_button.pack(padx=49,pady=2,side="left")
    #female_button.pack(padx=49,pady=2,side="right")
    balance.pack(padx=5,pady=5)
    
    frame.pack()
    login_title.pack()
    error_name.pack()
    username_frame.pack(padx=20,pady=5)
    error_password.pack()
    password_frame.pack(padx=20,pady=5)
    copy_password_frame.pack(padx=20,pady=5)
    age_frame.pack(padx=20,pady=5)
    error_gender.pack()
    gender_frame.pack(padx=20,pady=5)
    error_balance.pack()
    balance_frame.pack(padx=20,pady=5)
    
    back_button = button(frame,"back",'Louis George Cafe',14,10,"#E74C3C","#EFF3FC",sign_up_window.destroy,21,15,"left")
    sign_up_button = button(frame,"confirm",'Louis George Cafe',14,10,"#F4F7FF","#325BFF",lambda: check_sign_up(username.get(),password.get(),copy_password.get(),age.get(),gender_button.get(),balance.get()),21,15,"right")
    

#-------------------------main------------------------------
def button(frame,text,family,size,width,bcolor,fcolor,cmd,padx,pady,side):
    
    def on_enter(e):
        button['background'] = bcolor
        button['foreground'] = fcolor

    def on_leave(e):
        button['background'] = fcolor
        button['foreground'] = bcolor
       

    button = Button(frame,
                    text= text,
                    font= tkfont.Font(family=family,size=size),
                    width= width,
                    fg= bcolor,
                    bg= fcolor,
                    activeforeground= fcolor,
                    activebackground= bcolor,
                    border=0,
                    command=cmd)
    
    button.bind("<Enter>",on_enter)
    button.bind("<Leave>",on_leave)
    
    button.pack(padx=padx,pady=pady,side=side)

main = Tk()
main.geometry('900x600+150+20')
main.resizable(False, False)

label_background = Label(master=main,bg="#EFF3FC")
label_background.pack(fill=BOTH, expand=True)


frame = Frame(master=label_background,width=400,height=600,bg="#EFF3FC")
frame.pack()

frame_bank = Frame(master=frame,bg="#EFF3FC")
frame_bank.pack()

NewYork_font = tkfont.Font(family="NewYork", size=72, weight="normal")
bank_name = Label(frame_bank,text= "01 BANK",font=NewYork_font,padx=20,pady=60,bg="#EFF3FC")
bank_name.pack()

frame_button = Frame(master=frame,bg="#EFF3FC")
frame_button.pack(pady=60)

frame_exit = Frame(master=frame,bg="#EFF3FC")
frame_exit.pack(pady=20)

button_login = button(frame_button,"login",'Louis George Cafe',24,10,"#F4F7FF","#325BFF",open_login_window,10,0,"right")
button_sign_in = button(frame_button,"sign up",'Louis George Cafe',24,10,"#F4F7FF","#325BFF",open_sign_up_window,10,0,"left")
exit_button =   button(frame_exit,"exit",'Louis George Cafe',18,10,"#E74C3C","#EFF3FC",main.destroy,0,35,"bottom")

#-------------------------------------------------------


main.mainloop()