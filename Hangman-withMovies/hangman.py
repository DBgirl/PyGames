import pygame
import random
from pygame import gfxdraw


# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman - Guess the Movie Game")

# Define colors and fonts
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

font = pygame.font.Font(None, 30)
font_inst = pygame.font.Font(None, 20)
#Load words from a file
with open("Hangman\word.txt", "r") as file:
    words = file.readlines()

# Select a random word
word = random.choice(words).strip().upper()
#word ='TEST'
guessed_letters = set()
incorrect_guesses = 0

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key >= pygame.K_a and event.key <= pygame.K_z:
                letter = chr(event.key).upper()
                if letter not in guessed_letters:
                    guessed_letters.add(letter)
                    if letter not in word:
                        incorrect_guesses += 1

    # Draw word
    display_word = ""
    for char in word:
        if char == " ":
            display_word += "  "
        elif char in guessed_letters:
            display_word += char + " "
        else:
            display_word += "_ "

    text = font.render(display_word, True, WHITE)
    screen.blit(text, (30, 50))
    if (guessed_letters):
        text_guessed = font_inst.render("Guessed - " + str(guessed_letters), True, RED)
        screen.blit(text_guessed, (30, 575))

    # Draw hangman
    if incorrect_guesses > 0:
        pygame.draw.circle(screen, WHITE, (400, 200), 40)  # Head
    if incorrect_guesses > 1:
        pygame.draw.line(screen, WHITE, (400, 240), (400, 400), 3)  # Body
    if incorrect_guesses > 2:
        pygame.draw.line(screen, WHITE, (400, 280), (300, 340), 3)  # Left Arm
    if incorrect_guesses > 3:
        pygame.draw.line(screen, WHITE, (400, 280), (500, 340), 3)  # Right Arm
    if incorrect_guesses > 4:
        pygame.draw.line(screen, WHITE, (400, 400), (300, 500), 3)  # Left Leg
    if incorrect_guesses > 5:
        pygame.draw.line(screen, WHITE, (400, 400), (500, 500), 3)  # Right Leg
    if incorrect_guesses > 6: 
        # Hanging Stand
        pygame.draw.line(screen, WHITE, (200, 100), (500, 100), 10)
        pygame.draw.line(screen, WHITE, (400, 100), (400, 200), 10)
        pygame.draw.line(screen, WHITE, (200, 100), (200, 550), 10)
        pygame.draw.line(screen, WHITE, (100, 550), (550, 550), 10)

    # win/loss
    if incorrect_guesses >= 7:
        text = font.render("You lose! The word was: " + word, True, RED)
        screen.blit(text, (30, 600))
    elif all(char in guessed_letters or char == " " for char in word):
        text = font.render("You win!", True, GREEN)
        screen.blit(text, (50, 600))

    pygame.display.update()

# Quit Pygame
pygame.quit()
