

# Paper.io Inspired Game Manual

## Introduction

Welcome to the **Paper.io Inspired Game**! In this game, you aim to conquer as much territory as possible by drawing lines and enclosing areas. Each player starts with a small piece of land and expands it by moving around the screen using keyboard controls.

## Game Setup

### Requirements

- Python 3.12 or higher
- Pygame library

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/PaperIoGame.git
   cd PaperIoGame
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   python3.12 -m venv venv  # For Linux
   py -3.12 -m venv venv    # For Windows
   source venv/bin/activate # For Linux
   venv\Scripts\activate    # For Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Game**
   ```bash
   python src/game.py
   ```

## Gameplay

### Objective

- **Conquer territory**: Expand your land by drawing lines and enclosing areas.
- **Score points**: The more territory you capture, the higher your score will be.
- **Avoid opponents**: Be cautious of other players who might try to invade your space.

### Controls

- **Movement**: Use the arrow keys or WASD keys to move your player around the screen.
- **Toggle Full-Screen**: Press the `ESC` key to switch between full-screen and windowed modes.

### Game Mechanics

- **Drawing Trails**: As you move, you draw a trail behind you. This trail is used to capture territory.
- **Enclosing Areas**: To capture territory, you must complete a loop with your trail. Enclosed areas are added to your score.
- **Collision Detection**: If an opponent crosses your trail before you have completed an enclosure, you will lose, and you have to start from scratch.

## Troubleshooting

- **Game Not Starting**: Ensure that you have Python 3.12 and the required dependencies installed. Check the `requirements.txt` for the list of required packages.
- **Full-Screen Issues**: If the game does not enter full-screen mode, check your display settings and ensure that your graphics drivers are up to date.

## Contact

For any questions or support, please contact