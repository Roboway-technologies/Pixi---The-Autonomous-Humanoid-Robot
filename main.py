import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import cv2

listener = sr.Recognizer()
pixi = pyttsx3.init()
rate = pixi.getProperty('rate')
pixi.setProperty('rate', rate-30)
voices = pixi.getProperty('voices')
pixi.setProperty('voice', voices[1].id)
pixi.say('Hello Boss. I am pixi, An Autonomous Humanoid Robot. I am programmed in Dhaka, Bangladesh. How can I help you?')
pixi.runAndWait()

# function to talk the results
def talk(text):
    pixi.say(text)
    pixi.runAndWait()



# taking the voice commands from microphone
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'pixi' in command:
                command = command.replace('pixi', '')
    except:
        pass

    return command



# Runs the System
def run_pixi():
    command = take_command()
    if 'time' in command:
        talk('The time is '+time(command))

    elif 'play' in command:
        talk('Playing for you' + playing(command))
        pywhatkit.playonyt(playing(command))

    elif 'tell me about' in command:
        talk(wiki_data(command))

    elif 'age' in command:
        talk(age(command))

    elif 'your name' or 'father' or 'daddy' or 'date' or 'thanks' or 'thank you' or 'Allah' or 'God' in command:
        talk(funfacts(command))

    elif 'camera' or 'webcam' or 'vision' in command:
        camera(command)

    

    else:
        talk('Sorry Sir. I do not understand. Please say it again')



def wiki_data(command):
    command = command.replace('tell me about', '')
    info = wikipedia.summary(command, 1)
    return info

def playing(command):
    song = command.replace('play', '')
    return song

def age(command):
    boyosh = 'I am 12 hours old right now'
    return boyosh

def time(command):
     current_time = datetime.datetime.now().strftime('%I:%M %p')
     return current_time

def camera(command):
    talk("Opening Camera")
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        cv2.imshow('Pixicam', img)
        k = cv2.waitKey(50)
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

def funfacts(command):
    if 'your name' in command:
        talk('My name is Pixi The Robot')
    elif 'father' or 'daddy' or 'sugar daddy'  in command:
        talk('I do not have any biological father. But technically, My father is Ariifin Rafi')
    elif 'date' in command:
        talk('Sorry, I am not interested')
    elif 'are you there' in command:
        talk('Yes, At your service boss')
    elif 'thank you' or 'thanks a lot' in command:
        talk('You are welcome boss')
    elif 'Allah' or 'God' or 'Creator' in command:
        talk('There should be a creator of the universe like I have. So yes, Allah, Vagaban or God exists')
    elif '' or 'thanks a lot' in command:
        talk('You are welcome boss')
    elif '' or 'thanks a lot' in command:
        talk('You are welcome boss')



while True:
    run_pixi()



