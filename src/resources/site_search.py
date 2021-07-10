import webbrowser

def get_youtube():
    url = 'https://youtube.com'
    webbrowser.open_new(url= url)
    return 'opening youtube'

def search_youtube(terms):
    url = f'https://youtube.com/results?search_query={terms}'
    webbrowser.open_new(url= url)
    return 'searching youtube'

def search_browser(terms):
    url = f'https://{terms}'
    webbrowser.open_new(url= url)
    return 'searching'

def get_duckduckgo():
    url = 'https://duckduckgo.com'
    webbrowser.open_new(url= url)
    return 'opening search engine'

def search_duckduckgo(terms):
    url = f'https://duckduckgo.com/?q={terms}'
    webbrowser.open_new(url= url)
    return 'searching'

def get_google():
    url = 'https://google.com'
    webbrowser.open_new(url= url)
    return 'opening search engine'

def search_google(terms):
    url = f'https://google.com/search?q={terms}'
    webbrowser.open_new(url= url)
    return 'searching'

def get_bing():
    url = 'https://bing.com'
    webbrowser.open_new(url= url)
    return 'opening search engine'

def search_bing(terms):
    url = f'https://bing.com/search?q={terms}'
    webbrowser.open_new(url= url)
    return 'searching'