'''
Author: CodeWithVikash
Date: 22 March 2025
Purpose: This is a Jarvis AI Project
'''
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[1].id) # This is used to print characters 
engine.setProperty('voice',voices[0].id)

def speak(audio):
    '''
    This Function is used to speak 
    '''
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    '''
    This Function is used to greet user like say goodMorning etc according to time
    '''
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour < 12):
        speak("Good Morning Sir!")
    elif(hour >= 12 and hour < 18):
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")

    speak("Hello I am Jarvis How can I assist you")

def takeVoiceCommand():
    '''
   This Function is used to take Voice Command input from user and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio_text = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio_text)
        print(f'Text: {query} \n')
    except:
        print("Say, that again please...")
        # speak("Say, that again please...")
        return 'None'
    return query
if __name__ == '__main__':
    print("Jarvis here......")
    greetMe()
    while True:
        query = takeVoiceCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open facebook' in query:
            webbrowser.open('facebook.com')
        elif 'open linkedin' in query:
            webbrowser.open('linkedin.com')
        elif 'open instagram' in query:
            webbrowser.open('instagram.com')
        elif 'play music' in query:
            music_dir = 'C:\\Musics'
            songs = os.listdir(music_dir)
            print(songs)
            random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir, random_song))
        elif 'time batao' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'The time is {strTime}')
        elif 'open code' in query:
            Code_path = "D:\\Downloads\\Microsoft VS Code\\Code.exe"
            os.startfile(Code_path)

        elif 'bye-bye' in query:
            speak("Your program has been quit successfully")
            break
        else:
            speak("Say, that again please...")
            