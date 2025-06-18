class Account:
    def __init__(self,acc_name,acc_number,acc_balance,mobile_no,gender):
        self.name=acc_name
        self.number=acc_number
        self.balance=acc_balance
        self.mobile=mobile_no
        self.gen=gender
    def deposit(self,ammount):
        self.balance=self.balance+ammount
    def withdraw(self,ammount):
        if ammount>self.balance:
            print("\n\nInsufficient Bank Balnace")
            print("\nHere is your Balance details: ")
            self.display()
            return 1
        else:
            self.balance=self.balance-ammount
            return 0
    def display(self):
        print("\n\n")
        print(self.name," your account details are as followed: ")
        print(" ")
        print("User Name: ",self.name)
        print("User Account Number: ",self.number)
        print("User Mobile Number: ",self.mobile)
        print("Gender: ",self.gen)
        print("-------------------------")
        print("User Bank Balance: Rs.",self.balance)
        print("-------------------------")
        print(" \n\n")
    def get_balance(self):
        print("\nCurrent Bank Balance: ",self.balance)

dist={}
while True:
    print("HELLO USER\n\n")
    a=str(input("Options : Create Account / Delete Account / Check Balance / Deposit / Withdrawal / Exit")).lower()
    
    while a:
        match (a):
            case "create account":
                acc_num=str(input("Enter your account number (12 Digit): "))
                while len(acc_num)!=12:
                    print("Wrong account number! Enter again!!")
                    print(" ")
                    acc_num=str(input("Enter your account number again (12 DIGIT): "))
                    
                name=str(input("Enter your name: "))
                
                mobile=str(input("Enter your mobile number: "))
                while len(mobile)!=10:
                    print("Wrong mobile number! Enter again!!")
                    print(" ")
                    mobile=str(input("Enter your mobile number again:(10 DIGIT) "))
                    
                gender=input("Enter your gender (M/F/T): ").lower()
                if gender=="m":
                    gender="Male"
                elif gender=="f":
                    gender="Female"
                else:
                    gender="Trans Gender"
                balance=int(input("Enter the ammount to be deposited: "))
                         
                b1=Account(name,acc_num,balance,mobile,gender)
                dist[acc_num]=b1

                print("Account Successfully Created\n\n")
                b1.display()
                a=str(input("Options : Create Account / Delete Account / Check Balance / Deposit / Withdrawal / Exit")).lower()
                         
            case "delete account":
                         acc_num=str(input("Enter account number: "))
                         while len(acc_num)!=12:
                            print("Wrong account number! Enter again!!")
                            print(" ")
                            acc_num=str(input("Enter your account number again (12 DIGIT): "))
                         if acc_num in dist:
                             del dist[acc_num]
                             print("Account number: ",acc_num," Deleted Successfully")
                             a=str(input("Options : Create Account / Delete Account / Check Balance / Deposit / Withdrawal / Exit")).lower()
                         else:
                            print("Account not found.")
                            break
                        
            case "withdrawal":
                acc_num=str(input("Enter account number: "))
                while len(acc_num)!=12:
                            print("Wrong account number! Enter again!!")
                            print(" ")
                            acc_num=str(input("Enter your account number again (12 DIGIT): "))
                if acc_num in dist:
                    amm=int(input("Enter the ammount to be withdrawl: "))
                    s=dist[acc_num].withdraw(amm)
                    if s==0:
                        dist[acc_num].get_balance()
                        print(" ")
                        print("Ammount debited Successfully")
                        dist[acc_num].display()
                        break
                    elif s==1:
                        print("\nPlease Try again\n\n")
                        a=str(input("Options : Create Account / Delete Account / Check Balance / Deposit / Withdrawal / Exit")).lower()
                else:
                        print("Account not found.")
                        break
                    
            case "deposit":
                acc_num=str(input("Enter account number: "))
                while len(acc_num)!=12:
                    print("Wrong account number! Enter again!!")
                    print(" ")
                    acc_num=str(input("Enter your account number again (12 DIGIT): "))
                if acc_num in dist:
                    amm=int(input("Enter the ammount to be deposited: "))
                    dist[acc_num].deposit(amm)
                    dist[acc_num].get_balance()
                    dist[acc_num].display()
                    print("Ammount credited successfully!!\n")
                    a=str(input("Options : Create Account / Delete Account / Check Balance / Deposit / Withdrawal / Exit")).lower()
                else:
                    print("Account not found.")
                    break
                
            case "check balance":
                acc_num=str(input("Enter account number: "))
                while len(acc_num)!=12:
                    print("Wrong account number! Enter again!!")
                    print(" ")
                    acc_num=str(input("Enter your account number again (12 DIGIT): "))
                if acc_num in dist:
                    dist[acc_num].get_balance()
                    dist[acc_num].display()
                    a=str(input("Options : Create Account / Delete Account / Check Balance / Deposit / Withdrawal / Exit")).lower()
                else:
                    print("Account not found.")
                    break

            case "exit":
                    print("Thank you for choosing our bank!!")
                    break
            
            case _:
                print("Entered wrong! Please try again!")
                a=str(input("Options : Create Account / Delete Account / Check Balance / Deposit / Withdrawal / Exit")).lower()
    bc=input("Do you want to continue?: ").lower()
    if bc=="no":
        break
'''#for key in dist:
#    dist[key].display()
x=input("Enter account number: ")
dist[x].display()'''
