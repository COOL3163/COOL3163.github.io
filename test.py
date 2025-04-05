#!/usr/bin/env python3

import unittest
from io import StringIO
from unittest.mock import patch
import sys
from sustainability_game import SustainabilityGame

class TestSustainabilityGame(unittest.TestCase):

    def setUp(self):
        self.game = SustainabilityGame()
        self.game.player_name = "Test Player"

    def test_game_initialization(self):
        """Test that the game initializes with correct starting values"""
        self.assertEqual(self.game.eco_points, 0)
        self.assertEqual(self.game.days, 1)
        self.assertEqual(self.game.energy, 100)
        self.assertEqual(self.game.sustainability_level, 0)
        self.assertEqual(self.game.current_location, "home")

    def test_perform_action(self):
        """Test that performing an action correctly updates game state"""

        initial_eco_points = self.game.eco_points
        initial_energy = self.game.energy
        initial_sustainability = self.game.sustainability_level

        action = "save_energy"
        impact = self.game.action_impacts[action]


        captured_output = StringIO()
        sys.stdout = captured_output

        self.game.perform_action(action)


        sys.stdout = sys.__stdout__


        self.assertEqual(self.game.eco_points, initial_eco_points + impact["eco_points"])
        self.assertEqual(self.game.energy, initial_energy + impact["energy"])
        self.assertEqual(self.game.sustainability_level, initial_sustainability + impact["sustainability"])


        output = captured_output.getvalue()
        self.assertIn("You performed: Save Energy", output)

    def test_change_location(self):
        """Test that changing location works correctly"""

        self.assertEqual(self.game.current_location, "home")


        self.game.current_location = "work"
        self.assertEqual(self.game.current_location, "work")


        location_actions = self.game.locations["work"]["actions"]
        self.assertIn("use_public_transport", location_actions)
        self.assertIn("reduce_paper", location_actions)
        self.assertIn("advocate_sustainability", location_actions)

    def test_end_day(self):
        """Test that ending a day correctly updates game state"""
        initial_days = self.game.days


        self.game.energy = 50


        captured_output = StringIO()
        sys.stdout = captured_output

        with patch('builtins.input', return_value=''):
            self.game.end_day()


        sys.stdout = sys.__stdout__


        self.assertEqual(self.game.days, initial_days + 1)


        self.assertEqual(self.game.energy, 80)  # 50 + 30 = 80


        output = captured_output.getvalue()
        self.assertIn("End of Day", output)

    def test_display_random_fact(self):
        """Test that displaying a random fact works"""

        captured_output = StringIO()
        sys.stdout = captured_output

        self.game.display_random_fact()


        sys.stdout = sys.__stdout__


        output = captured_output.getvalue()
        self.assertIn("Did you know?", output)


        self.assertEqual(len(self.game.shown_facts), 1)

    def test_display_random_tip(self):
        """Test that displaying a random tip works"""

        captured_output = StringIO()
        sys.stdout = captured_output

        self.game.display_random_tip()


        sys.stdout = sys.__stdout__


        output = captured_output.getvalue()
        self.assertIn("Sustainability Tip:", output)


        self.assertEqual(len(self.game.shown_tips), 1)

    def test_display_location_fact(self):
        """Test that displaying a location fact works"""

        captured_output = StringIO()
        sys.stdout = captured_output

        self.game.display_location_fact()


        sys.stdout = sys.__stdout__


        output = captured_output.getvalue()
        self.assertIn("Home Fact:", output)


        self.assertEqual(len(self.game.shown_location_facts["home"]), 1)

if __name__ == '__main__':
    unittest.main()
