import subprocess 
import wolframalpha 
import pyttsx3 
import tkinter 
import pywhatkit
import json 
import random 
import operator 
import speech_recognition as sr 
import datetime 
import wikipedia 
import webbrowser 
import sys
import os 
import winshell 
import pyjokes 
import feedparser 
import smtplib 
import ctypes 
import time 
import requests 
import shutil 
# import cv2
from requests import get
from twilio.rest import Client 
from clint.textui import progress 
#from ecapture import ecapture as ec 
from bs4 import BeautifulSoup 
import win32com.client as wincl 
from urllib.request import urlopen 
# Now we will set our engine to Pyttsx3 which is used for text to speech in Python and sapi5 is Microsoft speech application platform interface we will be using this for text to speech function.

# filter_none
# brightness_4
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id) 
# You can change voice Id to “0” for Male voice while using assistant here we are using Female voice for all text to speech

# filter_none
# brightness_4
def speak(audio): 
    engine.say(audio) 
    engine.runAndWait() 
  
def wishMe(): 
    hour = int(datetime.datetime.now().hour) 
    if hour>= 0 and hour<12: 
        speak("Good Morning Sir !") 
   
    elif hour>= 12 and hour<18: 
        speak("Good Afternoon Sir !")    
   
    else: 
        speak("Good Evening Sir !")   
   
    assname =("Jarvis 1 point o") 
    speak("I am your Assistant") 
    speak(assname) 
      
  
def username(): 
    speak("What should i call you sir") 
    uname = takeCommand() 
    speak("Welcome Mister") 
    speak(uname) 
    columns = shutil.get_terminal_size().columns 
      
    print("#####################".center(columns)) 
    print("Welcome Mr.", uname.center(columns)) 
    print("#####################".center(columns)) 
      
    speak("How can i Help you, Sir") 
  
def takeCommand(): 
      
    r = sr.Recognizer() 
      
    with sr.Microphone() as source: 
          
        print("Listening...") 
        r.pause_threshold = 1
        audio = r.listen(source) 
   
    try: 
        print("Recognizing...")     
        query = r.recognize_google(audio, language ='en-in') 
        print(f"User said: {query}\n") 
   
    except Exception as e: 
        print(e)     
        print("Unable to Recognizing your voice.")   
        return "None"
      
    return query 
   
def sendEmail(to, content): 
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo() 
    server.starttls() 
      
    # Enable low security in gmail 
    server.login('your email id', 'your email passowrd') 
    server.sendmail('your email id', to, content) 
    server.close() 
# Main Function starts here, we will now call all these function in main function.

if __name__ == '__main__': 
    clear = lambda: os.system('cls') 
      
    # This Function will clean any 
    # command before execution of this python file 
    clear() 
    wishMe() 
    username() 
      
    while True: 
          
        query = takeCommand().lower() 
          
        # All the commands said by user will be  
        # stored here in 'query' and will be 
        # converted to lower case for easily  
        # recognition of command 
        if 'wikipedia' in query: 
            speak('Searching Wikipedia...') 
            query = query.replace("wikipedia", "") 
            results = wikipedia.summary(query, sentences = 3) 
            speak("According to Wikipedia") 
            print(results) 
            speak(results) 
  
        elif 'open youtube' in query: 
            speak("Here you go to Youtube\n") 
            webbrowser.open("youtube.com") 
  
        elif 'open google' in query: 
            speak("sir, what should i search on google") 
            webbrowser.open("google.com") 
  
        elif 'open stack overflow' in query: 
            speak("Here you go to Stack Over flow.Happy coding") 
            webbrowser.open("stackoverflow.com")    
  
        elif 'play music' in query or "play song" in query: 
            speak("Here you go with music") 
            # music_dir = "G:\\Song" 
            music_dir = "F:\sv1"
            songs = os.listdir(music_dir) 
            print(songs)     
            random = os.startfile(os.path.join(music_dir, songs[0])) 
        elif 'best friend' in query:
            speak('you is friend to yourself')

        elif 'where i am' in query or 'where we are' in query:
            speak("wait sir ,let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/geo/'+ipAdd+'.json' 
                geo_requests = requests.get(url)
                geo_data =  geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"sir i am not sure ,but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry sir, due to network issue i am not able to find where we are.")    
                pass
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\ABHISHEK KUMAR\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open notepad' in query: 
            codePath = r"C:\\Windows\\system32\\notepad.exe"
            os.startfile(codePath) 

        elif 'command prompt' in query or 'cmd ' in query: 
           os.system('start cmd')
  
        elif 'email to vivek' in query: 
            try: 
                speak("What should I say?") 
                content = takeCommand().lower() 
                to = "vk3796565@gmail.com"    
                sendEmail(to, content) 
                speak("Email has been sent !") 
            except Exception as e: 
                print(e) 
                speak("I am not able to send this email") 
  
        elif 'send a mail' in query: 
            try: 
                speak("What should I say?") 
                content = takeCommand() 
                speak("whome should i send") 
                to = input()     
                sendEmail(to, content) 
                speak("Email has been sent !") 
            except Exception as e: 
                print(e) 
                speak("I am not able to send this email") 
  
        elif 'how are you' in query: 
            speak("I am fine, Thank you") 
            speak("How are you, Sir") 
  
        elif 'fine' in query or "good" in query: 
            speak("It's good to know that your fine") 
  
        elif "change my name to" in query: 
            query = query.replace("change my name to", "") 
            assname = query 
  
        elif 'change name' in query: 
            speak("What would you like to call me, Sir ") 
            assname = takeCommand() 
            speak("Thanks for naming me") 
  
        elif  'What is your name' in query: 
            speak("My friends call me") 
            speak(assname) 
            print("My friends call me", assname) 
  
        elif 'exit' in query: 
            speak("Thanks for giving me your time") 
            exit() 
  
        elif "who made you" in query or "who created you" in query:  
            speak("I have been created by vivek ") 
              
        elif 'joke' in query: 
            speak(pyjokes.get_joke()) 
        
        elif "calculate" in query:  
              
            app_id = "Wolframalpha api id" 
            client = wolframalpha.Client(app_id) 
            indx = query.lower().split().index('calculate')  
            query = query.split()[indx + 1:]  
            res = client.query(' '.join(query))  
            answer = next(res.results).text 
            print("The answer is " + answer)  
            speak("The answer is " + answer)  
  
        elif 'search' in query or 'play' in query: 
              
            query = query.replace("search", "")  
            query = query.replace("play", "")           
            webbrowser.open(query)  
  
        elif "who i am" in query: 
            speak("If you talk then definately your human.") 
  
        elif "why you came to world" in query: 
            speak("a lot thanks for vivek . further It's a secret") 
  
        elif 'power point presentation' in query: 
            speak("opening Power Point presentation") 
            power = r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office"
            os.startfile(power) 
  
        elif 'is love' in query: 
            speak("It is 7th sense that destroy all other senses")

        elif 'about myself' in query:
            print(" full name vivek kumar prajapati bsc cs third year from raj sms babatpur siswa varanasi ")
            speak("your ffull name vivek kumar prajapati bsc cs third year from raj sms babatpur siswa varanasi")             
  
        elif "who are you" in query: 
            speak("I am your virtual assistant created by vivek") 
  
        elif 'reason for you' in query: 
            speak("I was created as a Minor project by Mister vivek ") 
  
        elif 'change background' in query: 
            ctypes.windll.user32.SystemParametersInfoW(20,  
                                                       0,  
                                                       "Location of wallpaper", 
                                                       0) 
            speak("Background changed succesfully") 
  
        elif 'news' in query: 
              
            try:  
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\=8cc180a6b06b48fea4edb88dd78338ef''') 
                data = json.load(jsonObj) 
                i = 1
                  
                speak('here are some top news from the times of india') 
                print('''=============== TIMES OF INDIA ============'''+ '\n') 
                  
                for item in data['articles']: 
                      
                    print(str(i) + '. ' + item['title'] + '\n') 
                    print(item['description'] + '\n') 
                    speak(str(i) + '. ' + item['title'] + '\n') 
                    i += 1
            except Exception as e: 
                  
                print(str(e)) 
  
          
        elif 'lock window' in query: 
                speak("locking the device") 
                ctypes.windll.user32.LockWorkStation() 
  
        elif 'shutdown system' in query: 
                speak("Hold On a Sec ! Your system is on its way to shut down") 
                subprocess.call('shutdown / p /f') 
                  
        elif 'empty recycle bin' in query: 
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
            speak("Recycle Bin Recycled") 
  
        elif "don't listen" in query or "stop listening" in query: 
            speak("for how much time you want to stop jarvis from listening commands") 
            a = int(takeCommand()) 
            time.sleep(a) 
            print(a) 

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip addressis {ip}")
        elif 'close notepad' in query:
            speak("ok sir,closing notepad")
            os.system("taskkill/f/im notepad.exe")

        elif "where is" in query: 
            query = query.replace("where is", "") 
            location = query 
            speak("User asked to Locate") 
            speak(location) 
            webbrowser.open("https://www.google.nl / maps / place/" + location + "") 
  
        elif "camera" in query or "take a photo" in query: 
            ec.capture(0, "Jarvis Camera ", "img.jpg") 
  
        elif "restart" in query: 
            subprocess.call(["shutdown", "/r"])    
              
        elif "hibernate" in query or "sleep" in query: 
            speak("Hibernating") 
            subprocess.call("shutdown / h") 

        elif 'play  on youtube' in query:
            kit.playonyt("zee karda")    
  
        elif "log off" in query or "sign out" in query: 
            speak("Make sure all the application are closed before sign-out") 
            time.sleep(5) 
            subprocess.call(["shutdown", "/l"]) 
  
        elif 'write a note' in query: 
            speak("What should i write, sir") 
            note = takeCommand() 
            file = open('jarvis.txt', 'w') 
            speak("Sir, Should i include date and time") 
            snfm = takeCommand() 
            if 'yes' in snfm or 'sure' in snfm: 
                strTime = datetime.datetime.now().strftime("% H:% M:% S") 
                file.write(strTime) 
                file.write(" :- ") 
                file.write(note) 
            else: 
                file.write(note) 
          
        elif 'show note' in query: 
            speak("Showing Notes") 
            file = open("jarvis.txt", "r")  
            print(file.read()) 
            speak(file.read(6)) 

                      
        elif "jarvis" in query: 
              
            wishMe() 
            speak("Jarvis 1 point o in your service Mister") 
            speak(usrname) 
  
        elif "weather" in query: 
              
            # Google Open weather website 
            # to get API of Open weather  
            api_key = "Api key" 
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ") 
            print("City name : ") 
            city_name = takeCommand() 
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name 
            response = requests.get(complete_url)  
            x = response.json()  
              
            if x["cod"] != "404":  
                y = x["main"]  
                current_temperature = y["temp"]  
                current_pressure = y["pressure"]  
                current_humidiy = y["humidity"]  
                z = x["weather"]  
                weather_description = z[0]["description"]  
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))  
              
            else:  
                speak(" City Not Found ") 
              
        elif "send message " in query: 
                # You need to create an account on Twilio to use this service 
                account_sid = 'Account Sid key'
                auth_token = 'Auth token'
                client = Client(account_sid, auth_token) 
  
                message = client.messages.create ( 
                                    body = takeCommand(), 
                                    from_='Sender No', 
                                    to ='Receiver No'
                                ) 
  
                print(message.sid) 
  
        elif "wikipedia" in query: 
            webbrowser.open("wikipedia.com") 
  
        elif "Good Morning" in query: 
            speak("A warm" +query) 
            speak("How are you Mister") 
            speak(assname) 
  
        # most asked question from google Assistant 
        elif "will you be my gf" in query or "will you be my bf" in query:    
            speak("I'm not sure about, may be you should give me some time") 
  
        elif "how are you" in query: 
            speak("I'm fine, glad you me that") 
  
        elif "i love you" in query: 
            speak("It's hard to understand") 
  
        elif 'about your information' in query:
            print("my name is jarvis 2.43 . my full name Just A Rather Very Intelligent System is a fictional artificial intelligence that first appeared in the Marvel Cinematic Universe where he was voiced by Paul Bettany in Iron Man, Iron Man 2, The Avengers, Iron Man 3, and Avengers: Age of Ultron")
            speak("my name is jarvis 2.43 . my full name Just A Rather Very Intelligent System is a fictional artificial intelligence that first appeared in the Marvel Cinematic Universe where he was voiced by Paul Bettany in Iron Man, Iron Man 2, The Avengers, Iron Man 3, and Avengers: Age of Ultron")    

        elif 'no thanks' in query:
            speak("thanks for using me sir, have a good day")
            sys.exit()

        speak('sure sir')    

