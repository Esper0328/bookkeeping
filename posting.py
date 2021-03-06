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


def findAccount(transaction_list):
    return_list = []
    for transaction in transaction_list:
        if(len(return_list) == 0):
            return_list.append(transaction.debtor)
        else:
            isFirstAccount = True
            if(transaction.debtor  == "None"):
                 continue
            for account in return_list:
                if(account == transaction.debtor):
                    isFirstAccount = False
            if(isFirstAccount):
                 return_list.append(transaction.debtor)
    for transaction in transaction_list:
        isFirstAccount = True
        if(transaction.creditor  == "None"):
             continue
        for account in return_list:
            if(account == transaction.creditor):
                isFirstAccount = False
        if(isFirstAccount):
            return_list.append(transaction.creditor)
    return return_list

def displayAccount(transaction_list, account_list):
    for account in account_list:
        print(account)
        debtor_list = []
        creditor_list = []
        for transaction in transaction_list:
            if(account == transaction.debtor):
                debtor_list.append(transaction.date + "," + transaction.creditor + "," + transaction.debtor_charge)
            if(account == transaction.creditor):
                creditor_list.append(transaction.date + "," + transaction.debtor + "," + transaction.creditor_charge)
        numberOfDebtorItem = len(debtor_list)
        numberOfCreditorItem = len(creditor_list)
        if(numberOfDebtorItem < numberOfCreditorItem):
            numberOfLarger = numberOfCreditorItem
            numberOfSmaller = numberOfDebtorItem 
        else:
            numberOfLarger = numberOfDebtorItem
            numberOfSmaller = numberOfCreditorItem
        if((numberOfDebtorItem == 0) and (numberOfCreditorItem == 0)):
            print("Nothing")
        elif((numberOfDebtorItem != 0) and (numberOfCreditorItem == 0)):
            for index in range(numberOfLarger):
                print(debtor_list[index])
        elif((numberOfDebtorItem == 0) and (numberOfCreditorItem != 0)):
            for index in range(numberOfLarger):
                print(",,," + creditor_list[index])
        else:
            for index in range(numberOfLarger):
                if((index < numberOfDebtorItem) and (index < numberOfCreditorItem)):
                    print(debtor_list[index] + "," + creditor_list[index])
                elif((index < numberOfDebtorItem) and (index >= numberOfCreditorItem)):
                    print(debtor_list[index])
                elif((index >= numberOfDebtorItem) and (index < numberOfCreditorItem)):
                    print(",,," + creditor_list[index])
        print("")

def writeAccount(transaction_list, account_list, outputfile):
    for account in account_list:
        outputfile.write(account + "\n")
        debtor_list = []
        creditor_list = []
        for transaction in transaction_list:
            if(account == transaction.debtor):
                debtor_list.append(transaction.date + "," + transaction.creditor + "," + transaction.debtor_charge)
            if(account == transaction.creditor):
                creditor_list.append(transaction.date + "," + transaction.debtor + "," + transaction.creditor_charge)
        numberOfDebtorItem = len(debtor_list)
        numberOfCreditorItem = len(creditor_list)
        if(numberOfDebtorItem < numberOfCreditorItem):
            numberOfLarger = numberOfCreditorItem
            numberOfSmaller = numberOfDebtorItem 
        else:
            numberOfLarger = numberOfDebtorItem
            numberOfSmaller = numberOfCreditorItem
        if((numberOfDebtorItem == 0) and (numberOfCreditorItem == 0)):
            outputfile.write("Nothing" + "\n")
        elif((numberOfDebtorItem != 0) and (numberOfCreditorItem == 0)):
            for index in range(numberOfLarger):
                outputfile.write(debtor_list[index] + "\n")
        elif((numberOfDebtorItem == 0) and (numberOfCreditorItem != 0)):
            for index in range(numberOfLarger):
                outputfile.write(",,," + creditor_list[index] + "\n")
        else:
            for index in range(numberOfLarger):
                if((index < numberOfDebtorItem) and (index < numberOfCreditorItem)):
                    outputfile.write(debtor_list[index] + "," + creditor_list[index] + "\n")
                elif((index < numberOfDebtorItem) and (index >= numberOfCreditorItem)):
                    outputfile.write(debtor_list[index] + "\n")
                elif((index >= numberOfDebtorItem) and (index < numberOfCreditorItem)):
                    outputfile.write(",,," + creditor_list[index] + "\n")
        outputfile.write("\n")

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
    account_list = findAccount(transaction_list)
    displayAccount(transaction_list, account_list)
    with open('output.csv', 'w') as outputfile:
        writeAccount(transaction_list, account_list, outputfile)
else:
    print('Invalid Number of Argument')
