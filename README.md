# Python Personal Assistant
## Personal Assistant Information
---
This personal assistant uses speechrecognition to convert STT and uses pyttsx3 for TTS. The purpose of this program is to help you with certain tasks on your computer or just to get information for you.

### Note
This program is only available for OS X computers at this moment in time.

### Dependencies
* speechrecognition
* pyaudio (install port audio if any problems)
* pyttsx3
* wikipedia

---
## Installation and Usage via GitHub
#### Setting up a virtual environment (optional)
```
virtualenv <environment name>
source <environment name>/bin/activate
```

### Clone the repository (Developers)
```
 git clone ...
```

### Or Download (Non-Developer)
* Click the download button
* Unzip the project file

### Go to the project root
```
cd personal-assistant
```

### Install
```
pip3 install .
```
#### Note
This may take around a minute

### Run

```
cd src 
python3 assistant.py
```
or
```
cd src
python3 assistant.py -h
```
for more information on optional arguments.

---
## Startup arguments
The optional startup arguments are mode and verbose.
* mode `-m text` for startup text mode - default is voice mode
* verbose `-v off` for no verbose - default is on

## Startup with Voice Mode
Personal assistant will say initialising... and then begin to listen indefinitely.
If the verbose argument is on, the speech it detects will be displayed in your terminal/IDE.
Otherwise no text will be outputted, except for errors.

## Startup with Text Mode
Personal assistant will output initialising... and then wait for your command to be entered indefinitely.

### Wake word
The default wake word is 'computer' and can be changed to any word.

---
## Voice Mode
If just the wake word is heard, personal assistant will play a welcoming tone and wait for your command for around 5 seconds. If no sound is heard, personal-assistant will disregard.

## Text Mode
All the inputs will need to be typed in your terminal/IDE, however, the wake word does not need to be typed. All the outputs, except for the timer, will all be outputted as text.

---
## Functions

The functions for this program are:
* Greetings (you can say)
    * hello, hi, hey etc
    * thank you, thanks, cheers
    * what is your name
* Change mode
* Get current time
* Get current Date
* Get spelling of word
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
## Unkown Commands
If you say an unknown command, personal assistant will play a disregard tone.

---
## Exiting
Personal assistant will exit by hearing one of three words (as well as the wake word):
* Stop
* Quit
* Exit

---
## License
Personal assistant is released under the MIT license. See LICENSE for details.
