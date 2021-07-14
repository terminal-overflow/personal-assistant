#create helper classes and functions
import time
import sys
import subprocess
from threading import Thread

#seperator title line
def seperator(title):
    print(f'\n{title:-^50}')

#loading text
loading = False
def loading_start():
    global loading
    loading = True

    def load_start():
        sys.stdout.write('loading...')

        while loading:
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(1)

    temp = Thread(target= load_start)
    temp.start()

def loading_stop():
    global loading
    loading = False

#get user input
def user_input(inpt):
    for x, item in enumerate(inpt):
        print(f'{x+1}) {item[0]}')

    while True:
        number = input(f'Select number {1}-{len(inpt)}: ')
        try:
            number = int(number) - 1
        except ValueError:
            continue

        if number >= 0 and number < len(inpt):
            return inpt[number][1]
        else:
            continue

#fail
def fail(msg= ''):
    print('')
    print('Installation failed!')
    sys.exit(1)

#execute shell command
def shell(cmd):
    class Fail:
        def check_fail(self):
            fail()

        def __str__(self):
            return(f'An error occured: {self.exception}.')

    class Success:
        def check_fail(self):
            pass

        def __str__(self):
            return 'No error occured.'

    exit_code = Success()

    loading_start()
    try:
        result = subprocess.check_output(cmd, shell=True, universal_newlines= True, stderr= subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        exit_code = Fail()
        exit_code.exception = str(e)

    loading_stop()
    time.sleep(0.5)
    sys.stdout.write('\n')

    return exit_code