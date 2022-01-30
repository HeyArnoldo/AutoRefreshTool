from turtle import st
from unittest import result
import time
import keyboard
import datetime

def ScriptTitle():
    print("""
    
                _        _____       __               _     
     /\        | |      |  __ \     / _|             | |    
    /  \  _   _| |_ ___ | |__) |___| |_ _ __ ___  ___| |__  
   / /\ \| | | | __/ _ \|  _  // _ \  _| '__/ _ \/ __| '_ \ 
  / ____ \ |_| | || (_) | | \ \  __/ | | | |  __/\__ \ | | |
 /_/____\_\__,_|\__\___/|_|_ \_\___|_| |_|  \___||___/_| |_|
  / ____|         (_)     | |                               
 | (___   ___ _ __ _ _ __ | |_                              
  \___ \ / __| '__| | '_ \| __|                             
  ____) | (__| |  | | |_) | |_                              
 |_____/ \___|_|  |_| .__/ \__|    by: Joao Souza                    
                    | |                                     
                    |_|                                     

    """)

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    keyboard.press("shift+f5")
    print("Script ejecutado con éxito!")


def bot():
    ScriptTitle()
    hour = input("Hora: ")
    minute = input("Minutos: ")
    segundos = input("Segundos: ")

    startTime = datetime.datetime.now()
    timenow = startTime.strftime('%Y-%m-%d %H:%M:%S')

    deadline = "{}-{}-{} {}:{}:{}".format(startTime.year,startTime.month,startTime.day,hour,minute,segundos)

    start = datetime.datetime.strptime(timenow,'%Y-%m-%d %H:%M:%S')
    ends = datetime.datetime.strptime(deadline, '%Y-%m-%d %H:%M:%S')

    result = ends - start
    print("Se ejecutará el script en {} seg | {} Min | {}".format(result.seconds,result,ends))

    countdown(result.seconds)

    time.sleep(120)

bot()
