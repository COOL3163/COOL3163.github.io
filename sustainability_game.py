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
        self.facts_shown = set()  # Track which facts have been shown to avoid repetition
        self.tips_shown = set()   # Track which tips have been shown
        self.locations = {
            "home": {"description": "Your apartment in Hong Kong", "actions": ["save_energy", "reduce_waste", "rest"]},
            "work": {"description": "Your office in Central", "actions": ["use_public_transport", "reduce_paper", "advocate_sustainability"]},
            "market": {"description": "Local wet market in Mong Kok", "actions": ["buy_local_produce", "reduce_plastic", "educate_vendors"]},
            "beach": {"description": "Repulse Bay Beach", "actions": ["clean_beach", "join_conservation", "raise_awareness"]},
            "park": {"description": "Hong Kong Park", "actions": ["plant_trees", "water_conservation", "community_garden"]}
        }
        self.current_location = "home"
        self.action_descriptions = {
            "save_energy": "Turn off unused appliances and use energy-efficient settings",
            "reduce_waste": "Separate recyclables and compost food waste",
            "rest": "Take a break and recharge your energy",
            "use_public_transport": "Take the MTR instead of a taxi",
            "reduce_paper": "Use digital documents instead of printing",
            "advocate_sustainability": "Promote sustainable practices at your workplace",
            "buy_local_produce": "Purchase locally grown vegetables to reduce carbon footprint",
            "reduce_plastic": "Bring your own bags and containers",
            "educate_vendors": "Talk to vendors about sustainable packaging",
            "clean_beach": "Pick up litter and plastics from the beach",
            "join_conservation": "Participate in marine conservation efforts",
            "raise_awareness": "Educate beach-goers about plastic pollution",
            "plant_trees": "Contribute to urban greening efforts",
            "water_conservation": "Help maintain efficient irrigation systems",
            "community_garden": "Work in the community garden growing local herbs"
        }
        self.action_impacts = {
            "save_energy": {"eco_points": 5, "energy": -10, "sustainability": 0.5},
            "reduce_waste": {"eco_points": 5, "energy": -15, "sustainability": 0.5},
            "rest": {"eco_points": 0, "energy": 50, "sustainability": 0},
            "use_public_transport": {"eco_points": 10, "energy": -10, "sustainability": 0.7},
            "reduce_paper": {"eco_points": 5, "energy": -5, "sustainability": 0.3},
            "advocate_sustainability": {"eco_points": 15, "energy": -25, "sustainability": 1},
            "buy_local_produce": {"eco_points": 10, "energy": -15, "sustainability": 0.6},
            "reduce_plastic": {"eco_points": 10, "energy": -10, "sustainability": 0.5},
            "educate_vendors": {"eco_points": 15, "energy": -20, "sustainability": 0.8},
            "clean_beach": {"eco_points": 20, "energy": -30, "sustainability": 1},
            "join_conservation": {"eco_points": 25, "energy": -35, "sustainability": 1.2},
            "raise_awareness": {"eco_points": 15, "energy": -25, "sustainability": 0.9},
            "plant_trees": {"eco_points": 20, "energy": -30, "sustainability": 1.1},
            "water_conservation": {"eco_points": 15, "energy": -20, "sustainability": 0.8},
            "community_garden": {"eco_points": 20, "energy": -25, "sustainability": 1}
        }
        self.events = [
            {"name": "Typhoon Warning", "description": "A typhoon is approaching Hong Kong. Emergency preparations are needed.",
             "impact": {"eco_points": -10, "energy": -20}},
            {"name": "Green Festival", "description": "A sustainability festival is happening at Tamar Park.",
             "impact": {"eco_points": 15, "energy": -15}},
            {"name": "Air Pollution Alert", "description": "High pollution levels today. Indoor activities recommended.",
             "impact": {"eco_points": -5, "energy": -15}},
            {"name": "Community Cleanup", "description": "Local community organizes a neighborhood cleanup.",
             "impact": {"eco_points": 20, "energy": -25}},
            {"name": "New Recycling Policy", "description": "Government announces improved recycling infrastructure.",
             "impact": {"eco_points": 10, "energy": 0}},
            {"name": "Water Shortage", "description": "Dongjiang water supply reduced due to drought in mainland China.",
             "impact": {"eco_points": -5, "energy": -10}},
            {"name": "Urban Heat Wave", "description": "Extreme temperatures in the concrete jungle of Hong Kong.",
             "impact": {"eco_points": -8, "energy": -25}},
            {"name": "Plastic Free Campaign", "description": "Local NGOs launch a campaign against single-use plastics.",
             "impact": {"eco_points": 12, "energy": -10}}
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
        print("\nYour actions will impact your Eco Points and the city's Sustainability Level.")
        print("\nThroughout the game, you'll learn real facts about Hong Kong's sustainability")
        print("challenges and how your choices can make a difference.")

        self.player_name = input("\nPlease enter your name: ")
        while not self.player_name.strip():
            self.player_name = input("Please enter a valid name: ")

        print(f"\nWelcome, {self.player_name}! Your sustainability journey in Hong Kong begins now.")

        # Show an initial sustainability fact
        self.show_random_fact()

        input("\nPress Enter to start the game...")

    def show_random_fact(self):
        """Display a random fact about sustainability in Hong Kong"""
        # First try to get facts we haven't shown yet
        available_facts = [f for f in HK_SUSTAINABILITY_FACTS if f not in self.facts_shown]

        # If we've shown all facts, reset the tracking
        if not available_facts:
            self.facts_shown = set()
            available_facts = HK_SUSTAINABILITY_FACTS

        fact = random.choice(available_facts)
        self.facts_shown.add(fact)

        print("\n" + "-" * 60)
        print("DID YOU KNOW? 🌿")
        print(fact)
        print("-" * 60)

    def show_location_fact(self):
        """Display a fact specific to the current location"""
        if random.random() < 0.5:  # 50% chance to show a location-specific fact
            location_facts = LOCATION_SPECIFIC_FACTS[self.current_location]
            fact = random.choice(location_facts)

            print("\n" + "-" * 60)
            print(f"ABOUT {self.current_location.upper()} IN HONG KONG 🌆")
            print(fact)
            print("-" * 60)

    def show_sustainability_tip(self):
        """Display a random sustainability tip"""
        # First try to get tips we haven't shown yet
        available_tips = [t for t in SUSTAINABILITY_TIPS if t not in self.tips_shown]

        # If we've shown all tips, reset the tracking
        if not available_tips:
            self.tips_shown = set()
            available_tips = SUSTAINABILITY_TIPS

        tip = random.choice(available_tips)
        self.tips_shown.add(tip)

        print("\n" + "-" * 60)
        print("SUSTAINABILITY TIP 💡")
        print(tip)
        print("-" * 60)

    def display_location(self):
        location_data = self.locations[self.current_location]
        print(f"\nLocation: {self.current_location.title()} - {location_data['description']}")

        # Chance to show a location-specific fact
        self.show_location_fact()

        print("\nAvailable actions:")
        for i, action in enumerate(location_data["actions"], 1):
            print(f"{i}. {action.replace('_', ' ').title()} - {self.action_descriptions[action]}")

    def display_locations(self):
        print("\nAvailable locations:")
        for i, location in enumerate(self.locations.keys(), 1):
            print(f"{i}. {location.title()} - {self.locations[location]['description']}")

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

        # Chance to show a sustainability tip after performing an action
        if random.random() < 0.3:  # 30% chance
            self.show_sustainability_tip()

        time.sleep(2)

    def random_event(self):
        if random.random() < 0.3:  # 30% chance of an event
            event = random.choice(self.events)
            print("\n" + "-" * 60)
            print(f"EVENT: {event['name']}")
            print(event['description'])

            self.eco_points += event['impact']['eco_points']
            self.energy += event['impact']['energy']

            print(f"Impact: {event['impact']['eco_points']} Eco Points, {event['impact']['energy']} Energy")
            print("-" * 60)

            if self.energy <= 0:
                print("\nYou're out of energy! Time to rest.")
                self.energy = 10

            # Chance to show a sustainability fact after an event
            if random.random() < 0.6:  # 60% chance after an event
                self.show_random_fact()

            time.sleep(3)

    def end_day(self):
        self.days += 1
        self.energy = min(100, self.energy + 30)  # Recover some energy for the next day

        print("\n" + "-" * 60)
        print(f"End of Day {self.days-1}")
        print(f"Total Eco Points: {self.eco_points}")
        print(f"Sustainability Impact: {self.sustainability_level:.1f}")

        # Assessment based on sustainability level
        if self.sustainability_level < 5:
            status = "Hong Kong is still facing significant environmental challenges."
        elif self.sustainability_level < 10:
            status = "Small improvements are visible in Hong Kong's environment."
        elif self.sustainability_level < 20:
            status = "Your efforts are making a noticeable difference in Hong Kong!"
        else:
            status = "Remarkable progress! Hong Kong is becoming a model for urban sustainability."

        print(f"Status: {status}")
        print("-" * 60)

        # Always show a fact at the end of the day
        self.show_random_fact()

        input("\nPress Enter to continue to the next day...")

    def game_over(self):
        self.clear_screen()
        print("\n" + "=" * 60)
        print(f"{'GAME OVER - FINAL RESULTS':^60}")
        print("=" * 60)
        print(f"Player: {self.player_name}")
        print(f"Days Played: {self.days}")
        print(f"Total Eco Points: {self.eco_points}")
        print(f"Final Sustainability Impact: {self.sustainability_level:.1f}")

        # Final assessment
        if self.sustainability_level < 10:
            message = "Your efforts were modest, but every action counts in the fight for sustainability."
        elif self.sustainability_level < 25:
            message = "You've made a positive impact on Hong Kong's environment!"
        elif self.sustainability_level < 50:
            message = "Great work! Your dedication has significantly improved Hong Kong's sustainability."
        else:
            message = "Extraordinary achievement! You've transformed Hong Kong into a beacon of urban sustainability!"

        print(f"\n{message}")

        # Show one last sustainability fact
        self.show_random_fact()

        print("\nThank you for playing the Hong Kong Sustainability Challenge!")
        print("We hope you've learned about sustainability challenges in Hong Kong")
        print("and feel inspired to make sustainable choices in your daily life.")
        print("=" * 60)

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
                    self.random_event()
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
