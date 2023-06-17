# Transcript Text Lines Formatter

Transcript Text Lines Formatter is a Python program that extracts and formats character lines from text files based on specific tags. It provides two variations: one for extracting all character lines and another for extracting character lines for a specific character. The program prompts the user to enter the target folder path for extraction, the saving path location, and the specific character name (optional). It then iterates over all text files in the specified folder, extracts the character lines that match the expected format, and saves them to separate files in the specified destination folder while preserving the original file format.

## Description

This repository contains two programs:

1. **Transcript Text Lines Formatter**: Extracts character lines from text files and saves them to separate files.
2. **Transcripts Character Text Lines Formatter**: Extracts character lines for a specific character from text files and saves them to separate files.

Both programs are designed specifically for text files containing transcripts or dialogue lines, such as those found in visual novels or screenplays. They identify lines with character names and extract the corresponding character lines, ignoring any non-character lines. The extracted lines are saved in new text files with the format [ext]original_filename.txt.

## Usage

1. Clone the repository or download the `transcript_text_lines_formatter.py` and `transcripts_character_text_lines_formatter.py` files.
2. Make sure you have Python installed (Python 3.6 or later).
3. Open a terminal or command prompt and navigate to the directory where the Python files are located.
4. Run the following command to execute the desired program:

   - For Transcript Text Lines Formatter:
     ```shell
     python transcript_text_lines_formatter.py
     ```

   - For Transcripts Character Text Lines Formatter:
     ```shell
     python transcripts_character_text_lines_formatter.py
     ```

5. Follow the prompts to enter the target folder path for extraction, the saving path location, and the specific character name (for Transcripts Character Text Lines Formatter).
6. The program will process the text files and save the extracted character lines to new files in the specified destination folder.

## Examples
**Transcript Text Lines Formatter**
![Example Image](examples/TTLF%20-%20SS001.JPG)

**Transcripts Character Text Lines Formatter**
![Example Image](examples/TCTLF%20-%20SS001.JPG)

## License

This project is licensed under the [MIT License](LICENSE).

## Author

Amstel-Dev
