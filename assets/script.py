import os
import platform

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def extract_all_character_lines():
    clear()
    print("Transcripts Text Lines Formatter\n")
    folder_path = input("Enter the target folder path: ")
    clear()
    print("Transcripts Text Lines Formatter\n")
    destination_folder = input("Enter the saving path location: ")

    def bulk_operation():
        for filename in os.listdir(folder_path):
            if filename.endswith('.txt'):
                input_file = os.path.join(folder_path, filename)
                output_file = os.path.join(destination_folder, "[All]" + filename)

                with open(input_file, 'r', encoding='utf-8') as f_input:
                    lines = f_input.readlines()

                with open(output_file, 'w', encoding='utf-8') as f_output:
                    character_name = None
                    for line in lines:
                        line = line.strip()
                        if line.startswith('[name]') and '[line]' in line and '[%p]' in line:
                            if character_name is not None:
                                f_output.write("\n\n")
                            name_start = line.index('[name]') + len('[name]')
                            name_end = line.index('[line]')
                            character_name = line[name_start:name_end].strip()

                            line_start = line.index('[line]') + len('[line]')
                            line_end = line.index('[%p]')
                            character_line = line[line_start:line_end].strip()

                            f_output.write(f"Name: {character_name}\n")
                            f_output.write(f"Character Line: {character_line}\n")

                        elif '[%p]' in line:
                            prompt_line = line.replace('[%p]', '').strip()
                            if prompt_line:
                                f_output.write(f"\nPrompt Line: {prompt_line}\n")

    def single_operation():
        clear()
        print("Transcripts S;G Text Lines Formatter\n")
        f_name = input("Please enter a name for the output file: ")
        output_file = os.path.join(destination_folder, f_name + ".txt")

        with open(output_file, 'w', encoding='utf-8') as f_output:
            for filename in os.listdir(folder_path):
                if filename.endswith('.txt'):
                    input_file = os.path.join(folder_path, filename)

                    with open(input_file, 'r', encoding='utf-8') as f_input:
                        lines = f_input.readlines()

                    character_name = None
                    for line in lines:
                        line = line.strip()
                        if line.startswith('[name]') and '[line]' in line and '[%p]' in line:
                            if character_name is not None:
                                f_output.write("\n\n")
                            name_start = line.index('[name]') + len('[name]')
                            name_end = line.index('[line]')
                            character_name = line[name_start:name_end].strip()

                            line_start = line.index('[line]') + len('[line]')
                            line_end = line.index('[%p]')
                            character_line = line[line_start:line_end].strip()

                            f_output.write(f"Name: {character_name}\n")
                            f_output.write(f"Character Line: {character_line}\n")

                        elif '[%p]' in line:
                            prompt_line = line.replace('[%p]', '').strip()
                            if prompt_line:
                                f_output.write(f"\nPrompt Line: {prompt_line}\n")

    clear()
    print("Transcripts Text Lines Formatter\n")
    operation = input("Do you want to save the output in a single TXT file? (Y/N): ")

    if operation.lower() == 'y':
        single_operation()

    elif operation.lower() == "n":
        bulk_operation()

    input("\nOperation is complete...")
    clear()

def extract_single_character_lines():
    clear()
    print("Transcripts Character Text Lines Formatter\n")
    folder_path = input("Enter the target folder path: ")
    clear()
    print("Transcripts Character Text Lines Formatter\n")
    destination_folder = input("Enter the saving path location: ")
    clear()
    print("Transcripts Character Text Lines Formatter\n")
    specific_name = input("Enter the specific name to extract character lines for: ")

    output_file = os.path.join(destination_folder, "[Character] " + specific_name + ".txt")

    with open(output_file, 'w', encoding='utf-8') as f_output:
        for filename in os.listdir(folder_path):
            if filename.endswith('.txt'):
                input_file = os.path.join(folder_path, filename)

                with open(input_file, 'r', encoding='utf-8') as f_input:
                    lines = f_input.readlines()

                for line in lines:
                    line = line.strip()
                    if line.startswith('[name]') and '[line]' in line and '[%p]' in line:
                        name_start = line.index('[name]') + len('[name]')
                        name_end = line.index('[line]')
                        character_name = line[name_start:name_end].strip()

                        if character_name == specific_name:
                            line_start = line.index('[line]') + len('[line]')
                            line_end = line.index('[%p]')
                            character_line = line[line_start:line_end].strip()

                            f_output.write(f"Name: {character_name}\n")
                            f_output.write(f"Character Line: {character_line}\n")
                            f_output.write("\n")

    input("\nOperation is complete...")
    clear()


def show_about():
    clear()
    print("╔═══════════════════════════════════════════════════╗")
    print("║             About Transcript Formatter            ║")
    print("╠═══════════════════════════════════════════════════╣")
    print("║ Transcript Formatter is a Python script designed  ║")
    print("║ to help you extract and format character lines    ║")
    print("║ from text files, specifically designed for S;G    ║")
    print("║ (Steins;Gate) transcripts.                        ║")
    print("║                                                   ║")
    print("║ Features:                                         ║")
    print("║  - Extract all character lines from a folder of   ║")
    print("║    text files and save them in a single output    ║")
    print("║    file.                                          ║")
    print("║  - Extract character lines for a specific         ║")
    print("║    character and save them in a separate output   ║")
    print("║    file.                                          ║")
    print("║  - Supports Windows and Unix/Linux operating      ║")
    print("║    systems.                                       ║")
    print("║                                                   ║")
    print("║ Author:                                           ║")
    print("║  - Name: Amstel-Dev                               ║")
    print("║  - Repository: https://github.com/Amstel-DEV/     ║")
    print("║    Transcript-Text-Lines-Formatter                ║")
    print("╚═══════════════════════════════════════════════════╝")
    input()
    clear()