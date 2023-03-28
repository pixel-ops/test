from dataclasses import dataclass, field
from getpass import getpass
import time
import json
import pandas as pd


@dataclass
class Transaction_history:
    sender_id: int
    sender_bank: str
    reciever_id: int
    reciever_bank: str
    amount: int


@dataclass()
class Userdata:
    user_bank: str
    userid: int
    username: str
    lastname: str
    password: str
    branch: str
    transaction: list[Transaction_history]
    balance: int = field(default=100)


@dataclass
class Bank_data:
    bank: str
    bank_id: int
    data: list[Userdata]


current_data = []


class Bank:

    user_login = False
    current_bank_id = 0

    # GETS THE ID OF THE CURRENT BANK
    def get_bank_id(self, name):
        lgt = len(current_data)
        for i in range(lgt):
            if name in current_data[i].bank:
                self.current_bank_id = i
                return True
            else:
                continue
        return False

    # ADD NEW BANK TO THE DATA

    def add_new_bank(self):
        bank_name = input("Enter the name of the bank: ")
        current_data.append(Bank_data(bank_name, len(current_data), []))

    #   CHECK THAT THE USER IS IN THE BANK DATABASE OR NOT
    def check_user_in_bank(self, username):
        for d in current_data[self.current_bank_id].data:
            if username in d.username:
                self.current_user_id = d.userid
                return True
            else:
                continue

    # CHECK LOGIN CREDENTIALS ON A CERTIAN BANK

    def login(self):
        print("-----Login-----")
        username = input("Enter your username: ")
        password = getpass("Enter your password: ")
        if self.check_user_in_bank(username):
            if username == current_data[self.current_bank_id].data[self.current_user_id].username and hash(password) == current_data[self.current_bank_id].data[self.current_user_id].password:
                print("Logged in successfully as ", username)
                self.user_login = True
            else:
                print("User does not exist")
                new_register = input(
                    "Do you want to register yourself?(y/n): ")
                if new_register == "y":
                    self.register()
                else:
                    print("Thank you!")
                    exit()
        else:
            print("Enter valid name")
            self.login()

    # REGISTER IF NOT ALREADY REGISTRED ON A SPECIFIC BANK

    def register(self):
        username = input("Enter your username: ")
        lastname = input("Enter your lastname: ")
        password = getpass("Enter your password: ")
        branch = input("Enter your Branch: ")
        if current_data[self.current_bank_id].data:
            self.current_user_id = len(current_data[self.current_bank_id].data)
        else:
            self.current_user_id = 0
        current_data[self.current_bank_id].data.append(Userdata(
            current_data[self.current_bank_id].bank, self.current_user_id, username, lastname, hash(password), branch, []))
        self.user_login = True
        print("Successfully registred!")
        self.login()

    # GET THE DATA FROM USER THAT HE WANTS TO UPDATE

    def get_user_updated_info(self):
        print("-----Update Info-----")
        username = input("Enter your new username: ")
        lastname = input("Enter your new lastname: ")
        password = input("Enter your new password: ")
        self.update_user_info(username, lastname, hash(password))

    # UPDATES USER'S INFORMATION
    def update_user_info(self, username, lastname, password):

        current_data[self.current_bank_id].data[self.current_user_id].username = username
        current_data[self.current_bank_id].data[self.current_user_id].lastname = lastname
        current_data[self.current_bank_id].data[self.current_user_id].password = password

    # DISPALYS THE DATA OF THE USER OR ANY DATA HE LIKES
    def display_all_data(self, disp="all"):
        print("Your infornamtion: ", disp)
        if disp == "all":
            data = current_data[self.current_bank_id].data[self.current_user_id].__dict__
            print("-----your data-----")
            for i, j in data.items():
                print(i, " : ", j)
            print("-----End-----")
        else:
            print(
                disp, " : ", current_data[self.current_bank_id].data[self.current_user_id].__getattribute__(disp))

    # FUNCTION PRINTS THE DATA OF ALL THE USERS IN THE CURRENT BANK IN A DICTIONARY
    def get_all_user_bank_data(self):
        choice = input("Input the name of the bank: ")
        for i in current_data:
            if i.data:
                if choice == i.bank:
                    for j in i.data:
                        print("----Account of user" + j.username + "of bank: " + j.user_bank + "----")
                        pd_object = pd.read_json(json.dumps(j.__dict__, indent=3), typ='series') #CREATING A PANDAS OBJECT TO PRINT IN TABLE FORMAT
                        print(pd.DataFrame(pd_object)) #CONVERTING PANDAS OBJECT TO DATA PRAME TO PRINT 
                else:
                    print("Given name does not exists")
            else:
                print("No data avaliable for the current bank")
    
    # INERFACE WHICH IS SHOWN IN THE START OF THE PROGRAM
    def employee_access_interface(self):
        while True:
            print("-----Welcome to ATM------")
            choice = input(
                "Select from options below \n1. Add bank \n2. Display bank data \n3. Continue to login \n4. Remove bank \n5. Exit \nEnter your option here: ")
            if choice == '1':
                self.add_new_bank()
            elif choice == '2':
                self.get_all_user_bank_data()
            elif choice == '3':
                break
            elif choice == '4':
                self.remove_bank()
            elif choice == '5':
                exit()
            else:
                print("Enter valid input")
    # REMOVE USER FROM THE BANK

    def remove_user(self):
        user = input("which user you want to remove?: ")

        if self.check_user_in_bank(user):
            del current_data[self.current_bank_id].data[self.current_bank_id]
            self.user_login = False
        else:
            print("user does not exists")
    # REMOVE BANK FROM THE DATA

    def remove_bank(self):
        bank = input("Enter the bank you want to remove: ")
        if self.get_bank_id(bank):
            del current_data[self.current_bank_id]
        else:
            print("bank does not exists178")
    # CHANGE PASSWORD OF THE USER

    def change_password(self):
        password = input("Enter your new password: ")
        current_data[self.current_bank_id].data[self.current_user_id].password = hash(
            password)
        self.display_all_data()

    # WITHDRAW MONEY FROM THE BANK
    def withdraw_money(self):
        new_balance = input("Enter the amount you want to withdraw(in Rs.): ")
        if int(new_balance) <= current_data[self.current_bank_id].data[self.current_user_id].balance:
            current_data[self.current_bank_id].data[self.current_user_id].balance -= int(
                new_balance)
            if input("Do you want to withdraw money again?(y/n): ") == "y":
                self.withdraw_money()
            else:
                print("Your money is coming....")
                time.sleep(3)
                print("Balance Updates!")
                self.display_all_data("balance")
        else:
            print("Enter amount less than your balance!!")
            self.withdraw_money()

    # ADDS BALANCE TO USERS ACCOUNT
    def deposit_money(self):
        new_balance = input("Enter the amount you want to add(in Rs.): ")
        current_data[self.current_bank_id].data[self.current_user_id].balance += int(
            new_balance)
        if input("Do you want to add balance again?(y/n): ") == "y":
            self.deposit_money()
        else:
            print("Balance Updates!")
            self.display_all_data("balance")

    # FOR THE USER TO LOGOUT AND LOGIN WITH ANOTHER ACCOUNT
    def logout(self):
        self.user_login = False

    # GET INDIVIDUAL ID OF THE PERSON
    def get_individual_user_id(self, name, reciever_bank_id):
        for d in current_data[reciever_bank_id].data:
            if name in d.username:
                userid = d.userid
                return int(userid)

    # GET INDIVIDUAL BANK ID OF THE PERSON
    def get_individual_bank_id(self, name):
        lgt = len(current_data)
        for i in range(lgt):
            if name in current_data[i].bank:
                return int(i)
    # FUNCTION TO MAKE A TRANSACTION

    def make_transaction(self):
        reciever_bank = input("Enter the bank of the user: ")
        reciever_bank_id = int(self.get_individual_bank_id(reciever_bank))
        reciever = input("Enter the name of the reciever: ")
        reciever_user_id = int(
            self.get_individual_user_id(reciever, reciever_bank_id))
        transffered_amout = int(
            input("Enter the amount you want to transfer: "))

        if int(transffered_amout) <= current_data[self.current_bank_id].data[self.current_user_id].balance:
            current_data[self.current_bank_id].data[self.current_user_id].balance -= int(
                transffered_amout)
            current_data[reciever_bank_id].data[reciever_user_id].balance += int(
                transffered_amout)
            self.display_all_data("balance")
            # print("Balance of reciever: "+str(current_data[reciever_bank_id].data[reciever_user_id].balance))

            current_data[self.current_bank_id].data[self.current_user_id].transaction.append(Transaction_history(
                self.current_user_id, self.current_bank_id, reciever_user_id, reciever_bank_id, transffered_amout))
        else:
            print("Enter valid input")
            self.make_transaction()
    # DISPLAY ALL THE REANSACTIONS

    def display_all_transaction(self):
        print("-----Transaction history-----")
        for i in current_data[self.current_bank_id].data[self.current_user_id].transaction:
            print(str(current_data[i.sender_bank].data[i.sender_id].username), "user of bank", str(current_data[i.sender_bank].data[i.sender_id].user_bank) + " sent Rs." + str(
                i.amount) + " to " + str(current_data[i.reciever_bank].data[i.reciever_id].username) + " user of bank " + str(current_data[i.reciever_bank].data[i.reciever_id].user_bank))


class ATM(Bank):

    # GIVES THE USER ALL THE OPTIONS TO USE IN THE ATM
    def all_options(self):
        print("-----Dashboard-----")
        choice = input(
            "Select from options below \n1. dispay data \n2. Add Balance \n3. Update Information \n4. Change Password \n5. Withdraw money \n6. Send money to other user \n7. Display all transaction \n8. Logout \nEnter your option here: ")
        match choice:
            case "1":
                self.display_all_data()
            case "2":
                self.deposit_money()
            case "3":
                self.get_user_updated_info()
            case "4":
                self.change_password()
            case "5":
                self.withdraw_money()
            case "6":
                self.make_transaction()
            case "7":
                self.display_all_transaction()
            case "8":
                self.logout()
            case _:
                print("Enter valid input")


meet = ATM()

while True:
    if not current_data: # IF THE LIST IS EMPTY THEN IT WILL REDIRECT USER EMPOYEE INTERFACE OF ADD ATLEAST ONE BANK
        meet.employee_access_interface()
        my_bank = input("Enter the bank you want to login into: ")
        if meet.get_bank_id(my_bank):
            pass
        else:
            print("Bank does not exists")
            meet.employee_access_interface()
            my_bank = input("Enter the bank you want to login into: ")
            meet.get_bank_id(my_bank)

    else:
        if meet.user_login:
            meet.all_options()
        else:
            print("-----Menu-----")

            user_choice = input(
                "1. Register \n2. Login \n3. Remove user \n4. Exit \nEnter your input: ")
            if user_choice == "1":
                meet.register()
            elif user_choice == "2":
                if len(current_data[meet.current_bank_id].data) == 0:
                    print("No user exists please register!")
                else:
                    meet.login()
            elif user_choice == "3":
                meet.remove_user()
            elif user_choice == "4":
                print("Thank you for using this ATM")
                meet.employee_access_interface()
                my_bank = input("Enter the bank you want to login into: ")
                meet.get_bank_id(my_bank)
            else:
                print("Enter valid inupt")

