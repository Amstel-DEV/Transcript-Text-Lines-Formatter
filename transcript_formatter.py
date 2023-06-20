import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

assets_dir = os.path.join(current_dir, 'assets')
sys.path.append(assets_dir)

import script

script.clear()

while True:
    print("╔════════════════════════════════════════════╗")
    print("║           Transcript Formatter             ║")
    print("╠════════════════════════════════════════════╣")
    print("║  Main Menu:                                ║")
    print("║    1. Extract All Character Lines          ║")
    print("║    2. Extract Character Lines by Name      ║")
    print("║    3. About                                ║")
    print("║    Q. Quit                                 ║")
    print("╚════════════════════════════════════════════╝")

    selection = input("\n\nPlease enter your selection: ")

    if selection == "1":
        script.extract_all_character_lines()

    elif selection == "2":
        script.extract_single_character_lines()

    elif selection == "3":
        script.show_about()

    elif selection.lower() == "q":
        break

    else:
        script.clear()
        input("Invalid input. Try again...")
        script.clear()
