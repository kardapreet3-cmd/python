class pay:
    def payment(self):
        print("Payment")
class upi(pay):
    def payment(self):
        print("upi")
class check(pay):
    def payment(self):
        print("check")
class bank(pay):
    def payment(self):
        print("bank")
u=upi()
u.payment()
p=pay()
p.payment()
c=check()
c.payment()
p=pay()
p.payment()
b=bank()
b.payment()
p=pay()
p.payment()