
class InsufficientBalanceError(Exception):
    pass
Balance=999999990
amount=int(input("How many money to withdraw: "))


if amount > Balance:
    raise InsufficientBalanceError("Not enough balance")
print("transaction successful")