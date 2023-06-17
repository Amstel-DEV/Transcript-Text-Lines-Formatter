##################################################################################
#                                                                                #
#  Text Lines Formatter                                                          #
#                                                                                #
#  Description:                                                                  #
#  This program extracts and formats character lines from text files based on    #
#  specific tags. It prompts the user to enter the target folder path for        #
#  extraction and the saving path location. The program then iterates over       #
#  all text files in the specified folder, extracts the character lines that     #
#  match the expected format, and saves them to separate files in the specified  #
#  destination folder while preserving the original file format.                 #
#                                                                                #
#  Author: Amstel-Dev                                                            #
#  Github: https://github.com/Amstel-DEV                                         #
#                                                                                #
##################################################################################

import os

def extract_character_lines():
    print("Transcripts S;G Text Lines Formatter\n")
    folder_path = input("Enter the target folder path: ")

    destination_folder = input("Enter the saving path location: ")

    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            input_file = os.path.join(folder_path, filename)
            output_file = os.path.join(destination_folder, "[ext]" + filename)

            with open(input_file, 'r', encoding='utf-8') as f_input:
                lines = f_input.readlines()


            if any('[name]' in line and '[line]' in line and '[%p]' in line for line in lines):
                with open(output_file, 'w', encoding='utf-8') as f_output:
                    for line in lines:
                        if '[name]' in line and '[line]' in line and '[%p]' in line:

                            name_start = line.index('[name]') + len('[name]')
                            name_end = line.index('[line]')
                            name = line[name_start:name_end].strip()

                            line_start = line.index('[line]') + len('[line]')
                            line_end = line.index('[%p]')
                            character_line = line[line_start:line_end].strip()

                            f_output.write(f"Name: {name}\n")
                            f_output.write(f"Character Line: {character_line}\n")
                            f_output.write("\n")
    print("\nOperation is complete...")

extract_character_lines()