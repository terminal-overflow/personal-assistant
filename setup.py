from setuptools import setup, find_packages

with open('README.md', 'r') as readme_file:
    ld = readme_file.read()

setup(
    name= 'personal-assistant',
    version= '1.0.0',
    #url= '',
    description= 'A virtual assistant that completes tasks and gives you results from your computer',
    long_description= ld,
    long_description_content_type= 'text/markdown',
    license= 'MIT',
    classifiers= [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License'
    ],
    keywords= 'personal virtual assistant',
    packages= find_packages(),
    py_modules= ['assistant'],
    package_dir= {'': 'src'},
    include_package_data= True,
    install_requires= ['speechrecognition', 'wikipedia', 'pyttsx3', 'pyaudio'],
    python_requires= '>=3.6'
)
