#  ============ Singleton With __NEW__ ( Way 1 ) =====================
# class Singleton:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance
# ============== Singleton With METACLASS =======================
# class singletonMeta(type):
#     _instances={}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances=super.__call__(*args, **kwargs)
#         return cls._instances[cls]
#
# ====================Logger example==============
class SingleMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=SingleMeta):
    def __init__(self):
        self.logs = []

    def log(self, msg):
        self.logs.append(msg)

    def show_logs(self):
        for log in self.logs:
            print(f"{log}")
        return None


if __name__ == "__main__":
    logger1 = Logger()
    logger2 = Logger()

    logger1.log("Start program")
    logger2.log("Something happened")

    # بررسی اینکه logger1 و logger2 یکی هستن
    print(logger1 is logger2)  # باید True باشه
    logger1.show_logs()  # باید دو پیام چاپ بشه
