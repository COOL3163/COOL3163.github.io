#!/usr/bin/env python3

import random
import time
import os
from hong_kong_sustainability_facts import HK_SUSTAINABILITY_FACTS, LOCATION_SPECIFIC_FACTS, SUSTAINABILITY_TIPS

class SustainabilityGame:
    def __init__(self):
        self.player_name = ""
        self.eco_points = 0
        self.days = 1
        self.energy = 100
        self.sustainability_level = 0
        self.facts_shown = set()
        self.tips_shown = set()
        self.locations = {
            "home": {"description": "Your apartment in Hong Kong", "actions": ["save_energy", "reduce_waste", "rest"]},
            "work": {"description": "Your office in Central", "actions": ["use_public_transport", "reduce_paper", "advocate_sustainability"]},
            "market": {"description": "Local wet market in Mong Kok", "actions": ["buy_local_produce", "reduce_plastic", "educate_vendors"]},
            "beach": {"description": "Repulse Bay Beach", "actions": ["clean_beach", "join_conservation", "raise_awareness"]},
            "park": {"description": "Hong Kong Park", "actions": ["plant_trees", "water_conservation", "community_garden"]}
        }
        self.action_impacts = {
            "save_energy": {"eco_points": -5, "energy": 10, "sustainability": 0.5},
            "reduce_waste": {"eco_points": -10, "energy": 15, "sustainability": 0.5},
            "rest": {"eco_points": 0, "energy": 50, "sustainability": 0},
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
            "community_garden": {"eco_points": 20, "energy": -25, "sustainability": 1}
        }
        self.tips = [
            "Bring your own shopping bag to reduce waste.",
            "Use a reusable water bottle instead of buying bottled water.",
            "Take public transport to reduce your carbon footprint.",
            "Support local farms by purchasing locally grown produce.",
            "Turn off unnecessary lights to save energy."
        ]

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self):
        self.clear_screen()
        print("\n" + "=" * 60)
        print(f"{'HONG KONG SUSTAINABILITY CHALLENGE':^60}")
        print("=" * 60)
        print(f"Player: {self.player_name} | Day: {self.days} | Eco Points: {self.eco_points} | Energy: {self.energy}%")
        print(f"Sustainability Impact: {self.sustainability_level:.1f}")
        print("-" * 60)

    def get_player_info(self):
        self.clear_screen()
        print("\n" + "=" * 60)
        print(f"{'HONG KONG SUSTAINABILITY CHALLENGE':^60}")
        print("=" * 60)
        print("\nWelcome to the Hong Kong Sustainability Challenge!")
        print("Your mission is to improve sustainability in Hong Kong through")
        print("daily choices and actions. Navigate different locations, make")
        print("sustainable choices, and deal with Hong Kong's unique environmental challenges.")

        self.player_name = input("\nPlease enter your name: ")
        while not self.player_name.strip():
            self.player_name = input("Please enter a valid name: ")

        print(f"\nWelcome, {self.player_name}! Your sustainability journey in Hong Kong begins now.")
        self.show_random_fact()
        input("\nPress Enter to start the game...")

    def show_random_fact(self):
        available_facts = [f for f in HK_SUSTAINABILITY_FACTS if f not in self.facts_shown]
        if not available_facts:
            self.facts_shown = set()
            available_facts = HK_SUSTAINABILITY_FACTS

        fact = random.choice(available_facts)
        self.facts_shown.add(fact)
        print("\n" + "-" * 60)
        print("DID YOU KNOW? 🌿")
        print(fact)
        print("-" * 60)

    def display_location(self):
        location_data = self.locations[self.current_location]
        print(f"\nLocation: {self.current_location.title()} - {location_data['description']}")
        print("\nAvailable actions:")
        for i, action in enumerate(location_data["actions"], 1):
            print(f"{i}. {action.replace('_', ' ').title()} - {self.action_descriptions[action]}")

    def perform_action(self, action):
        impact = self.action_impacts[action]
        self.eco_points += impact["eco_points"]
        self.energy += impact["energy"]
        self.sustainability_level += impact["sustainability"]

        print(f"\nYou performed: {action.replace('_', ' ').title()}")
        print(f"Impact: {impact['eco_points']} Eco Points, {impact['energy']} Energy, {impact['sustainability']} Sustainability")

        if self.energy <= 0:
            print("\nYou're out of energy! Time to rest.")
            self.energy = 10

        time.sleep(2)

    def end_day(self):
        self.days += 1
        self.energy = min(100, self.energy + 20)  # Reduced energy recovery
        print("\n" + "-" * 60)
        print(f"End of Day {self.days-1}")
        print(f"Total Eco Points: {self.eco_points}")
        print(f"Sustainability Impact: {self.sustainability_level:.1f}")

        status = self.get_sustainability_status()
        print(f"Status: {status}")
        print("-" * 60)
        self.show_random_fact()
        input("\nPress Enter to continue to the next day...")

    def get_sustainability_status(self):
        if self.sustainability_level < 5:
            return "Hong Kong is still facing significant environmental challenges."
        elif self.sustainability_level < 10:
            return "Small improvements are visible in Hong Kong's environment."
        elif self.sustainability_level < 20:
            return "Your efforts are making a noticeable difference in Hong Kong!"
        else:
            return "Remarkable progress! Hong Kong is becoming a model for urban sustainability."

    def game_over(self):
        self.clear_screen()
        print("\n" + "=" * 60)
        print(f"{'GAME OVER - FINAL RESULTS':^60}")
        print("=" * 60)
        print(f"Player: {self.player_name}")
        print(f"Days Played: {self.days}")
        print(f"Total Eco Points: {self.eco_points}")
        print(f"Final Sustainability Impact: {self.sustainability_level:.1f}")

        message = self.get_final_message()
        print(f"\n{message}")
        self.show_random_fact()
        print("\nThank you for playing the Hong Kong Sustainability Challenge!")
        print("=" * 60)

    def get_final_message(self):
        if self.sustainability_level < 10:
            return "Your efforts were modest, but every action counts in the fight for sustainability."
        elif self.sustainability_level < 25:
            return "You've made a positive impact on Hong Kong's environment!"
        elif self.sustainability_level < 50:
            return "Great work! Your dedication has significantly improved Hong Kong's sustainability."
        else:
            return "Extraordinary achievement! You've transformed Hong Kong into a beacon of urban sustainability."

    def play(self):
        self.get_player_info()

        game_duration = 7  # Game lasts for 7 days

        while self.days <= game_duration:
            self.print_header()
            self.display_location()

            print("\nWhat would you like to do?")
            print("1-3. Perform an action at this location")
            print("4. Change location")
            print("5. End the day")
            print("6. Quit game")
            print("7. Learn a sustainability fact")

            choice = input("\nEnter your choice (1-7): ")

            if choice in ['1', '2', '3']:
                action_idx = int(choice) - 1
                if action_idx < len(self.locations[self.current_location]["actions"]):
                    action = self.locations[self.current_location]["actions"][action_idx]
                    self.perform_action(action)
                else:
                    print("\nInvalid action number. Try again.")
                    time.sleep(1)

            elif choice == '4':
                self.print_header()
                self.display_locations()
                loc_choice = input("\nEnter location number: ")
                try:
                    loc_idx = int(loc_choice) - 1
                    if 0 <= loc_idx < len(self.locations):
                        self.current_location = list(self.locations.keys())[loc_idx]
                        print(f"\nTraveled to {self.current_location.title()}")
                        self.energy -= 5  # Travel consumes energy
                        time.sleep(1)
                    else:
                        print("\nInvalid location number. Try again.")
                        time.sleep(1)
                except ValueError:
                    print("\nPlease enter a valid number.")
                    time.sleep(1)

            elif choice == '5':
                self.end_day()

            elif choice == '6':
                confirm = input("\nAre you sure you want to quit? (y/n): ")
                if confirm.lower() == 'y':
                    break

            elif choice == '7':
                self.show_random_fact()
                input("\nPress Enter to continue...")

            else:
                print("\nInvalid choice. Please enter a number from 1 to 7.")
                time.sleep(1)

        self.game_over()

if __name__ == "__main__":
    game = SustainabilityGame()
    game.play()