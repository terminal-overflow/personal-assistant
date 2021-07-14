#setup virtualenv
import os
import sys
from tools import *

#check if virtualenv is running
if hasattr(sys, 'real_prefix'):
    fail('Please exit virtualenv!')

virtualenv_exists = os.path.isdir('env')

#replace virtualenv
if virtualenv_exists:
    seperator('Recreating virtualenv')
    shell('rm -rf env').check_fail()
    virtualenv_exists = False
else:
    seperator('Creating virtualenv')

#create virtualenv
if not virtualenv_exists:
    shell('virtualenv env').check_fail()