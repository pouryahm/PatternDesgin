from abc import ABC, abstractmethod


# Abstracts Class and  methods
class ProductBase(ABC):
    @property
    @abstractmethod
    def detail(self):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @property
    @abstractmethod
    def shipping(self):
        pass


class DetailBase(ABC):
    def show(self):
        pass


# RUGS DETAIL AND CLASSES
class GiftCardDetail(DetailBase):
    def __init__(self, card):
        self.card = card

    def show(self):
        return f'the GiftCard Company is {self.card.company}'


class GiftCardPrice(DetailBase):
    def __init__(self, card):
        self.card = card

    def show(self):
        return f' the Gift Card Price is between {self.card.min_price} and {self.card.max_price}'


class GiftCardShipping(DetailBase):
    def __init__(self, card):
        self.card = card

    def show(self):
        return f' The  Gift Card Ship by {self.card.shipping_method} '


class GiftCard(ProductBase):
    def __init__(self, company, min_price, max_price, shipping_method):
        self.company = company
        self.min_price = min_price
        self.max_price = max_price
        self.shipping_method = shipping_method

    @property
    def detail(self):
        return GiftCardDetail(self)

    @property
    def price(self):
        return GiftCardPrice(self)

    @property
    def shipping(self):
        return GiftCardShipping(self)


# RUGS DETAIL AND CLASSES
class RugsDetail(DetailBase):
    def __init__(self, rug):
        self.rug = rug

    def show(self):
        return f"rug name is {self.rug.name}"


class RugsPrice(DetailBase):
    def __init__(self, rug):
        self.rug = rug

    def show(self):
        return f'the price is {self.rug._price}'


class RugShipping(DetailBase):
    def __init__(self, rug):
        self.rug = rug

    def show(self):
        return f'shipping method is {self.rug.shippingMethod}'


class Rugs(ProductBase):
    def __init__(self, name, price, shippingMethod):
        self.name = name
        self._price = price
        self.shippingMethod = shippingMethod

    @property
    def detail(self):
        return RugsDetail(self)

    @property
    def price(self):
        return RugsPrice(self)

    @property
    def shipping(self):
        return RugShipping(self)


if __name__ == "__main__":
    r1 = Rugs("persian rug", 150, "plane")
    r2 = Rugs("ghom rug", 170, "car")

    g1 = GiftCard("Google", 20, 60, "bike")
    # g2 = Giftcard()
    #
    products = [r1, r2, g1]
    for product in products:
        print(product.detail.show())
        print(product.price.show())
        print(product.shipping.show())
        print("\t-------------\t")
