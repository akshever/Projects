import webbrowser
import subprocess
import os
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
print("INITIALIZING AK47")
speak("INITIALIZING AK47")

speak("Hello sir...Ak47 here...How can I help...type help if you want the commands")
enter = (input("hello sir\nAk47here.\nHow can I help\n type help if you want the commands\n"))
if enter == ("help"):
     print("the commands are-\n google\ncmd\ncalculator\nyoutube\ngmail\ncalender\nfacebook\nmusic\ntime\nkrunker.io\nroblox\n\ninstagram\nnews\ndictionary\ntwitter\nwhatsapp\nprimevideo\namazon\nnetflix\namazon\nflipkart\npottermore\nsourcecode")
     speak("the commands are-...google...cmd...calculator...youtube...gmail...calender...facebook...music...time...krunker.io...roblox...instagram...news...dictionary...twitter...whatsapp...primevideo...amazon...netflix...namazon...flipkart...pottermore...sourcecode")

elif enter == ("calculator"):
    webbrowser.open("https://www.google.com/search?q=google+calculator&rlz=1C1CHBF_enIN859IN859&oq=google+cal&aqs=chrome.0.0l3j69i57j0l4.6392j0j7&sourceid=chrome&ie=UTF-8")
elif enter == ("youtube"):
    webbrowser.open("www.youtube.com")
elif enter == ("gmail"):
    webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
elif enter == ("music"):
    webbrowser.open("www.gaana.com")
elif enter == ("calendar"):
    webbrowser.open("https://calendar.google.com/calendar/r?pli")
elif enter == ("facebook"):
    webbrowser.open("https://www.facebook.com")
elif enter == ("time"):
    webbrowser.open("https://www.google.com/search?q=ist+time&rlz=1C1CHBD_enIN903IN903&oq=ist+time&aqs=chrome..69i57j0l7.2164j0j7&sourceid=chrome&ie=UTF-8")
elif enter ==('google'):
    webbrowser.open("https://www.google.com")
elif enter == ("krunker.io"):
    webbrowser.open("https://krunker.io/")
elif enter == ("roblox"):
    webbrowser.open("https://web.roblox.com/home")
elif enter == ("browser"):
    subprocess.call("chrome.exe")   
elif enter == ("wikipedia"):
    webbrowser.open('https://www.wikipedia.org/')
elif enter == ("news"):
    webbrowser.open("https://www.google.com/search?q=Latest+news&rlz=1C1CHBF_enIN859IN859&sxsrf=ALeKk00ksbvj3xvlGjWDs40uOnU5phlLFQ:1599112022184&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjb7abApMzrAhXaT30KHYVsBKEQ_AUoAXoECA0QAw&biw=1366&bih=625")
elif enter == ("dictionary"):
    webbrowser.open("https://www.dictionary.com/")
elif enter == ("instagram"):
    webbrowser.open("https://www.instagram.com/")
elif enter == ("twitter"):
    webbrowser.open("https://www.twitter.com/")
elif enter == ("primevideo"):
    webbrowser.open("https://www.primevideo.com")
elif enter == ("netflix"):
    webbrowser.open("https://www.netflix.com")
elif enter == ("amazon"):
    webbrowser.open("https://www.amazon.com")
elif enter == ("flipkart"):
    webbrowser.open("https://www.flipkart.com")
elif enter == ("whatsapp"):
    webbrowser.open("https://web.whatsapp.com")
elif enter == ("sourcecode"):
    webbrowser.open("https://github.com/Ak-kid-Coder/Projects")
elif enter == ("pottermore"):
    webbrowser.open("https://wizardingworld.com")
else:
    print("Sorry Cannot do that sir...")
    speak('Sorry Cannot do that sir...')
    speak("MAYBE I WILL IMPROVE ONE DAY")

    


     

    


     
