import pygame



import math
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Love Heart Animation")

# Colors
BLACK = (0, 0, 0)
PINK = (234, 128, 176)  # #ea80b0 matching the CSS color in the image
GLOW_COLOR = (255, 255, 255)

# Font configuration
try:
    font = pygame.font.SysFont("Arial", 14, bold=True)
except:
    font = pygame.font.Font(None, 14)

clock = pygame.time.Clock()

def get_heart_coordinates(t, scale):
    """Parametric equations for a heart shape."""
    x = 16 * math.sin(t) ** 3
    # Invert y because Pygame's y-axis goes downwards
    y = -(13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
    return x * scale, y * scale

# Generate base particles along the heart curve
particles = []
num_particles = 180
for i in range(num_particles):
    t = (i / num_particles) * 2 * math.pi
    # Add slight random offset for a organic, layered look like the image
    offset = random.uniform(0.95, 1.05) 
    particles.append((t, offset))

running = True
frame = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Create a dynamic pulse/breathing effect using a sine wave
    pulse_scale = 15 + math.sin(frame * 0.05) * 1.2
    frame += 1

    for t, offset in particles:
        # Calculate base position
        x, y = get_heart_coordinates(t, pulse_scale * offset)
        
        # Center the heart on the screen
        pos_x = int(WIDTH / 2 + x)
        pos_y = int(HEIGHT / 2 + y)

        # Render "i love you" text
        text_surface = font.render("I love you", True, PINK)
        
        # Rotate text slightly based on its position along the curve to align it
        angle = math.degrees(-t) + 90
        rotated_surface = pygame.transform.rotate(text_surface, angle)
        
        # Get rect and center it on the calculated coordinate
        rect = rotated_surface.get_rect(center=(pos_x, pos_y))
        
        # Blit text to screen
        screen.blit(rotated_surface, rect)

    pygame.display.flip()
    clock.tick(60)  # Maintain 60 FPS

pygame.quit()
sys.exit()
