print("Welcome to Bank")
Pin=int(input("Enter your 4 digit pin: "))
Balance=10000
if(Pin==1234):
    print("1 for Withdraw")
    print("2 for Balance")
    print("3 for Deposit")
    
else:
    print("Invalid PIN number")
    choice=int(input("please choose your transaction: "))
if(choice==1):
    withdraw=int(input("enter your amount: "))
    if(withdraw<Balance):
        print("please take your cash")
        Balance=Balance-withdraw
        print("your balance: ",Balance)
    else:
        print("your withdraw amount is higher than your balance")
if(choice==2):
    print("your balance: ",Balance)
if(choice==3):
    deposit=int(input("please enter your deposit amount: "))
    Balance=Balance+deposit
    print("your balance: ",Balance)
  
    

    

