import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BIRD_WIDTH = 20
BIRD_HEIGHT = 20
COLUMN_WIDTH = 10
GAP_SIZE = 200
FPS = 60
SPEED_INCREASE_INTERVAL = 30000  # milliseconds
SPEED_INCREASE_AMOUNT = 0.05
INITIAL_COLUMN_SPEED = 2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND_COLOR = (30, 30, 30)

# Paths
import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BIRD_WIDTH = 50
BIRD_HEIGHT = 50
COLUMN_WIDTH = 80
GAP_SIZE = 200
FPS = 60
SPEED_INCREASE_INTERVAL = 5000  # milliseconds
SPEED_INCREASE_AMOUNT = 0.15
INITIAL_COLUMN_SPEED = 2

# Colors
WHITE = (30, 30, 30)
BLACK = (0, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)

# Paths
 # Path to your bird image
BIRD_IMAGE_PATH = r"C:\Users\Behrooz Moniri\Documents\Programming\Python Projects\Tkinter\pythonProject2\FlyingBird\images\bird.jpeg"  # Path to your bird image
directory = r"C:\Users\Behrooz Moniri\Documents\Programming\Python Projects\Tkinter\pythonProject2\FlyingBird\images"
upper_list = ["upper1.png", "upper2.png", "upper3.png", "upper4.png"]
TOP_COLUMN_IMAGES = [  os.path.join( directory, upper_list[i]) for i in range(4) ]

lower_list =  ["lower1.png", "lower2.png", "lower3.png", "lower4.png"]
BOTTOM_COLUMN_IMAGES = [os.path.join( directory, lower_list[i]) for i in range(4)]
music_path = os.path.join( directory,  'bensound-memories.mp3')

pygame.mixer.init()
pygame.mixer.music.load(music_path)
# Load bird image
bird_image = pygame.image.load(BIRD_IMAGE_PATH)
bird_image = pygame.transform.scale(bird_image, (BIRD_WIDTH, BIRD_HEIGHT))

# Load column images
top_column_images = [pygame.image.load(img) for img in TOP_COLUMN_IMAGES]
bottom_column_images = [pygame.image.load(img) for img in BOTTOM_COLUMN_IMAGES]

# Set up screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flying Bird Game')

# Fonts
font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 72)

# Load or initialize best scores
if os.path.exists("best_scores.txt"):
    with open("best_scores.txt", "r") as f:
        best_time, best_level = map(float, f.read().split(','))
else:
    best_time, best_level = 0.0, 0

# Game Classes
class Bird:
    def __init__(self):
        self.x = 100
        self.y = SCREEN_HEIGHT // 2
        self.speed = 5

    def move(self, dy):
        self.y += dy

    def draw(self, screen):
        screen.blit(bird_image, (self.x, self.y))

class Column:
    def __init__(self, x):
        self.x = x
        self.gap_y = random.randint(100, SCREEN_HEIGHT - 100 - GAP_SIZE)
        self.speed = INITIAL_COLUMN_SPEED
        self.top_image = random.choice(top_column_images)
        self.bottom_image = random.choice(bottom_column_images)
        self.top_image = pygame.transform.scale(self.top_image, (COLUMN_WIDTH, self.gap_y))
        self.bottom_image = pygame.transform.scale(self.bottom_image, (COLUMN_WIDTH, SCREEN_HEIGHT - (self.gap_y + GAP_SIZE)))

    def update(self):
        self.x -= self.speed

    def draw(self, screen):
        screen.blit(self.top_image, (self.x, 0))
        screen.blit(self.bottom_image, (self.x, self.gap_y + GAP_SIZE))

    def is_off_screen(self):
        return self.x < -COLUMN_WIDTH

    def collides_with(self, bird):
        bird_rect = pygame.Rect(bird.x, bird.y, BIRD_WIDTH, BIRD_HEIGHT)
        top_column_rect = pygame.Rect(self.x, 0, COLUMN_WIDTH, self.gap_y)
        bottom_column_rect = pygame.Rect(self.x, self.gap_y + GAP_SIZE, COLUMN_WIDTH, SCREEN_HEIGHT)
        return bird_rect.colliderect(top_column_rect) or bird_rect.colliderect(bottom_column_rect)

def game_over_screen(screen, time_survived, level_reached):
    global best_time, best_level

    if time_survived > best_time:
        best_time = time_survived
        new_best_time = True
    else:
        new_best_time = False

    if level_reached > best_level:
        best_level = level_reached
        new_best_level = True
    else:
        new_best_level = False

    save_best_scores(best_time, best_level)

    screen.fill(BACKGROUND_COLOR)
    text = large_font.render("Game Over", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2 - 100))

    text = font.render(f"Time: {time_survived:.2f} s", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

    text = font.render(f"Level: {level_reached}", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2 + 50))

    if new_best_time:
        text = font.render("New Best Time!", True, WHITE)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2 + 100))

    if new_best_level:
        text = font.render("New Best Level!", True, WHITE)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2 + 150))

    text = font.render("Press R to Restart or Q to Quit", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2 + 200))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()

def save_best_scores(best_time, best_level):
    with open("best_scores.txt", "w") as f:
        f.write(f"{best_time},{best_level}")

def main():
    bird = Bird()
    columns = [Column(SCREEN_WIDTH + i * (COLUMN_WIDTH + 200)) for i in range(5)]
    clock = pygame.time.Clock()
    running = True
    start_time = pygame.time.get_ticks()
    level_start_time = start_time
    pygame.mixer.music.play()

    while running:
        dt = clock.tick(FPS)
        time_elapsed = (pygame.time.get_ticks() - start_time) / 1000.0
        current_level_time = pygame.time.get_ticks() - level_start_time
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            bird.move(-bird.speed)
        if keys[pygame.K_DOWN]:
            bird.move(bird.speed)

        if current_level_time > SPEED_INCREASE_INTERVAL:
            for column in columns:
                column.speed += SPEED_INCREASE_AMOUNT * column.speed
            level_start_time = pygame.time.get_ticks()

        screen.fill(BACKGROUND_COLOR)

        bird.draw(screen)

        for column in columns:
            column.update()
            column.draw(screen)
            if column.is_off_screen():
                columns.remove(column)
                columns.append(Column(SCREEN_WIDTH + 200))
            if column.collides_with(bird):
                running = False

        text = font.render(f"Time: {time_elapsed:.2f} s", True, WHITE)
        screen.blit(text, (10, 10))

        current_level = int(time_elapsed // 60) + 1
        text = font.render(f"Level: {current_level}", True, WHITE)
        screen.blit(text, (10, 40))

        pygame.display.flip()

    game_over_screen(screen, time_elapsed, current_level)
    pygame.mixer.music.stop()

if __name__ == "__main__":
    main()
    pygame.quit()
