from დავალებაN24 import Vehicle, ElectricVehicle
import unittest


class TestVehicle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Let's set up testing of the code")

    @classmethod
    def tearDownClass(cls):
        print("finish of a code testing!")

    def setUp(self):
        print("Let's set up testing of the case!")
        self.ferrari = Vehicle('Ferrari', 'Ferrari43Ga', 'sportCar')
        self.bugatti = Vehicle('Bugatti', 'BugattiX89', 'sportCar')

    def tearDown(self):
        print('finish the testing of the case')

    def test_fuel_up(self):
        self.assertEqual(self.ferrari.drive, 'The Ferrari43Ga is now driving.')
        self.assertEqual(self.bugatti.drive, 'The BugattiX89 is now driving.')

    def test_drive(self):
        self.assertEqual(self.ferrari.fuel_up, 'Gas tank is now full.')
        self.assertEqual(self.bugatti.fuel_up, 'Gas tank is now full.')


class Test_Electrict(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Let's set up testing of the Electric")

    @classmethod
    def tearDownClass(cls):
        print("finish of Electric testing!")

    def setUp(self):
        print("Let's set up testing of the case!")
        self.electro_ferrari = ElectricVehicle('Ferrari', 'Ferrari6Gl', 'electric')
        self.electro_bugatti = ElectricVehicle('Bugatti', 'BugattiJ4', 'electric')

    def tearDown(self):
        print('finish the testing of the case')

    def test_charge(self):
        self.assertEqual(self.electro_ferrari.charge, 'The vehicle is now charged.')
        self.assertEqual(self.electro_bugatti.charge, 'The vehicle is now charged.')

    def test_fuel_up(self):
        self.assertEqual(self.electro_ferrari.fuel_up, 'This vehicle has no fuel tank!')
        self.assertEqual(self.electro_bugatti.fuel_up, 'This vehicle has no fuel tank!')

    def test_drive(self):
        self.assertEqual(self.electro_ferrari.drive, 'The Ferrari6Gl is now driving.')
        self.assertEqual(self.electro_bugatti.drive, 'The BugattiJ4 is now driving.')
