from tabulate import tabulate
import pandas as pd

class ATM():

    bank = {"ICICI":["meet"],"HDFC":[]}
    user = {1:{"username":"meet","lastname":"Parekh","password":"123","branch":"Bopal","balance":100},}
    user_id = len(user)
    my_bank = ""        
        

    def add_bank(self):
        bank_exists = input("Do you want to enter new bank(y/n): ")
        if bank_exists == "y":
            print("you have to enter a bank")
            self.my_bank = input("Enter your bank name: ")
            self.bank[self.my_bank] = [] 
            print(self.bank,self.my_bank)
            r =self.login()
            return r

        else:
            self.my_bank = input("Enter your bank: ")
            if self.my_bank in self.bank.keys():
                r = self.login()
                return r
            else:
                print("Enter correct details")

    def login(self):
        account_exists = input("Do you have an account?(y/n): ")
        if account_exists == "y": 
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if username in self.bank.get(self.my_bank):
                for i in self.user.keys():
                    if self.user[i]["username"] == username and self.user[i]["password"] == password:
                        self.user_id = i
                        print("Logged in successfully!")
                        return True
                        
                    else:
                        print("User does not exist")
                        new_register = input("Do you want to register yourself?(y/n): ")
                        if new_register == "y":
                            r = self.register()
                            return r
                        else:
                            print("Thank you!")
                            return False
            else:
                print("User does not exist")
                new_register = input("Do you want to register yourself?(y/n): ")
                if new_register == "y":
                    r = self.register()
                    return r
                else:
                    print("Thank you!")
                    return False
                    
        else:
            new_register = input("Do you want to register (y/n): ")
            if new_register == 'y':
                r = self.register()
                return r
            else:
                print("thank you for using our facility")
                return False
            
    def register(self):
        my_user = {}
        my_user["username"] = input("Enter your username: ")
        my_user["lastname"] = input("Enter your lastname: ")
        my_user["password"] = input("Enter your password: ")
        my_user["Branch"] = input("Enter your Branch: ")
        my_user["balance"] = 100
        self.user[len(self.user)+1] = my_user
        self.user_id +=1
        print("Successfully registred!")
        return True

    def display(self,disp="all"):
        print("Your infornamtion: ")
        if disp == "all":
            for i,j in self.user[self.user_id].items():
                print(i," : ",j)
        else:
            print(disp," : ",self.user[self.user_id].get(disp))
        

    def add_balance(self):
        new_balance = input("Enter the amount you want to add(in Rs.): ")
        self.user[self.user_id]["balance"]+=int(new_balance)
        if input("Do you want to add balance again?(y/n): ") == "y":
            self.add_balance()
        else:
            print("Balance Updates!")
            self.display("balance")


a = ATM()
print("-----Welcome to banking management system-----")
if a.add_bank():
    while True:
        print("What else you want to do?")
        choice = input(" 1. Display your data\n 2. add balance\n 3. display balance\n 4. exit\n Enter your input here: ")
        if choice == "1":
            a.display()
        elif choice == "2":
            a.add_balance()
        elif choice == "3":
            a.display("balance")
        elif choice == "4":
            break
        else:
            print("Enter a valid input")
else:
    print("Something went wrong")