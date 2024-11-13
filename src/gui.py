import pygame
import pygame_gui
import sys
from button import Button

# initialize pygame instance
pygame.init()

# setup window size and title
width, height = 768, 960
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Budgeting App GUI Mockup")
clock = pygame.time.Clock()
manager = pygame_gui.UIManager((width, height), 'theme.json')

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
small_text_font = pygame.font.Font(font_path, 18)

# setup images
user_icon = pygame.image.load("images/user_icon.png")
user_icon = pygame.transform.scale(user_icon, (40,40))
settings_icon = pygame.image.load("images/settings_icon.png")
settings_icon = pygame.transform.scale(settings_icon, (40,40))


def clear_ui(elements):
    for element in elements:
        element.kill()

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

    settings_button = Button(image=settings_icon, pos=(width-30,25), text_input="", font=button_font, base_color=(0,0,0))
    settings_button.update(screen)

    return settings_button


# main screen functions:
def dashboard():
    page_title = "My Dashboard"
    pygame.display.set_caption(page_title)

    while True:
        dash_mouse_pos = pygame.mouse.get_pos()

        # fill in background
        screen.fill(background_color)

        settings_button = drawHeader(page_title)

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
                elif settings_button.checkForInput(dash_mouse_pos):
                    settings(page_title)

        pygame.display.update()

def expenses():
    page_title = "Expenses Tracker/Input"
    pygame.display.set_caption(page_title)

    while True:
        dash_mouse_pos = pygame.mouse.get_pos()

        # fill in background
        screen.fill(background_color)

        settings_button = drawHeader(page_title)
        
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
                elif settings_button.checkForInput(dash_mouse_pos):
                    settings(page_title)

        pygame.display.update()

def income():
    page_title = "Income Tracker"
    pygame.display.set_caption(page_title)

    while True:
        dash_mouse_pos = pygame.mouse.get_pos()

        # fill in background
        screen.fill(background_color)

        settings_button = drawHeader(page_title)
        
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
                elif settings_button.checkForInput(dash_mouse_pos):
                    settings(page_title)

        pygame.display.update()

def goals():
    page_title = "Goal Progress & Setup"
    pygame.display.set_caption(page_title)

    while True:
        dash_mouse_pos = pygame.mouse.get_pos()

        # fill in background
        screen.fill(background_color)

        settings_button = drawHeader(page_title)
        
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
                elif settings_button.checkForInput(dash_mouse_pos):
                    settings(page_title)

        pygame.display.update()

# login & signup screens
def create_login_elements():
    welcome_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((50, (350/2)-50), (668, 100)), manager=manager, text="Welcome to", object_id="title_label")
    balancebuddy_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((50, 50 + (350/2)), (668, 100)), manager=manager, text="BalanceBuddy", object_id="title_label")

    email_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(((width/2) - 175, 460), (200, 50)), manager=manager, text="Email:", object_id="email_label")
    email_text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(((width/2)-100, 500), (200, 50)), manager=manager, object_id="email_input")

    password_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(((width/2 - 160), 585), (200, 50)), manager=manager, text="Password:", object_id="password_label")
    password_text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(((width/2)-100, 625), (200, 50)), manager=manager, object_id="password_input")
    password_text_input.set_text_hidden(True)

    login_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((width - 230, height - 90), (200, 60)), text="Login", manager=manager, object_id="login_button")

    signup_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((30, height - 90), (200, 60)), text="Sign Up", manager=manager, object_id="signup_button")

    error_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((214, 620), (300, 50)), manager=manager, text="", object_id="error_label")

    return [welcome_label, balancebuddy_label, email_label, email_text_input, password_label, password_text_input, login_button, signup_button, error_label]

def login():
    pygame.display.set_caption("Login Screen")

    current_elements = create_login_elements()

    # game loop
    while True:
        ui_refresh_rate = clock.tick(60)/1000

        login_mouse_pos = pygame.mouse.get_pos()

        # set background color
        screen.fill(background_color)

        # setup login screen background block
        pygame.draw.rect(screen, dock_color, (50, 50, 668, 350))

        # setup email and password borders
        pygame.draw.rect(screen, dock_option_color, ((width/2)-102, 498, 204, 54))
        pygame.draw.rect(screen, dock_option_color, ((width/2)-102, 623, 204, 54))

        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == current_elements[6]:
                        # check if login is valid
                        clear_ui(current_elements)
                        dashboard()
                    elif event.ui_element == current_elements[7]:
                        clear_ui(current_elements)
                        signUp()
            
            manager.process_events(event)
        
        manager.update(ui_refresh_rate)

        manager.draw_ui(screen)

        pygame.display.update()

def create_signup_elements():
    title_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((50, 50), (668, 100)), manager=manager, text="Get Started With BalanceBuddy", object_id="title_label_signup")

    name_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(((width/2)-270, 210), (300, 50)), manager=manager, text="Name:", object_id="name_label")
    name_text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(((width/2)-150, 250), (300, 50)), manager=manager, object_id="name_input")

    email_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(((width/2)-270, 335), (300, 50)), manager=manager, text="Email:", object_id="email_label")
    email_text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(((width/2)-150, 375), (300, 50)), manager=manager, object_id="email_input")

    password_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(((width/2)-255, 460), (300, 50)), manager=manager, text="Password:", object_id="password_label")
    password_text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(((width/2)-150, 500), (300, 50)), manager=manager, object_id="password_input")
    password_text_input.set_text_hidden(True)

    confirm_password_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(((width/2)-220, 585), (300, 50)), manager=manager, text="Confirm Password:", object_id="password_label")
    confirm_password_text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(((width/2)-150, 625), (300, 50)), manager=manager, object_id="password_input")
    confirm_password_text_input.set_text_hidden(True)

    create_account_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((width - 230, height - 90), (200, 60)), text="Create Account", manager=manager, object_id="create_account_button")

    return_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, height - 150), (265, 100)), manager=manager, text="Already have an account?", object_id="return_label")
    login_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((30, height - 90), (200, 60)), text="Login", manager=manager, object_id="login_button")

    return [title_label, name_label, name_text_input, email_label, email_text_input, password_label, password_text_input, confirm_password_label, confirm_password_text_input, create_account_button, login_button, return_label]

def signUp():
    pygame.display.set_caption("Sign Up Screen")

    current_elements = create_signup_elements()

    # game loop
    while True:
        ui_refresh_rate = clock.tick(60)/1000

        signup_mouse_pos = pygame.mouse.get_pos()

        # set background color
        screen.fill(background_color)

        # setup login screen background block
        pygame.draw.rect(screen, dock_color, (50, 50, 668, 100))

        # setup input box borders
        pygame.draw.rect(screen, dock_option_color, ((width/2)-152, 248, 304, 54))
        pygame.draw.rect(screen, dock_option_color, ((width/2)-152, 373, 304, 54))
        pygame.draw.rect(screen, dock_option_color, ((width/2)-152, 498, 304, 54))
        pygame.draw.rect(screen, dock_option_color, ((width/2)-152, 623, 304, 54))

        # check for exit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == current_elements[9]:
                        # check if login is valid
                        clear_ui(current_elements)
                        dashboard()
                    elif event.ui_element == current_elements[10]:
                        clear_ui(current_elements)
                        login()

            manager.process_events(event)

        manager.update(ui_refresh_rate)

        manager.draw_ui(screen)

        pygame.display.update()


# settings menu
def settings(current):
    while True:
        settings_button = drawHeader(current)

        menu_mouse_pos = pygame.mouse.get_pos()

        pygame.draw.rect(screen, dock_color, (width-310, 60, 300, height-160))

        user_text = small_text_font.render("User: Connor Valley", True, text_color)
        text_rect = user_text.get_rect()

        text_x_pos = (width-310 + (300 - text_rect.width) // 2) 
        text_y_pos = (60 + (text_rect.height) // 2)

        screen.blit(user_text, (text_x_pos, text_y_pos))

        # logout button

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if settings_button.checkForInput(menu_mouse_pos):
                    if (current == "My Dashboard"):
                        dashboard()
                    elif (current == "Expenses Tracker/Input"):
                        expenses()
                    elif (current == "Income Tracker"):
                        income()
                    elif (current == "Goal Progress & Setup"):
                        goals()
                

        pygame.display.update()


# start the app on the login page
login()