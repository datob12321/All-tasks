import pytest
import დავალებაN25
from დავალებაN25 import Vehicle, ElectricVehicle


class TestCars:
    def setup(self):
        self.car1 = Vehicle('BMW', 'X6', 'SportCar')
        self.car2 = Vehicle('Opel', 'Opel Astra', 'Normal')
        print("setting up testing")

    def teardown(self):
        print("tearing down testing")

    def test_fuel_up(self, capfd):
        self.car1.fuel_up()
        out, err = capfd.readouterr()
        assert out == 'Gas tank is now full.\n'

    def test_drive(self):
        assert self.car1.drive() == 'The X6 is now driving.'


class TestElectricCars:
    def setup(self):
        self.car1 = ElectricVehicle('BMW', 'X6-electric', 'Electric')
        self.car2 = ElectricVehicle('Opel', 'Opel Astra-electric', 'Electric')
        print("setting up testing")

    def teardown(self):
        print("tearing down testing")

    def test_fuel_up(self, capfd):
        self.car1.fuel_up()
        out, err = capfd.readouterr()
        assert out == 'This vehicle has no fuel tank!\n'

    def test_charge(self):
        assert self.car1.charge() == 'The vehicle is now charged.'
