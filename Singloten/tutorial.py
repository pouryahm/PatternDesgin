## id generator

class SingleId(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class IdGenerator(metaclass=SingleId):
    def __init__(self):
        self.id = 0

    def next_id(self):
        self.id += 1
        return self.id


if __name__ == "__main__":
    g1=IdGenerator()
    g2=IdGenerator()

    print(g1.next_id())
    print(g2.next_id())