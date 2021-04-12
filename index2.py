import random 


class Banking:
    def __init__(self):
        self.initialize()

    def initialize(self):
        self.userDatabase = []
        print("Welcome to JBANK \n")
        print("What would you like to do ? \n")
        action = int(float(input('Select 1 to register  Select 2 to login  Select 3 to exit')))
        if(action==1):
            self.register()
            exit()
        if (action==2):
            self.login()
            exit()
        if (action==3): 
            exit()         
        else:
            print('invalid entry')
            self.initialize()
            exit()
        return

    def register(self):
        firstname = input("Enter your first name \n")
        lastname = input("Enter your last name \n")
        email = input("Enter your email \n")
        password = input("Create your password \n")
        accountNumber = random.randrange(11111111111, 88888888888)

        print(accountNumber)
        for user in self.userDatabase:
            if(user['email'] == email):
                print('Invalid Email. Please try again')
                self.initialize()
                exit()
        currentUser = {
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'password': password,
            'balance': 0,
            'accountNumber': accountNumber
        }
        self.userDatabase.append(currentUser)
        print('Your regiseration was successful \n')
        self.login()
        exit()

 
    def login(self):
        print("*****Please enter your login credentials to resume banking operations****** \n")
        email = input('Enter your email \n')
        password = input('Enter your password \n')
        for userid,user in enumerate(self.userDatabase):
            if(user['email'] == email and user['password'] == password):
                print('Your login was successful \n')
                print('*****Profile*****\n')
                print(f"Name: {user['firstname']} {user['lastname']} \n")
                print(f"Email: {user['email']} \n")
                print(f"Account Number: {user['accountNumber']} \n")
                self.bankingOperations(userid)
                return
        print('Your login credential is invalid, please try again \n')
        self.login()
        return

    def bankingOperations(self,userId):
        operation = int('Select an operation (Enter 1 for withdrawal, 2 for deposit, 3 for customerCare, 4 for logout)')
        if(operation == 1):
            self.withdrawal(userId)
            return
        if(operation == 2):
            self.deposit(userId)
            return
        if(operation == 3):
            self.customerCare(userId)
            return
        if(operation == 4):
            self.logout()
            return
        else:
            print('Invalid input. Please try again')
            self.bankingOperations(userId)
            return
            
    def deposit(self,userId):
        print('***Deposit*** \n')
        depositAmount = int(input('How much are you depositing ?'))
        self.userDatabase[userId]['balance'] += depositAmount 
        print(f"Current balance is #{self.userDatabase[userId]['balance']}")
        self.bankingOperations(userId)

    def withdrawal(self,userId): 
        withdrawAmount = int(input('how much would you like to withdraw ?'))
        if(withdrawAmount > self.userDatabase[userId]['balance']):
            print('Your balance is too small for the withdrawal ! please try again')
            self.bankingOperations(userId)
            return 
        self.userDatabase[userId]['balance'] -= withdrawAmount   
        print(f"Withdrawal successful. Current balance is #{self.userDatabase[userId]['balance']}")
        self.bankingOperations(userId)

    def customerCare(self,userId):
        complaint=input('state your issue \n')
        print('Thank you for contacting us')
        self.bankingOperations(userId)


    def logout(self):
        self.login()

bankApp = Banking()    

