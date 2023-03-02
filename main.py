from tabulate import tabulate

class ATM():

    bank = []
    user = {1:{"username":"meet","lastname":"Parekh","password":"123","branch":"Bopal","balance":100},}
    initial_balance = 100

    # def __init__(self) -> None:
        
        

    def add_bank(self):

        if not bool(self.bank):
            print("you have to enter a bank")
            self.bank.append(input("Enter your bank name: "))
            print(self.bank)
            self.login()

        else:
            my_bank = input("Enter your bank: ")

            if my_bank in self.bank:
                self.login()

            else:
                print("Enter correct details")


    def login(self):

        account_exists = input("Do you have an account?(y/n): ")

        if account_exists == "y": 

            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if self.user[1]["username"] == username and self.user[1]["password"] == password:

                self.display()
            
            else:

                print("User does not exist")
        else:

            new_register = input("Do you want to register (y/n): ")

            if new_register == 'y':

                self.register()

            else:

                print("thank you for using our facility")

            
    def register(self):
        my_user = {}
        my_user["username"] = input("Enter your username: ")
        my_user["lastname"] = input("Enter your lastname: ")
        my_user["password"] = input("Enter your password: ")
        my_user["Branch"] = input("Enter your Branch: ")
        my_user["balance"] = 100
        self.user[1] = my_user
        print(self.user)


    def display(self):
        print("Your infornamtion: ")
        # print(tabulate(self.user[1].values(),headers=self.user[1].keys()))
        print(self.user[1])


a = ATM()
a.add_bank()
    