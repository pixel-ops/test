from dataclasses import dataclass,field
from getpass import getpass


@dataclass()
class Userdata:
    user_bank: str
    userid: int
    username: str
    lastname: str
    password: str
    branch: str
    balance: int = field(default=100)

@dataclass
class Bank_data:
    bank: str
    bank_id: int
    data: list[Userdata]


# current_data = [Bank_data('a',0,[Userdata('a',1,'b','b','b','b')]),Bank_data('b',1,[])]

current_data = []

class Bank:
    
    
    user_login = False
    current_bank_id = 0


    #GETS THE ID OF THE CURRENT BANK
    def get_bank_id(self,name):
        lgt = len(current_data)
        for i in range(lgt):
            if name in current_data[i].bank:
                print(current_data[i])
                self.current_bank_id = i
    

    # ADD NEW BANK TO THE DATA
    def add_new_bank(self):
        bank_name = input("Enter the name of the bank: ")
        current_data.append(Bank_data(bank_name,len(current_data),[]))


    #   CHECK THAT THE USER IS IN THE BANK DATABASE OR NOT
    def check_user_in_bank(self,username):
        for d in current_data[self.current_bank_id].data:
            if username in d.username:
                self.current_user_id = d.userid
                return True
            else:
                continue


    #CHECK LOGIN CREDENTIALS ON A CERTIAN BANK
    def login(self):
        print("-----Login-----")
        username = input("Enter your username: ")
        password = getpass("Enter your password: ")
        if self.check_user_in_bank(username):
            if username == current_data[self.current_bank_id].data[self.current_user_id].username and hash(password) == current_data[self.current_bank_id].data[self.current_user_id].password:
                print("Logged in successfully as ",username)
                self.user_login = True
            else:
                print("User does not exist")
                print(current_data[self.current_bank_id].data[self.current_user_id].username)
                print(self.current_bank_id)
                new_register = input("Do you want to register yourself?(y/n): ")
                if new_register == "y":
                    self.register()
                else:
                    print("Thank you!")


    #REGISTER IF NOT ALREADY REGISTRED ON A SPECIFIC BANK
    def register(self):
        print(self.current_bank_id)
        username = input("Enter your username: ")
        lastname = input("Enter your lastname: ")
        password = getpass("Enter your password: ")
        branch   = input("Enter your Branch: ")
        if current_data[self.current_bank_id].data:
            self.current_user_id = len(current_data[self.current_bank_id].data)
        else:
            self.current_user_id = 0
        current_data[meet.current_bank_id].data.append(Userdata(current_data[meet.current_bank_id].bank,self.current_user_id,username,lastname,hash(password),branch))
        self.user_login = True
        print("Successfully registred!")
        self.login()


    #GET THE DATA FROM USER THAT HE WANTS TO UPDATE
    def get_user_updated_info(self):
        print("-----Update Info-----")
        username = input("Enter your new username: ")
        lastname = input("Enter your new lastname: ")    
        password = input("Enter your new password: ")
        self.update_user_info(username,lastname,hash(password))


    #UPDATES USER'S INFORMATION
    def update_user_info(self,username,lastname,password):

        current_data[self.current_bank_id].data[self.current_user_id].username = username
        current_data[self.current_bank_id].data[self.current_user_id].lastname = lastname
        current_data[self.current_bank_id].data[self.current_user_id].password = password


    #DISPALYS THE DATA OF THE USER OR ANY DATA HE LIKES
    def display_all_data(self,disp="all"):
        print("Your infornamtion: ",disp)
        if disp == "all":
            print(self.current_user_id)
            data = current_data[self.current_bank_id].data[self.current_user_id].__dict__
            print("-----your data-----")
            for i,j in data.items():
                print(i," : ",j)
            print("-----End-----")
        else:
            print(disp," : ",current_data[self.current_bank_id].data[self.current_user_id].__getattribute__(disp))

    # FUNCTION PRINTS THE DATA OF ALL THE USERS IN THE CURRENT BANK IN A DICTIONARY
    def get_all_user_bank_data(self):
        choice = input("Input the name of the bank: ")
        for i in current_data:
            if choice == i.bank:
                for j in i.data:
                    print(j.__dict__)
            else:
                print("Given name does not exists")

    # INERFACE WHICH IS SHOWN IN THE START OF THE PROGRAM
    def employee_access_interface(self):
        while True:
            print("-----Welcome to ATM------")
            choice = input("Select from options below \n1. Add bank \n2. Display bank data \n3. Continue to login \n4. Exit \nEnter your option here: ")
            if choice == '1':
                self.add_new_bank()
            elif choice == '2':
                self.get_all_user_bank_data()
            elif choice == '3':
                break
            elif choice == '4':
                exit()
            else:
                print("Enter valid input")


class ATM(Bank):

    

    #GIVES THE USER ALL THE OPTIONS TO USE IN THE ATM
    def all_options(self):
        print("-----Dashboard-----")
        choice = input("Select from options below \n1. dispay data \n2. Add Balance \n3. Update Information \n4. Logout \nEnter your option here: ")
        match choice:
            case "1":
                self.display_all_data()
            case "2":
                self.add_balance()
            case "3":
                self.get_user_updated_info()
            case "4":
                self.logout()
            case _:
                print("Enter valid input")

    #ADDS BALANCE TO USERS ACCOUNT
    def add_balance(self):
        new_balance = input("Enter the amount you want to add(in Rs.): ")
        current_data[self.current_bank_id].data[self.current_user_id].balance+=int(new_balance)
        if input("Do you want to add balance again?(y/n): ") == "y":
            self.add_balance()
        else:
            print("Balance Updates!")
            self.display_all_data("balance")

    #FOR THE USER TO LOGOUT AND LOGIN WITH ANOTHER ACCOUNT
    def logout(self):
        self.user_login = False



meet = ATM()
meet.employee_access_interface()
# print(current_data)
my_bank = input("Enter the bank you want to login into: ")
meet.get_bank_id(my_bank)
# print(meet.current_bank_id)



 
while True:
    if not current_data:
        pass
    else:
        if meet.user_login:
            meet.all_options()
        else:
            print("-----Menu-----")

            user_choice = input("1. Register \n2. Login  \n3. Exit \nEnter your input: ")
            if user_choice == "1":
                meet.register()
            elif user_choice == "2":
                if len(current_data[meet.current_bank_id].data) == 0:
                    print("No user exists please register!")
                else:
                    meet.login()
            elif user_choice == "3":
                    print("Thank you for using this ATM")
                    meet.employee_access_interface()
                    my_bank = input("Enter the bank you want to login into: ")
                    meet.get_bank_id(my_bank)
            else:
                print("Enter valid inupt")
