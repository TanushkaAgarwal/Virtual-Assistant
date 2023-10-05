import datetime
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
import pprint
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'photo' in command:
        photo = command.replace('show', '')
        print('photos' + photo)
        pywhatkit.search(photo)
    elif 'open youtube' in command:
        webbrowser.open('www.youtube.com')
    elif 'open google' in command:
        webbrowser.open('www.google.com')
    elif 'tell me about' in command:
        about = command.replace('tell me about', '')
        topic = wikipedia.summary(about, 1)
        print(topic)
        talk(topic)
    elif 'news' in command:
        pywhatkit.search('news')
    elif 'weather' in command:
        weather_res = command.replace('city', '')
        talk('showing' + weather_res)
        pywhatkit.search(weather_res)
    elif 'how are you' in command:
        talk('I am Fine')
    elif 'who are you' in command:
        print('I am your personal assistant')
        talk('I am your personal assistant')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'what can you do' in command:
        li_commands = {
            "open websites": "Example: 'open youtube.com",
            "time": "Example: 'what time it is?'",
            "date": "Example: 'what date it is?'",
            "tell me": "Example: 'tell me about India'",
            "weather": "Example: 'what weather/temperature in Mumbai?'",
            "news": "Example: 'news for today' ",
        }
        ans = """I can do lots of things. See the list of commands"""
        print(ans)
        pprint.pprint(li_commands)
        talk(ans)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
