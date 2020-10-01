import pyttsx3
import os

def speak(text):
      engine.say(text)
      engine.runAndWait()

engine= pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)
engine.setProperty('rate' , 150)



print("\t\t\t\t *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* \t\t\t\t")
print("\t\t\t\t *  Welcome to Command Line Assistant  * \t\t\t\t")
print("\t\t\t\t *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* \t\t\t\t")
pyttsx3.speak("Weclome to Command Line Assistant")

while True:
    print("------------------------------------------------------------------------------------------------------------------------")
    print("\t\t What can I do for you : "  , end='')
    p = input()
    

    if ("run" in p)  and ("chrome" in p):
        pyttsx3.speak("opening chrome")
        os.system("chrome")
        

    elif (("run" in p) or  ("execute" in p )) and  (("notepad" in p) or ("editor" in p)) :
        pyttsx3.speak("opening notepad")
        os.system("notepad")
        
    elif ("run" in p)  and ("player" in p) and ("media" in p):
        pyttsx3.speak("opening music player")
        os.system("wmplayer")
        
    elif ("run" in p)  and ("vlc" in p):
        pyttsx3.speak("opening vlc media player")
        os.system("vlc")
        
    elif ("run" in p)  and  ("gitbash" in p) :
        pyttsx3.speak("opening git bash")
        os.system("git-bash")

    elif ("run" in p)  and ("virtualbox" in p) :
        pyttsx3.speak("opening virtualbox")
        os.system("virtualbox")

    elif ("run" in p) and ("teamviewer" in p) :
        pyttsx3.speak("opening team viewer")
        os.system("teamviewer")

    elif ("run" in p)  and ("whatsapp" in p) :
        pyttsx3.speak("opening whatsapp")
        os.system("whatsapp")

    elif ("run" in p)  and  ("c" in p) and ("compiler" in p) :
        pyttsx3.speak("opening compiler")
        os.system("devcpp")

    elif ("run" in p)  and ("pdfreader" in p) :
        pyttsx3.speak("opening pdf reader")
        os.system("AcroRd32")

    elif ("run" in p) and ("cisco" in p) and ("packet" in p) and ("tracer" in p) :
        pyttsx3.speak("opening cisco packet tracer")
        os.system("packettracer5")

    elif ("run" in p)  and ("internet" in p) and ("explorer" in p) :
        pyttsx3.speak("opening internet explorer")
        os.system("msedge")

    elif ("shutdown" in p)  and  ("system" in p) :
        pyttsx3.speak("System is about to shutdown") 
        os.system("shutdown/s")

    elif ("system" in p)  and ("information" in p) :
        pyttsx3.speak("getting the system information")
        os.system("systeminfo")

    elif ("run" in p) and ("file" in p) and ("explorer" in p) :
        pyttsx3.speak("opening file explorer")
        os.system("explorer")

    elif ("run" in p)  and ("calculator" in p):
        pyttsx3.speak("opening calculator")
        os.system("calc")

    elif ("run" in p)  and ("paint" in p):
        pyttsx3.speak("opening paint editor")
        os.system("mspaint")

    elif ("run" in p)  and ("magnifier" in p):
        pyttsx3.speak("opening magifier")
        os.system("magnify")

    elif ("run" in p)  and ("wordpad" in p) :
        pyttsx3.speak("opening wordpad") 
        os.system("write")
   
    elif ("open" in p) and ("google" in p) and ("drive" in p) :
        pyttsx3.speak("opening google drive")
        os.system("chrome drive.google.com")

    elif ("open" in p)  and ("linkedin" in p) :
        pyttsx3.speak("opening linkedin.com")
        os.system("chrome linkedin.com")

    elif ("open" in p)  and ("youtube" in p) :
        pyttsx3.speak("opening youtube.com")
        os.system("chrome youtube.com")

    elif ("open" in p)  and ("github" in p) :
        pyttsx3.speak("opening github.com")
        os.system("chrome github.com")

    elif ("open" in p)  and ("facebook" in p) :
        pyttsx3.speak("opening facebook.com")
        os.system("chrome facebook.com")

    elif ("open" in p)  and ("compose" in p) and ("mail" in p) :
        pyttsx3.speak("opening email")
        os.system("chrome https://mail.google.com/mail/u/0/#inbox?compose=new")


    elif ("run" in p)  and ("zoom" in p) :
        pyttsx3.speak("opening zoom")
        os.system("zoom")

    elif ("clear" in p)  and ("screen" in p) :
        pyttsx3.speak("screen cleared")
        os.system("cls")

    elif ("close" in p)  and ("command" in p) and ("prompt" in p) :
        pyttsx3.speak("exiting command terminal")
        os.system("exit")

    elif  ("exit" in p)  or ("quit" in p):
        
        print("\t\t Have A Good Day")
        print("\t\t ~~~~~~~~~~~~~~~")
        pyttsx3.speak("Have a Good Day")
        break

    else:
        print("\t\t Couldn't find what you are looking for. Try Again!")
        pyttsx3("Couldn't find what you are looking for. Try Again!")

