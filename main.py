from menus import settings
from menus.main_menu import PyToolkit

if __name__ == "__main__":
    print("I'm opening")
    settings.MainMenu = PyToolkit()
    settings.MainMenu.run()
