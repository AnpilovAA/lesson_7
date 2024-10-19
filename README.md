# Home work №7: Timer telegram bot


In this project i made timer telegram bot. I use [[python-telegram-bot](https://python-telegram-bot.org/)] 13.2 version.

![ptb](https://raw.githubusercontent.com/python-telegram-bot/logos/master/logo-text/png/ptb-logo-text_768.png)


![Card](https://dvmn.org/media/lessons/ezgif-6-b2535beb1cbc_cQWIE2e.gif)

## Installation guide

### First step clone this project
- git clone https://github.com/AnpilovAA/lesson_7

### Second step install virtual environment

For Windows
- py -m venv env 

For Unix or MacOS
- python3 -m venv env

### Third step activate virtual environment

For Windows
- path\to\env\Scripts\activate

For Unix or MacOS
- source path/to/env/bin/activate

### Fourth step install dependencies

For Windows
- py -m pip install -r requirement.txt

For Unix/Linux you have to install pip
- https://pip.pypa.io/en/stable/installation/#
- python -m pip install -r requirements.txt

### Fifth step dependency file
- create a config.py file
- create in to config.py 2 globals variable

- `TG_TOKEN = "Your Token"`
- `TG_CHAT_ID = "ID"`
### sixth step launch the program

For Windows
- py main.py

For Unix or MacOS
- python3 main.py