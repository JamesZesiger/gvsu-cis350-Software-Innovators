import pygame
import sys
from button import Button

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
font_path = "fonts/AgenorNeue-Regular.otf"
header_font = pygame.font.Font(font_path, 24)
login_font = pygame.font.Font(font_path, 76)
signup_font = pygame.font.Font(font_path, 36)
button_font = pygame.font.Font(font_path, 24)
return_text_font = pygame.font.Font(font_path, 18)

# setup images
user_icon = pygame.image.load("images/user_icon.png")
user_icon = pygame.transform.scale(user_icon, (40,40))
settings_icon = pygame.image.load("images/settings_icon.png")
settings_icon = pygame.transform.scale(settings_icon, (40,40))


# utility functions:
def drawDock(current):
    # set colors for dock items & text
    dash_item_color = dock_option_color
    dash_item_text_color = text_color
    expenses_item_color = dock_option_color
    expenses_item_text_color = text_color
    income_item_color = dock_option_color
    income_item_text_color = text_color
    goals_item_color = dock_option_color
    goals_item_text_color = text_color

    # reverse colors for currently selected dock item
    if current == "dash":
        dash_item_color = background_color
        dash_item_text_color = dock_option_color
    elif current == "expenses":
        expenses_item_color = background_color
        expenses_item_text_color = dock_option_color
    elif current == "income":
        income_item_color = background_color
        income_item_text_color = dock_option_color
    elif current == "goals":
        goals_item_color = background_color
        goals_item_text_color = dock_option_color

    # setup dock background element
    pygame.draw.rect(screen, dock_color, (10, height-90, width-20, 80))

    # setup individual dock elements
    padding_edge = 20
    padding_between = 36

    dash_item_pos = (padding_edge, height-80)
    expenses_item_pos = (dash_item_pos[0] + 150 + padding_between, height-80)
    income_item_pos = (expenses_item_pos[0] + 150 + padding_between, height-80)
    goals_item_pos = (income_item_pos[0] + 150 + padding_between, height-80)

    dash_item = pygame.draw.rect(screen, dash_item_color, (dash_item_pos[0], dash_item_pos[1], 150, 60))
    expenses_item = pygame.draw.rect(screen, expenses_item_color, (expenses_item_pos[0], expenses_item_pos[1], 150, 60))
    income_item = pygame.draw.rect(screen, income_item_color, (income_item_pos[0], income_item_pos[1], 150, 60))
    goals_item = pygame.draw.rect(screen, goals_item_color, (goals_item_pos[0], goals_item_pos[1], 150, 60))

    dash_button_x_pos = (dash_item_pos[0] + 75)
    dash_button_y_pos = (dash_item_pos[1] + 30)
    dash_item_button = Button(image=None, pos=(dash_button_x_pos, dash_button_y_pos), text_input="Dash", font=button_font, base_color=dash_item_text_color)
    dash_item_button.update(screen)

    expenses_button_x_pos = (expenses_item_pos[0] + 75)
    expenses_button_y_pos = (expenses_item_pos[1] + 30)
    expenses_item_button = Button(image=None, pos=(expenses_button_x_pos, expenses_button_y_pos), text_input="Expenses", font=button_font, base_color=expenses_item_text_color)
    expenses_item_button.update(screen)

    income_button_x_pos = (income_item_pos[0] + 75)
    income_button_y_pos = (income_item_pos[1] + 30)
    income_item_button = Button(image=None, pos=(income_button_x_pos,income_button_y_pos), text_input="Income", font=button_font, base_color=income_item_text_color)
    income_item_button.update(screen)

    goals_button_x_pos = (goals_item_pos[0] + 75)
    goals_button_y_pos = (goals_item_pos[1] + 30)
    goals_item_button = Button(image=None, pos=(goals_button_x_pos,goals_button_y_pos), text_input="Goals", font=button_font, base_color=goals_item_text_color)
    goals_item_button.update(screen)

    return dash_item_button, expenses_item_button, income_item_button, goals_item_button

def drawHeader(text):
    # setup text
    header_text = header_font.render(text, True, text_color)
    text_rect_hd = header_text.get_rect()

    texthd_x_pos = (width - text_rect_hd.width) // 2
    texthd_y_pos = (50 - text_rect_hd.height) // 2

    # setup header element
    pygame.draw.rect(screen, dock_color, (0, 0, width, 50))
    screen.blit(header_text, (texthd_x_pos, texthd_y_pos))
    # screen.blit(user_icon, (10,5))
    # screen.blit(settings_icon, (width-50, 5))

    user_button = Button(image=user_icon, pos=(30,25), text_input="", font=button_font, base_color=(0,0,0))
    user_button.update(screen)

    settings_button = Button(image=settings_icon, pos=(width-30,25), text_input="", font=button_font, base_color=(0,0,0))
    settings_button.update(screen)

    return user_button, settings_button


# screen functions:
def dashboard():
    page_title = "My Dashboard"
    pygame.display.set_caption(page_title)

    while True:
        dash_mouse_pos = pygame.mouse.get_pos()

        # fill in background
        screen.fill(background_color)

        user_button, settings_button = drawHeader(page_title)

        # setup modules
        # pygame.draw.rect(screen, module_color, (30, 80, width-60, 225))
        # pygame.draw.rect(screen, module_color, (30, 350, width-60, 225))
        # pygame.draw.rect(screen, module_color, (30, 620, width-60, 225))
        
        dash_item_button, expenses_item_button, income_item_button, goals_item_button = drawDock("dash")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if dash_item_button.checkForInput(dash_mouse_pos):
                    print("Already on dashboard page")
                elif expenses_item_button.checkForInput(dash_mouse_pos):
                    expenses()
                elif income_item_button.checkForInput(dash_mouse_pos):
                    income()
                elif goals_item_button.checkForInput(dash_mouse_pos):
                    goals()
                elif user_button.checkForInput(dash_mouse_pos):
                    userMenu(page_title)
                elif settings_button.checkForInput(dash_mouse_pos):
                    settings()

        pygame.display.update()

def expenses():
    page_title = "Expenses Tracker/Input"
    pygame.display.set_caption(page_title)

    while True:
        dash_mouse_pos = pygame.mouse.get_pos()

        # fill in background
        screen.fill(background_color)

        user_button, settings_button = drawHeader(page_title)
        
        dash_item_button, expenses_item_button, income_item_button, goals_item_button = drawDock("expenses")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if dash_item_button.checkForInput(dash_mouse_pos):
                    dashboard()
                elif expenses_item_button.checkForInput(dash_mouse_pos):
                    print("already on expenses page")
                elif income_item_button.checkForInput(dash_mouse_pos):
                    income()
                elif goals_item_button.checkForInput(dash_mouse_pos):
                    goals()
                elif user_button.checkForInput(dash_mouse_pos):
                    userMenu(page_title)
                elif settings_button.checkForInput(dash_mouse_pos):
                    settings()

        pygame.display.update()

def income():
    page_title = "Income Tracker"
    pygame.display.set_caption(page_title)

    while True:
        dash_mouse_pos = pygame.mouse.get_pos()

        # fill in background
        screen.fill(background_color)

        user_button, settings_button = drawHeader(page_title)
        
        dash_item_button, expenses_item_button, income_item_button, goals_item_button = drawDock("income")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if dash_item_button.checkForInput(dash_mouse_pos):
                    dashboard()
                elif expenses_item_button.checkForInput(dash_mouse_pos):
                    expenses()
                elif income_item_button.checkForInput(dash_mouse_pos):
                    print("already on income page")
                elif goals_item_button.checkForInput(dash_mouse_pos):
                    goals()
                elif user_button.checkForInput(dash_mouse_pos):
                    userMenu(page_title)
                elif settings_button.checkForInput(dash_mouse_pos):
                    settings()

        pygame.display.update()

def goals():
    page_title = "Goal Progress & Setup"
    pygame.display.set_caption(page_title)

    while True:
        dash_mouse_pos = pygame.mouse.get_pos()

        # fill in background
        screen.fill(background_color)

        user_button, settings_button = drawHeader(page_title)
        
        dash_item_button, expenses_item_button, income_item_button, goals_item_button = drawDock("goals")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if dash_item_button.checkForInput(dash_mouse_pos):
                    dashboard()
                elif expenses_item_button.checkForInput(dash_mouse_pos):
                    expenses()
                elif income_item_button.checkForInput(dash_mouse_pos):
                    income()
                elif goals_item_button.checkForInput(dash_mouse_pos):
                    print("already on goals page")
                elif user_button.checkForInput(dash_mouse_pos):
                    userMenu(page_title)
                elif settings_button.checkForInput(dash_mouse_pos):
                    settings()

        pygame.display.update()

def login():
    pygame.display.set_caption("Login Screen")

    # game loop
    while True:
        login_mouse_pos = pygame.mouse.get_pos()

        # set background color
        screen.fill(background_color)

        # setup login screen background block
        pygame.draw.rect(screen, dock_color, (50, 50, 668, 350))

        # setup login screen title
        welcome_text = login_font.render("Welcome to", True, text_color)
        balance_buddy_text = login_font.render("BalanceBuddy", True, text_color)
        
        text_rect_bb = balance_buddy_text.get_rect()
        text_rect_wt = welcome_text.get_rect()

        textwt_x_pos = 50 + ((668 - text_rect_wt.width) // 2)
        textwt_y_pos = 50 + ((350 - text_rect_wt.height) // 2) - (text_rect_bb.height // 2)

        textbb_x_pos = 50 + ((668 - text_rect_bb.width) // 2)
        textbb_y_pos = 50 + ((350 - text_rect_bb.height) // 2) + (text_rect_wt.height // 2)

        screen.blit(welcome_text, (textwt_x_pos, textwt_y_pos))
        screen.blit(balance_buddy_text, (textbb_x_pos, textbb_y_pos))


        # INPUT TEXT BOXES WILL GO HERE


        # setup login button
        pygame.draw.rect(screen, dock_option_color, (width-230, height-90, 200, 60))

        textlgn_x_pos = (width-230) + (200//2)
        textlgn_y_pos = (height-90) + (60//2)

        login_button = Button(image=None, pos=(textlgn_x_pos, textlgn_y_pos), text_input="Login", font=button_font, base_color=text_color)
        login_button.update(screen)

        # setup sign up button
        pygame.draw.rect(screen, dock_option_color, (30, height-90, 200, 60))

        textsu_x_pos = (30) + (200//2)
        textsu_y_pos = (height-90) + (60//2)

        signup_button = Button(image=None, pos=(textsu_x_pos, textsu_y_pos), text_input="Sign Up", font=button_font, base_color=text_color)
        signup_button.update(screen)

        # check for exit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if login_button.checkForInput(login_mouse_pos):
                    dashboard()
                if signup_button.checkForInput(login_mouse_pos):
                    signUp()

        pygame.display.update()

def signUp():
    pygame.display.set_caption("Sign Up Screen")

    # game loop
    while True:
        signup_mouse_pos = pygame.mouse.get_pos()

        # set background color
        screen.fill(background_color)

        # setup login screen background block
        pygame.draw.rect(screen, dock_color, (50, 50, 668, 100))

        # setup login screen title
        sign_up_text = signup_font.render("Get Started With BalanceBuddy", True, text_color)
        
        text_rect = sign_up_text.get_rect()

        text_x_pos = 50 + ((668 - text_rect.width) // 2)
        text_y_pos = 50 + ((100 - text_rect.height) // 2)

        screen.blit(sign_up_text, (text_x_pos, text_y_pos))


        # INPUT TEXT BOXES WILL GO HERE


        # setup create account button
        pygame.draw.rect(screen, dock_option_color, ((width/2)-100, height-280, 200, 60))

        textca_x_pos = ((width/2) - 100) + (200//2)
        textca_y_pos = (height-280) + (60//2)

        create_account_button = Button(image=None, pos=(textca_x_pos, textca_y_pos), text_input="Create Account", font=button_font, base_color=text_color)
        create_account_button.update(screen)

        return_text = return_text_font.render("Already have an account?", True, (85, 0, 0))
        textrt_rect = return_text.get_rect()

        textrt_x_pos = (width/2) - (textrt_rect.width//2)
        textrt_y_pos = (height-150)

        screen.blit(return_text, (textrt_x_pos, textrt_y_pos))

        # setup login button
        pygame.draw.rect(screen, dock_option_color, ((width/2)-100, height-120, 200, 60))

        textlgn_x_pos = ((width/2) - 100) + (200//2)
        textlgn_y_pos = (height-120) + (60//2)

        login_button = Button(image=None, pos=(textlgn_x_pos, textlgn_y_pos), text_input="Login", font=button_font, base_color=text_color)
        login_button.update(screen)

        # check for exit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if create_account_button.checkForInput(signup_mouse_pos):
                    # create account using input data
                    dashboard()
                if login_button.checkForInput(signup_mouse_pos):
                    login()

        pygame.display.update()


# menu functions
def userMenu(current):
    # print("user menu")
    while True:

        user_button, settings_button = drawHeader(current)

        menu_mouse_pos = pygame.mouse.get_pos()

        pygame.draw.rect(screen, dock_color, (10, 60, 250, height-110))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if user_button.checkForInput(menu_mouse_pos):
                    if (current == "My Dashboard"):
                        dashboard()
                    elif (current == "Expenses Tracker/Input"):
                        expenses()
                    elif (current == "Income Tracker"):
                        income()
                    elif (current == "Goal Progress & Setup"):
                        goals()

        pygame.display.update()

def settings():
    print("settings")


# start the app on the login page
login()