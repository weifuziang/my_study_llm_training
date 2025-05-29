
__all__ = ["num","age","add"]
__age = 18
age = __age
num = 100


def __add(a, b):
    """求两个数据的和"""
    return num + b

def add(a, b):
    """求两个数据的和"""
    return num + b

print(__name__)
#被别的模块调用时，则不会被执行
if __name__ == "__main__":
    print(add(1, 2))
    print(__name__)
    print("hello world")