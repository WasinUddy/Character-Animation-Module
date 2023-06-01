import pygame as pg
from character import CharacterSprite

# Initialize Pygame
pg.init()

# Set up the screen
screen_width, screen_height = 400, 350
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Character Animation Test")

# Set up the clock
clock = pg.time.Clock()

# Create the character sprite
character = CharacterSprite(path_to_tiles="demo/sprite.json", target_size=(300, 300))

# Set initial state
tile = character.idle()
running = True
walk = False
direction = "S"

# Main game loop
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYUP:
            if event.key in (pg.K_DOWN, pg.K_UP, pg.K_LEFT, pg.K_RIGHT):
                walk = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                walk = True
                direction = "S"
            elif event.key == pg.K_UP:
                walk = True
                direction = "N"
            elif event.key == pg.K_LEFT:
                walk = True
                direction = "W"
            elif event.key == pg.K_RIGHT:
                walk = True
                direction = "E"

    # Clear the screen
    screen.fill((0, 0, 0))

    # Update the character sprite based on state
    if walk:
        tile = character.walk(direction)
    else:
        tile = character.idle(direction)

    # Render the character sprite
    screen.blit(tile, (50, 0))

    # Show key press status
    font = pg.font.Font(None, 30)
    text = font.render(f"Walk: {walk} {direction}", True, (255, 255, 255))
    screen.blit(text, (0, 0))

    # Update the display
    pg.display.flip()

    # Limit the frame rate
    clock.tick(12)

# Quit Pygame
pg.quit()
