#create executable file and provide options
import os
from tools import *

seperator('Creating executable file')

file_text = '''
#!/bin/bash
source "{PATH}/env/bin/activate"
python3 "{PATH}/src/assistant.py" "$@"
'''

#create text file
file_ex = open('assistant', 'w')
file_ex.write(file_text.format(PATH= os.getcwd()))
file_ex.close()

#convert to executable
shell('chmod +x assistant').check_fail()

install_options = [('Install personal assistant in /usr/local/bin (requires root)', 0),
                    (f'Add {os.getcwd()} to $PATH (.bashrc)', 1),
                    (f'Add {os.getcwd()} to $PATH (.zshrc)', 2),
                    ('Do nothing (Call personal assistant by full path)', 3)]

option = user_input(install_options)

#copy executable to /usr/local/bin
if option == 0:
    os.system('sudo cp assistant /usr/local/bin')
#add to PATH in .bashrc or .zshrc
elif option == 1 or option == 2:
    path_insert = f'export PATH="$PATH:{os.getcwd()}"'

    #add to PATH in .bashrc
    if option == 1:
        bashrc = f'{os.path.expanduser("~")}/.bashrc'

        if not os.path.exists(bashrc):
            print('No .bashrc file found!')
            shell(f'touch {bashrc}').check_fail()
            print('.bashrc file created.')

        file_bash = open(bashrc, 'r')
        line_exists = False

        for line in file_bash.readlines():
            if line.startswith(path_insert):
                line_exists = True
                print('assistant has already been added to the $PATH in .bashrc!')
        file_bash.close()

        if not line_exists:
            file_bash = open(bashrc, 'a')
            file_bash.write(path_insert)
            file_bash.write('\n')
            file_bash.close()

    #add to PATH in .zshrc
    if option == 2:
        zshrc = f'{os.path.expanduser("~")}/.zshrc'

        if not os.path.exists(zshrc):
            print('No .zshrc file found!')
            shell(f'touch {zshrc}').check_fail()
            print('.zshrc file created.')

        file_zsh = open(zshrc, 'r')
        line_exists = False

        for line in file_zsh.readlines():
            if line.startswith(path_insert):
                line_exists = True
                print('assistant has already been added to the $PATH in .zshrc!')
        file_zsh.close()

        if not line_exists:
            file_zsh = open(zshrc, 'a')
            file_zsh.write(path_insert)
            file_zsh.write('\n')
            file_zsh.close()

print('\nInstallation complete! Use personal assistant at anytime with the command:')
if option == 1 or option == 2:
    print(f'{"$" if option == 1 else "%"} "assistant"')
elif option == 0:
    print('"assistant"')
else:
    print(f'{os.getcwd()}/assistant')