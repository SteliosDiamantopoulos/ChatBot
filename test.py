import pyttsx3 #pip install pyttsx3
import datetime #pip install datetime
import speech_recognition as sr # pip isntall speek recognition
import wikipedia#pip install wikipedia
import smtplib#pip install smtlib
import webbrowser as wb#pip install webbrowser
import os#pip install os
import pyautogui#pip install ptautogui
import psutil#pip install psutil
import pyjokes#pip install jokes
import playsound
from playsound import playsound
from pyttsx3 import voice
import requests#WR
from pprint import pprint#WR
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 178)#200 words per min

def speak(audio):#This is a function for the Ai to speak use pyttsx3 library

    engine.say(audio)
    engine.runAndWait()
def time(): # This is a Function that gives the Time use datetime library
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak ("The Current Time is")
    speak(Time)
def date(): #This is a Function that gives the Date use datetime library
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("the current date is ")
    speak(day)
    
    if month == 1 :
        speak ("January")
    elif month == 2 :
        speak ("February")
    elif month == 3 :
        speak ("March")
    elif month == 4 :
        speak ("April")
    elif month == 5 :
        speak ("May")
    elif month == 6 :
        speak ("June")
    elif month == 7 :
        speak ("July")
    elif month == 8 :
        speak ("August")
    elif month == 9 :
        speak ("September")
    elif month == 10 :
        speak ("Ocrober")
    elif month == 12 :
        speak ("November")
    elif month == 12 :
        speak ("December")
    
    speak(year)
def wishme(): #Greeting
    
    hour = datetime.datetime.now().hour#hour check for am pm
    if hour>=6 and hour<12:
        speak("Good morning Sir ")
    elif hour>=12 and hour<=18:
        speak("Good afternoon Sir ")  
    elif hour >=18 and hour <24:
        speak ("Good evening Sir ")
    else :
        speak ("GoodNight Sir ")
      
    speak("I am Mike , How can i help you ?")
def cpu():#we use the cpu data
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
def battery():#we use battery data
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
def takeCommand(): #Listen 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')#what ever recognized
        print(query)
    except Exception as e:
        print(e)
        speak("I dont understand PLZ repeat")
        return"None"
    return query
def screenshot(): #screenshot
    img = pyautogui.screenshot()
    img.save("C:\\Users\\User\\Desktop\\Jarvis\\ss.png")
def sendEmail(to, content):#email sent function
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('stdiamant951test@gmail.com','stelios1234!')
    server.sendmail('stdiamant951@gmail.com',to,content)
    server.close()
def jokes():
    speak(pyjokes.get_joke())
def weather_data(city_place):#wr
 res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+city_place+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
 return res.json();
def speak_weather(result,city):#wr
	speak("{}'s temperature: {}°C ".format(city,result['main']['temp']))
	speak("Wind speed: {} meter's per second".format(result['wind']['speed']))
	speak("Description: {}".format(result['weather'][0]['description']))
	speak("Weather: {}".format(result['weather'][0]['main']))
def weather_report():
 speak("What city are you interested in ?")
 city=takeCommand().lower()
 print()
 try:
  city_place='q='+city;
  w_data=weather_data(city_place);
  speak_weather(w_data, city)
  
 except:
	  print('City name not found...')

if __name__ == "__main__":
    playsound("C:\\Users\\User\\Desktop\\Jarvis\\activ (mp3cut.net) (1).mp3")
    query = takeCommand().lower()

    if 'mike' in query:
        wishme()
        while True:
         query = takeCommand().lower()
         if 'time' in query:
            time()
            speak ("can i do anything else")
         elif 'date' in query:
            date()
            speak ("can i do anything else")
            
         elif 'wikipedia' in query:
            speak("Serching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
            speak ("can i do anything else")
            
         elif 'mail' in query:
            try:
                speak("What is the text?")
                content = takeCommand()
                to = 'stdiamant951@gmail.com'
                sendEmail(to,content)
                speak("Email has benn sent")
            except Exception as e:
                print(e)
                speak("Unable to send the email")

         elif 'google search' in query:##Search only websites(Facebook,Youtube,Insta)
            speak("What should i search?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')
            speak ("can i do anything else")
        

         elif 'logout' in query:#checked maybe
            os.system("shutdown -1")  

         elif 'shutdown' in query:
            os.system("shutdown /s /t 1") 

         elif 'restart' in query:#checked
            os.system("shutdown /r /t 1") 
        
    
         elif 'music' in query :
            songs_dir = 'C:\\Users\\User\\Music\\playlist'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))

         elif 'remember that' in query : #remember
            speak("what should I me to remember?")
            data = takeCommand()
            speak("you said me to remember" + data)
            remember = open('metadata.txt','w')
            remember.write(data)
            remember.close()

         elif 'do you know anything' in query :
            remember = open('metadata.txt', 'r')
            speak ("you said me to remember"+remember.read())

         elif 'screenshot' in query:
            screenshot()
            speak ("screenshot captured")
       
         elif 'cpu' in query :
            cpu()
            speak("Anything else Sir?")
       
         elif 'battery' in query :
            battery()
            speak("Anything else Sir?")
        
         elif 'jokes' in query :
            jokes()
        
         elif 'weather' in query:
            weather_report()
 
         elif 'done' in query:
            speak("See u soon Sir")
            playsound("C:\\Users\\User\\Desktop\\Jarvis\\activ (mp3cut.net) (1).mp3")
            quit()
     
         