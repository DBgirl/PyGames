import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700  # Increased height to accommodate the score display
GRID_SIZE = 4
CELL_SIZE = 150
MOLE_SIZE = 100
GRID_SPACING = 10  # Space between the tiles
BACKGROUND_COLOR = (0, 128, 0)
HOLE_COLOR = (139, 69, 19)
FPS = 30
MOLE_TIME = 1  # Time a mole stays up in seconds
GAME_TIME = 60  # Total game time in seconds

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Whack-a-Mole")

# Load images
MOLE_IMAGE_PATH = '6_wack-a-mole\mole.png'  
HAMMER_IMAGE_PATH = '6_wack-a-mole\hammer.png' 
mole_image = pygame.image.load(MOLE_IMAGE_PATH)
mole_image = pygame.transform.scale(mole_image, (MOLE_SIZE, MOLE_SIZE))
hammer_image = pygame.image.load(HAMMER_IMAGE_PATH)
hammer_image = pygame.transform.scale(hammer_image, (50, 50))  # Adjust size as needed

# Font
font = pygame.font.SysFont('arial', 36)

# Functions
def draw_grid():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = col * (CELL_SIZE + GRID_SPACING)
            y = row * (CELL_SIZE + GRID_SPACING)
            pygame.draw.rect(screen, HOLE_COLOR, (x, y, CELL_SIZE, CELL_SIZE))

def draw_mole(mole_position):
    row, col = mole_position
    x = col * (CELL_SIZE + GRID_SPACING) + (CELL_SIZE - MOLE_SIZE) // 2
    y = row * (CELL_SIZE + GRID_SPACING) + (CELL_SIZE - MOLE_SIZE) // 2
    screen.blit(mole_image, (x, y))

def get_cell_from_mouse_pos(pos):
    x, y = pos
    col = x // (CELL_SIZE + GRID_SPACING)
    row = y // (CELL_SIZE + GRID_SPACING)
    return row, col

def main():
    clock = pygame.time.Clock()
    score = 0
    last_mole_time = 0
    mole_position = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
    mole_visible = False
    start_time = time.time()

    pygame.mouse.set_visible(False)  # Hide the default mouse cursor

    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)
        draw_grid()

        current_time = time.time()
        elapsed_time = current_time - start_time
        remaining_time = GAME_TIME - elapsed_time

        if remaining_time <= 0:
            running = False

        if current_time - last_mole_time > MOLE_TIME:
            mole_position = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
            last_mole_time = current_time
            mole_visible = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mole_visible:
                    mouse_pos = pygame.mouse.get_pos()
                    clicked_cell = get_cell_from_mouse_pos(mouse_pos)
                    if clicked_cell == mole_position:
                        score += 1
                        mole_visible = False

        if mole_visible:
            draw_mole(mole_position)

        # Display remaining time
        time_text = font.render(f"Time: {int(remaining_time)}s", True, (0, 0, 0))
        screen.blit(time_text, (400, SCREEN_HEIGHT - 50))

        # Display score
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, SCREEN_HEIGHT - 50))

        # Draw the hammer cursor
        mouse_pos = pygame.mouse.get_pos()
        hammer_rect = hammer_image.get_rect(center=mouse_pos)
        screen.blit(hammer_image, hammer_rect.topleft)

        pygame.display.flip()
        clock.tick(FPS)

    # Game over screen
    screen.fill(BACKGROUND_COLOR)
    game_over_text = font.render("Game Over!", True, (0, 0, 0))
    final_score_text = font.render(f"Final Score: {score}", True, (0, 0, 0))
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(final_score_text, (SCREEN_WIDTH // 2 - final_score_text.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)

    pygame.quit()

if __name__ == "__main__":
    main()
