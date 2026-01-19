bal_file="Balance.txt"
pin="1234"

def get_balance():
    try:
        return int(open(bal_file).read())
    except:
        return 0
def save_balance(new):
    with open(bal_file,"w") as f:
        f.write(str(new))


def atm():
    if input("enter pin")!=pin:
        print("wrong pin")
        return
    while True:
        print("\n1 balance 2 deposit 3 withdraw 4 exit")  
        ch=input("choice:")
        bal=get_balance()

        if ch=="1":
            
           print("balance:",bal)
        elif ch=="2":
           amt=int(input("amount:"))
           save_balance(bal+amt)
           print("deposited")
        elif ch=="3":
           amt=int(input("amount:"))
           save_balance(bal-amt)
           print("withdrawn")
        else:
            print("insufficiant")
            break

atm()        
            
