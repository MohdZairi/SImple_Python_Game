import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Load the background image
background = pygame.image.load("image/snakebcg.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Initialize clock
clock = pygame.time.Clock()

# Initialize Snake
snake = [(4, 3), (4, 2), (4, 1)]
snake_direction = RIGHT

# Initialize Food
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Score
score = 0

# Game Over flag
game_over = False

# Font for the score display
font = pygame.font.Font(None, 36)

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != DOWN:
                snake_direction = UP
            if event.key == pygame.K_DOWN and snake_direction != UP:
                snake_direction = DOWN
            if event.key == pygame.K_LEFT and snake_direction != RIGHT:
                snake_direction = LEFT
            if event.key == pygame.K_RIGHT and snake_direction != LEFT:
                snake_direction = RIGHT

    # Move the snake
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake.insert(0, new_head)

    # Check for collisions
    if snake[0] == food:
        score += 1
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()

    # Check if the snake collided with itself
    if len(snake) != len(set(snake)):
        game_over = True

    # Check if the snake hit the wall
    if (
        snake[0][0] < 0
        or snake[0][0] >= GRID_WIDTH
        or snake[0][1] < 0
        or snake[0][1] >= GRID_HEIGHT
    ):
        game_over = True

    # Draw the background image
    screen.blit(background, (0, 0))

    # Draw everything else on top of the background
    for segment in snake:
        pygame.draw.rect(
            screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        )
    pygame.draw.rect(
        screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    )

    # Display the score
    score_text = font.render(f"Score: {score}", True, GREEN)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control game speed
    clock.tick(10)

# Game over screen
game_over_text = font.render("Game Over", True, RED)
game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(game_over_text, game_over_rect)
pygame.display.flip()

# Wait for a few seconds before quitting
pygame.time.wait(2000)

# Quit Pygame
pygame.quit()
