import requests

API_KEY = 'fc90de97e8336aaa4722a2ad9435206f'
BASE_URL = 'http://data.fixer.io/api/'


def get_rial_rates():
    url = BASE_URL + 'latest'
    params = {
        'access_key': API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        # ✅ مقدار نرخ ریال (IRR)
        irr_rate = data['rates'].get('IRR')  # .get() ایمن‌تر از [] است
        # print("IRR rate:", irr_rate)

        return irr_rate
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None


# ===================== Old System: Store Products =====================

class Clothing:
    def __init__(self, name, price, size):
        self.name = name
        self.price = price  # price in Toman
        self.size = size

    def __str__(self):
        return f"{self.name} ({self.size}) - {self.price:,} Toman"


class Electronic:
    def __init__(self, name, price, warranty_years):
        self.name = name
        self.price = price  # price in Toman
        self.warranty_years = warranty_years

    def __str__(self):
        return f"{self.name} ({self.warranty_years} years warranty) - {self.price:,} Toman"


class Book:
    def __init__(self, name, price, author):
        self.name = name
        self.price = price  # price in Toman
        self.author = author

    def __str__(self):
        return f"'{self.name}' by {self.author} - {self.price:,} Toman"


# ===================== Currency Adapter =====================
class CurrencyAdapter:
    def __init__(self, irr_rate):
        self.irr_rate = irr_rate

    def convert(self, product):
        dollar_price = product.price / self.irr_rate
        return f"{product.name} -> {round(dollar_price, 2)} $"


# ===================== Sample Inventory =====================

if __name__ == "__main__":
    products = [
        Clothing("Nike T-Shirt", 850000, "L"),
        Electronic("iPhone 14", 70000000, 2),
        Book("Atomic Habits", 1100000, "James Clear")
    ]

    print("🛍 Product List (Toman):")
    for item in products:
        print("-", item)

    adaptorRate = CurrencyAdapter(get_rial_rates())

    print("🛍 Product List (Dollar):")
    for item in products:
        print("-", adaptorRate.convert(item))
