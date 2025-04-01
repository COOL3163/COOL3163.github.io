#!/usr/bin/env python3

"""
Hong Kong Sustainability Challenge
Launch Script

This script provides a simple way to start the game.
"""

import os
import sys
import time

def check_dependencies():
    """Check if the required files exist"""
    required_files = [
        "sustainability_game.py",
        "hong_kong_sustainability_facts.py"
    ]

    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)

    if missing_files:
        print("Error: The following required files are missing:")
        for file in missing_files:
            print(f"  - {file}")
        print("\nPlease make sure all game files are in the same directory.")
        return False

    return True

def display_welcome():
    """Display welcome message and basic instructions"""
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n" + "=" * 70)
    print(f"{'HONG KONG SUSTAINABILITY CHALLENGE':^70}")
    print("=" * 70)

    print("""
Welcome to the Hong Kong Sustainability Challenge!

In this game, you'll take actions to improve sustainability in Hong Kong
while learning about real environmental challenges facing the city.

GAME FEATURES:
- Explore 5 different locations around Hong Kong
- Perform various sustainability actions
- Manage your energy and eco points
- Learn real facts about Hong Kong's environment
- Deal with random events and challenges
- Make strategic decisions for maximum positive impact

Are you ready to make Hong Kong more sustainable?
""")

def start_game():
    """Start the sustainability game"""
    # Import here to prevent errors if the file doesn't exist
    from sustainability_game import SustainabilityGame

    game = SustainabilityGame()
    game.play()

def main():
    """Main function to launch the game"""
    if not check_dependencies():
        input("\nPress Enter to exit...")
        sys.exit(1)

    while True:
        display_welcome()

        choice = input("\nStart game? (y/n): ")

        if choice.lower() in ['y', 'yes']:
            start_game()

            print("\nGame finished! Would you like to play again?")
            play_again = input("Play again? (y/n): ")

            if play_again.lower() not in ['y', 'yes']:
                break
        else:
            print("\nExiting the game. See you next time!")
            time.sleep(1)
            break

if __name__ == "__main__":
    main()
