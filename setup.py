from setuptools import setup#, find_packages

with open('README.md', 'r') as readme_file:
    ld = readme_file.read()

setup(
    name= 'personal-assistant',
    version= '2.5',
    url= 'https://github.com/terminal-flow/personal-assistant',
    description= 'A virtual assistant that helps you with certain tasks or gets information for you.',
    long_description= ld,
    long_description_content_type= 'text/markdown',
    license= 'MIT',
    keywords= 'personal virtual assistant',
    install_requires= ['speechrecognition', 'wikipedia', 'pyttsx3', 'pyaudio'],
    python_requires= '>=3.6'
)
