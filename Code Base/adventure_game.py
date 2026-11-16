"""
PS 22 - Text-Based Adventure Game
Language : Python 3
Concepts : Conditions, Loops, Functions, Random

The player explores a Forest, a Cave and a River by choosing options
from a menu. The game ends when the player quits or Health reaches 0.
"""

import random

# ---------------- Configuration ----------------
START_HEALTH = 100      # Set to 30 to test the boundary case (Test Case 2)
FIXED_DAMAGE = 30     # Set to 30 for testing; None = random damage (10-40)
MIN_DAMAGE = 10
MAX_DAMAGE = 40
KEY_SCORE = 20
TREASURE_SCORE = 50


# ---------------- Helper ----------------
def get_damage():
    """Return monster damage: fixed value if testing, else random 10-40."""
    if FIXED_DAMAGE is not None:
        return FIXED_DAMAGE
    return random.randint(MIN_DAMAGE, MAX_DAMAGE)


# ---------------- Places (one function each) ----------------
def forest():
    """Starting place. Shows the menu and returns a validated choice (1/2/3)."""
    print("\nYou are in the Forest.")
    print("1. Go to the Cave")
    print("2. Go to the River")
    print("3. Quit")

    while True:
        choice = input("Enter your choice: ").strip()
        if choice in ("1", "2", "3"):
            return int(choice)
        print("Invalid choice. Enter 1, 2 or 3.")
        print("No health lost.")


def cave(health, score):
    """A monster attacks. If the player survives, a key gives +20 score."""
    damage = get_damage()
    health = max(0, health - damage)
    print(f"Cave: Monster attacks! Damage: {damage}. Health: {health}")

    if health > 0:
        score += KEY_SCORE
        print(f"You found a key! Score: {score}")
    return health, score


def river(health, score):
    """The player finds a treasure: +50 score."""
    score += TREASURE_SCORE
    print(f"River: You found a treasure! Score: {score} | Health: {health}")
    return health, score


# ---------------- Main game loop ----------------
def main():
    health = START_HEALTH
    score = 0

    print("=== Text-Based Adventure Game ===")

    while health > 0:
        choice = forest()

        if choice == 1:
            health, score = cave(health, score)
        elif choice == 2:
            health, score = river(health, score)
        else:  # choice == 3
            print(f"You left the adventure. Final score: {score} | Health: {health}")
            return

    print(f"Game Over! Final score: {score}")


if __name__ == "__main__":
    main()
