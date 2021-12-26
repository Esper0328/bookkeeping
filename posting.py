import sys

class Transaction:
    def __init__(self, date, debtor, debtor_charge, creditor, creditor_charge):
        self.date = date
        self.debtor = debtor
        self.debtor_charge = debtor_charge
        self.creditor = creditor
        self.creditor_charge = creditor_charge

    def print(self):
        print(self.date)
        print(self.debtor)
        print(self.debtor_charge)
        print(self.creditor)
        print(self.creditor_charge)

transaction_list = []
account_list = []

args = sys.argv
if len(args) == 2:
    with open(args[1]) as f:
        lines = f.read()
        for line in lines.split("\n"):
            items = line.split(",")
            if(len(items[0]) != 0):
                transaction = Transaction(items[0], items[1], items[2], items[3], items[4])
                transaction_list.append(transaction)
    for transaction in transaction_list:
        if(len(account_list) == 0):
            print(transaction.debtor)
            account_list.append(transaction.debtor)
        else:
            print(len(account_list))
            isFirstAccount = True
            for account in account_list:
                print("Account:"+account)
                print("Transaction:"+transaction.debtor)
                if(account == transaction.debtor):
                    isFirstAccount = False
            if(isFirstAccount):
                 print("New")
                 account_list.append(transaction.debtor)
        
else:
    print('Invalid Number of Argument')
