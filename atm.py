class Atm: 
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber,
        self.pin = pin,
    
    def check_balance(self):
        print("your balance is $1000.")

    def cash_withdrawl(self, amount):
        new_amount = 1000-amount
        print("you have withdrawn amount "+str(amount)+
        ". your remianing balance is "+str(new_amount))

def main():
    cardnumber = input("input your card number:")
    pin = input("enter your pin number:")
    new_user = Atm(cardnumber,pin)
    print("choose your activity:")
    print("1. balance \n 2.withdrawl")
    activity = int(input("enter the activity number:"))
    if (activity == 1):
        new_user.check_balance()
    elif(activity == 2):
        amount = int(input("enter the amount:"))
        new_user.cash_withdrawl(amount)
    else: print("enter a valid number please:")

main()
