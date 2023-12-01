import json


class JsonFile:
    def __init__(self):
        self.filename = None
        self.python_dict = {}

    # 1
    def create_json_file(self, data, filename):
        self.python_dict = dict(data)
        self.filename = f'{filename}.json'
        with open(self.filename, 'w') as j_file:
            json.dump(self.python_dict, j_file, indent=3)

    # 2
    def update_value(self,  keys, new_values):

        with open(self.filename) as j_file:
            self.python_dict = json.load(j_file)

        for key, value in zip(keys, new_values):
            if key in self.python_dict.keys():
                self.python_dict[key] = value

        with open(self.filename, 'w') as j_file:
            json.dump(self.python_dict, j_file, indent=3)

    def delete_key(self, keys):
        with open(self.filename) as j_file:
            self.python_dict = json.load(j_file)

        for key in keys:
            if key in self.python_dict.keys():
                del self.python_dict[key]

        with open(self.filename, 'w') as j_file:
            json.dump(self.python_dict, j_file, indent=3)

    def add_key(self, keys, values = None):
        with open(self.filename) as j_file:
            self.python_dict = json.load(j_file)

        if values == None:
            values = []
            for k in keys:
                values.append(None)
        for key, value in zip(keys, values):
            if key not in self.python_dict.keys():
                self.python_dict[key] = value

        with open(self.filename, 'w') as j_file:
            json.dump(self.python_dict, j_file, indent=3)


my_data = [('name', 'dato'), ('surname', 'bitsadze'), ('age', 19), ('country', 'georgia')]

my_file = JsonFile()
my_file.create_json_file(my_data, 'my info')

keys = ['name', 'country', 'age']
values = ['Dato', 'Georgia', 19]

my_file.update_value(keys, values)
my_file.delete_key(['age'])
my_file.add_key(['age', 'phone_number'], [19, '577957386'])


