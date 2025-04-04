#!/usr/bin/env python3

import random

class SustainabilityGame:
    def __init__(self):
        self.player_name = ""
        self.eco_points = 0
        self.days = 1
        self.energy = 100
        self.sustainability_level = 0
        self.current_location = "home"
        self.locations = {
            "home": {"description": "Your apartment in Hong Kong", "actions": ["save_energy", "reduce_waste", "rest", "consume_alot_of_meat"]},
            "work": {"description": "Your office in Central", "actions": ["use_public_transport", "reduce_paper", "advocate_sustainability", "eat_junk_food", "Drive_a_car"]},
            "market": {"description": "Local wet market in Mong Kok", "actions": ["buy_local_produce", "reduce_plastic", "educate_vendors", "use_single_use_plastics", "buy_fast_fashion"]},
            "beach": {"description": "Repulse Bay Beach", "actions": ["clean_beach", "join_conservation", "raise_awareness", "order_takeout"]},
            "park": {"description": "Hong Kong Park", "actions": ["plant_trees", "water_conservation", "community_garden", "skip_recycling", "consume_sugar_drinks"]}
        }
        self.action_impacts = {
            # Rest
            "rest": {"eco_points": 0, "energy": 50, "sustainability": 0},

            # Positive actions
            "save_energy": {"eco_points": 10, "energy": -15, "sustainability": 0.3},
            "reduce_waste": {"eco_points": 8, "energy": -10, "sustainability": 0.5},
            "use_public_transport": {"eco_points": 5, "energy": -10, "sustainability": 0.7},
            "reduce_paper": {"eco_points": 3, "energy": -5, "sustainability": 0.3},
            "advocate_sustainability": {"eco_points": 10, "energy": -25, "sustainability": 1},
            "buy_local_produce": {"eco_points": 5, "energy": -10, "sustainability": 0.6},
            "reduce_plastic": {"eco_points": 7, "energy": -5, "sustainability": 0.5},
            "educate_vendors": {"eco_points": 15, "energy": -20, "sustainability": 0.8},
            "clean_beach": {"eco_points": 20, "energy": -30, "sustainability": 1},
            "join_conservation": {"eco_points": 25, "energy": -35, "sustainability": 1.2},
            "raise_awareness": {"eco_points": 15, "energy": -25, "sustainability": 0.9},
            "plant_trees": {"eco_points": 20, "energy": -30, "sustainability": 1.1},
            "water_conservation": {"eco_points": 15, "energy": -20, "sustainability": 0.8},
            "community_garden": {"eco_points": 20, "energy": -25, "sustainability": 1},

            # Negative actions
            "consume_alot_of_meat": {"eco_points": -18, "energy": 20, "sustainability": -1.0},
            "eat_junk_food": {"eco_points": -10, "energy": 25, "sustainability": -1},
            "drive_a_car": {"eco_points": -25, "energy": 30, "sustainability": -0.8},
            "use_single_use_plastics": {"eco_points": -5, "energy": 20, "sustainability": -0.5},
            "buy_fast_fashion": {"eco_points": -30, "energy": 15, "sustainability": -1.2},
            "order_takeout": {"eco_points": -8, "energy": 10, "sustainability": -0.4},
            "skip_recycling": {"eco_points": -12, "energy": 25, "sustainability": -0.7},
            "consume_sugar_drinks": {"eco_points": -10, "energy": 15, "sustainability": -0.6}
        }
        self.tips = [
            "Bring your own shopping bag to reduce waste.",
            "Use a reusable water bottle instead of buying bottled water.",
            "Take public transport to reduce your carbon footprint.",
            "Support local farms by purchasing locally grown produce.",
            "Turn off unnecessary lights to save energy."
        ]

    def perform_action(self, action):
        """Perform an action and update the game state."""
        if action not in self.action_impacts:
            return {"error": "Invalid action"}
        impact = self.action_impacts[action]
        self.eco_points += impact["eco_points"]
        self.energy += impact["energy"]
        self.sustainability_level += impact["sustainability"]
        return {
            "action": action,
            "eco_points": impact["eco_points"],
            "energy": impact["energy"],
            "sustainability": impact["sustainability"]
        }

    def end_day(self):
        """End the current day and recover energy."""
        self.days += 1
        self.energy = min(100, self.energy + 20)  # Reduced energy recovery
        return {
            "days": self.days,
            "energy": self.energy
        }

    def get_random_tip(self):
        """Return a random sustainability tip."""
        return random.choice(self.tips)