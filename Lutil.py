import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def copy(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)
    
def pause():
    os.system('pause')

def lengthChecker(target, limit):
    if len(target) != limit:
        if len(target) >= limit:
            lengthResult = "long"
            return lengthResult
        elif len(target) <= limit:
            lengthResult = "short"
            return lengthResult
    elif len(target) == limit:
        lengthResult = "pass"
        return lengthResult

def numCheck(target):
    try:
        int(target)
        numCheckResult = 'pass'
        return numCheckResult
    except ValueError:
        numCheckResult = 'fail'
        return numCheckResult

def strCheck(target):
    if target.isalpha():
        strCheckResult = 'pass'
        return strCheckResult
    else:
        strCheckResult = 'fail'
        return strCheckResult

def fileLog(name, date, data):
    timeCheck = now.strftime("%Y-%m-%d %H:%M" + ':')
    f = open(name + '.txt', 'a')
    if date == 'true':
        f.write(timeCheck + data)
    elif data == 'false':
        f.write(data)