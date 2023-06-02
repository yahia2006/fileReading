print(""" 
 _____ _ _        ____           _ _
|  ___(_) | ___  |  _ \ __ _  __| (_)_ __   __ _
| |_  | | |/ _ \ | |_) / _` |/ _` | | '_ \ / _` |
|  _| | | |  __/ |  _ < (_| | (_| | | | | | (_| |
|_|   |_|_|\___| |_| \_\__,_|\__,_|_|_| |_|\__, |
                                           |___/




""")
import pyttsx3
inpfile=input('filename==>')
with open(inpfile,'r')as file:
    filecon=file.readlines()
    numlines=len(filecon)
    for i in range(0,numlines):
        text=filecon[i]
        en=pyttsx3.init()
        voices = en.getProperty('voices')
        en.setProperty('voice', voices[1].id)
        en.say(text)
        print(text)
        en.runAndWait()
        import time
        time.sleep(0.5)

    


