# Text-Based Adventure Game

A console-based adventure game written in **Python 3**. The player explores a Forest, a Cave and a River by choosing options from a menu, faces random monster attacks, collects score, and ends the game by quitting or losing all health.

> **PS No.:** 22  |  **Language:** Python 3  |  **Concepts:** Conditions, Loops, Functions, Random

---

## Features
- Menu-driven gameplay with three choices: Cave, River, Quit
- Random monster damage (10 to 40) in the Cave
- Score system: key (+20) and treasure (+50)
- Health tracking; the game ends when Health reaches 0
- Input validation: invalid choices never reduce health
- Final score shown at the end

## Game Rules
| Item | Value |
|------|-------|
| Starting location | Forest |
| Starting Health | 100 |
| Starting Score | 0 |
| Cave | Monster attacks (damage 10-40). If the player survives, a key gives **+20** score |
| River | Treasure gives **+50** score |
| Quit | Ends the game and shows the final score |
| Game over | When Health reaches 0 |

## Menu
```
1. Go to the Cave
2. Go to the River
3. Quit
```

## Requirements
- Python 3.x (no external libraries needed)

## How to Run
```bash
python adventure_game.py
```
On Mac/Linux you may need `python3 adventure_game.py`.

In VS Code, open the file and click the **Run Python File** button.

## Program Structure
| Function | Purpose |
|----------|---------|
| `forest()` | Shows the menu and validates the choice (1, 2 or 3) |
| `cave(health, score)` | Monster attack; key reward if the player survives |
| `river(health, score)` | Treasure reward |
| `get_damage()` | Random damage 10-40, or a fixed value when testing |
| `main()` | Game loop that runs until the player quits or Health is 0 |

## Configuration (for testing)
Constants at the top of `adventure_game.py`:
```python
START_HEALTH = 100   # set to 30 for Test Case 2
FIXED_DAMAGE = None  # set to 30 for Test Cases 2 and 4 (None = random damage)
```
Set them back to `100` and `None` for normal gameplay.

## Test Cases
**Test Case 1: Normal input**
- Input: `2` (River)
- Output:
  ```
  River: You found a treasure! Score: 50 | Health: 100
  ```

**Test Case 2: Boundary / minimum input**
- Setup: `START_HEALTH = 30`, `FIXED_DAMAGE = 30`
- Input: `1` (Cave)
- Output:
  ```
  Cave: Monster attacks! Damage: 30. Health: 0
  Game Over! Final score: 0
  ```

**Test Case 3: Invalid input**
- Input: `7`, then `abc`, then `3`
- Output:
  ```
  Invalid choice. Enter 1, 2 or 3.
  Invalid choice. Enter 1, 2 or 3.
  No health lost.
  You left the adventure. Final score: 0 | Health: 100
  ```

**Test Case 4: Different valid scenario**
- Setup: `FIXED_DAMAGE = 30`
- Input: `1`, `2`, `3`
- Output:
  ```
  Cave: Monster attacks! Damage: 30. Health: 70
  You found a key! Score: 20
  River: You found a treasure! Score: 70 | Health: 70
  You left the adventure. Final score: 70 | Health: 70
  ```

All four test cases pass.

## Sample Run
```
=== Text-Based Adventure Game ===

You are in the Forest.
1. Go to the Cave
2. Go to the River
3. Quit
Enter your choice: 2
River: You found a treasure! Score: 50 | Health: 100
```

## Project Structure
```
text-adventure-game/
├── adventure_game.py
└── README.md
```

## Author
Md Inamul Haque
