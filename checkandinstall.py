import importlib

def check_and_install_libraries():
    required_libraries = ['basicpitch', 'mido', 'pydub']
    missing_libraries = []
    
    for library in required_libraries:
        try:
            importlib.import_module(library)
        except ImportError:
            missing_libraries.append(library)
    
    if missing_libraries:
        print(f"Missing libraries: {', '.join(missing_libraries)}")
        print("Installing libraries...")
        for library in missing_libraries:
            try:
                importlib.import_module('pip').main(['install', library])
                print(f"Successfully installed {library}")
            except Exception as e:
                print(f"Failed to install {library}: {str(e)}")
    else:
        print("All required libraries are already installed.")

# Call the function to check and install libraries
