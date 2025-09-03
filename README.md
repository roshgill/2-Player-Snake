# 2-Player Snake Game

A competitive two-player Snake game where both players race to collect food and reach a score of 21 first. Watch out though - if either snake touches the wall or itself, that player loses instantly!

## Technology Used

This game is built using **Python 3** with the built-in **Turtle graphics library**. No external dependencies are required - just run it with any standard Python installation!

## Code Overview

The game is organized into four main modules that work together:

- **`main.py`** - The heart of the game that sets up the screen, handles player input, and runs the main game loop. It manages collision detection for food, walls, and snake bodies.

- **`snake.py`** - Contains the Snake class that handles all snake behavior including movement, direction changes, and growing when food is eaten.

- **`food.py`** - Manages the blue food dots that appear randomly on the screen. When eaten, the food moves to a new random location.

- **`score.py`** - Tracks and displays each player's score on screen, and shows the winner when the game ends.

## How to Play

Player 1 uses **WASD** keys (W=up, A=left, S=down, D=right) and Player 2 uses **IJKL** keys (I=up, J=left, K=down, L=right). The first snake to eat 21 food items wins the game!

<img width="694" alt="Screen Shot 2022-04-12 at 6 42 17 PM" src="https://user-images.githubusercontent.com/99330131/163066484-3d952c7e-d06e-4b38-bc31-ec65353c4fc2.png">

<img width="694" alt="Screen Shot 2022-04-12 at 6 45 56 PM" src="https://user-images.githubusercontent.com/99330131/163066970-5218ca90-0d61-4d62-a0ce-883009ef92fc.png">
