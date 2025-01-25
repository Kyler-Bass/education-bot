import os
import pygame 

from src.window import Window
from src.util_funcs import programShouldExit

API_KEY = os.getenv("API_KEY")

def main():
    SCREEN_SIZE = (600,600)
    FONT_SIZE = 30
    window = Window(SCREEN_SIZE, FONT_SIZE)
    
    # Add start screen 
    window.displayStartMenu()
    
    while window.running:
        if (programShouldExit()):
            pygame.quit()
            break
        
        # Update window 
        window.updateScreen()

        # Check for mouse clicks 



if __name__ == "__main__":
    main()