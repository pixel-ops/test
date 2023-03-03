from dataclasses import dataclass, field
from attr import asdict
@dataclass
class userdata():
    bank: str = field(default="HDFC")
    username: str = field(default="meet")
    lastname: str = field(default="Parekh")
    password: str = field(default="123")
    branch: str = field(default="Bopal")
    balance: int = field(default=100)

class ATM():
    bank = ["ICICI","HDFC"]
    p =userdata()
    my_bank = ""        
        
    def add_bank(self):
        bank_exists = input("Do you want to enter new bank(y/n): ")

        if bank_exists == "y":
            print("you have to enter a bank")
            self.my_bank = input("Enter your bank name: ")
            self.bank.append(self.my_bank)
            self.p.bank = self.my_bank
            r =self.register()
            return r

        else:
            self.my_bank = input("Enter your bank: ")
            if self.my_bank in self.bank:
                r = self.login()
                return r
            else:
                print("Enter correct details")

    def login(self):
        account_exists = input("Do you have an account?(y/n): ")
        if account_exists == "y": 
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if username == self.p.username and password == self.p.password and self.my_bank == self.p.bank:
                print("Logged in successfully")
                return True
            else:
                print("User does not exist")
                new_register = input("Do you want to register yourself?(y/n): ")
                if new_register == "y":
                    r = self.register()
                    return r
                else:
                    print("Thank you!")
                    
        else:
            new_register = input("Do you want to register (y/n): ")
            if new_register == 'y':
                r = self.register()
                return r
            else:
                print("thank you for using our facility")
            
    def register(self):
        print("-----Register here-----")
        self.p.username = input("Enter your username: ")
        self.p.lastname = input("Enter your lastname: ")
        self.p.password = input("Enter your password: ")
        self.p.branch = input("Enter your Branch: ")
        print("Successfully registred!")
        return True

    def display(self,disp="all"):
        print("Your infornamtion: ")
        if disp == "all":
            data = self.p.__dict__
            print("-----your data-----")
            for i,j in data.items():
                print(i," : ",j)
            print("-----End-----")
        else:
            print(disp," : ",self.p.__getattribute__(disp))
        

    def add_balance(self):
        new_balance = input("Enter the amount you want to add(in Rs.): ")
        self.p.balance+=int(new_balance)
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