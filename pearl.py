import pyttsx3
import speech_recognition as sr
import datetime
import requests

# <<< Voice Samples >>>
HAZEL = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0' #FEMALE
ZIRA = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0' #FEMALE
DAVID = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0' #MALE

# Function for text-to-speach:
def speak(text_message):
    engine = pyttsx3.init()
    id = ZIRA
    engine.setProperty('voice', id)
    engine.say(text = text_message)
    engine.runAndWait()

# << Test Part >>
#speak("Good evening Boss, I'm Pearl, Your personalized AI assistant.")

# Function for input to the AI:
def voiceInput():
    r = sr.Recognizer()
    with sr.microphone() as source:
        print("Listening....")
        r. pause_threshold=1
        audio = r.listen(source,0,8)
    
    try:
        print("Recognizing. ... ")
        query = r.recognize_google(audio,language="en")
        return query.lower()
    
    except:
        return ""

# << Test Part >>
#print(voiceInput())

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "Kolkata"
API_KEY = "46afb3af322e7f76dbc9a97c8bce75c1"
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
response = requests.get(URL)
def get_weather_report():
    if response.status_code == 200:
        data = response.json() 
        main = data['main']
        temperature = round(main['temp']-273)
        humidity = main['humidity']
        pressure = main['pressure']
        report = data['weather']
        finalWeatherReport = (f"The temparature today in {CITY} is {temperature} degree celcius.\nHumidity in air is\
 {humidity}%.\nPressure is {pressure} hectoPascal.\nWeather type is {report[0]['description']}.\
\nThat's all, sir! ")
        return finalWeatherReport
    else:
        return("Error in the HTTP request")
    
def get_date():
    d = datetime.date.today().strftime("%B %d, %Y")
    return(f"Today is the{d}.")
def get_time():
    t = datetime.datetime.now().time().strftime("%H:%M")
    return(f"Now The time is {t}")