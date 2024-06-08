# PyMacKit

**PyMacKit** is a simple macOS toolkit that allows developers to customize menu items for automating tasks such as file modifications and command executions. It's designed with flexibility in mind, making it suitable for developers who wish to tailor tools to their specific needs.

![image](https://github.com/lokile/PyMacKit/assets/107489661/c3c179ca-188c-4092-b5cd-3cf751233f86)




## Features
- **Android Device Management**: Initially equipped with features to manage Android devices via adb. Android developers can easily extend or customize adb commands to enhance functionality like opening a deep link within their apps.

- **Custom Commands**: Developers can add any frequently used commands for quick access and streamlined workflow.

## Setup
1. **Install Python with Homebrew (if not installed yet)**:
   ```bash
   brew install python
2. **Install Virtualenv with Homebrew**: Virtualenv allows you to create isolated Python environments.
    ```bash
    brew install virtualenv
3. **Navigate to the project directory and create the virtual environment**: Change to your project directory and set up a virtual environment named venv. Then, activate it using:
   ```bash
   virtualenv venv
   source venv/bin/active
4. **Install Python packages**: Install all required Python packages specified in your requirements.txt file using pip:
   ```bash
   pip3 install -r requirements.txt
5. **Run the app to ensure it works successfully**:
   ```bash
   python main.py
   
6. **Compile and launch at startup**: After customizing for your needs, you can compile it and set it to launch at startup using the following script:
   ```bash
   ./build.sh
   
## Project Structures
- PyMacKit
  - menu
    - `main_menu.py`: Manages the configuration of the menu UI.
    - `settings.py`: Contains global variables and constants.
    - utils
      - `menu_actions.py`: Handles actions triggered by menu clicks.
  - `build.sh`: A convenient script to compile and run the application.
  - `main.py`: The entry point of the app
  - `setup.py`: Configures the compiled macOS application.

## Author
- Loki Le

## Acknowledgements
- Special thanks to Jared Suttles for developing [rumps](https://github.com/jaredks/rumps), a library that simplifies creating macOS Python statusbar apps. 

## License
- PyMacKit is released under the MIT License. See the `LICENSE` file for the full text.
- This project includes the [rumps](https://github.com/jaredks/rumps) library, which is licensed under the [BSD-3-Clause License](https://github.com/jaredks/rumps/blob/master/LICENSE).
