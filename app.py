import os
import importlib
from colorama import Fore, Style, init
from loader.route_loader import load_routes


# Initialize colorama
init(autoreset=True)

# Create a function to log messages with colors
def log_info(message):
    print(Fore.GREEN + "[INFO] " + message)

def log_error(message):
    print(Fore.RED + "[ERROR] " + message)

def log_warning(message):
    print(Fore.YELLOW + "[WARNING] " + message)

# Load modules dynamically from the ./modules directory
def load_modules():
    # Get the path to the modules directory
    modules_dir = './modules'

    # Check if the directory exists
    if not os.path.exists(modules_dir):
        log_error("Modules directory does not exist!")
        return

    # Get all Python files in the modules directory
    for filename in os.listdir(modules_dir):
        if filename.endswith('.py'):
            module_name = filename[:-3]  # Remove '.py' extension
            log_info(f"Loading module: {module_name}")

            try:
                # Dynamically import the module
                module = importlib.import_module(f'modules.{module_name}')
                log_info(f"Module {module_name} loaded successfully.")
            except Exception as e:
                log_error(f"Failed to load module {module_name}: {e}")

# Default route for Flask app
from flask import Flask

app = Flask(__name__)
load_routes(app)


@app.route('/')
def home():
    log_info("Home route accessed.")
    return 'Hello, World!'

# Run the app
if __name__ == '__main__':
    log_info("Starting the Flask app.")
    load_modules()  # Load all modules from the ./modules directory
    app.run(debug=True)
