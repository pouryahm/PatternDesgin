from copy import deepcopy


class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, email={self.email})"


if __name__ == "__main__":
    p1 = Person("Pouria", 25, "pouria@example.com")
    p2 = p1.clone()
    p2.name = "Saba"

    print(p1)
    print(p2)
