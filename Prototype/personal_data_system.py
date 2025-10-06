from copy import deepcopy


class Person:
    def __init__(self, name, age, note):
        self.name = name
        self.age = age
        self.note = note or []

    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, data={self.note})"


if __name__ == "__main__":
    p1 = Person("Pouria", 25, ["pouria@example.com", "VIP"])
    p2 = p1.clone()
    p2.note.append("new item")

    print(p1)
    print(p2)
