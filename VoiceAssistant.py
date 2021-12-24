import speech_recognition as sr
import pyttsx3
import pywhatkit
from datetime import datetime
import wikipedia
import random
import pyjokes
import time
import pyaudio
import sys
import python_weather
import asyncio

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

##### Check installed voices (optional)
# Default for Windows 10: 0 is male, 1 is female
# If you install alternate voice packs, this list might be slightly different, i.e.
# index -> 0 -- Microsoft David Desktop - English (United States)
# index -> 1 -- Microsoft Linda - English (Canada)
# index -> 2 -- Microsoft Susan - English (United Kingdom)
# index -> 3 -- Microsoft Heera - English (India)
# index -> 4 -- Microsoft Hazel Desktop - English (Great Britain)
# index -> 5 -- Microsoft Catherine - English (Australia)
# index -> 6 -- Microsoft Zira Desktop - English (United States)
# def check_voice_list():
#     index = 0
#     for voice in voices:
#         print(f'index -> {index} -- {voice.name}')
#         index +=1
# check_voice_list()

##### SET VOICE NAME HERE:
# voices_dict = {0: 'David', 1: 'Linda', 2: 'Susan', 3: 'Heera', 4: 'Hazel', 5: 'Catherine', 6: 'Zira'}
# voice_num = 4
# voice_name = voices_dict[voice_num]
# Note: the voice recognition library can distinguish some names better than others.

voice_name = "laura"
engine.setProperty('voice', voices[4].id)

# rate = engine.getProperty('rate')
# engine.say('My current speaking rate is ' + str(rate))

def talk(text):
    engine.say(text)

def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, timeout = 5)
            command = listener.recognize_google(voice, language='en-US')
            command = command.lower()
    except Exception as ex:
        print(ex)
        command = ''
        pass
    return command

def get_pa():
    rannum = random.randint(1, 3)
    if rannum == 1:
        talk('I am here')
    elif rannum == 2:
        talk('Hello')
    elif rannum == 3:
        talk('I am listening')
    talk('How can I help?')

def it_crowd():
    talk('Have you tried turning it off and on again?')

def wishMe():
    engine.say('Booting ' + voice_name + ' system')

    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk('Good morning!')
    elif hour >= 12 and hour < 17:
        talk('Good afternoon!')
    else:
        talk('Good evening.')

    engine.say('How can I help?')

async def getweather():
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)

    # fetch a weather forecast from a city
    weather = await client.find("Des Moines IA")

    # returns the current day's forecast temperature (int)
    temp_now = str(weather.current.temperature)
    sky_now = str(weather.current.sky_text) # sunny, cloudy, etc.
    humid_now = str(weather.current.humidity)
    wind_now = str(weather.current.wind_speed)

    print('The current temperature is ' + temp_now + ' degrees.')
    print('It is ' + sky_now + ', ' + humid_now + ' percent humidity,' + 
        ' wind speed ' + wind_now + ' miles per hour')
    
    talk('The current temperature is ' + temp_now + ' degrees.')
    talk('It is ' + sky_now + ', ' + humid_now + ' percent humidity,' + 
        ' wind speed ' + wind_now + ' miles per hour')

    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        todays_date = datetime.today().strftime('%Y-%m-%d')
        if (str(forecast.date).find(todays_date) != -1):
            sky_forecast = str(forecast.sky_text)
            temp_high = str(forecast.high)
            precip_forecast = str(forecast.precip)
            print('Today will be ' + sky_forecast + ' with a high of ' + temp_high + ' degrees,' + 
                'and a ' + precip_forecast + ' percent chance of precipitation.')
            talk('Today will be ' + sky_forecast + ' with a high of ' + temp_high + ' degrees,' + 
                'and a ' + precip_forecast + ' percent chance of precipitation.')

    # close the wrapper once done
    await client.close()

def run_pa(command):
    if 'today\'s date' in command or 'what day is it' in command:
        todays_date = datetime.today().strftime('%B %d, %Y')
        day = datetime.today().weekday() + 1
        Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 
                    5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
        day_of_the_week = Day_dict[day]
        talk('Today is ' + day_of_the_week + ", " + todays_date)
    elif 'time' in command:
        time = datetime.now().strftime('%H:%M %p')
        talk('Current time is ' + time)
    elif 'tell' in command and 'joke' in command:
        talk('Ok, Here is a joke:')
        talk(pyjokes.get_joke())
    elif 'computer' in command or 'is broken' in command or 'problem with' in command:
        it_crowd()
    elif 'weather' in command:
        if 'forecast' in command:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(getweather())
    elif 'play' in command:
        song = command.replace('play', '')
        talk('Searching for ' + song + ' on YouTube.')
        talk('Now playing first result for ' + song)
        pywhatkit.playonyt(song)
    elif 'who' in command or 'what' in command or 'how' in command or 'when' in command or 'why' in command:
        talk('I am searching Wikipedia for ' + command)
        question = command
        info = wikipedia.summary(question, 3)
        talk(info)
    elif 'thank you' in command or 'thanks' in command:
        talk('You\'re welcome.')
    else:
        talk('Sorry I did not understand')

def main():
    wishMe()
    while True:
        engine.runAndWait()
        command = take_command()

        if command == 'exit' or command == 'quit':
            sys.exit()
        elif command == None or command == '':
            # talk('Sorry I did not hear you')
            continue
        elif voice_name in command:
            get_pa()
        else:
            run_pa(command)

if __name__ == "__main__":
    main()