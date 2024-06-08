from menu import settings
from menu.main_menu import PyMacKit

if __name__ == "__main__":
    print("I'm opening")
    settings.MainMenu = PyMacKit()
    settings.MainMenu.run()
