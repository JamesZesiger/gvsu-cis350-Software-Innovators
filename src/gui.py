import pygame
import pygame_gui
import sys
from database import *
from datetime import date, timedelta
import matplotlib.pyplot as plt
import io 

user = None

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

# setup images
user_icon = pygame.image.load("images/user_icon.png")
user_icon = pygame.transform.scale(user_icon, (40,40))
settings_icon = pygame.image.load("images/settings_icon.png")
settings_icon = pygame.transform.scale(settings_icon, (40,40)).convert_alpha()

# mock user data:
user_expenses = "Down"
user_expense_percent = "10%"
user_expense_list = {"Gas": 50, "Groceries": 100, "Rent": 500, "Utilities": 100, "Entertainment": 50}


def clear_ui(elements):
    for element in elements:
        element.kill()

# utility functions:
def create_dock_elements(current):
    padding_edge = 20
    padding_between = 36

    dash_button_pos = (padding_edge, height-80)
    expenses_button_pos = (dash_button_pos[0] + 150 + padding_between, height-80)
    income_button_pos = (expenses_button_pos[0] + 150 + padding_between, height-80)
    goals_button_pos = (income_button_pos[0] + 150 + padding_between, height-80)
    
    dash_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(dash_button_pos, (150, 60)), text="Dash", manager=manager, object_id="dash_button")
    expenses_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(expenses_button_pos, (150, 60)), text="Expenses", manager=manager, object_id="expenses_button")
    income_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(income_button_pos, (150, 60)), text="Income", manager=manager, object_id="income_button")
    goals_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(goals_button_pos, (150, 60)), text="Goals", manager=manager, object_id="goals_button")

    if (current == "dash"):
        dash_button.disable()
    elif (current == "expenses"):
        expenses_button.disable()
    elif (current == "income"):
        income_button.disable()
    elif (current == "goals"):
        goals_button.disable()

    return [dash_button, expenses_button, income_button, goals_button]

def create_header_elements(text):

    header_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((50, 0), (668, 50)), manager=manager, text=text, object_id="header_label")
    settings_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((width-55, 0), (50, 50)), text="", manager=manager, object_id="settings_button")

    return [header_label, settings_button]

# main screen functions:
def dashboard():
    page_title = "My Dashboard"
    pygame.display.set_caption(page_title)

    dock_elements = create_dock_elements("dash")

    header_elements = create_header_elements(page_title)

    local_elements = []

    recent_expenses_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((30, 80), (344, 50)), manager=manager, text="Recent Expenses:", object_id="module_label")
    expenses_change_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(((width/2) + 5, 80), (344, 50)), manager=manager, text=f"Expenses {user_expenses}", object_id="module_label")
    from_prev_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(((width/2) + 5, 255), (344, 50)), manager=manager, text="From Previous Week", object_id="module_label")

    local_elements.append(recent_expenses_label)
    local_elements.append(expenses_change_label)
    local_elements.append(from_prev_label)

    key_column_width = 15
    cost_column_width = 8

    i = 0
    for key, value in user_expense_list.items():
        if i < 3:
            formatted_key = key.ljust(key_column_width)
            label_text = f"{formatted_key}-- {f'${value}':>{cost_column_width}}"
            expense_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((30, 140 + (list(user_expense_list.keys()).index(key) * 30)), (344, 50)), manager=manager, text=label_text, object_id="expense_item")
            local_elements.append(expense_label)
            i += 1

    expense_percent_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(((width/2) + 5, 80), (344, 225)), manager=manager, text=user_expense_percent, object_id="percent_label")
    local_elements.append(expense_percent_label)

    while True:
        ui_refresh_rate = clock.tick(60)/1000
        dash_mouse_pos = pygame.mouse.get_pos()

        # fill in background
        screen.fill(background_color)

        # draw dock background
        pygame.draw.rect(screen, dock_color, (10, height-90, width-20, 80))

        # draw header background & settings icon
        pygame.draw.rect(screen, dock_color, (0, 0, width, 50))
        screen.blit(settings_icon, (width-50, 5))

        # setup modules
        pygame.draw.rect(screen, module_color, (30, 80, width-60, 225))
        pygame.draw.rect(screen, background_color, ((width/2)-10, 85, 20, 215))
        pygame.draw.rect(screen, module_color, (30, 350, width-60, 225))
        pygame.draw.rect(screen, background_color, ((width/2)-10, 355, 20, 215))
        pygame.draw.rect(screen, module_color, (30, 620, width-60, 225))

        # module 1: expenses module

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == dock_elements[1]:
                        # expenses button
                        clear_ui(dock_elements)
                        clear_ui(header_elements)
                        clear_ui(local_elements)
                        expenses()
                    elif event.ui_element == dock_elements[2]:
                        # income button
                        clear_ui(dock_elements)
                        clear_ui(header_elements)
                        clear_ui(local_elements)
                        income()
                    elif event.ui_element == dock_elements[3]:
                        # goals button
                        clear_ui(dock_elements)
                        clear_ui(header_elements)
                        clear_ui(local_elements)
                        goals()
                    elif event.ui_element == header_elements[1]:
                        # settings button
                        print("open settings menu")
                        # settings(page_title)
            
            manager.process_events(event)

        manager.update(ui_refresh_rate)
        manager.draw_ui(screen)
        pygame.display.update()

def expenses():
    global user
    page_title = "Expenses Tracker/Input"
    pygame.display.set_caption(page_title)

    dock_elements = create_dock_elements("expenses")
    header_elements = create_header_elements(page_title)

    # Track local elements to clear them later
    local_elements = []

    # Create Text Input and Button Elements
    expense_name_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((200, 520), (150, 30)),  # Adjusted position to leave space below the graph
        text="Expense Name:",
        manager=manager,
        object_id="email_label"
    )
    expense_name_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((360, 520), (200, 30)),  # Positioned next to label
        manager=manager,
        object_id="name_input"
    )
    expense_cost_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((200, 570), (150, 30)),  # Adjusted position
        text="Expense Cost:",
        manager=manager,
        object_id="email_label"
    )
    expense_cost_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((360, 570), (200, 30)),  # Positioned next to label
        manager=manager,
        object_id="name_input"
    )
    add_expense_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((width // 2 - 100, 630), (200, 60)),  # Increased button size
        text="Add Expense",
        manager=manager,
        object_id="login_button"
    )

    # Add elements to the local tracking list
    local_elements.extend([
        expense_name_label,
        expense_name_input,
        expense_cost_label,
        expense_cost_input,
        add_expense_button
    ])

    # Function to create the expenses graph
    def create_expenses_graph(user):
        days = []
        totals = []
        day_pointer = date.today() - timedelta(days=6)

        for _ in range(7):
            formatted_date = day_pointer.strftime("%m/%d/%y")
            day_expense = sum(user.expenses.get(formatted_date, {}).values())
            days.append(formatted_date)
            totals.append(day_expense)
            day_pointer += timedelta(days=1)

        # Adjusted figure size for a slightly smaller graph
        plt.figure(figsize=(7, 3.5))  
        plt.bar(days, totals, color='green')
        plt.title("Expenses Last 7 Days")
        plt.xlabel("Date")
        plt.ylabel("Amount ($)")
        plt.xticks(rotation=45)
        plt.ylim(0, max(totals) + 50)  # Axis from 0 to max value + buffer
        plt.tight_layout()

        # Render to a surface
        buffer = io.BytesIO()
        plt.savefig(buffer, format="PNG")
        buffer.seek(0)
        plt.close()
        graph_image = pygame.image.load(buffer)
        buffer.close()

        return graph_image

    # Generate the initial graph
    graph_surface = create_expenses_graph(user)

    while True:
        ui_refresh_rate = clock.tick(60) / 1000

        # Fill in background
        screen.fill(background_color)

        # Draw dock background
        pygame.draw.rect(screen, dock_color, (10, height - 90, width - 20, 80))

        # Draw header background & settings icon
        pygame.draw.rect(screen, dock_color, (0, 0, width, 50))
        screen.blit(settings_icon, (width - 50, 5))

        # Draw module background
        pygame.draw.rect(screen, module_color, (30, 80, width - 60, 425))

        # Display the graph
        graph_rect = graph_surface.get_rect(center=(width // 2, 285))  # Adjusted vertical position
        screen.blit(graph_surface, graph_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == dock_elements[0]:
                        # Dashboard button
                        clear_ui(dock_elements)
                        clear_ui(header_elements)
                        clear_ui(local_elements)
                        dashboard()
                    elif event.ui_element == dock_elements[2]:
                        # Income button
                        clear_ui(dock_elements)
                        clear_ui(header_elements)
                        clear_ui(local_elements)
                        income()
                    elif event.ui_element == dock_elements[3]:
                        # Goals button
                        clear_ui(dock_elements)
                        clear_ui(header_elements)
                        clear_ui(local_elements)
                        goals()
                    elif event.ui_element == add_expense_button:
                        # Handle adding an expense
                        expense_name = expense_name_input.get_text()
                        try:
                            expense_cost = float(expense_cost_input.get_text())
                            user.add_expenses(expense_name, expense_cost)
                            update_user_data(user)
                            print(f"Added expense: {expense_name} - ${expense_cost}")
                            # Clear inputs
                            expense_name_input.set_text("")
                            expense_cost_input.set_text("")
                            # Update the graph
                            graph_surface = create_expenses_graph(user)
                        except ValueError:
                            print("Invalid cost. Please enter a numeric value.")

            manager.process_events(event)

        manager.update(ui_refresh_rate)
        manager.draw_ui(screen)
        pygame.display.update()

def income():
    page_title = "Income Tracker"
    pygame.display.set_caption(page_title)

    dock_elements = create_dock_elements("income")

    header_elements = create_header_elements(page_title)

    while True:
        ui_refresh_rate = clock.tick(60)/1000
        dash_mouse_pos = pygame.mouse.get_pos()

        # fill in background
        screen.fill(background_color)

        # draw dock background
        pygame.draw.rect(screen, dock_color, (10, height-90, width-20, 80))

        # draw header background & settings icon
        pygame.draw.rect(screen, dock_color, (0, 0, width, 50))
        screen.blit(settings_icon, (width-50, 5))

        # draw modules
        pygame.draw.rect(screen, module_color, (30, 80, width-60, 425))
        pygame.draw.rect(screen, text_color, ((width/2)-244, 640, 488, 170))
        pygame.draw.rect(screen, module_color, ((width/2)-244, 640, 488, 170), 8)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == dock_elements[0]:
                        # dashboard button
                        clear_ui(dock_elements)
                        clear_ui(header_elements)
                        dashboard()
                    elif event.ui_element == dock_elements[1]:
                        # expenses button
                        clear_ui(dock_elements)
                        clear_ui(header_elements)
                        expenses()
                    elif event.ui_element == dock_elements[3]:
                        # goals button
                        clear_ui(dock_elements)
                        clear_ui(header_elements)
                        goals()
                    # elif event.ui_element == header_elements[1]:
                    #     settings(page_title)

            manager.process_events(event)

        manager.update(ui_refresh_rate)
        manager.draw_ui(screen)
        pygame.display.update()

def goals():
    page_title = "Goal Progress & Setup"
    pygame.display.set_caption(page_title)

    dock_elements = create_dock_elements("goals")

    header_elements = create_header_elements(page_title)

    while True:
        ui_refresh_rate = clock.tick(60)/1000
        dash_mouse_pos = pygame.mouse.get_pos()

        # fill in background
        screen.fill(background_color)

        # draw dock background
        pygame.draw.rect(screen, dock_color, (10, height-90, width-20, 80))

        # draw header background & settings icon
        pygame.draw.rect(screen, dock_color, (0, 0, width, 50))
        screen.blit(settings_icon, (width-50, 5))

        # draw modules
        pygame.draw.rect(screen, module_color, (30, 80, width-60, 225))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == dock_elements[0]:
                        # dashboard button
                        clear_ui(dock_elements)
                        clear_ui(header_elements)
                        dashboard()
                    elif event.ui_element == dock_elements[1]:
                        # expenses button
                        clear_ui(dock_elements)
                        clear_ui(header_elements)
                        expenses()
                    elif event.ui_element == dock_elements[2]:
                        # income button
                        clear_ui(dock_elements)
                        clear_ui(header_elements)
                        income()
                    elif event.ui_element == header_elements[1]:
                        # settings button
                        print("open settings menu")
                        # settings(page_title)

            manager.process_events(event)
        
        manager.update(ui_refresh_rate)
        manager.draw_ui(screen)
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
    global user
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
                        user = login_user(current_elements[3].get_text(), current_elements[5].get_text())
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
# def settings(current):
#     while True:

#         menu_mouse_pos = pygame.mouse.get_pos()

#         pygame.draw.rect(screen, dock_color, (width-310, 60, 300, height-160))

#         user_text = small_text_font.render("User: Connor Valley", True, text_color)
#         text_rect = user_text.get_rect()

#         text_x_pos = (width-310 + (300 - text_rect.width) // 2) 
#         text_y_pos = (60 + (text_rect.height) // 2)

#         screen.blit(user_text, (text_x_pos, text_y_pos))

#         # logout button

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

        # pygame.display.update()

# settings menu
def settings():
    
    pass

# start the app on the login page
login()
