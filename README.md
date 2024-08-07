# Alien Invasion

Alien Invasion is a 2D shooting game where the player controls a spaceship and must shoot down waves of aliens.
The game is built using Python and Pygame.

## Features

- Fullscreen game window
- Player-controlled spaceship
- Waves of aliens with increasing difficulty
- Score tracking and high score management
- Play button to start a new game
- Ship lives display
- Level progression

## Installation

To run the Alien Invasion game on your local machine, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/sashakukhtyk/alien-invasion.git
   ```

2. Navigate to the project directory:
   ```sh
   cd alien-invasion
   ```

3. Create a virtual environment:
   ```sh
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```sh
     source venv/bin/activate
     ```

5. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

6. Run the game:
   ```sh
   python alien_invasion.py
   ```

## Usage

- Use the **Right Arrow** and **Left Arrow** keys to move the spaceship.
- Press the **Spacebars** to shoot bullets.
- Press the **Q** key to quit the game.
- Click the **Play** button with the mouse to start a new game.

## Dependencies

- Python 3.x
- Pygame

## Project Structure

```
alien-invasion/
├── alien_invasion.py      # Main game file
├── settings.py            # Settings for the game
├── game_stats.py          # Game statistics
├── scoreboard.py          # Scoreboard display
├── button.py              # Play button
├── ship.py                # Player's spaceship
├── bullet.py              # Bullets fired by the spaceship
├── alien.py               # Aliens
├── requirements.txt       # Required dependencies
└── README.md              # Project documentation
```

## Contributing

Contributions are welcome! If you have any improvements or suggestions, submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Pygame community for their excellent resources and support.

---

Feel free to customize this README to fit your project's specific details and requirements.