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
    logout_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((width-130, 5), (120, 40)), text="Logout", manager=manager, object_id="logout_button")
    if (user.experience != None):
        experience_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 0), (200, 50)), manager=manager, text=f"EXP: {user.experience}", object_id="experience_label")
    else:
        experience_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 0), (200, 50)), manager=manager, text="EXP: 0", object_id="experience_label")

    return [header_label, logout_button, experience_label]

# main screen functions:
def dashboard():
    page_title = "My Dashboard"
    pygame.display.set_caption(page_title)

    get_all_expenses(user)
    get_all_income(user)

    dock_elements = create_dock_elements("dash")

    header_elements = create_header_elements(page_title)

    local_elements = []

    if (user.expenses != {}):
        print(user.expenses)
        key_column_width = 15
        cost_column_width = 8

        i = 0
        for item in user.expenses:
            expense = user.expenses[item]
            for key in expense:
                cost = expense[key]
                if i < 4:
                    formatted_key = key.ljust(key_column_width)
                    label_text = f"{formatted_key}-- {f'${cost}':>{cost_column_width}}"
                    expense_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((30, 140 + (i * 30)), (344, 50)), manager=manager, text=label_text, object_id="expense_item")
                    local_elements.append(expense_label)
                    i += 1
        
        # expenses module
        recent_expenses_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((30, 80), (344, 50)), manager=manager, text="Recent Expenses:", object_id="module_label")
        expenses_change_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(((width/2) + 5, 80), (344, 50)), manager=manager, text="Total Expenses:", object_id="module_label")
        from_prev_expenses_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(((width/2) + 5, 255), (344, 50)), manager=manager, text="Current Week", object_id="module_label")

        local_elements.append(recent_expenses_label)
        local_elements.append(expenses_change_label)
        local_elements.append(from_prev_expenses_label)

        sum_expenses = user.sum_of_current_expenses()

        expense_total_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(((width/2) + 5, 80), (344, 225)), manager=manager, text=f"${sum_expenses}", object_id="total_label")
        local_elements.append(expense_total_label)

    else:
        no_expenses_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((30, 80), (width-60, 225)), manager=manager, text="Expenses data will show up here!", object_id="module_label")
        local_elements.append(no_expenses_label)

    if (user.income != {}):
        # income module
        i = 0
        for item in user.income:
            userIncome = user.income[item]
            for key in userIncome:
                amount = userIncome[key]
                if i < 4:
                    formatted_key = key.ljust(key_column_width)
                    label_text = f"{formatted_key}-- {f'${amount}':>{cost_column_width}}"
                    income_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((30, 400 + (i * 30)), (344, 50)), manager=manager, text=label_text, object_id="income_item")
                    local_elements.append(income_label)
                    i += 1

        prev_income = user.sum_of_current_income()

        recent_income_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((30, 350), (344, 50)), manager=manager, text="Recent Income:", object_id="module_label")
        last_week_income_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(((width/2), 350), (344, 50)), manager=manager, text="Total Income:", object_id="module_label")
        total_income_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(((width/2), 400), (344, 100)), manager=manager, text=f"${prev_income}", object_id="total_label")
        from_prev_income_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(((width/2), 500), (344, 50)), manager=manager, text="Current Week", object_id="module_label")
        
        local_elements.append(recent_income_label)
        local_elements.append(last_week_income_label)
        local_elements.append(total_income_label)
        local_elements.append(from_prev_income_label)
    else:
        no_income_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((30, 350), (width-60, 225)), manager=manager, text="Income data will show up here!", object_id="module_label")
        local_elements.append(no_income_label)

    # goals module

    # savings_goal_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((30, 620), (344, 30)), manager=manager, text=f"Savings Goal: ${user_savings_goal}", object_id="module_label")
    # current_balance_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((width-404, 815), (344, 30)), manager=manager, text=f"Current Balance: ${user_balance}", object_id="module_label")

    # local_elements.append(savings_goal_label)
    # local_elements.append(current_balance_label)

    while True:
        ui_refresh_rate = clock.tick(60)/1000

        # fill in background
        screen.fill(background_color)

        # draw dock background
        pygame.draw.rect(screen, dock_color, (10, height-90, width-20, 80))

        # draw header background
        pygame.draw.rect(screen, dock_color, (0, 0, width, 50))

        # setup modules
        pygame.draw.rect(screen, module_color, (30, 80, width-60, 225))
        if (user.expenses != {}):
            pygame.draw.rect(screen, background_color, ((width/2)-10, 85, 20, 215))

        pygame.draw.rect(screen, module_color, (30, 350, width-60, 225))
        if (user.income != {}):
            pygame.draw.rect(screen, background_color, ((width/2)-10, 355, 20, 215))

        # pygame.draw.rect(screen, module_color, (30, 620, width-60, 225))

        # bar for goals module

        # pygame.draw.rect(screen, background_color, ((width/2)-300, 710, 600, 50))
        
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
                        # logout button
                        clear_ui(dock_elements)
                        clear_ui(header_elements)
                        clear_ui(local_elements)
                        login()
            
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
        day_pointer = datetime.now() - timedelta(days=6)

        for _ in range(7):
            formatted_date = day_pointer.strftime("%m/%d/%y")

            # Sum all expenses that match the current date
            day_expense = sum(
                amount
                for key, expenses in user.expenses.items()
                if key.startswith(formatted_date)  # Match keys that start with the date
                for amount in expenses.values()  # Sum all amounts for the date
            )

            days.append(formatted_date)
            totals.append(day_expense)
            day_pointer += timedelta(days=1)

        plt.figure(figsize=(7, 3.5))  
        plt.bar(days, totals, color='green')
        plt.title("Expenses Last 7 Days")
        plt.xlabel("Date")
        plt.ylabel("Amount ($)")
        plt.xticks(rotation=45)
        plt.ylim(0, max(totals) + 50)  # Axis from 0 to max value + buffer
        plt.tight_layout()

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
                    elif event.ui_element == header_elements[1]:
                        # logout button
                        clear_ui(dock_elements)
                        clear_ui(header_elements)
                        clear_ui(local_elements)
                        login()

            manager.process_events(event)

        manager.update(ui_refresh_rate)
        manager.draw_ui(screen)
        pygame.display.update()

def income():
    page_title = "Income Tracker"
    pygame.display.set_caption(page_title)

    dock_elements = create_dock_elements("income")
    current_elements = create_income_elements()
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
                    if event.ui_element == current_elements[5]:
                        user.add_income(current_elements[2].get_text(),float(current_elements[4].get_text()))
                        update_user_data(user)
                        current_elements[3].kill()
                        if (user.income != {}):
                            current_elements[3] = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((50, 50 + (height/2)+150), (668, 100)), manager=manager, text=(f"${user.sum_of_current_income()}"), object_id="password_label")
                        else:
                            current_elements[3] = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((50, 50 + (height/2)+150), (668, 100)), manager=manager, text="Income Data Will Show Up Here!", object_id="password_label")
                        #database.update_user_data(user)
                    elif event.ui_element == dock_elements[0]:
                        # dashboard button
                        clear_ui(dock_elements)
                        clear_ui(header_elements)
                        clear_ui(current_elements)
                        dashboard()
                    elif event.ui_element == dock_elements[1]:
                        # expenses button
                        clear_ui(dock_elements)
                        clear_ui(header_elements)
                        clear_ui(current_elements)
                        expenses()
                    elif event.ui_element == dock_elements[3]:
                        # goals button
                        clear_ui(dock_elements)
                        clear_ui(header_elements)
                        clear_ui(current_elements)
                        goals()
                    # elif event.ui_element == header_elements[1]:
                    #     settings(page_title)

            manager.process_events(event)

        manager.update(ui_refresh_rate)
        manager.draw_ui(screen)
        pygame.display.update()

def create_income_elements():
    global user
    income_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((width/8, 100), (65, 65)), manager=manager, text="Label:", object_id="password_label")
    Amount = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(((width-300), 100), (65, 65)), manager=manager, text="Amount", object_id="password_label")
    income_label_text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(((width/8), 150), (200, 50)), manager=manager, object_id="email_input")
    Amount_text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(((width-300), 150), (200, 50)), manager=manager, object_id="password_input")
    log_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 200 + (350/2)), (668, 100)), text="Log", manager=manager, object_id="log_button")
    sunday = date.today() - timedelta(days = date.today().isoweekday())
    saturday = sunday + timedelta(days = 6)
    current_bal = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(((width/2)-200, (height/2)+40), (400, 200)), manager=manager, text=f"Total Income for week of {sunday.strftime("%m/%d")}-{saturday.strftime("%m/%d")}", object_id="password_label")
    balance = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((50, 50 + (height/2)+150), (668, 100)), manager=manager, text=(f"${user.sum_of_current_income()}"), object_id="password_label")

    error_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((214, 620), (300, 50)), manager=manager, text="", object_id="error_label")

    return [income_label, Amount, income_label_text_input, balance, Amount_text_input, log_button, current_bal, error_label]


def goals():
    page_title = "Goal Progress & Setup"
    pygame.display.set_caption(page_title)

    dock_elements = create_dock_elements("goals")

    header_elements = create_header_elements(page_title)

    local_elements = []

    user_construction_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((30, 80), (width-60, 225)), manager=manager, text="This module is under construction!", object_id="module_label")

    local_elements.append(user_construction_label)

    while True:
        ui_refresh_rate = clock.tick(60)/1000
        dash_mouse_pos = pygame.mouse.get_pos()

        # fill in background
        screen.fill(background_color)

        # draw dock background
        pygame.draw.rect(screen, dock_color, (10, height-90, width-20, 80))

        # draw header background & settings icon
        pygame.draw.rect(screen, dock_color, (0, 0, width, 50))

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
                        clear_ui(local_elements)
                        dashboard()
                    elif event.ui_element == dock_elements[1]:
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
                    elif event.ui_element == header_elements[1]:
                        # logout button
                        clear_ui(dock_elements)
                        clear_ui(header_elements)
                        clear_ui(local_elements)
                        login()

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

    error_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(((width/2)-150, 700), (300, 50)), manager=manager, text="", object_id="error_label")

    return [welcome_label, balancebuddy_label, email_label, email_text_input, password_label, password_text_input, login_button, signup_button, error_label]

def login():
    global user
    user = None
    pygame.display.set_caption("Login Screen")

    current_elements = create_login_elements()

    # game loop
    while True:
        ui_refresh_rate = clock.tick(60)/1000

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
                        email = current_elements[3].get_text()
                        password = current_elements[5].get_text()
                        # check if login is valid
                        if (email) and (password):
                            user = login_user(email, password)
                            if user:
                                clear_ui(current_elements)
                                dashboard()
                            else:
                                current_elements[8].set_text("Invalid Credentials")
                        else:
                            current_elements[8].set_text("Please enter each field")

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

    error_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(((width/2)-334, 700), (668, 50)), manager=manager, text="", object_id="error_label")

    return [title_label, name_label, name_text_input, email_label, email_text_input, password_label, password_text_input, confirm_password_label, confirm_password_text_input, create_account_button, login_button, return_label, error_label]

def signUp():
    global user
    user = None
    pygame.display.set_caption("Sign Up Screen")

    current_elements = create_signup_elements()

    # game loop
    while True:
        ui_refresh_rate = clock.tick(60)/1000

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
                        # check if signup is valid
                        error = False
                        if (current_elements[2].get_text()):
                            user_name = current_elements[2].get_text()
                        else:
                            current_elements[12].set_text("Please enter each field")
                            error = True
                        if (current_elements[4].get_text()):
                            email = current_elements[4].get_text()
                        else:
                            current_elements[12].set_text("Please enter each field")
                            error = True
                        if (current_elements[6]) and (current_elements[6].get_text() == current_elements[8].get_text()):
                            password = current_elements[6].get_text()
                            if len(password) < 8:
                                current_elements[12].set_text("Password must be at least 8 characters")
                                error = True
                        else:
                            current_elements[12].set_text("Passwords do not match")
                            error = True

                        if not error:
                            register_user(email, password, user_name)
                            user = login_user(email, password)
                            if user:
                                clear_ui(current_elements)
                                dashboard()
                            else:
                                current_elements[12].set_text("Failed to Create Account")
                            
                    elif event.ui_element == current_elements[10]:
                        clear_ui(current_elements)
                        login()

            manager.process_events(event)

        manager.update(ui_refresh_rate)

        manager.draw_ui(screen)

        pygame.display.update()

# start the app on the login page
login()
