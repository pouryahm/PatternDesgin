from abc import ABC, abstractmethod


class Paypal:
    def pay(self, amount):
        return f"{amount} send to paypal "


# class Stripe:
#     def pay_strip(self, amount):
#         return f"{amount} send to strip "
#
#
# class Zarin:
#     def pay_zarin(self, amount):
#         return f"{amount} send to zarin "


class GlobalPayment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def process_payment(self):
        return self.amount


class Paypal_Adaptor(GlobalPayment):
    def __init__(self, amount):
        super().__init__(amount)
        self.service = Paypal()

    def process_payment(self):
        return self.service.pay(self.amount)


if __name__ == "__main__":
    a1 = Paypal_Adaptor(100000)
    print(a1.process_payment())
