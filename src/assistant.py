import speech_recognition as sr
import wikipedia
import pyttsx3
import datetime
import os
import random
import subprocess
import argparse

#get initial startup arguments
ap = argparse.ArgumentParser()
ap.add_argument('-m', '--mode', default= 'voice',
help= 'type \'text\' to initialise in text mode')
ap.add_argument('-v', '--verbose', default= 'on',
help= 'type \'off\' to turn off the output for words spoken')
args = vars(ap.parse_args())
args['mode'] = args['mode'].lower()
args['verbose'] = args['verbose'].lower()

#check for unknown arguments
if (args['mode'] != 'voice' and args['mode'] != 'text'
or args['verbose'] != 'on' and args['verbose'] != 'off'):
    print('Unknown argument')
    exit()

#startup
def startup(mode):
    response = 'Personal assistant initialised'
    if mode == 'text':
        print(response)
    else:
        assistant_response(response)

#listen to audio and return audio as string
def record_audio():
    #record inputted audio
    r = sr.Recognizer() #create a recogniser object

    #open mic and start recording
    with sr.Microphone() as source:
        audio = r.listen(source)

    #recognise speech
    voice = ''
    try:
        voice = r.recognize_google(audio)
        if args['verbose'] == 'on':
            print('You said: ' + voice)
    except sr.UnknownValueError:
        pass
    except sr.requestError as e:
        print('Error Results: ' + e)
    except:
        print('An error occured')
    return voice

#assistant response
def assistant_response(text):
    try:
        #convert text to speech
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice',voices[0].id)
        engine.say(text)
        engine.setProperty('rate',110)
        engine.runAndWait()
        engine.stop()
    except AssertionError:
        pass

#wake word control
def wake_word(text= None, command= None):
    #write wake word
    if command == 'change':
        #one word failsafe
        if ' ' in text:
            return 'invalid wake word'
        file = open('resources/settings/wake_word.txt', 'w')
        file.write(text)
        file.close()
        return 'wake word changed'

    #read wake word
    file = open('resources/settings/wake_word.txt', 'r')
    wake_words = file.read()
    if wake_words == '':
        wake_words = 'Computer'
    wake_words = wake_words.lower()
    file.close()

    #one word failsafe
    if ' ' in wake_words:
        print('Invalid wake word')
        exit()

    #return current wake word
    if command == 'request':
        return wake_words

    text = text.lower()
    #check for wake word
    if text.startswith(wake_words):
        return True
    return False

#current date
def get_date():
    now = datetime.datetime.now()
    dayNum = str(now.day)
    monthNum = str(now.month)
    yearNum = str(now.year)
    weekName = str(datetime.datetime.today().strftime('%A'))
    monthName = str(datetime.datetime.today().strftime('%B'))

    today_date = 'It\'s ' + weekName + ', ' + dayNum + ' ' + monthName
    return today_date

def get_time():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute

    if minute < 10:
        minute = str(minute)
        minute = '0' + minute

    if hour >= 0 and hour < 12:
        ampm = 'AM'
    else:
        ampm = 'PM'

    if hour >= 13:
        hour = hour - 12

    minute = str(minute)
    hour = str(hour)

    full_time = 'It\'s ' + hour + ' ' + minute + ' ' + ampm
    return full_time

def greeting(text):
    greetings_in = ['hi', 'hello', 'hey', 'morning', 'afternoon', 'evening']

    greetings_out = ['hi', 'hello', 'hi there']

    praise = ['your welcome', 'no problem', 'any time']

    local_request = wake_word(command= 'request')
    name = f'my name is {local_request}, I am your personal assistant'

    text_split = text.split()
    for i in range(len(text_split)):
        if text_split[i] in greetings_in:
            #failsafe for only returning for greetings_in
            if len(text_split) == 1:
                return random.choice(greetings_out)

    if 'thank you' == text or 'cheers' == text or 'thanks' == text:
        return random.choice(praise)

    if ('what is your name' == text or 'what\'s your name' == text or
    'who are you' == text):
        return name

    #if no greeting
    return ''

#break word up into letters with pauses
def get_spelling(text):
    word_list = text.split()
    letter_r = ''

    for i in range(len(word_list)):
        if word_list[i].lower() == 'you' and word_list[i+1].lower() == 'spell':
            try:
                word_list[i+3]
            except IndexError:
                try:
                    spell_word = word_list[i+2]
                    for letter in spell_word:
                        letter_r = letter_r + '. ' + letter
                    return f'{spell_word} is spelled {letter_r}'
                except IndexError:
                    return ''
            return ''
        elif 'spell' in word_list[i+1]:
            return ''

def get_functions(text):
    from resources import func_list
    if text == 'partial':
        partial = func_list.get_list('partial')
        return partial
    else:
        full = func_list.get_list('full')
        return full

#system commands
def system(command):
    from resources import sys_commands
    if command == 'system report':
        system_report = sys_commands.system_report()
        return system_report

    if command == 'mute':
        mute = sys_commands.mute()
        return mute

    if command == 'unmute':
        unmute = sys_commands.unmute()
        return unmute

    if command == 'increase volume':
        increase_volume = sys_commands.increase_volume()
        return increase_volume

    if command == 'decrease volume':
        decrease_volume = sys_commands.decrease_volume()
        return decrease_volume

    if command == 'sleep':
        sleep = sys_commands.sleep()
        return sleep

#return a second value for timer
def get_timer(text):
    import time
    minute_num = None
    second_num = None
    hour_num = None

    for i in range(len(text)):
        if text[i] == '-':
            text = text.replace('-', ' ')

    text = text.split()

    if 'one' in text:
        str(text.replace('one', 1))
    elif 'two' in text:
        str(text.replace('two', 2))
    elif 'three' in text:
        str(text.replace('three', 3))
    elif 'four' in text:
        str(text.replace('four', 4))
    elif 'five' in text:
        str(text.replace('five', 5))
    elif 'six' in text:
        str(text.replace('six', 6))
    elif 'seven' in text:
        str(text.replace('seven', 7))
    elif 'eight' in text:
        str(text.replace('eight', 8))
    elif 'nine' in text:
        str(text.replace('nine', 9))

    if 'second' in text or 'seconds':
        for i in range(len(text)):
            if text[i] == 'second' or text[i] == 'seconds':
                second_num = text[i-1]
                second_num = int(second_num)
    if 'minute' in text or 'minutes' in text:
        for i in range(len(text)):
            if text[i] == 'minute' or text[i] == 'minutes':
                minute_num = text[i-1]
                minute_num = int(minute_num)
                minute_num = minute_num * 60
    if 'hour' in text or 'hours' in text:
        for i in range(len(text)):
            if text[i] == 'hour' or text[i] == 'hours':
                hour_num = text[i-1]
                hour_num = int(hour_num)
                hour_num = hour_num * 3600

    if hour_num == None and minute_num == None and second_num == None:
        return ''
    elif hour_num == None and minute_num == None:
        final_num = second_num
    elif hour_num == None and second_num == None:
        final_num = minute_num
    elif minute_num == None and second_num == None:
        final_num = hour_num
    elif second_num == None:
        final_num = hour_num + minute_num
    elif minute_num == None:
        final_num = hour_num + second_num
    elif hour_num == None:
        final_num = minute_num + second_num
    else:
        final_num = hour_num + minute_num + second_num

    final_num = float(final_num)
    return final_num
#sound function for timer thread
def timer_sound():
    audio_file = 'resources/sounds/alarm.wav'
    subprocess.Popen(['afplay', audio_file])

#get wikipedia search words
def get_wiki(text):
    word_list = text.split()

    for i in range(0, len(word_list)):
        if (word_list[i].lower() == 'search' and
        word_list[i+1].lower() == 'wikipedia' and word_list[i+2] == 'for'):
            word_list = word_list[i+3:]
            return word_list

#complete math equations
def get_math(text):
    from resources import maths_results
    maths_results = maths_results.math_results(text)
    return maths_results

#make new iNote
def get_inote(text):
    file = open('resources/notes/notes_content.txt', 'w')
    text = text.capitalize()
    file.write(text)
    file.close()

    subprocess.call(['osascript', 'resources/notes/make_inote.applescript'])

    file = open('resources/notes/notes_content.txt', 'w')
    file.write('')
    file.close()

    return 'note added'

#make new text note
def get_note(text):
    import uuid

    file = open('resources/settings/notes_dir.txt', 'r')
    file_path = file.read()
    file.close()

    file_name = uuid.uuid4().hex
    if file_path == '':
        file = open(f'resources/notes/{file_name}.txt', 'w')
    elif not file_path.startswith('/') or not file_path.endswith('/'):
        if not file_path.startswith('/') and file_path.endswith('/'):
            file = open(f'/{file_path}{file_name}.txt', 'w')
        elif file_path.startswith('/') and not file_path.endswith('/'):
            file = open(f'{file_path}/{file_name}.txt', 'w')
        else:
            file = open(f'/{file_path}/{file_name}.txt', 'w')
    else:
        file = open(f'{file_path}{file_name}.txt', 'w')
    text = text.capitalize()
    file.write(text)
    file.close()

    return 'note added'

#webbroswer commands
def get_site(text, terms= None):
    from resources import site_search
    if text == 'open youtube':
        get_youtube = site_search.get_youtube()
        return get_youtube
    elif text == 'search youtube':
        search_youtube = site_search.search_youtube(terms)
        return search_youtube
    elif text == 'search browser':
        search_browser = site_search.search_browser(terms)
        return search_browser
    elif text == 'open duckduckgo':
        get_duckduckgo = site_search.get_duckduckgo()
        return get_duckduckgo
    elif text == 'search duckduckgo':
        search_duckduckgo = site_search.search_duckduckgo(terms)
        return search_duckduckgo
    elif text == 'open google':
        get_google = site_search.get_google()
        return get_google
    elif text == 'search google':
        search_google = site_search.search_google(terms)
        return search_google
    elif text == 'open bing':
        get_bing = site_search.get_bing()
        return get_bing
    elif text == 'search bing':
        search_bing = site_search.search_bing(terms)
        return search_bing
    else:
        return ''

#search for and open application on system
def open_application(app):
    application_dir = os.listdir('/Applications')
    application_dir1 = os.listdir('/System/Applications')
    application_dir2 = os.listdir('/System/Applications/Utilities')
    for i in range(len(application_dir)):
        application_dir.append(application_dir[i].lower())

    for i in range(len(application_dir1)):
        application_dir.append(application_dir1[i].lower())

    try:
        for i in range(len(application_dir2)):
            application_dir.append(application_dir2[i].lower())
    except:
        pass

    if f'{app}.app' in application_dir and not app.startswith('.'):
        r = f'osascript -e \'tell application "{app}" to activate\''
        result = subprocess.check_output(r, shell= True)
        result = result.decode('UTF-8')

        return 'opening'
    return ''

#search for and close application on system
def close_application(app):
    application_dir = os.listdir('/Applications')
    application_dir1 = os.listdir('/System/Applications')
    application_dir2 = os.listdir('/System/Applications/Utilities')
    for i in range(len(application_dir)):
        application_dir.append(application_dir[i].lower())

    for i in range(len(application_dir1)):
        application_dir.append(application_dir1[i].lower())

    try:
        for i in range(len(application_dir2)):
            application_dir.append(application_dir2[i].lower())
    except:
        pass

    if f'{app}.app' in application_dir and not app.startswith('.'):
        r = f'osascript -e \'tell application "{app}" to quit\''
        result = subprocess.check_output(r, shell= True)
        result = result.decode('UTF-8')

        return 'closing'
    return ''

def main_loop():
    import threading

    #start initial sequence
    if args['mode'] == 'text':
        startup('text')
        voice = False
    else:
        startup('voice')
        voice = True
    timerT = False
    while True:
        #get wake word
        local_request = wake_word(command= 'request')

        if voice == True:
            text = record_audio()
        else:
            text = input(f'{local_request.capitalize()}: ')
            local_request = wake_word(command= 'request')
            text = f'{local_request} {text}'
        text = str(text.lower())
        text_split = text.split()

        response = ''
        if wake_word(text= text) == True:
            #check just for wake word
            if local_request == text:
                audio_file = 'resources/sounds/accept.wav'
                subprocess.call(['afplay', audio_file])
                text = record_audio()
                text = str(text.lower())
                text_split = text.split()
            else:
                text = text.replace(f'{local_request} ', '')

            #check for blank input for text mode
            if text.strip() == '' and voice == False:
                continue

            #beginning of functions
            #check for greetings
            response = greeting(text)

            #check for math questions
            if response == '':
                response = get_math(text)

            #stop personal-assistant
            if ('quit' == text or 'exit' == text or 'stop' == text):
                response = 'goodbye'
                if voice == True:
                    assistant_response(response)
                else:
                    print(response.capitalize())
                exit()

            #function list
            if (('what can you do' == text or 'what are your abilities' == text
            or 'what are your functions' == text) and response == ''):
                response = get_functions('partial')
                if voice == True:
                    assistant_response(response)
                    assistant_response('would you like the full list')
                    text = record_audio()
                else:
                    print(response.capitalize())
                    print('would you like the full list'.capitalize())
                    text = input('Function: ')
                text = str(text.lower())
                if 'yes' in text:
                    full_response = get_functions('full')
                    for i in range(len(full_response)):
                        print(full_response[i])
                    continue
                elif text == '' and voice == True:
                    response = ''
                elif text == '' and voice == False:
                    continue
                else:
                    response = 'okay'

            #check for mode change
            if 'change mode' == text and response == '':
                if voice == True:
                    voice = False
                    response = 'text mode activated'
                else:
                    voice = True
                    response = 'voice mode activated'

            #change wake word
            if 'change wake word' in text and response == '':
                if voice == True:
                    assistant_response('what is your new wake word')
                    text = record_audio()
                else:
                    print('What is your new wake word')
                    text = input('Wake word: ')
                text = str(text.lower())
                response = wake_word(text= text, command= 'change')
            
            #reset wake word
            if 'reset wake word' in text and response == '':
                response = wake_word(text= '', command= 'change')

            #check for date
            if (('what is the date' in text or 'what\'s the date' in text) and
            response == ''):
                response = get_date()

            #check for the time
            if (('what is the time' in text or 'what\'s the time' in text) and
            response == ''):
                response = get_time()

            #check spelling
            if 'how do you spell' in text and response == '':
                if voice == True:
                    response = get_spelling(text)
                else:
                    pass

            #system commands
            #system report
            if (('system report' == text or 'system status' == text)
            and response == ''):
                response = system('system report')

            #unmute
            if ('unmute' == text or 'stop mute' == text) and response == '':
                response = system('unmute')

            #mute
            if 'mute' == text and response == '':
                response = system('mute')

            #change volume
            if 'volume' in text and response == '':
                increase = ['volume up', 'increase volume',
                'increase the volume']
                decrease = ['volume down', 'decrease volume',
                'decrease the volume']

                for i in range(len(increase)):
                    if increase[i] in text:
                        response = system('increase volume')

                for i in range(len(decrease)):
                    if decrease[i] in text:
                        response = system('decrease volume')

            #sleep
            if 'sleep' == text and response == '':
                response = system('sleep')
                exit()

            #set a timer
            if (('set a timer' in text or 'start a timer' in text
            or 'start timer' in text) and response == ''):
                try:
                    if timerT.is_alive():
                        response = 'timer is already set'
                    else:
                        if voice == True:
                            assistant_response('timer for how long')
                            text = record_audio()
                        else:
                            print('Timer for how long')
                            text = input('Timer: ')
                        text = str(text.lower())
                        if text == '':
                            response = ''
                        else:
                            interval = get_timer(text)
                            if type(interval) == float:
                                timerT = threading.Timer(interval= interval,
                                function= timer_sound)
                                timerT.start()
                                response = 'timer set'
                            else:
                                response = ''

                except AttributeError:
                    if voice == True:
                        assistant_response('timer for how long')
                        text = record_audio()
                    else:
                        print('Timer for how long')
                        text = input('Timer: ')
                    text = str(text.lower())
                    if text == '':
                        response = ''
                    else:
                        interval = get_timer(text)
                        if type(interval) == float:
                            timerT = threading.Timer(interval= interval,
                            function= timer_sound)
                            timerT.start()
                            response = 'timer set'
                        else:
                            response = ''

            #stop a timer
            if (('stop the timer' in text or 'cancel the timer' in text
            or 'cancel timer' in text) and response == ''):
                try:
                    if timerT.is_alive():
                        timerT.cancel()
                        response = 'timer stopped'
                    else:
                        response = 'timer is not set'
                except AttributeError:
                    response = 'timer is not set'

            #check wikipedia
            if 'search wikipedia' in text and response == '':
                info = get_wiki(text)
                try:
                    response = wikipedia.summary(info, sentences= 2)
                except ValueError:
                    pass # to little options
                except wikipedia.DisambiguationError:
                    pass # to many options

            #make an iNote
            if 'make a note' in text and response == '':
                if voice == True:
                    assistant_response('what is your note')
                    text = record_audio()
                else:
                    print('What is your note')
                    text = input('Note: ')
                if text == '':
                    response = ''
                else:
                    response = get_inote(text)

            #make a text note
            if 'make a text note' in text and response == '':
                if voice == True:
                    assistant_response('what is your note')
                    text = record_audio()
                else:
                    print('What is your note')
                    text = input('Note: ')
                if text == '':
                    response = ''
                else:
                    response = get_note(text)

            #youtube
            if 'open youtube' in text and response == '':
                response = get_site('open youtube')

            if 'search youtube' in text and response == '':
                for i in range(len(text_split)):
                    if (text_split[i] == 'search' and text_split[i+1] == 'youtube'
                    and text_split[i+2] == 'for'):
                        terms = text_split[i+3:]
                        terms = '+'.join(terms)
                        response = get_site(text= 'search youtube', terms= terms)

            #search engines
            if 'search for' in text and '.' in text and response == '':
                for i in range(len(text_split)):
                    if text_split[i] == 'search' and text_split[i+1] == 'for':
                        terms = text_split[i+2:]
                        terms = '+'.join(terms)
                        response = get_site(text= 'search browser', terms= terms)

            #duckduckgo (default)
            if (('open the internet' in text or 'open duckduckgo' in text)
            and response == ''):
                response = get_site('open duckduckgo')

            if (('search for' in text or 'search the internet for' in text
            or 'search duckduckgo for' in text) and response == ''):
                for i in range(len(text_split)):
                    if text_split[i] == 'search' and text_split[i+1] == 'for':
                        terms = text_split[i+2:]
                        terms = '+'.join(terms)
                        response = get_site(text= 'search duckduckgo', terms= terms)

            #google
            if 'open google' in text and response == '':
                response = get_site('open google')

            if 'search google for' in text and response == '':
                for i in range(len(text_split)):
                    if (text_split[i] == 'search' and text_split[i+1] == 'google'
                    and text_split[i+2] == 'for'):
                        terms = text_split[i+3:]
                        terms = '+'.join(terms)
                        response = get_site(text= 'search google', terms= terms)

            #bing
            if 'open bing' in text and response == '':
                response = get_site('open bing')

            if 'search bing for' in text and response == '':
                for i in range(len(text_split)):
                    if (text_split[i] == 'search' and text_split[i+1] == 'bing'
                    and text_split[i+2] == 'for'):
                        terms = text_split[i+3:]
                        terms = '+'.join(terms)
                        response = get_site(text= 'search bing', terms= terms)

            #open application
            if 'open' in text and response == '':
                for i in range(len(text_split)):
                    if text_split[i] == 'open':
                        app = text_split[i+1:]
                        app = ' '.join(app)
                        response = open_application(app)
            #open news application
            if (('what\'s the' in text and 'news' in text
            or 'what is the' in text and 'news' in text) and response == ''):
                open_application('news')
                response = 'opening news'

            #close application
            if 'close' in text and response == '':
                for i in range(len(text_split)):
                    if text_split[i] == 'close':
                        app = text_split[i+1:]
                        app = ' '.join(app)
                        response = close_application(app)


            #response
            if (response == '' or response == None) and voice == True:
                audio_file = 'resources/sounds/unsure.wav'
                subprocess.call(['afplay', audio_file])
            elif (response == '' or response == None) and voice == False:
                print('I\'m not sure')
            elif voice == False:
                print(response.capitalize())
            else:
                assistant_response(response)

main_loop()
