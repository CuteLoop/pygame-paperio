# Paper.io-inspired Game

## Overview
This is a 2D multiplayer game inspired by *Paper.io*, built using Pygame. In this game, players move around the screen, leaving a paint trail behind them.
The goal is to capture territory by completing closed loops and avoiding collisions with other players.

## Features
- **Player Movement**: Control your player using the arrow keys or WASD.
- **Trail Creation**: Leave a visible trail as you move around the game area.
- **Area Capture**: Close a loop to capture the area inside it.
- **Collision Detection**: Lose a life or the game if you collide with your own or another player's trail.
- **Multiplayer**: Compete against other players in real-time (future feature).

## Project Structure
```
my_paperio_game/
│
├── assets/
│   ├── images/
│   │   └── player.png
│   ├── sounds/
│   │   └── capture.wav
│   └── fonts/
│       └── game_font.ttf
│
├── src/
│   ├── main.py
│   ├── player.py
│   ├── game.py
│   ├── utils.py
│   ├── settings.py
│   ├── collision.py
│   └── __init__.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

### create directory structure 

```python ./create_dir_structure.py```

### create virtual enviroment
```
py -3.12 -m venv venv
.\venv\Scripts\activate
pip install pygame
```

