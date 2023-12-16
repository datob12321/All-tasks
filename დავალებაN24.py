class Vehicle:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type
        self.gas_tank_size = 14
        self.fuel_level = 0

    @property
    def fuel_up(self):
        self.fuel_level = self.gas_tank_size
        return 'Gas tank is now full.'

    @property
    def drive(self):
        return f'The {self.model} is now driving.'


class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model, type)
        self.battery_size = 85
        self.charge_level = 0

    @property
    def charge(self):
        self.charge_level = 100
        return 'The vehicle is now charged.'

    @property
    def fuel_up(self):
        return 'This vehicle has no fuel tank!'
