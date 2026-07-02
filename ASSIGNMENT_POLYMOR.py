class UPI:
    def payment(self):
        print("Payment done by UPI")
class Bank:
    def payment(self):
        print("Payment done by Bank")
class check:
    def payment(self):
        print("Payment done by check")
U=UPI()
B=Bank()
c=check()
U.payment()
B.payment()
c.payment()
