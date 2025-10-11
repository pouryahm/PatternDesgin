from datetime import datetime


def log_time(fn):
    def internal_function(*args, **kwargs):
        start = datetime.now()
        result = fn(*args, **kwargs)
        end = datetime.now()
        print(end - start)
        return result

    return internal_function


@log_time
def test():
    pass


def test2():
    pass


if __name__ == "__main__":
    test()

    # line before function call
    test2()
    # line aftar function call
