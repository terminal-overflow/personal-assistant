#import all stages and catch errors
import sys

#exit if platform is not MacOS
import platform
if platform.system() != 'Darwin':
    print('System is not MacOS!')
    sys.exit(1)

#exit if python3 is not installed
if sys.version_info.major != 3:
    print('No python3 installation was found!')

try:
    import os
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    import stages.a_virtualenv
    import stages.b_requirements
    import stages.c_execute
except SystemExit:
    pass
except BaseException as e:
    print('\nAn error occured.')
    print('Here is the error:')
    print(e)