from dataclasses import dataclass,field
from getpass import getpass


@dataclass()
class userdata:
    bank: dict
    userid: int
    username: str
    lastname: str
    password: str
    branch: str
    balance: int = field(default=100)

@dataclass
class all_data:
    data: list[userdata]


my_data = all_data([])
# CLASS BANK CONTAINING ALL THE METHODS FOR THE USER
class Bank:

    user_login = False
    user_bank = ""
    print(type(my_data.data))
    userid = len(my_data.data)

    #ADD NEW BANK TO THE DATA
    # def add_new_bank(self):
    #     self.my_bank = input("Enter bank name: ")
    #     my_data.bank[self.my_bank] = [] 
    #     print(my_data.bank,self.my_bank)
    #     self.login()



    #CHECK LOGIN CREDENTIALS ON A CERTIAN BANK
    def login(self):
        print("-----Login-----")
        username = input("Enter your username: ")
        password = getpass("Enter your password: ")
        temp_user = {}
        for i in range(0,len(my_data.data)):
            temp_user[i] = my_data.data[i].username
        self.userid =  int(''.join([str(i) for i in temp_user if temp_user[i]==username]))
        # self.userid = int(''.join(self.userid))

        if username == my_data.data[self.userid].username and hash(password) == my_data.data[self.userid].password:
           print("Logged in successfully as ",username)
           self.user_login = True
        else:
            print("User does not exist")
            new_register = input("Do you want to register yourself?(y/n): ")
            if new_register == "y":
                self.register()
            else:
                print("Thank you!")



    #REGISTER IF NOT ALREADY REGISTRED ON A SPECIFIC BANK
    def register(self):
        print("-----Register here-----")
        username = input("Enter your username: ")
        lastname = input("Enter your lastname: ")
        password = getpass("Enter your password: ")
        branch   = input("Enter your Branch: ")
        if not my_data.data:
            self.userid = 0
        else: 
            self.userid = len(my_data.data) 
        my_data.data.append(userdata(self.user_bank,self.userid,username,lastname,hash(password),branch))
        print(my_data.data)
        self.user_login = True
        print("Successfully registred!")
    #GET THE DATA FROM USER THAT HE WANTS TO UPDATE
    def get_user_updated_info(self):
        print("-----Update Info-----")
        username = input("Enter your new username: ")
        lastname = input("Enter your new lastname: ")    
        password = input("Enter your new password: ")
        self.update_user_info(username,lastname,password)


    #UPDATES USER'S INFORMATION
    def update_user_info(self,username,lastname,password):
        my_data.data[self.userid].username = username
        my_data.data[self.userid].lastname = lastname
        my_data.data[self.userid].password = password
        
    
    #DISPALYS THE DATA OF THE USER OR ANY DATA HE LIKES
    def display_all_data(self,disp="all"):
        print("Your infornamtion: ",disp)
        if disp == "all":
            print(self.userid)
            data = my_data.data[self.userid].__dict__
            print("-----your data-----")
            for i,j in data.items():
                print(i," : ",j)
            print("-----End-----")
        else:
            print(disp," : ",my_data.data[self.userid].__getattribute__(disp))




#CLASS ATM CONTAINS ALL THE INFORMATION THAT THE USER CAN ENTER IN ATM
class ATM(Bank):


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
        my_data.data[self.userid].balance+=int(new_balance)
        if input("Do you want to add balance again?(y/n): ") == "y":
            self.add_balance()
        else:
            print("Balance Updates!")
            self.display_all_data("balance")




    #FOR THE USER TO LOGOUT AND LOGIN WITH ANOTHER ACCOUNT
    def logout(self):
        self.user_login = False


meet = ATM()


while True:
    if meet.user_login:
        meet.all_options()
    else:
        print("-----Menu-----")

        user_choice = input("1. Register \n2. Login  \n3. Exit \nEnter your input: ")
        if user_choice == "1":
            meet.register()
        elif user_choice == "2":
            if not my_data.data:
                print("No user exists please register!")
            else:
                meet.login()
        elif user_choice == "3":
                print("Thank you for using this ATM")
                exit()
        else:
            print("Enter valid inupt")

# meet.display_all_data()
# meet.add_balance()
