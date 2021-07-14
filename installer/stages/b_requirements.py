#install requirements
from tools import *

seperator('Installing requirements')

shell('env/bin/pip3 install -r installer/requirements.txt').check_fail()