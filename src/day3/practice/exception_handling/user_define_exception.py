class BankError(Exception):
    def __init__(self,message,balance):
        self.message=message
        self.balance=balance
        super().__init__(message)
try:
    n=int(input("Enter the Amount to be widrawed :"))
    if n<100:
        raise BankError("Can't witdraw amount less than 100",n)
except BankError as Be:
    print(Be.message,f"Amount : {Be.balance}")