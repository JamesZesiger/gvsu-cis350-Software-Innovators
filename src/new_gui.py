import dearpygui.dearpygui as dpg

# Create the context
dpg.create_context()

# Define a function to create a custom module with text and background shape
def create_module(x, y, width, height, title, value):
    with dpg.drawlist(width=width, height=height, pos=(x, y)):
        # Draw module background
        dpg.draw_rectangle((0, 0), (width, height), color=(100, 100, 200, 255), fill=(100, 100, 200, 255), thickness=1)
        
        # Draw the title
        dpg.draw_text((10, 10), title, color=(255, 255, 255, 255), size=20)
        
        # Draw the value text below the title
        dpg.draw_text((10, 40), value, color=(255, 255, 255, 255), size=18)

# Create the main window
with dpg.window(label="Custom Dashboard", width=768, height=960):
    
    # Draw a header background with text
    with dpg.drawlist(width=600, height=80, pos=(0, 0)):
        dpg.draw_rectangle((0, 0), (600, 80), color=(50, 150, 50, 255), fill=(50, 150, 50, 255), thickness=1)
        dpg.draw_text((20, 25), "Budget Overview", color=(255, 255, 255, 255), size=30)
    
    # Create a custom module for "Balance"
    create_module(20, 100, 250, 100, "Balance", "$5000")
    
    # Create another module for "Expenses"
    create_module(300, 100, 250, 100, "Expenses", "$1200")
    
    # Create another module for "Savings Goal"
    create_module(20, 220, 530, 100, "Savings Goal", "40%")

# Setup and display the viewport
dpg.create_viewport(title='Custom Dashboard', width=600, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()

# Start the event loop
dpg.start_dearpygui()
dpg.destroy_context()
