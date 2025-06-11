# Meltdown-Snowman

**Practice project for the Masterschool Software Engineering course from Term 4: "Version Control and Testing"**

## Contents
- [Project Goal](#project-goal)
- [Game Principle](#game-principle)
- [Project Structure](#project-structure)
- [Installation & Execution](#installation--execution)
- [Add Custom Word Set or ASCII Art](#add-custom-word-set-or-ascii-art)

## Project Goal
"Snowman Meltdown" is a simple console-based adaptation of Hangman.  
Every incorrect letter melts the snowman a little until it completely disappears.

The code demonstrates:
- **Modularization** using Python packages (`game_logic`, `ascii_art`)
- **Basic input validation** to prevent errors
- **Loop control** for a replay function
- **Clean project organization** – ideal for practicing Git commits, branches, and pull requests.

## Game Principle
- The program **randomly** selects a word from the `WORDS` list.
- You enter a **letter**.
- If the letter is **incorrect**, the snowman melts (ASCII art).
- After **a maximum of four mistakes**, the snowman is gone → _Game Over_.
- If you **guess all letters in time**, you win and can start a new round immediately.

## Project Structure

- ascii_art.py: Contains the STAGES list with the snowman frames
- game_logic.py: Full game logic (input + game loop)
- snowman.py: Mini entry point to start the game
- README.md: This file

## Installation & Execution

### Requirement
Python **≥ 3.8**

### Clone the project & start
```bash
git clone https://github.com/Gecker0815/Melting-Snowman.git
cd snowman-meltdown

# Install dependencies
pip install random

# Start the game
python snowman.py
```

## Add Custom Word Set or ASCII Art

### Modify word list
Simply edit the list in `game_logic.py`:
```python
WORDS = ["python", "git", "masterschool", "yourword", ...]
```
### Change snowman animation
All frames are stored in `ascii_art.py` → `STAGES`.  
The more frames, the smoother the melting animation.  
Keep in mind that the allowed number of mistakes in `game_logic.py` is directly linked to the number of stages in the melting animation:
```python
max_mistakes = len(ascii_art.STAGES) - 1
```

Enjoy and don't let the snowman melt completely! ⛄🧤