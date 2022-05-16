from datetime import datetime, timedelta

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BULLET_COLOR = (255, 255, 255)

GAME_WIDTH = 400
GAME_HIGH = 600

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

BETWEEN_SHOTS = timedelta(seconds=2)
BETWEEN_ALIENS = timedelta(seconds=3)

MAX_DOWNED_ALIENS = 5

SUCCESS_COLOR = (0, 0, 255)
FAILURE_COLOR = RED
SUCCESS_TEXT = "Congrats!"
FAILURE_TEXT = "Sorry..."

