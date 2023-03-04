import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia

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
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('The time is '+time)

    elif 'play' in command:
        talk('Playing for you' + playing(command))
        pywhatkit.playonyt(playing(command))

    elif 'tell me about' in command:
        talk(wiki_data(command))

    elif 'age' in command:
        talk(age(command))

    elif 'are you single' in command:
        talk('I am single. But I can not produce any child. So, I cant date you sir')

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



while True:
    run_pixi()



