import os
import subprocess

def system_report():
    #getting over sysload
    r = 'pmset -g sysload'
    result = subprocess.check_output(r, shell= True)
    result = result.decode('UTF-8')
    __, result, __, __, __, __ = result.split('\n')

    for i in range(len(result)):
        if result[i] == '=':
            result = result[i+1:]
            result = result.strip()
            break

    #getting battery percentage
    r = 'pmset -g ps'
    battery_p = subprocess.check_output(r, shell= True)
    battery_p = battery_p.decode('UTF-8')

    for i in range(len(battery_p)):
        if battery_p[i] == '%':
            battery_p = battery_p[i-3:i]
            battery_p = battery_p.strip()
            break

    #getting battery status
    r = 'pmset -g ps'
    battery_s = subprocess.check_output(r, shell= True)
    battery_s = battery_s.decode('UTF-8')

    for i in range(len(battery_s)):
        if battery_s[i] == ';':
            battery_s = battery_s[i+1:]
            break

    for i in range(len(battery_s)):
        if battery_s[i] == ';':
            battery_s = battery_s.strip()
            battery_s = battery_s[:i-1]
            break

    report = f'all systems are {result}. battery percentage is {battery_p}%. the battery is currently {battery_s}'
    return report

def increase_volume():
    r = 'osascript -e \'get volume settings\''
    result = subprocess.check_output(r, shell=True)
    result = str(result)
    result, __, __, __ = result.split(', ')
    result = result[16:]
    result = int(result)
    if result <= 80:
        result = result +20
        os.system(f'osascript -e \'set volume OUTPUT volume {result}\'')
    else:
        os.system('osascript -e \'set volume OUTPUT volume 100\'')
    return 'okay'

def decrease_volume():
    r = 'osascript -e \'get volume settings\''
    result = subprocess.check_output(r, shell=True)
    result = str(result)
    result, __, __, __ = result.split(', ')
    result = result[16:]
    result = int(result)
    if result >= 20:
        result = result -20
        os.system(f'osascript -e \'set volume OUTPUT volume {result}\'')
        return 'okay'
    else:
        mute()

def mute():
    os.system('''
        osascript -e 'set volume output muted TRUE'
        ''')
    return 'muted'

def unmute():
    os.system('''
        osascript -e 'set volume output muted FALSE'
        ''')
    return 'unmuted'

def sleep():
    os.system('''
        pmset sleepnow
        ''')