#pip3 install pygame
import pygame, random, sys
pygame.init()

# Window setup
WIDTH, HEIGHT = 600, 450
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HCI Gaming App - Avoid the Falling Blocks")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 100, 255)
LIGHT_BLUE = (100, 149, 237)
DARK_BLUE = (10, 25, 70)
GRAY = (180, 180, 180)

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
arrow_font = pygame.font.Font(None, 60)

# Player setup
player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 60, 50, 50)
player_speed = 7

# Obstacle setup
obstacle = pygame.Rect(random.randint(0, WIDTH - 50), -50, 50, 50)
obstacle_speed = 5

# Buttons for HCI controls
btn_size = 65
left_btn = pygame.Rect(70, HEIGHT - 90, btn_size, btn_size)
right_btn = pygame.Rect(180, HEIGHT - 90, btn_size, btn_size)

# Score
score = 0
game_over = False

def draw_game():
    win.fill(DARK_BLUE)
    
    # Draw player and obstacle
    pygame.draw.rect(win, RED, player)
    pygame.draw.rect(win, BLUE, obstacle)
    
    # Draw HCI buttons
    pygame.draw.rect(win, LIGHT_BLUE, left_btn, border_radius=10)
    pygame.draw.rect(win, LIGHT_BLUE, right_btn, border_radius=10)
    
    # Draw arrow symbols on buttons
    left_arrow = arrow_font.render("←", True, WHITE)
    right_arrow = arrow_font.render("→", True, WHITE)
    win.blit(left_arrow, (left_btn.x + 15, left_btn.y + 5))
    win.blit(right_arrow, (right_btn.x + 15, right_btn.y + 5))
    
    # Score display
    score_text = font.render(f"Score: {score}", True, WHITE)
    win.blit(score_text, (20, 20))
    
    pygame.display.update()

def show_game_over():
    win.fill(BLACK)
    over_text = font.render("GAME OVER!", True, RED)
    score_text = font.render(f"Final Score: {score}", True, WHITE)
    restart_text = font.render("Press R to Restart or Q to Quit", True, GRAY)
    win.blit(over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 60))
    win.blit(score_text, (WIDTH // 2 - 120, HEIGHT // 2))
    win.blit(restart_text, (WIDTH // 2 - 180, HEIGHT // 2 + 50))
    pygame.display.update()

# Main game loop
while True:
    clock.tick(30)
    if not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse (HCI) Controls
            if event.type == pygame.MOUSEBUTTONDOWN:
                if left_btn.collidepoint(event.pos):
                    player.x -= player_speed
                if right_btn.collidepoint(event.pos):
                    player.x += player_speed

        # Keyboard Controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player.x += player_speed

        # Obstacle movement
        obstacle.y += obstacle_speed
        if obstacle.y > HEIGHT:
            obstacle.y = -50
            obstacle.x = random.randint(0, WIDTH - 50)
            score += 1  # Increase score for surviving

        # Collision detection
        if player.colliderect(obstacle):
            game_over = True

        # Boundary check
        if player.x < 0: player.x = 0
        if player.x > WIDTH - 50: player.x = WIDTH - 50

        draw_game()
    
    else:
        show_game_over()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Restart game
                    player.x, player.y = WIDTH // 2 - 25, HEIGHT - 60
                    obstacle.y = -50
                    score = 0
                    game_over = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
