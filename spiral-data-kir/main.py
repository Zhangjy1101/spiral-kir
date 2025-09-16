import pygame
import numpy as np
import math
import sys

# Simulate tidal data (replace with real data as needed)
def get_tidal_data(t):
    # Example: simple sine wave to simulate tide
    return 100 * math.sin(2 * math.pi * t / 600) + 200

def draw_spiral(screen, center, t, num_points=500):
    points = []
    colors = []
    for i in range(num_points):
        angle = 0.1 * i + 0.01 * t
        radius = get_tidal_data((t + i) % 600) * (i / num_points)
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        points.append((x, y))
        # Color gradient: cycle through hues
        hue = (i + t) % 360
        color = pygame.Color(0)
        color.hsva = (hue, 100, 100, 100)
        colors.append(color)
    # Draw colored segments
    if len(points) > 1:
        for i in range(len(points) - 1):
            pygame.draw.line(screen, colors[i], points[i], points[i + 1], 2)

def main():
    pygame.init()
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Tidal Spiral Visualization')
    clock = pygame.time.Clock()
    t = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((10, 10, 30))
        draw_spiral(screen, (width // 2, height // 2), t)
        pygame.display.flip()
        t += 1
        clock.tick(60)
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
