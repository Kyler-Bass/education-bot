import os
import pygame 

from src.window import Window
from src.util_funcs import programShouldExit

API_KEY = os.getenv("API_KEY")

def main():
    SCREEN_SIZE = (600,800)
    FONT_SIZE = 30
    window = Window(SCREEN_SIZE, FONT_SIZE)
    
    
    
    while window.running:
        if (programShouldExit()):
            pygame.quit()
            break
        

        # Run a specific function based on the current state of the window 
        funcToRun = {
            0: window.displayStartMenu,
            1: window.displayGame
        }
        funcToRun[window.state]()

        # Update window, pass in mouse clicks and pos 
        window.updateScreen(pygame.mouse.get_pressed(), pygame.mouse.get_pos())



if __name__ == "__main__":
    main()