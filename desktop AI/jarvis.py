import pyttsx3                    #pip install pyttsx3
import datetime
import speech_recognition as sr    #pip install speechRecognition
import pyaudio                     #pip install pipwin --- then----pipwin install pyaudio
import wikipedia                   #pip install wikipedia
import googlesearch
import webbrowser
import os
import smtplib
import random
'''takes voice as input using pyttsx3 module '''
engine = pyttsx3.init('sapi5')
# two voices --- one is male and one is female
voices = engine.getProperty("voices")
# print(voices[1].id)
      # select voice
engine.setProperty("voice",voices[1].id)
dic = {"mallika":"mallika20jun@gmail.com","agarwal":"agarwalmallika20@gmail.com"}
'''speak function speaks the sentence in the voice selected above'''
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

'''This is wishme() function which uses datetime module and its method to get current time and wish accordingly 
        by calling speak() function '''
def wishme():
#     wish according to time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning")
    elif hour>12 and hour<=16:
        speak("Good Afternoon")
    elif hour>16 and hour<=19:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak("Hello ! How may I help you. ")

'''using speechRecognition module ...the machine hears what we speak and recognises the text spoken 
with microphone as source
speech to text recognition'''
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.energy_threshold=50
        r.pause_threshold = 1     #after starting to listen wait for 1 second of non-speaking and then end the phase
        audio = r.listen(source)
        '''try to recognize the audio using google recognize engine ...convert the audio into particular language
        and print what text is recognized'''
        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language='en-in')
            print("User said : ",query)
        except Exception as e:
            # print(e)
            print("Speak again ")
            return "None"      #if some problem occurs
        return query
def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    # server.login("email","password")
    server.login("mallika20jun@gmail.com","mail#back")
    server.sendmail("mallika20jun@gmail.com",to,content)
    server.close()
if __name__ == "__main__":
    # speak("good boy!!!!")
    wishme()
    while True:
        query = takecommand().lower()
        #logic to execute task based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia .....")
            query = query.replace("wikipedia","")
            #summary() function is used to search in wikepdia and show some part of it
            result = wikipedia.summary(query, sentences = 5)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")     #webbrowser is used to open sites uisng webbrowser module
            # query = query.replace("google","")
            # res =googlesearch.search(query)
            # print(res)
            # speak(res)
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        #how to play music  using os module
        elif "play music" in query:
            # webbrowser.open("spotify.com")
            music_dir ="D:\\mymusic"
            songs = os.listdir(music_dir)   #listdir is used to list all files
            print(songs)
            #startfile(path,songnumber)
            song = random.randint(0,(len(songs)-1))
            os.startfile(os.path.join(music_dir,songs[song]))
        elif 'tell time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is : {strtime}")
        elif 'open pycharm' in query:
            path = "D:\\PyCharm Community Edition 2021.3.1\\bin\\pycharm64.exe"
            os.startfile(path)
        elif "send email" in query:
            try:
                speak("to whom I should send")
                to = takecommand()
                speak("What should I say")
                content = takecommand()
                sendemail(dic[to],content)
                speak("email has been sent")
            except Exception as e:
                # print(e)
                print("sorry i am not able to send")

        elif "exit" or "quit" in query:
            exit()
