
# MP3 Section Removal Program

This program allows you to remove a specific section from an MP3 file without altering the offset, since audacity can't apparently.

## Usage

1. Run the program.
2. Enter the name of the MP3 file you want to edit.
3. Specify the start and end times (in milliseconds) of the section to remove.
4. The program will output a new MP3 file with the specified section removed.


## Dependencies

1. **Python 3.6 or latest version**:
    [Python website] (https://www.python.org/downloads/)

2. **Install pydub**:
   ```bash
   pip install pydub
   ```

3. **Install ffmpeg or libav**:
   - For Windows: Download the executable from the [official website](https://ffmpeg.org/download.html) and add it to your system PATH.
   - For Linux: Use your package manager to install it.
     ```bash
     sudo apt-get install ffmpeg
     ```