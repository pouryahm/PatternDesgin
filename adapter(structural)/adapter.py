from FactoryAndAbstractFactory.abstract_factory import Rugs


class PriceAdapter:
    def __init__(self, rate):
        self.rate = rate

    def exchange(self, product):
        return self.rate * product._price


if __name__ == "__main__":
    r1 = Rugs("persian", 20, "bike")
    r2 = Rugs("nayin", 15, "bike")
    r3 = Rugs("tabriz", 13, "bike")
    rugs = [r1, r2, r3]

    adapter = PriceAdapter(rate=100000)

    for rug in rugs:
        print(f"{rug.name} : {adapter.exchange(rug)}")
