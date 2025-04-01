#!/usr/bin/env python3

import unittest
from io import StringIO
from unittest.mock import patch
import sys
from sustainability_game import SustainabilityGame

class TestSustainabilityGame(unittest.TestCase):

    def setUp(self):
        self.game = SustainabilityGame()
        # Pre-set player name to avoid input in tests
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
        # Save initial values
        initial_eco_points = self.game.eco_points
        initial_energy = self.game.energy
        initial_sustainability = self.game.sustainability_level

        # Perform the "save_energy" action
        action = "save_energy"
        impact = self.game.action_impacts[action]

        # Redirect stdout to capture print output
        captured_output = StringIO()
        sys.stdout = captured_output

        self.game.perform_action(action)

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Check that values were updated correctly
        self.assertEqual(self.game.eco_points, initial_eco_points + impact["eco_points"])
        self.assertEqual(self.game.energy, initial_energy + impact["energy"])
        self.assertEqual(self.game.sustainability_level, initial_sustainability + impact["sustainability"])

        # Check that the output contains the expected text
        output = captured_output.getvalue()
        self.assertIn("You performed: Save Energy", output)

    def test_change_location(self):
        """Test that changing location works correctly"""
        # Start at home
        self.assertEqual(self.game.current_location, "home")

        # Change location to work
        self.game.current_location = "work"
        self.assertEqual(self.game.current_location, "work")

        # Check that actions for this location are available
        location_actions = self.game.locations["work"]["actions"]
        self.assertIn("use_public_transport", location_actions)
        self.assertIn("reduce_paper", location_actions)
        self.assertIn("advocate_sustainability", location_actions)

    def test_end_day(self):
        """Test that ending a day correctly updates game state"""
        initial_days = self.game.days

        # Set energy to a low value to test recovery
        self.game.energy = 50

        # Redirect stdout to capture print output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Mock the input function for "Press Enter to continue..."
        with patch('builtins.input', return_value=''):
            self.game.end_day()

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Check that day incremented
        self.assertEqual(self.game.days, initial_days + 1)

        # Check that energy recovered but didn't exceed 100
        self.assertEqual(self.game.energy, 80)  # 50 + 30 = 80

        # Check that output includes expected text
        output = captured_output.getvalue()
        self.assertIn("End of Day", output)

    def test_display_random_fact(self):
        """Test that displaying a random fact works"""
        # Redirect stdout to capture print output
        captured_output = StringIO()
        sys.stdout = captured_output

        self.game.display_random_fact()

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Check that output includes expected text
        output = captured_output.getvalue()
        self.assertIn("Did you know?", output)

        # Check that a fact was marked as shown
        self.assertEqual(len(self.game.shown_facts), 1)

    def test_display_random_tip(self):
        """Test that displaying a random tip works"""
        # Redirect stdout to capture print output
        captured_output = StringIO()
        sys.stdout = captured_output

        self.game.display_random_tip()

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Check that output includes expected text
        output = captured_output.getvalue()
        self.assertIn("Sustainability Tip:", output)

        # Check that a tip was marked as shown
        self.assertEqual(len(self.game.shown_tips), 1)

    def test_display_location_fact(self):
        """Test that displaying a location fact works"""
        # Redirect stdout to capture print output
        captured_output = StringIO()
        sys.stdout = captured_output

        self.game.display_location_fact()

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Check that output includes expected text
        output = captured_output.getvalue()
        self.assertIn("Home Fact:", output)

        # Check that a location fact was marked as shown
        self.assertEqual(len(self.game.shown_location_facts["home"]), 1)

if __name__ == '__main__':
    unittest.main()
