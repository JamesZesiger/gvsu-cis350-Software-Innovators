import pygame
import sys

# initialize pygame instance
pygame.init()

# setup window size and title
width, height = 768, 960
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Budgeting App GUI Mockup")

# setup colors for screen elements
dock_color = (37, 58, 45)
dock_option_color = (48, 91, 63)
module_color = (97, 135, 76)
text_color = (207, 207, 165)
background_color = (215, 221, 176)

# setup fonts
pygame.font.init()
header_font = pygame.font.Font(None, 36)

# setup text
header_text = header_font.render("Welcome to Your Budget Dashboard!", True, text_color)

# setup images
user_icon = pygame.image.load("images/user_icon.png")
user_icon = pygame.transform.scale(user_icon, (40,40))
settings_icon = pygame.image.load("images/settings_icon.png")
settings_icon = pygame.transform.scale(settings_icon, (40,40))

# main app loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill in background color
    screen.fill(background_color)

    # setup header element
    pygame.draw.rect(screen, dock_color, (0, 0, width, 50))
    screen.blit(header_text, (170, 15))
    screen.blit(user_icon, (10,5))
    screen.blit(settings_icon, (width-50, 5))

    # setup modules
    pygame.draw.rect(screen, module_color, (30, 80, width-60, 225))
    pygame.draw.rect(screen, module_color, (30, 350, width-60, 225))
    pygame.draw.rect(screen, module_color, (30, 620, width-60, 225))

    # setup dock element
    pygame.draw.rect(screen, dock_color, (10, height-90, width-20, 80))
    # pygame.draw.rect(screen, dock_option_color, (30, height-100, 100, 60))

    pygame.display.flip()

# close app after user quits
pygame.quit()
sys.exit()