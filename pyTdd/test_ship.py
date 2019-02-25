import unittest
from app.ship import Ship
class ShipTestCase(unittest.TestCase):
    def setUp(self):
        self.ship = Ship(10.4, 15.5)

    def test_crew(self):
        self.assertIsInstance(self.ship.crew, int, msg = 'Crew can only be a number')
        self.assertLessEqual(self.ship.crew, 100000, msg = 'Crew cant exeed 100000')
    
    def test_draft(self):
        self.assertIsInstance(self.ship.draft, float, msg = 'Draft can either be a number or a delcimal')
        self.assertLessEqual(self.ship.draft, 100, msg = 'Draft cant exeed 100')

    def test_correct_results(self):
        self.ship.draft = 40
        self.ship.crew = 10
        self.assertEqual('Loot', self.ship.is_worth_it(), msg = 'Wrong results generated')

    def test_wrong_results(self):
        self.ship.draft = 30
        self.ship.crew = 10
        self.assertEqual('Do not loot', self.ship.is_worth_it(), msg = 'Wrong results generated')