#Instance variable - Name Amount Address Acount no
#Instance Method

class Bank_Account:

    #Class Variable

    Bank_Name = "HDFC Bank PVT LTD"
    ROI_On_FC = 6.7

    def __init__(self):
        #Instance variables
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNO = 0

    def CreateAccount(self):

        print("Enter your name:")
        self.Name = input()

        print("Enter your Address:")
        self.Address = input()

        print("Enter your initial amount:")
        self.Amount = int(input())

        print("Enter your Account no:")
        self.AccountNO = input()

    def DisplayAccountInfo(self):

        print("______Your Account Details are as below________")

        print("Name :",self.Name)
        print("Address:",self.Address)
        print("Account No:", self.AccountNO)
        print("Current Amount :",self.Amount)

    #Decorator for class method @name of class is decorator

    @classmethod
    def DisplayBankInformation(cls):
        print("Welcome to Banking console")
        print("Name of our bank is",cls.Bank_Name)
        print("ROI offered is:",cls.ROI_On_FC)

def main():

    print("Name of bank:",Bank_Account.Bank_Name)
    print("Rate of Interest ",Bank_Account.ROI_On_FC)

    Bank_Account.DisplayBankInformation()

    User1 = Bank_Account()
    User2 = Bank_Account()

    User1.CreateAccount()
    User2.CreateAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()

if __name__ =="__main__":

    main()

