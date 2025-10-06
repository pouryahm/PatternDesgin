class Fahrenheit:
    @staticmethod
    def call_Temp():
        return 70


class Celsius:
    def __init__(self, temp):
        self.temp = temp

    def show_temp(self):
        return f"the temperature is {self.temp} celsius"


class TempConvertor:
    def __init__(self, data: Fahrenheit):
        self.data = data

    def convert(self):
        f_temp = self.data.call_Temp()
        new_cels = (f_temp - 32) * (5 / 9)
        return f"new temp convert to {new_cels : .2f} C "


if __name__ == '__main__':
    f1 = Fahrenheit()
    adaptor = TempConvertor(f1)
    c1=Celsius(adaptor)

    print(c1.show_temp())
