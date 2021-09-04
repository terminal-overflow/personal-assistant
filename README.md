# Python Personal Assistant
## Personal Assistant Information
This personal assistant uses speechrecognition to convert STT and uses pyttsx3 for TTS. The purpose of this program is to help you with certain tasks on your computer or to get information for you.

### Note
**The development of this program has slowed down and will be updated very occasionally.**
This program is only available for MacOS (Darwin) computers.

### Dependencies
* speechrecognition
* pyaudio (install port audio if any problems)
* pyttsx3
* wikipedia

---
## Installation via GitHub
### Clone the repository (Developers)
```
 git clone https://github.com/terminal-flow/personal-assistant.git
```

### Or Download (Non-Developer)
* Click the download button
* Unzip the project file

### Change directory the project root
```
cd path/to/personal-assistant
```

### Install
```
source setup.sh
```
or
```
python3 installer
```
#### Note
**A virtualenv is automatically created and used.** This may take around a minute.

### Run
Follow the installation message on how to run personal assistant.

---
## Usage
### Startup arguments
The optional startup arguments are mode and verbose.
* mode `-m text` for startup text mode - default is voice mode
* verbose `-v off` for no verbose - default is on
* help `-h` for more information on these arguments

### Startup with Voice Mode
Personal assistant will say initialise and then begin to listen indefinitely.
If the verbose argument is on, the speech it detects will be displayed in your terminal/IDE.
Otherwise no text will be outputted, except for errors.

### Startup with Text Mode
Personal assistant will output initialising... and then wait for your command to be entered indefinitely.

### Wake word
The default wake word is 'computer'. To change the wake word, input 'change wake word' and then input your new **one word** wake word. To change back to default, input 'reset wake word'.

---
## Voice Mode
If just the wake word is heard, personal assistant will play a welcoming tone and wait for your command for around 5 seconds. If no sound is heard, personal assistant will disregard.

## Text Mode
All the inputs will need to be typed in your terminal/IDE, however, the wake word does not need to be typed.

---
## Functions

The functions for this program are:
* Greetings (you can say)
    * hello, hi, hey etc
    * thank you, thanks, cheers
    * what is your name
* Change mode
* Change wake word
* Get current time
* Get current Date
* Get spelling of word
* Ask the functions
* Simple system controls
    * System report
    * Volume up
    * Volume down
    * Mute
    * Unmute
    * Sleep
* Set a timer
* Search wikipedia for...
* Perform maths calculations
    * +, -, *, /
    * Square a number
    * Cube a number
    * x to the power of x
    * Find the square root
* Make a note... (iNote)
* Make a text note...
* Open YouTube
* Search YouTube for...
* Open and search with search engines (Default is DuckDuckGo)
    * Open DuckDuckGo
    * Search for...
    * Open Google
    * Search Google for...
    * Open Bing
    * Search Bing for...
* Open... (apps on system)
* Close... (apps on system)

---
## Unknown Commands
If you say an unknown command, personal assistant will disregard.

---
## Exiting
Personal assistant will exit by recognising one of three words:
* Stop
* Quit
* Exit

---
## License
Personal assistant is released under the Apache License 2.0. See LICENSE for details.
