import pygame
import math

pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Set up the clock
clock = pygame.time.Clock()

# Define the arrow class
class Arrow(pygame.sprite.Sprite):
    def __init__(self, start_pos, end_pos):
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.rect(self.image, WHITE, pygame.Rect(0, 0, 20, 2))
        self.rect = self.image.get_rect()
        self.rect.center = start_pos
        self.speed = 10
        self.angle = math.atan2(end_pos[1] - start_pos[1], end_pos[0] - start_pos[0])
        self.image = pygame.transform.rotate(self.image, math.degrees(-self.angle))
        self.rect = self.image.get_rect(center=self.rect.center)
    
    def update(self):
        self.rect.move_ip(self.speed * math.cos(self.angle), self.speed * math.sin(self.angle))
        if not screen.get_rect().colliderect(self.rect):
            self.kill()

# Set up the sprite group for arrows
arrow_group = pygame.sprite.Group()

# Set up the cooldown bar
cooldown_timer = 0
cooldown_length = 100 # in milliseconds
cooldown_surface = pygame.Surface((40, 10))
cooldown_surface.fill(WHITE)

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if cooldown_timer <= 0:
                # Spawn a new arrow when the left mouse button is clicked
                start_pos = (screen.get_width() // 2, screen.get_height() // 2)
                end_pos = pygame.mouse.get_pos()
                arrow = Arrow(start_pos, end_pos)
                arrow_group.add(arrow)
                cooldown_timer = cooldown_length
                cooldown_surface.fill(GRAY)

    # Update the game state
    arrow_group.update()

    # Update the cooldown bar
    if cooldown_timer > 0:
        cooldown_timer -= clock.get_time()
        cooldown_width = int(40 * (cooldown_timer / cooldown_length))
        cooldown_surface.fill(GRAY, (cooldown_width, 0, 40 - cooldown_width, 10))
        if cooldown_timer <= 0:
            cooldown_surface.fill(WHITE)

    # Draw everything
    screen.fill(BLACK)
    arrow_group.draw(screen)

    # Draw the cooldown bar
    screen.blit(cooldown_surface, (10, 10))

    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Clean up
pygame.quit()