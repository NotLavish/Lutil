import os
import datetime
import platform

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
        numCheckResult = True
        return numCheckResult
    except ValueError:
        numCheckResult = False
        return numCheckResult

def strCheck(target):
    if target.isalpha():
        strCheckResult = True
        return strCheckResult
    else:
        strCheckResult = False
        return strCheckResult

def fileLog(name, date, data):
    now = datetime.datetime.now()
    timeCheck = now.strftime("%Y-%m-%d %H:%M" + ':')
    f = open(name + '.txt', 'a')
    if date == True:
        f.write(timeCheck + data)
    elif data == False:
        f.write(data)