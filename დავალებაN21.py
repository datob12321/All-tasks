import json
import pickle
import dill

# 1
def serialization(py_obj, filename):
    success = False
    try:
        with open(f"{filename}.json", 'w') as json_file:
            json.dump(py_obj, json_file)
            print('data is serialized with json')
            success = True
            print('------------------------------------------')
    except:
        print("Serialization was not successful with json!")
    if  success == False:
        try:
            with open(f"{filename}.pickle", 'wb') as pickle_file:
                pickle.dump(py_obj, pickle_file)
                print('data is serialized with pickle')
                success = True
                print('------------------------------------------')

        except:
            print("Serialization was not successful with pickle!")
        if  success == False:
            try:
                with open(f'{filename}.dill', 'wb') as dill_file:
                    dill.dump(py_obj, dill_file)
                    print('data is serialized with dill')
                    print('------------------------------------------')
            except:
                print("Serialization of the object is impossible!")


def deserialization(filename, lambda_arg = None):
    try:
        with open(f'{filename}.json', 'r') as json_file:
            python_obj = json.load(json_file)
            print('data is deserialized with json')
            print(python_obj)
            print('------------------------------------------')
    except:
        print("Deserialization was not successful with json!")
        try:
            with open(f'{filename}.pickle', 'rb') as pickle_file:
                python_obj = pickle.load(pickle_file)
                print('data is deserialized with pickle')
                print(python_obj.__dict__)
                print('------------------------------------------')
        except:
            print("Deserialization was not successful with pickle!")
            try:
                with open(f'{filename}.dill', 'rb') as dill_file:
                    python_obj = dill.load(dill_file)
                    print('data is deserialized with dill')
                    print(python_obj(lambda_arg))
                    print('------------------------------------------')
            except:
                print("Deserialization of the object is impossible!")
                print('------------------------------------------')


class Myclass:
    def __init__(self, par1=True, par2=False):
        self.par1 = par1
        self.par2 = par2

    def print1(self):
        print('some text1')

    def print2(self):
        print('some text2')


# my_dict = {1: "apple", 2: None, '3': {'name': 'dato', 'surname': 'bitsadze'}, 4: True}
# serialization(my_dict, 'obj1')
# deserialization('obj1')
#
# obj = Myclass()
# serialization(obj, 'obj2')
# deserialization('obj2')
#
# func = lambda x: x.upper()
# serialization(func, 'obj3')
# deserialization('obj3', 'python deserialization')
# print()

# 2
from random import choice, randint

class Sinking:
    winner = None
    def __init__(self, username, ship1, ship2, ship3):
        self.name = username
        self.ship1 = ship1
        self.ship2 = ship2
        self.ship3 = ship3
        self.squares = [x for x in range(1, 21)]
        self.positions = []
        while True:
            rand = randint(1, 20)
            if not rand in self.positions:
                self.positions.append(rand)
                if len(self.positions) == 6:
                    break
        self.ships = {ship1: [self.positions[0], self.positions[1], self.positions[2]], ship2: [self.positions[3], self.positions[4]], ship3: [self.positions[5]]}


    def start_game(self):
        comp = Sinking('computer', 'ship1', 'ship2', 'ship3')

        comp_attacks = []
        user_attacks = []

        while True:
            try:
                user_attack = int(input('Attack the opponent(Enter the number between 1 and 20): '))
                if not user_attack in user_attacks and 1 <= user_attack <= 20:
                    user_attacks.append(user_attack)
                    for ship in comp.ships.values():
                        if user_attack in ship:
                            ship.remove(user_attack)
                            comp.positions.remove(user_attack)
                            print(comp.ships)
                else:
                    print("You have already entered this number!")
            except:
                print('Invalid input')

            comp_attack = randint(1, 20)
            if not comp_attack in comp_attacks and 1 <= comp_attack <= 20:
                comp_attacks.append(comp_attack)
                for ship in self.ships.values():
                    if comp_attack in ship:
                        ship.remove(comp_attack)
                        self.positions.remove(comp_attack)
                        print(self.ships)
            else:
                print("Comp has already entered this number!")

            if self.positions == []:
                Sinking.winner = comp.name
            elif comp.positions == []:
                Sinking.winner = self.name

                if Sinking.winner != None:
                    print(f'Winner is {Sinking.winner}')
                    break


# my_ship = Sinking('dato', 'my_ship1', 'my_ship2', 'my_ship3')
# my_ship.start_game()
