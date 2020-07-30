import webbrowser

def get_youtube():
    url = 'https://www.youtube.com'
    webbrowser.open_new(url= url)
    return 'opening youtube'

def search_youtube(terms):
    url = f'https://www.youtube.com/results?search_query={terms}'
    webbrowser.open_new(url= url)
    return 'searching youtube'

def search_browser(terms):
    url = f'https://www.{terms}'
    webbrowser.open_new(url= url)
    return 'searching'

def get_duckduckgo():
    url = 'https://www.duckduckgo.com'
    webbrowser.open_new(url= url)
    return 'opening search engine'

def search_duckduckgo(terms):
    url = f'https://duckduckgo.com/?q={terms}'
    webbrowser.open_new(url= url)
    return 'searching'

def get_google():
    url = 'https://www.google.com'
    webbrowser.open_new(url= url)
    return 'opening search engine'

def search_google(terms):
    url = f'https://www.google.com/search?q={terms}'
    webbrowser.open_new(url= url)
    return 'searching'

def get_bing():
    url = 'https://www.bing.com'
    webbrowser.open_new(url= url)
    return 'opening search engine'

def search_bing(terms):
    url = f'https://www.bing.com/search?q={terms}'
    webbrowser.open_new(url= url)
    return 'searching'