import unittest
from app.mission import Mission

class MissionTestCase(unittest.TestCase):
    def setUp(self):
        self.mission = Mission(100)
    
    def test_if_bullets_is_an_integer(self):
        self.assertIsInstance(self.mission.bullets, int, msg = 'Bullets can only be a number')
    
    def test_correct_results(self):
        # test for correct results
        self.mission.dragons = 50
        self.mission.goToWar()
        self.assertEqual(self.mission.getStatus(), 'Mission won', msg = 'wrong results working')

        # test for wrong results
        self.mission.dragons = 100
        self.mission.goToWar()
        self.assertEqual(self.mission.getStatus(), 'Mission failed', msg = 'wrong results working')