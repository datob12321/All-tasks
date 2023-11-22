from time import time


# 1
class Car:

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


# 2

class MyClass:

    def __init__(self, name, nation):
        self.name = name
        self.nation = nation

    @staticmethod
    def dec_func(func):
        def wrapper(obj, *args):
            start_time = time()
            func(obj, *args)
            end_time = time()
            execute_time = end_time-start_time
            print(execute_time)
            print(obj.__dict__)
        return wrapper

    @dec_func
    def obj_method(self):
        print(f'Hello, I am an instance of {self.__class__.__name__} class.')

    @dec_func
    def obj_method1(self, num1, num2):
        print(num1+num2)

    @dec_func
    def info(self):
        print(f'My name is {self.name} and I am from {self.nation}')


# obj = MyClass('Dato', 'Georgia')
# obj.obj_method()
# print()
# obj.obj_method1(43, 54)
# print()
# obj.info()


# 3

class Validator:
    def __init__(self, attr_name, validation_func):
        self.attr_name = attr_name
        self.validation_func = validation_func

    def __get__(self, instance, owner):
        return instance.__dict__[self.attr_name]

    def __set__(self, instance, value):
        if self.validation_func(value):
            instance.__dict__[self.attr_name] = value


class Car1:

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def __init__(self, brand: str, model: str, year: int):

        self.__brand = brand
        self.__model = model
        self.__year = year

    @staticmethod
    def valid_year(year):
        if isinstance(year, int) and year > 0:
            return True
        else:
            return False

    brandVal = Validator('_Car1__brand', lambda x: type(x) == str)
    modelVal = Validator('_Car1__model', lambda x: type(x) == str)
    yearVal = Validator('_Car1__year', valid_year)


# myCar = Car1('BMW', 'AE3', 35)
# myCar.brandVal = -4
# myCar.yearVal = '3'
# print(myCar.yearVal)
