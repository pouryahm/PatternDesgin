from FactoryAndAbstractFactory.abstract_factory import Rugs


class PayPalPayment:
    def __init__(self, amount):
        self.amount = amount

    def pay_done(self):
        return f" pay has done :  {self.amount} $"


class PayAdaptor:
    def __init__(self, rate):
        self.rate = rate

    def pay(self, product):
        dollar = self.rate * product._price
        paypal = PayPalPayment(dollar)
        return paypal.pay_done()


if __name__ == '__main__':
    r1 = Rugs("persian ruge", 2000, "plain")

    adaptor = PayAdaptor(20000)
    print(adaptor.pay(r1))
