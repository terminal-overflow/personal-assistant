from setuptools import setup#, find_packages

with open('README.md', 'r') as readme_file:
    ld = readme_file.read()

setup(
    name= 'personal-assistant',
    version= '2.4.6',
    url= 'https://github.com/terminal-flow/personal-assistant',
    description= 'A virtual assistant that helps you with certain tasks or gets information for you.',
    long_description= ld,
    long_description_content_type= 'text/markdown',
    license= 'MIT',
    #classifiers= [
    #    'Development Status :: 5 - Production/Stable',
    #    'Intended Audience :: Developers',
    #    'License :: OSI Approved :: MIT License'
    #],
    keywords= 'personal virtual assistant',
    #packages= find_packages(),
    #py_modules= ['assistant'],
    package_dir= {'': 'src'},
    include_package_data= True,
    install_requires= ['speechrecognition', 'wikipedia', 'pyttsx3', 'pyaudio'],
    python_requires= '>=3.6'
)
