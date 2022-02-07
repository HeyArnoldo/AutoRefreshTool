import imp
from lib2to3.pgen2 import driver
from telnetlib import EC
from selenium import webdriver
import datetime
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
from os import system, name

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
  

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
try:
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    driver_path = "chromedriver.exe"
    driver = webdriver.Chrome(driver_path, chrome_options= options)
    linkArchive = open("link.txt").read()
    driver.get(linkArchive)
    for i in range(3):
        time.sleep(1)
        clear()
except:
  print("Ha ocurrido un error!")

def countdown(t):
    global driver
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    driver.refresh()
    print("""
    Script ejecutado con éxito!

    NOTA: Si cierras esta consola se cerrará el navegador!
    """)

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

    time.sleep(1200000)

bot()