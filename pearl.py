import pyttsx3
import speech_recognition as sr

# <<< Voice Samples >>>
HAZEL = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0' #FEMALE
ZIRA = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0' #FEMALE
DAVID = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0' #MALE

# Function for text-to-speach:
def speak(text_message):
    engine = pyttsx3.init()
    id = HAZEL
    engine.setProperty('voice', id)
    engine.say(text = text_message)
    engine.runAndWait()
    
# << Test Part >>
#speak("Good evening Boss, I'm Pearl, Your personalized AI assistant.")

# Function for input to the AI:
def speechrecognition():
    r = sr.Recognizer()
    with sr.microphone() as source:
        print("Listening....")
        r. pause_threshold=1
        audio = r. listen(source,0,8)
    
    try:
        print( "Recogizing. ... ")
        query = r.recognize_google(audio,language="en")
        return query.lower()
    
    except:
        return ""

# << Test Part >>
#print(speechrecognition())
