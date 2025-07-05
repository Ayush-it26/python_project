import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit


engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
#text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#To convert voice into text 
def takecommand():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            try:
                audio = r.listen(source, timeout=1, phrase_time_limit=5)
            except sr.WaitTimeoutError:
                speak("Listening timed out, please try again.")
                speak("Do you have any other work for me")
                return "none"
            
            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language='en-in')
                print(f"User said: {query}")
            except sr.UnknownValueError:
                speak("Sorry, I did not catch that.")
                return "none"
            except sr.RequestError:
                speak("Speech service is down")
                return "none"
            return query

    except OSError as e:
        speak("Microphone is not available or not accessible.")
        print(f"Microphone Error: {e}")
        return "none"



#to wish 
def wish():
        hour=int(datetime.datetime.now().hour)

        if hour>=0 and hour<=12:
            speak("good morning ayush sir")
        elif hour>12 and hour<18:
            speak("good afternoon ayush sir")
        
        if hour:
            speak("I am starvix....  sir,please tell me how can i help you")



if __name__ == "__main__":
    wish()
    while True:

      query= takecommand().lower()

    #   speak("Do you have any other work for me")
    #logic bulding for tasks 

      if "open notepad" in query:
        npath="c:\\Windows\\notepad.exe"
        os.startfile(npath)
      
      elif"open cmd" in query:
          apath = "C:\\Windows\\WinSxS\\wow64_microsoft-windows-commandprompt_31bf3856ad364e35_10.0.19041.1_none_4b527e92ee1ad1e5\\cmd.exe"
          os.startfile(apath)

      elif "open yt" in query:
        dpath="https://www.youtube.com"
        os.startfile(dpath) 

      elif "open camera" in query:
        cap= cv2.VideoCapture(0)
        while True:
            ret, img=cap.read()
            cv2.inshow('webcam', img)
            k=cv2.waitKey(50)
            if k==27:
                break
            cap.release()
            cv2.destroyAllWindows()

      elif "play music" in query:
           music_dir="C:\\Users\\Rahul\\Music"  
           songs=os.listdir(music_dir)
           os.startfile(os.path.join(music_dir,songs[0]))


      elif "ip address" in query:
        ip= get('https://api.ipify.org').text
        speak(f"your IP address is {ip}")
        print(ip)

      elif "who is you" in query:
          speak("I am starvix sir,please tell me how can i help you")

      elif "give me respect" in query:
          speak("I am literly very sorry ,Ayush sir")


      elif "wikipedia" in query:
          speak("searching wikipedia...")
          query= query.replace("wikipedia","")
          results=wikipedia.summary(query, sentences=4)
          speak("according to wikipedia")
          speak(results)
          print(results)


      elif "open youtube" in query:
          webbrowser.open("www.youtube.com")

      elif "open facebook" in query:
          webbrowser.open("www.facebook.com")
    


      elif "open instagram" in query:
          webbrowser.open("www.instagram.com")

      elif "open google chrome" in query:
          speak("sir, what should i search on google chrome")

          cm=takecommand().lower()
          webbrowser.open(f"{cm}")

      elif "send message" in query:
          kit.sendwhatmsg_instantly("+917499522509", "Hi!! dude", wait_time=50, tab_close=True)

      elif "play song on youtube" in query:
          kit.playonyt("haan ke haan")

    
         

      elif "exit" in query or "stop" in query or "quit" in query:
            speak("Okay, exiting. Have a nice day Ayush!")
            speak("Thanks for using me ,have a beautifull day")
            break
      
