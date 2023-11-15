# 1
from math import pi, pow


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * pow(self.radius, 2)


# 2
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError as z:
            return z


# 3
class ShoppingBasket:
    def __init__(self):
        self.list_of_products = []
        self.price = 0

    def add_item(self, product, price):
        self.list_of_products.append(product)
        self.price += price

    def remove_item(self, product, price):
        self.list_of_products.remove(product)
        self.price -= price

    def product_list(self):
        print(tuple(self.list_of_products))

    def total_price(self):
        print(self.price)

# 4


class BankAccount:

    def __init__(self, current_money=0):
        self.current_money = current_money

    def deposit(self, money):
        self.current_money += money

    def withdrawal(self, money):
        if self.current_money >= money:
            self.current_money -= money
        else:
            print('You have not enough money to withdrawal!')

    def transfer(self, money, other_account):
        if type(other_account) == BankAccount:
            self.current_money -= money
            other_account.current_money += money
        else:
            print('Enter valid account to transfer money!')

    def operations(self):
        while True:
            operation_num = input("1.deposit, 2.withdrawal, 3.transfer, 4.exit ")
            if operation_num == '1':
                deposit_money = int(input('Enter the deposit money: '))
                self.deposit(deposit_money)
            elif operation_num == '2':
                withdrawal_money = int(input('Enter the withdrawal money: '))
                self.withdrawal(withdrawal_money)
            elif operation_num == '3':
                transfer_money = int(input('Enter the transfer money: '))
                self.transfer(transfer_money, BankAccount())
            else:
                break
