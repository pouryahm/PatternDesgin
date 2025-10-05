from abc import ABC, abstractmethod


# ==================== Product Factory and Car Types ===============
class ProductBase(ABC):
    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def engine(self):
        pass


class SuvBase(ProductBase):
    def info(self):
        pass

    def engine(self):
        pass


class CoupeBase(ProductBase):
    def info(self):
        pass

    def engine(self):
        pass


# ==================== BMW MODELS ===============

class BmwSuv(SuvBase):
    def __init__(self, car):
        self.car = car

    def info(self):
        return f" === BMW SUV === \n Color: \"{self.car.color}\" \n Engine: \"{self.car.engine}cc\" \n GearBox: \"{self.car.gearbox}\""

    def engine(self):
        return f"{self.car.engine}cc"

    def __str__(self):
        return self.info()


class BmwCoupe(CoupeBase):
    def __init__(self, car):
        self.car = car


# ==================== Car Base Factory ===============
class CarFactoryBase(ABC):
    @abstractmethod
    def create_suv(self):
        pass

    @abstractmethod
    def create_coupe(self):
        pass


# ==================== BMW Factory ===============
class BmwFactory(CarFactoryBase):
    def __init__(self, engine, color, gearbox):
        self.engine = engine
        self.color = color
        self.gearbox = gearbox

    def create_suv(self):
        return BmwSuv(self)

    def create_coupe(self):
        return BmwCoupe(self)


if __name__ == "__main__":
    c1 = BmwFactory(3500, "black", "AT")
    print(c1.create_suv())
