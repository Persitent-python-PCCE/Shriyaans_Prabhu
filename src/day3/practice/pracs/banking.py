accounts = {"ACC-1001": 5000.0, "ACC-1002": 250.0, "ACC-1003": 0.0}

# TODO STEP 1 -- Define two custom exceptions:
# - InsufficientFundsError : raised when a withdrawal exceeds the balance
# - InvalidAmountError : raised when amount -= 0
# (make InvalidAmountError inherit from ValueError)
#
# class InsufficientFundsError(______):
# pass
# class InvalidAmountError(______):
# pass
class InsufficientFundsError(Exception):
    def __init__(self,amount,message):
        self.amount=amount
        self.message=message
class InvalidAmountError(Exception):
    def __init__(self,amount,message):
        self.amount=amount
        self.message=message



def withdraw(account_id, amount):
    """Withdraw 'amount' from an account and return the new balance."""
    # TODO STEP 2 -- Raise the right exception:
    # - account_id not in accounts: raise KeyError(account_id)
    # - amount <= 0: raise InvalidAmountError
    # - amount > accounts[account_id]: raise InsufficientFundsError
    # Otherwise subtract the amount, update the balance, and return it.
    if amount <=0:
        raise InvalidAmountError(amount," Withdrawal amount must be positive.")
    if amount >accounts[account_id]:
        raise InsufficientFundsError(amount,f"Insufficient funds in {account_id}.")
    else:
        accounts[account_id] -=amount
        return accounts[account_id]


def process_withdrawal(account_id, amount):
    """TODO STEP 3 -- call withdraw(...) inside try/except and handle:
    - KeyError: "Unknown account: {account_id}"
    - InvalidAmountError: "Withdrawal amount must be positive."
    - InsufficientFundsError: "Insufficient funds in {account_id}."

    """
    try:
        wd=withdraw(account_id,amount)
        print(f"OK {wd}")
    except KeyError:
        print(f"Unknown account: {account_id}")
    except InvalidAmountError as I:
        print(f"{I.message} {I.amount}")
    except InsufficientFundsError as Inf:
        print(f"{Inf.message} {Inf.amount}")



# --- Test cases ---
process_withdrawal("ACC-1001", 1200)
# OK: 3800.0
process_withdrawal("ACC-9999", 100)
# KeyError handled
process_withdrawal("ACC-1002", -50)
# InvalidAmountError handled
process_withdrawal("ACC-1003", 100)
# InsufficientFundsError handled